import streamlit as st

st.set_page_config(page_title="Glossary", page_icon="📈", layout="wide")

st.markdown(
            """
            <h3 style="margin-top: 30px; font-size: 30px;">📊  Real-time stock overview</h3>
            """,
            unsafe_allow_html=True,
  )
st.markdown(
            """
            <h5 style="margin-top: 10px; font-size: 25px;">1. Current Price</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                The current price of a stock is the most recent trading price at which the stock was bought or sold in the market. 
                It reflects the immediate valuation determined by supply and demand dynamics during active trading hours.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Example:</span> 
                If Apple Inc.'s (AAPL) stock is trading at $220, this is its current price.
            </h6>
            <h6 style="margin-top: 5px;">
        <span style="font-size: 18px; font-weight: bold;">Importance to stock price prediction:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>The current price is a baseline for predictions as it represents the market’s present valuation of a stock.</li>
            <li>Predicting future prices often involves analyzing how the stock's current price aligns with historical trends, moving averages, or technical indicators.</li>
        </ul>
    </h6>
            """,
            unsafe_allow_html=True,
  )
st.markdown(
            """
            <h5 style="margin-top: -20px; font-size: 25px;">2. Volume</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                Volume is the total number of shares of a stock traded during a specific period (e.g., daily). It measures the activity and liquidity of a stock. 
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Example:</span> 
                If 5 million shares of Microsoft (MSFT) are traded today, the trading volume for the day is 5 million.
            </h6>
            <h6 style="margin-top: 5px;">
        <span style="font-size: 18px; font-weight: bold;">Importance to stock price prediction:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>Higher volume often indicates strong investor interest, which can lead to significant price movements.</li>
            <li>It helps identify trends; a sharp price change on high volume is more reliable than one on low volume.</li>
        </ul>
    </h6>
            """,
            unsafe_allow_html=True,
  )

st.markdown(
            """
            <h5 style="margin-top: -20px; font-size: 25px;">3. Daily Range</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                The daily range is the difference between the highest and lowest prices of a stock during a trading day.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Example:</span> 
                If Tesla’s stock price fluctuates between $800 and $820 today, its daily range is $20.
            </h6>
            <h6 style="margin-top: 5px;">
        <span style="font-size: 18px; font-weight: bold;">Importance to stock price prediction:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>It indicates market volatility, which is critical for predicting price behavior.</li>
            <li>Traders use the range to set stop-loss or target prices, aiding short-term strategies.</li>
        </ul>
    </h6>
            """,
            unsafe_allow_html=True,
  )
st.markdown(
            """
            <h5 style="margin-top: -20px; font-size: 25px;">4. 52 Week Range</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                The 52-week range is the highest and lowest prices a stock has traded at during the past year.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Example:</span> 
                If Amazon (AMZN) traded between $2,800 and $3,500 in the last 52 weeks, this is its 52-week range.
            </h6>
            <h6 style="margin-top: 5px;">
        <span style="font-size: 18px; font-weight: bold;">Importance to stock price prediction:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>It helps gauge a stock’s overall performance and potential growth.</li>
            <li>Stocks trading near their 52-week high may indicate bullish momentum, while those near the low could signify undervaluation or market pessimism.</li>
        </ul>
    </h6>
            """,
            unsafe_allow_html=True,
  )

st.markdown(
            """
            <h3 style="margin-top: -10px;">📈 Technical Analysis</h3>
            """,
            unsafe_allow_html=True,
  )

