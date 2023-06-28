NASDAQ Companies Analysis Script

This Python script allows you to analyze the NASDAQ companies using financial data and determine if they are undervalued based on Benjamin Graham's and Warren Buffett's ideas.

Functionality:

1. Fetch Stock Data:
   - The program fetches the financial data for a given NASDAQ symbol using the Alpha Vantage API.
   - It retrieves the company's name, sector, description, latest price, and 5-year average price.

2. Calculate Intrinsic Value:
   - The script calculates the intrinsic value of a stock using Benjamin Graham's formula.
   - It combines the average price and latest price to estimate the stock's fair value.

3. Determine Undervalued Stocks:
   - The program determines if a stock is undervalued based on Warren Buffett's and Benjamin Graham's ideas.
   - It compares the latest price with the calculated intrinsic value.
   - If the latest price is lower than the intrinsic value, the stock is considered undervalued.

4. Additional Insights and Analysis:
   - The script provides additional insights and analysis to enhance the understanding of the NASDAQ companies' valuation.
   - It identifies the top undervalued stocks and presents a sector-wise analysis.
   - The overall market analysis provides key statistics such as the total number of stocks, undervalued stocks, average price change, and average annual return.

Usage:
1. Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key in the code.
2. Run the script in a Python environment.
3. Enter a NASDAQ symbol when prompted to perform analysis for a specific stock.
4. The script will fetch the necessary data, calculate intrinsic value, determine if the stock is undervalued, and provide comprehensive analysis and insights.

Note: Ensure you have a stable internet connection to access the Alpha Vantage API and retrieve the required financial data.

---

This script aims to provide a comprehensive analysis of NASDAQ companies, considering financial indicators and valuation concepts to assist in identifying potentially undervalued stocks. It serves as a valuable tool for investors and individuals interested in analyzing the stock market.

Please let me know if you need further assistance!

Created by: JuanPaynor
