# NASDAQ Analysis Script (Casual Edition)

Hey there! So, I was on this super long bus trip, and I ended up writing this Python script. Now, before we go any further, let me make it clear—I don't recommend using this for your stock decisions. Seriously, don't blame me if things go haywire!

## Overview

This script aims to provide a comprehensive analysis of NASDAQ companies, considering financial indicators and valuation concepts to assist in identifying potentially undervalued stocks. It serves as a valuable tool for investors and individuals interested in analyzing the stock market.

## Functionality

1. **Fetch Stock Data:**
   - It grabs financial data for a NASDAQ symbol from the Alpha Vantage API.
   - It pulls out cool stuff like the company's name, sector, description, latest price, and 5-year average price.

2. **Calculate Intrinsic Value:**
   - The script calculates the "intrinsic value" of a stock using some fancy Benjamin Graham formula.
   - It throws in the average price and latest price to estimate what the stock is really worth.

3. **Determine Undervalued Stocks:**
   - This part gets even more interesting. The script figures out if a stock is undervalued using Warren Buffett's and Benjamin Graham's ideas.
   - It compares the latest price with the calculated intrinsic value.
   - If the latest price is lower than the intrinsic value, it's like finding a hidden treasure—the stock is considered undervalued!

4. **Additional Insights and Analysis:**
   - Brace yourself, 'cause there's more. The script provides extra insights and analysis to level up your understanding of NASDAQ companies' valuation.
   - You'll discover the top undervalued stocks and get a sector-wise breakdown.
   - Oh, and we've got some fancy market analysis with stats like total number of stocks, undervalued stocks, average price change, and average annual return. Woohoo!

## Usage

1. Replace `'YOUR_API_KEY'` with your actual Alpha Vantage API key in the code.
2. Run the script in Python.
3. When prompted, enter a NASDAQ symbol to analyze a specific stock.
4. The script will fetch the necessary data, calculate intrinsic value, check if the stock is undervalued, and serve you a wholesome plate of analysis and insights.

**Note:** Make sure you've got a stable internet connection to access the Alpha Vantage API and fetch all those finance goodies.

## Disclaimer

So, there you have it—a script I cooked up during that never-ending bus ride. It's all about analyzing NASDAQ companies and trying to spot those undervalued gems. But hey, take it easy and remember, this is just for fun. Don't go blaming me if things don't turn out as expected!

If you need any more help, feel free to give me a shout!

Created by: JuanPaynor
