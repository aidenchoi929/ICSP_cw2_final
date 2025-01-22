import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta, date
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from openai import OpenAI
import warnings
from streamlit.runtime.scriptrunner import add_script_run_ctx
from streamlit.runtime.scriptrunner import get_script_run_ctx

warnings.filterwarnings("ignore")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(page_title="Stock Analysis and Forecasting", layout="wide", page_icon="📈")

# Hide Streamlit navigation bar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stock-info {
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        margin: 10px 0;
    }
    .custom-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e6e6e6;
        margin: 10px 0;
    }
    .analysis-text {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Back button in the top right corner
col1, col2, col3 = st.columns([1, 1, 0.2])
with col3:
    if st.button("← Back", key="back_button"):
        st.switch_page("pages/Layer02_Stock_Insights.py")

# Check if a stock ticker has been selected
if (
    "selected_ticker" not in st.session_state
    or st.session_state.selected_ticker is None
):
    st.warning("Please select a stock on the previous page.")
    if st.button("← Go back to stock selection page"):
        st.switch_page("pages/Layer02_Stock_Insights.py")
    st.stop()


# Chatbot functions
def get_stock_chat_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4", messages=messages, temperature=0.7, max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def create_system_prompt(ticker, current_price, price_change_pct):
    return f"""You are a helpful stock market assistant analyzing {ticker}. 
    Current price: ${current_price:.2f} ({price_change_pct:+.2f}%).
    Provide clear, concise answers about this stock's performance, trends, and analysis.
    Base your responses on general market knowledge and technical analysis principles."""


# Technical analysis functions
def calculate_rsi(data, periods=14):
    delta = data["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def calculate_bollinger_bands(data, window=20):
    sma = data["Close"].rolling(window=window).mean()
    std = data["Close"].rolling(window=window).std()
    upper_band = sma + (std * 2)
    lower_band = sma - (std * 2)
    return sma, upper_band, lower_band


def interpret_technical_indicators(rsi, current_price, lower_band, upper_band):
    analysis = []

    if rsi < 30:
        analysis.append(
            "RSI is below 30, indicating an oversold condition with a potential rebound."
        )
    elif rsi > 70:
        analysis.append(
            "RSI is above 70, indicating an overbought condition with potential corrections."
        )
    else:
        analysis.append("RSI is in a neutral range.")

    if current_price < lower_band:
        analysis.append(
            "The stock price is below the lower band, indicating a potential technical rebound."
        )
    elif current_price > upper_band:
        analysis.append(
            "The stock price is above the upper band, indicating a potential technical correction."
        )
    else:
        analysis.append(
            "The stock price is moving normally within the Bollinger Bands."
        )

    return analysis


# ML model functions
def prepare_data(data, lookback=60):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

    X, y = [], []
    for i in range(lookback, len(scaled_data)):
        X.append(scaled_data[i - lookback : i, 0])
        y.append(scaled_data[i, 0])

    return np.array(X), np.array(y), scaler


def create_lstm_model(lookback):
    model = Sequential(
        [
            LSTM(50, return_sequences=True, input_shape=(lookback, 1)),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(1),
        ]
    )
    model.compile(optimizer="adam", loss="mse")
    return model


def add_chat_section(current_price, price_change_pct):
    st.markdown(
        """
        <div style="margin-top: 30px;"> <!-- Adds space above -->
            <h3>💬 Stock Chat Assistant</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Predefined prompts
    prompts = {
        "Technical Analysis": "Can you explain the current technical analysis indicators for this stock?",
        "Investment Risk": "What are the main investment risks for this stock?",
        "Market Sentiment": "What's the current market sentiment for this stock?",
        "Price Targets": "What are the potential price targets based on technical analysis?",
        "Trading Strategy": "What would be a good trading strategy for this stock?",
    }

    # Display predefined prompt buttons
    st.markdown("#### Quick Questions")
    cols = st.columns(len(prompts))
    for col, (prompt_title, prompt_text) in zip(cols, prompts.items()):
        if col.button(prompt_title):
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt_text})

            # Get chatbot response
            messages = [
                {
                    "role": "system",
                    "content": create_system_prompt(
                        st.session_state.selected_ticker,
                        current_price,
                        price_change_pct,
                    ),
                },
                {"role": "user", "content": prompt_text},
            ]
            response = get_stock_chat_response(messages)
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Display chat history
    st.markdown("#### Chat History")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Ask about the stock..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Prepare messages with system prompt
        messages = [
            {
                "role": "system",
                "content": create_system_prompt(
                    st.session_state.selected_ticker, current_price, price_change_pct
                ),
            },
            {"role": "user", "content": prompt},
        ]

        # Get response
        response = get_stock_chat_response(messages)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Rerun to update chat display
        st.rerun()


# Main content
def main():
    ticker = st.session_state.selected_ticker

    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        end_date = date.today()
        start_date = end_date - timedelta(days=365)
        data = stock.history(start=start_date, end=end_date)

        if data.empty:
            st.error("No data found for the selected stock.")
            return

        # Display current stock information
        current_price = data["Close"].iloc[-1]
        price_change = data["Close"].iloc[-1] - data["Close"].iloc[-2]
        price_change_pct = (price_change / data["Close"].iloc[-2]) * 100

        # Stock overview section
        st.markdown("### 📊 Real-time Stock Overview")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""
                <div class="custom-box">
                    <h4>Current Price</h4>
                    <h2>${current_price:.2f}</h2>
                    <p style="color: {'green' if price_change >= 0 else 'red'}">
                        {price_change:+.2f} ({price_change_pct:+.2f}%)
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                f"""
                <div class="custom-box">
                    <h4>Volume</h4>
                    <h2>{data['Volume'].iloc[-1]:,.0f}</h2>
                    <p>Recent Trading Day</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col3:
            st.markdown(
                f"""
                <div class="custom-box">
                    <h4>Daily Range</h4>
                    <h2>${data['Low'].iloc[-1]:.2f} - ${data['High'].iloc[-1]:.2f}</h2>
                    <p>The daily range between the highest and lowest price</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col4:
            st.markdown(
                f"""
                <div class="custom-box">
                    <h4>52-week Range</h4>
                    <h2>${data['Low'].min():.2f} - ${data['High'].max():.2f}</h2>
                    <p>The highest and lowest prices during the past year</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Technical analysis section
        st.markdown(
            """
            <h3 style="margin-top: 30px;">📈 Technical Analysis</h3>
            """,
            unsafe_allow_html=True,
        )

        # Calculate indicators
        data["RSI"] = calculate_rsi(data)
        sma, upper_band, lower_band = calculate_bollinger_bands(data)

        # Interpret technical analysis
        analysis = interpret_technical_indicators(
            data["RSI"].iloc[-1],
            data["Close"].iloc[-1],
            lower_band.iloc[-1],
            upper_band.iloc[-1],
        )

        # Display analysis results
        st.markdown("#### Interpretation of Technical Analysis")
        for point in analysis:
            st.markdown(
                f"<div class='analysis-text'>{point}</div>", unsafe_allow_html=True
            )

        # Create charts
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.03,
            subplot_titles=("Price & Bollinger Bands", "RSI"),
            row_heights=[0.7, 0.3],
        )

        # Candlestick chart
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
                name="OHLC",
            ),
            row=1,
            col=1,
        )

        # Bollinger Bands
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=upper_band,
                name="Upper Band",
                line=dict(color="gray", dash="dash"),
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=lower_band,
                name="Lower Band",
                line=dict(color="gray", dash="dash"),
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=sma,
                name="20-day Moving Average",
                line=dict(color="orange"),
            ),
            row=1,
            col=1,
        )

        # RSI
        fig.add_trace(
            go.Scatter(
                x=data.index, y=data["RSI"], name="RSI", line=dict(color="purple")
            ),
            row=2,
            col=1,
        )

        fig.update_layout(height=800, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)

        # Machine learning predictions
        st.markdown("### 🤖 Machine Learning Predictions")

        with st.spinner("Generating predictions..."):
            X, y, scaler = prepare_data(data)
            X = X.reshape((X.shape[0], X.shape[1], 1))
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            # LSTM prediction
            lstm_model = create_lstm_model(60)
            lstm_model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
            lstm_pred = lstm_model.predict(X_test)[-1][0]
            lstm_price = scaler.inverse_transform([[lstm_pred]])[0][0]

            # Random Forest prediction
            rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
            rf_model.fit(X_train.reshape(X_train.shape[0], -1), y_train)
            rf_pred = rf_model.predict(X_test.reshape(X_test.shape[0], -1))[-1]
            rf_price = scaler.inverse_transform([[rf_pred]])[0][0]

            # Linear Regression prediction
            lr_model = LinearRegression()
            lr_model.fit(X_train.reshape(X_train.shape[0], -1), y_train)
            lr_pred = lr_model.predict(X_test.reshape(X_test.shape[0], -1))[-1]
            lr_price = scaler.inverse_transform([[lr_pred]])[0][0]

            # Display predictions
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(
                    f"""
                    <div class="custom-box">
                        <h4>LSTM Predicted Price</h4>
                        <h2>${lstm_price:.2f}</h2>
                        <p>Compared to current price: {((lstm_price/current_price - 1) * 100):+.2f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:
                st.markdown(
                    f"""
                    <div class="custom-box">
                        <h4>Random Forest Predicted Price</h4>
                        <h2>${rf_price:.2f}</h2>
                        <p>Compared to current price: {((rf_price/current_price - 1) * 100):+.2f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col3:
                st.markdown(
                    f"""
                    <div class="custom-box">
                        <h4>Linear Regression Predicted Price</h4>
                        <h2>${lr_price:.2f}</h2>
                        <p>Compared to current price: {((lr_price/current_price - 1) * 100):+.2f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Interpret prediction results
            st.markdown("#### Interpretation of Machine Learning Predictions")
            avg_prediction = (lstm_price + rf_price + lr_price) / 3
            pred_change = (avg_prediction / current_price - 1) * 100

            interpretation = f"""
            <div class='analysis-text'>
                The average predicted price from the three models is ${avg_prediction:.2f}, representing a {pred_change:+.2f}% 
                {'increase' if pred_change > 0 else 'decrease'} compared to the current price.
                A {'bullish' if pred_change > 5 else 'bearish' if pred_change < -5 else 'neutral'} trend is anticipated.
            </div>
            """
            st.markdown(interpretation, unsafe_allow_html=True)

        # Trading signals
        st.markdown(
            """
            <div style="margin-top: 30px;"> <!-- Adds space above -->
                <h3>📊 Trading Signals</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        rsi = data["RSI"].iloc[-1]
        macd = data["Close"].ewm(span=12).mean() - data["Close"].ewm(span=26).mean()

        # Determine trading signal
        signal = "Neutral"
        if rsi < 30 and data["Close"].iloc[-1] < lower_band.iloc[-1]:
            signal = "Strong Buy"
        elif rsi < 40:
            signal = "Buy"
        elif rsi > 70 and data["Close"].iloc[-1] > upper_band.iloc[-1]:
            signal = "Strong Sell"
        elif rsi > 60:
            signal = "Sell"

        signal_color = {
            "Strong Buy": "darkgreen",
            "Buy": "green",
            "Neutral": "gray",
            "Sell": "red",
            "Strong Sell": "darkred",
        }

        # Display trading signal
        st.markdown(
            f"""
            <div class="custom-box" style="text-align: center; padding: 10px 0px;">
                <h4 style="font-size: 25px;">Current Trading Signal</h4>
                <h1 style="color: {signal_color[signal]};">{signal}</h1>
                <div class="analysis-text" style="margin-top: 25px;">
                    <p>• RSI: {rsi:.2f} {'(Oversold)' if rsi < 30 else '(Overbought)' if rsi > 70 else '(Neutral)'}</p>
                    <p>• Bollinger Bands: {'Below Lower Band' if data["Close"].iloc[-1] < lower_band.iloc[-1] else 'Above Upper Band' if data["Close"].iloc[-1] > upper_band.iloc[-1] else 'Within Bands'}</p>
                    <p>• Recommendation: {
                        "Strong technical rebound signals detected. Consider buying." if signal == "Strong Buy"
                        else "Buying opportunity forming. Consider entering." if signal == "Buy"
                        else "Strong selling signals detected. Consider taking profits." if signal == "Strong Sell"
                        else "Selling signals detected. Consider partial selling." if signal == "Sell"
                        else "No clear trading signals. Maintain current position."
                    }</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


        # Add chat section
        add_chat_section(current_price, price_change_pct)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


# Footer
st.markdown(
    """
    <div style="position:fixed; bottom:0; left:0; right:0; background-color:#f8f9fa; text-align:center; padding:10px; font-size:14px; font-weight:bold; font-family:Arial, sans-serif; color:black;">
        All rights reserved by Aiden Choi for ICSP © 2025
    </div>
""",
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    main()