st.markdown(
    """
    <h6 style="margin-top: 10px;">
        <span style="font-size: 25px; font-weight: bold;">1. Relative Strength Index (RSI):</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>
                <span style="font-weight: bold;">Definition:</span> RSI is a momentum oscillator that measures the speed and change of price movements, ranging from 0 to 100. It identifies overbought or oversold conditions in the market.
            </li>
            <li>
                <span style="font-weight: bold;">How It Works:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li>RSI is calculated using the formula: RSI = 100 - (100 / (1 + (Average Gain / Average Loss))).</li>
                    <li><span style="font-weight: bold;">Overbought:</span> RSI > 70 indicates the stock might be overvalued and due for a price correction.</li>
                    <li><span style="font-weight: bold;">Oversold:</span> RSI < 30 signals the stock may be undervalued and poised for a rebound.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">History:</span> Developed by J. Welles Wilder in 1978, RSI became a cornerstone for technical analysis with its introduction in his book "New Concepts in Technical Trading Systems."
            </li>
            <li>
                <span style="font-weight: bold;">Why It Is Important:</span> RSI highlights potential trend reversals, helping traders make decisions about entering or exiting positions.
            </li>
            <li>
                <span style="font-weight: bold;">Suitable For:</span> Momentum trading, short-term strategies, and identifying price correction or trend continuation points.
            </li>
        </ul>
    </h6>

    <h6 style="margin-top: -10px;">
        <span style="font-size: 25px; font-weight: bold;">2. Bollinger Bands:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>
                <span style="font-weight: bold;">Definition:</span> Bollinger Bands consist of a middle band (a simple moving average) and two outer bands that represent price volatility.
            </li>
            <li>
                <span style="font-weight: bold;">How It Works:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li>The bands are calculated as: Upper Band = SMA + (k × σ), Lower Band = SMA − (k × σ), where k is the multiplier (usually 2), and σ is the standard deviation.</li>
                    <li>Prices near the upper band suggest overbought conditions, while those near the lower band indicate oversold conditions.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">History:</span> Created by John Bollinger in the 1980s, it became widely used for volatility and mean reversion trading.
            </li>
            <li>
                <span style="font-weight: bold;">Why It Is Important:</span> Bollinger Bands help identify periods of high and low volatility, guiding entry/exit points and trend confirmations.
            </li>
            <li>
                <span style="font-weight: bold;">Suitable For:</span> Volatility trading, swing trading, and breakout strategies.
            </li>
        </ul>
    </h6>

    <h6 style="margin-top: -10px;">
        <span style="font-size: 25px; font-weight: bold;">3. Moving Average:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>
                <span style="font-weight: bold;">Definition:</span> A moving average is a technical indicator that smooths out price data to identify trends over time. Common types include simple moving average (SMA) and exponential moving average (EMA).
            </li>
            <li>
                <span style="font-weight: bold;">How It Works:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">SMA:</span> The average price over a specific period. SMA = Sum of Prices Over Period / Number of Periods.</li>
                    <li><span style="font-weight: bold;">EMA:</span> Gives more weight to recent prices, making it more responsive to new information.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">History:</span> Moving averages have been used since the early 20th century, becoming popular as charting tools developed for financial markets.
            </li>
            <li>
                <span style="font-weight: bold;">Why It Is Important:</span> Moving averages smooth out noise, identify trend directions, and act as dynamic support or resistance levels.
            </li>
            <li>
                <span style="font-weight: bold;">Suitable For:</span> Trend-following strategies, crossover strategies (e.g., golden cross, death cross), and long-term investments.
            </li>
        </ul>
    </h6>

    <h6 style="margin-top: -10px;">
        <span style="font-size: 25px; font-weight: bold;">4. Candlestick Chart:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>
                <span style="font-weight: bold;">Definition:</span> A candlestick chart represents price movements over a specified period using "candlesticks" that show the open, high, low, and close prices.
            </li>
            <li>
                <span style="font-weight: bold;">How It Works:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Body:</span> Represents the open and close prices.</li>
                    <li><span style="font-weight: bold;">Wicks (Shadows):</span> Represent the high and low prices.</li>
                    <li><span style="font-weight: bold;">Colors (or fill):</span> Green/white (bullish) if close > open; red/black (bearish) if close < open.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">History:</span> Originated in Japan in the 18th century by rice trader Munehisa Homma. It gained global popularity with the work of Steve Nison in the 1990s.
            </li>
            <li>
                <span style="font-weight: bold;">Why It Is Important:</span> Candlestick patterns (e.g., Doji, Hammer, Engulfing) provide insights into market psychology and potential price reversals or continuations.
            </li>
            <li>
                <span style="font-weight: bold;">Suitable For:</span> Day trading, swing trading, and analyzing short-term price action.
            </li>
        </ul>
    </h6>
    """,
    unsafe_allow_html=True,
)

st.markdown(
            """
            <h3 style="margin-top: -10px;">🤖 Machine Learning Predictions</h3>
            """,
            unsafe_allow_html=True,
  )
