import streamlit as st
import requests

# Set page configuration
st.set_page_config(layout="wide", page_title="Stock Insights", page_icon="📈")

# Hide streamlit navigation bar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)

# Main banner
st.markdown(
    """
    <style>
        .main-banner {
            background-color: #FFFFFF;
            padding: 30px;
            text-align: center;
            border-radius: 30px;
            border: 5px dotted black;
            font-size: 20px;
            font-family: Arial, sans-serif;
            font-weight: bold;
            color: #000000;
            margin-bottom: 20px;
        }
    </style>
    <div class="main-banner">
        This product is for informational purposes only and should not be considered financial advice. Please note that past performance is not indicative of future results. Investments carry inherent risks, including the potential loss of principal. Consult with a qualified financial advisor to assess your individual circumstances before making any investment decisions.
    </div>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    """
    <div style="background-color:#FFFFFF; padding:15px; border-radius:10px; text-align:Center; font-size:30px; font-family: Arial, sans-serif; font-weight:bold; color:#000000; margin-bottom: 10px;">
        Simply enter a stock ticker to fetch detailed insights
    </div>
""",
    unsafe_allow_html=True,
)

# Initialize session state
if "stock_info" not in st.session_state:
    st.session_state.stock_info = None
if "selected_ticker" not in st.session_state:
    st.session_state.selected_ticker = None


# Helper Functions
def format_large_number(number_str):
    try:
        number = int(number_str)
        if number >= 1_000_000_000:
            return f"{number / 1_000_000_000:.2f}B"
        elif number >= 1_000_000:
            return f"{number / 1_000_000:.2f}M"
        return f"{number:,}"
    except ValueError:
        return "N/A"


def format_percentage(value):
    try:
        return f"{float(value) * 100:.2f}%"
    except ValueError:
        return "N/A"


def add_dollar_sign(value):
    try:
        return f"${float(value):,.2f}"
    except ValueError:
        return "N/A"


def get_stock_info(ticker):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey=I0UIP5S724XG4FDT"
    try:
        response = requests.get(url)
        print(response.status_code)
        print(response.json())

        if response.status_code == 200:
            data = response.json()
            if "Symbol" in data:
                return {
                    "Company Name": data.get("Name", "N/A"),
                    "Sector": data.get("Sector", "N/A"),
                    "Industry": data.get("Industry", "N/A"),
                    "Country": data.get("Country", "N/A"),
                    "Description": data.get("Description", "N/A"),
                    "Market Cap": format_large_number(
                        data.get("MarketCapitalization", "N/A")
                    ),
                    "Dividend Yield": format_percentage(
                        data.get("DividendYield", "N/A")
                    ),
                    "52-Week High": add_dollar_sign(data.get("52WeekHigh", "N/A")),
                    "52-Week Low": add_dollar_sign(data.get("52WeekLow", "N/A")),
                    "Currency": data.get("Currency", "N/A"),
                    "Exchange": data.get("Exchange", "N/A"),
                }
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
    return None


# Main layout with columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Input field for stock ticker
    ticker = st.text_input(
        "Enter Stock Ticker",
        placeholder="e.g., AAPL, TSLA, MSFT",
        help="Enter a stock ticker symbol to fetch detailed insights.",
    )

    # Fetch data button
    if st.button("Fetch Insights", use_container_width=True):
        if ticker:
            with st.spinner("Fetching stock information..."):
                stock_info = get_stock_info(ticker.upper())
                if stock_info:
                    st.session_state.stock_info = stock_info
                    st.session_state.selected_ticker = ticker.upper()
                    st.success(
                        f"Stock information successfully fetched for {ticker.upper()}"
                    )
                else:
                    st.error(
                        "Unable to fetch stock information. Please check the ticker symbol."
                    )
        else:
            st.warning("Please enter a stock ticker symbol.")

# Display stock information if available
if st.session_state.stock_info:
    st.markdown(
        """
        <div style="background-color:#FFFFFF; padding:10px; border-radius:10px; margin:20px 0;">
            <h2 style="text-align:center; color:black; font-size: 40px;margin-bottom: -10px;">
                Stock Analysis for {}
            </h2>
        </div>
    """.format(
            st.session_state.selected_ticker
        ),
        unsafe_allow_html=True,
    )

    # Display information in a grid
    col1, col2 = st.columns(2)

    info = st.session_state.stock_info

    with col1:
        st.markdown("### Company Overview")
        st.markdown(f"**Company Name:** {info['Company Name']}")
        st.markdown(f"**Sector:** {info['Sector']}")
        st.markdown(f"**Industry:** {info['Industry']}")
        st.markdown(f"**Country:** {info['Country']}")
        st.markdown(f"**Exchange:** {info['Exchange']}")
        st.markdown(f"**Currency:** {info['Currency']}")

    with col2:
        st.markdown("### Financial Metrics")
        st.markdown(f"**Market Cap:** {info['Market Cap']}")
        st.markdown(f"**Dividend Yield:** {info['Dividend Yield']}")
        st.markdown(f"**52-Week High:** {info['52-Week High']}")
        st.markdown(f"**52-Week Low:** {info['52-Week Low']}")

    st.markdown("### Company Description")
    st.markdown(info["Description"])

    # Proceed to analysis button
    if st.button("Proceed to Detailed Analysis and Forecasting", use_container_width=True):
        st.switch_page("pages/Layer03_Stock_Analysis&Forecasting.py")

# Back to home button
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("Layer01_Landing_Page.py")

# Footer
st.markdown(
    """
    <div style="position:fixed; bottom:0; left:0; right:0; background-color:#f8f9fa; text-align:center; padding:10px; font-size:14px; font-weight:bold; font-family:Arial, sans-serif; color:black;">
        All rights reserved by Aiden Choi for ICSP © 2025
    </div>
""",
    unsafe_allow_html=True,
)
