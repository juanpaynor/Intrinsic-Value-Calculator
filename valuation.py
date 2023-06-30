import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'Get your API key here https://www.alphavantage.co/'

# Function to fetch stock data for a given symbol
def get_stock_data(symbol):
    overview_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
    overview_response = requests.get(overview_url)

    try:
        overview_data = overview_response.json()
    except ValueError:
        print(f"Error decoding JSON response for symbol: {symbol}")
        return None

    if 'Symbol' not in overview_data:
        print(f"No data available for symbol: {symbol}")
        return None

    symbol = overview_data['Symbol']
    name = overview_data.get('Name', '')
    sector = overview_data.get('Sector', '')
    description = overview_data.get('Description', '')

    history_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={API_KEY}'
    history_response = requests.get(history_url)

    try:
        history_data = history_response.json()
    except ValueError:
        print(f"Error decoding JSON response for symbol: {symbol}")
        return None

    if 'Time Series (Daily)' not in history_data:
        print(f"No historical data available for symbol: {symbol}")
        return None

    time_series = history_data['Time Series (Daily)']

    # Extract the latest closing price and calculate the 5-year average closing price
    closing_prices = [float(data['4. close']) for data in time_series.values()]
    latest_price = closing_prices[0]
    avg_price = sum(closing_prices[-1250:]) / 1250  # Assuming 250 trading days per year over 5 years

    return symbol, name, sector, description, latest_price, avg_price

# Function to calculate the intrinsic value using Benjamin Graham's formula
def calculate_intrinsic_value(avg_price, latest_price):
    return (avg_price + 2 * latest_price) / 3

# Function to determine if a stock is undervalued based on Warren Buffett's and Benjamin Graham's ideas
def is_undervalued(intrinsic_value, latest_price):
    return latest_price < intrinsic_value

# Main function for analyzing NASDAQ companies
def analyze_nasdaq_companies():
    symbols = []
    while len(symbols) < 1:
        symbol = input("Enter a NASDAQ symbol: ")
        symbols.append(symbol)

    # Initialize empty lists for data
    names = []
    sectors = []
    descriptions = []
    latest_prices = []
    avg_prices = []
    intrinsic_values = []
    undervalued = []
    price_changes = []
    annual_returns = []

    for symbol in symbols:
        # Fetch stock data for the symbol
        stock_data = get_stock_data(symbol)
        if stock_data is not None:
            symbol, name, sector, description, latest_price, avg_price = stock_data

            # Append data to respective lists
            names.append(name)
            sectors.append(sector)
            descriptions.append(description)
            latest_prices.append(latest_price)
            avg_prices.append(avg_price)

            # Calculate intrinsic value
            intrinsic_value = calculate_intrinsic_value(avg_price, latest_price)
            intrinsic_values.append(intrinsic_value)

            # Determine if the stock is undervalued
            undervalued_flag = is_undervalued(intrinsic_value, latest_price)
            undervalued.append(undervalued_flag)

            # Calculate the price change and annual return
            price_change = latest_price - avg_price
            annual_return = (latest_price - avg_price) / avg_price * 100
            price_changes.append(price_change)
            annual_returns.append(annual_return)

    # Create a DataFrame to store the collected data
    data = pd.DataFrame({
        'Symbol': symbols,
        'Company Name': names,
        'Sector': sectors,
        'Description': descriptions,
        'Latest Price': latest_prices,
        '5-Year Avg Price': avg_prices,
        'Intrinsic Value': intrinsic_values,
        'Undervalued': undervalued,
        'Price Change': price_changes,
        'Annual Return (%)': annual_returns
    })

    # Sort the data by Intrinsic Value in descending order
    data = data.sort_values(by='Intrinsic Value', ascending=False)

    # Print the analysis result
    print("---------- NASDAQ Companies Analysis Report ----------")
    print(data.to_string(index=False))
    print("----------------------------------------------------")

    # Additional Insights and Analysis
    print("\nAdditional Insights:")
    print("--------------------")

    # Top Undervalued Stocks
    top_undervalued_stocks = data[data['Undervalued'] == True]
    if len(top_undervalued_stocks) > 0:
        print("\nTop Undervalued Stocks:")
        print(top_undervalued_stocks.to_string(index=False))
    else:
        print("\nNo undervalued stocks found.")

    # Sector-wise Analysis
    sector_analysis = data.groupby('Sector').agg({'Symbol': 'count', 'Intrinsic Value': 'mean', 'Price Change': 'mean'})
    sector_analysis = sector_analysis.rename(columns={'Symbol': 'Stock Count', 'Intrinsic Value': 'Avg Intrinsic Value',
                                                      'Price Change': 'Avg Price Change'})
    print("\nSector-wise Analysis:")
    print(sector_analysis.to_string())

    # Overall Market Analysis
    market_analysis = {
        'Total Stocks': len(data),
        'Undervalued Stocks': len(data[data['Undervalued'] == True]),
        'Average Price Change': data['Price Change'].mean(),
        'Average Annual Return (%)': data['Annual Return (%)'].mean()
    }
    print("\nOverall Market Analysis:")
    for key, value in market_analysis.items():
        print(f"{key}: {value}")

# Execute the analysis
analyze_nasdaq_companies()