st.markdown(
            """
            <h5 style="margin-top: 10px; font-size: 25px;">1. LSTM (Long Short-Term Memory)</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                LSTM is a type of recurrent neural network (RNN) capable of learning and remembering patterns in sequential data over long periods. It uses memory cells to manage long-term dependencies and avoid issues like vanishing gradients, which RNNs typically face.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Why It Is Relevant to Stock Price Prediction:</span> 
                Stock prices are inherently time-series data, where the current price depends on historical patterns and trends. LSTMs excel at analyzing sequential data, making them highly effective for predicting future stock prices based on past trends, moving averages, and other historical inputs.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Important Information Related to Finance:</span>
                <ul style="margin-top: 10px; margin-left: 20px;">
                    <li>LSTMs can model non-linear relationships, capturing market complexities better than traditional algorithms.</li>
                    <li>They are used in predicting stock prices, cryptocurrency trends, and market volatility.</li>
                    <li>However, they require substantial computational power and large datasets for training, which can be a limitation.</li>
            </ul>
            </h6>

            <h5 style="margin-top: -20px; font-size: 25px;">2. Random Forest</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                Random Forest is an ensemble learning algorithm that builds multiple decision trees and aggregates their outputs (through averaging for regression or voting for classification) to improve accuracy and reduce overfitting.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Why It Is Relevant to Stock Price Prediction:</span> 
                It can capture complex relationships between features such as trading volume, moving averages, and macroeconomic indicators, which influence stock prices. Random Forest works well with diverse datasets and can handle missing or categorical data, making it flexible for financial data.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Important Information Related to Finance:</span>
                <ul style="margin-top: 10px; margin-left: 20px;">
                    <li>Random Forest is commonly used for feature importance analysis, helping identify which factors (e.g., volume, technical indicators) contribute most to stock price changes.</li>
                    <li>It is interpretable compared to neural networks, providing insights into decision-making processes.</li>
                    <li>However, it may struggle with extrapolating future trends when the underlying data patterns significantly change.</li>
            </ul>
            </h6>

            <h5 style="margin-top: -20px; font-size: 25px;">3. Linear Regression</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Definition:</span> 
                Linear Regression is a statistical method used to model the relationship between a dependent variable (e.g., stock price) and one or more independent variables (e.g., trading volume, market indices). It assumes a linear relationship between variables.
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Why It Is Relevant to Stock Price Prediction:</span> 
                It is simple and interpretable, making it a good baseline model for predicting stock prices. Linear Regression works well in identifying trends and understanding the impact of specific factors (e.g., how an increase in market volume affects prices).
            </h6>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">Important Information Related to Finance:</span>
                <ul style="margin-top: 10px; margin-left: 20px;">
                    <li>It is often used in combination with other algorithms to forecast prices and evaluate market sensitivities.</li>
                    <li>Its simplicity is a double-edged sword: while easy to implement, it struggles with non-linear relationships or market complexities (e.g., sudden volatility).</li>
                    <li>In finance, it is also used for portfolio optimization and risk assessment.</li>
                </ul>
            </h6>
            """,
            unsafe_allow_html=True,
  )

st.markdown(
            """
            <h3 style="margin-top: -10px;">📊 Trading Signals</h3>
            """,
            unsafe_allow_html=True,
  )
st.markdown(
    """
    
    <h6 style="margin-top: 10px;">
        <span style="font-size: 25px; font-weight: bold;">1. RSI Condition:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>
                <span style="font-weight: bold;">RSI below 30:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Indicates:</span> Oversold conditions</li>
                    <li><span style="font-weight: bold;">Interpretation:</span> The asset might be undervalued, and there is a potential for a price rebound or reversal to the upside.</li>
                    <li><span style="font-weight: bold;">Action:</span> Traders often look for buying opportunities if other indicators support the potential for a reversal.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">RSI above 70:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Indicates:</span> Overbought conditions</li>
                    <li><span style="font-weight: bold;">Interpretation:</span> The asset might be overvalued, and there is a potential for a price correction or reversal to the downside.</li>
                    <li><span style="font-weight: bold;">Action:</span> Traders may look for selling opportunities or prepare for a potential decline if other signals align.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">RSI between 31 and 69:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Indicates:</span> Neutral or trending conditions</li>
                    <li><span style="font-weight: bold;">Interpretation:</span> The asset is neither overbought nor oversold and is often seen as trading within a normal range.</li>
                    <li><span style="font-weight: bold;">Action:</span> During this range, traders might use other indicators or chart patterns to confirm trends, as RSI alone does not suggest extreme market conditions.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">Additional context:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Divergences:</span> If the RSI shows a divergence (e.g., price is making new highs but RSI is not), it may indicate a potential reversal.</li>
                    <li><span style="font-weight: bold;">Trend Influence:</span> In strong uptrends, RSI can remain above 70 for an extended period, and in strong downtrends, it can stay below 30.</li>
                </ul>
            </li>
        </ul>
    </h6>

    <h6 style="margin-top: -15px;">
        <span style="font-size: 25px; font-weight: bold;">2. Bollinger Bands Condition:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li>
                <span style="font-weight: bold;">Lower Band:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Represents:</span> A potential oversold condition</li>
                    <li><span style="font-weight: bold;">Interpretation:</span> Prices near or below the lower band suggest that the asset may be undervalued or experiencing strong bearish momentum.</li>
                    <li><span style="font-weight: bold;">Action:</span> Look for buying opportunities; wait for confirmation from other indicators or patterns to confirm a reversal.</li>
                    <li><span style="font-weight: bold;">Note:</span> In strong downtrends, the price can "ride" the lower band, signaling continued bearish strength.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">Upper Band:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Represents:</span> A potential overbought condition</li>
                    <li><span style="font-weight: bold;">Interpretation:</span> Prices near or above the upper band suggest that the asset may be overvalued or experiencing strong bullish momentum.</li>
                    <li><span style="font-weight: bold;">Action:</span> Take profits; look for reversal patterns or other indicators that confirm potential price correction.</li>
                    <li><span style="font-weight: bold;">Note:</span> In strong uptrends, the price can "ride" the upper band, signaling continued bullish strength rather than an immediate reversal.</li>
                </ul>
            </li>
            <li>
                <span style="font-weight: bold;">Key Concepts:</span>
                <ul style="margin-top: 5px; margin-left: 20px;">
                    <li><span style="font-weight: bold;">Mean Reversion:</span> Bollinger Bands assume that prices tend to revert to the mean (middle band), so movements outside the bands often signal a reversion.</li>
                    <li><span style="font-weight: bold;">Breakouts:</span> A price move outside the bands doesn't necessarily indicate overbought or oversold conditions. It could signal increased volatility and the start of a trend.</li>
                    <li>
                        <span style="font-weight: bold;">Width of Bands:</span>
                        <ul style="margin-left: 20px;">
                            <li>Wide bands: High volatility</li>
                            <li>Narrow bands: Low volatility, potentially signaling a consolidation phase or an impending breakout.</li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </h6>

    <h6 style="margin-top: -15px;">
        <span style="font-size: 25px; font-weight: bold;">3. Recommendation Condition:</span>
        <ul style="margin-top: 10px; margin-left: 20px;">
            <li><span style="font-weight: bold;">Strong Buy:</span> RSI < 30 represents strong buy (Dark green).</li>
            <li><span style="font-weight: bold;">Buy:</span> RSI < 40 represents buy (Green).</li>
            <li><span style="font-weight: bold;">Strong Sell:</span> RSI > 70 represents strong sell (Gray).</li>
            <li><span style="font-weight: bold;">Sell:</span> RSI > 60 represents sell (Dark Red).</li>
            <li><span style="font-weight: bold;">No Clear Trading Signals:</span> Maintain current position.</li>
        </ul>
    </h6>
    """,
    unsafe_allow_html=True,
)

st.markdown(
            """
            <h3 style="margin-top: -10px;">💬 Stock Chat Assistant</h3>
            <h5 style="margin-top: 10px; font-size: 25px;">How each prompts are defined?</h5>
            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">1. Technical Analysis:</span> 
                Can you explain the current technical analysis indicators for this stock?
            </h6>

            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">2. Investment Risk:</span> 
                What are the main investment risks for this stock?
            </h6>

            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">3. Market Sentiment:</span> 
                What's the current market sentiment for this stock?
            </h6>

            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">4. Price Targets:</span> 
                What are the potential price targets based on technical analysis?
            </h6>

            <h6 style="margin-top: 5px;">
                <span style="font-size: 18px; font-weight: bold;">5. Trading Strategy:</span> 
                What would be a good trading strategy for this stock?
            </h6>
            
            """,
            unsafe_allow_html=True,
  )
