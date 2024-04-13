# Cointegrated Pairs Trading Bot

## Project objectives

Develop a bot that analyzes the market and finds cointegrated currency pairs, automatically opening and closing transactions.

## Project description

I am taking a course on trading bots, specifically focusing on using Python to interact with the DYDX Layer 2 Ethereum trading exchange. The course teaches how to run a trading bot on AWS Elastic Cloud Compute (EC2) and emphasizes utilizing statistical arbitrage opportunities in Pairs Trading. This strategy is particularly valuable because it takes advantage of the close relationship between various cryptocurrencies in terms of price behavior.

The trading bot I am working on can send notifications via Telegram, providing live updates on the script's performance. It offers the following functionalities:

1. Automatically close any existing open positions.
2. Identify cointegrated (linked Crypto pairs) for trading and determine whether it is statistically profitable to open a trade.
3. Manage and monitor open positions, seeking appropriate exit opportunities.
4. Discover and execute new trading opportunities.
5. Provide alerts if any issues or errors arise.
6. Run the bot continuously on AWS EC2 without needing to keep my laptop running.


## Tasks
1. Set up a virtual environment for the project;
2. Connecting to the DYDX crypto exchange using the API;
3. Implement the functionality to automatically close any open positions;
4. Develop a method to find cointegrated crypto pairs for trading;
5. Create functions to manage and monitor open positions for appropriate exit opportunities;
6. Implement logic to discover and execute new trading opportunities;
7. Set up an error handling system to provide alerts if any issues or errors occur;
8. Test the bot and ensure its functionality is working as intended;
9.  Create a Telegram bot and obtain the API credentials;
10. Connect the Telegram bot to the trading bot to receive live notifications;
11. Deploy the trading bot on AWS Elastic Cloud Compute (EC2)


## Conclusion

At this stage, the bot is running on a local server on a test account. The bot can analyze the market, find cointegrated pairs, and open and close trades. 
The bot shows unstable trading success. It is necessary to adjust the selection of cointegrated currency pairs.

## Further development

- Adjust the selection of cointegrated currency pairs;
- Add a cryptocurrency volatility analysis function;
- Deploy the bot on AWS Elastic Cloud Compute (EC2).

## Skills and tools 

* Data extraction
* Python
* Pandas
* NumPy
* Virtual environments
* DYDX API
* Statistical arbitrage
* Telegram API
  
## Project status
- [x] Starting the bot
- [ ] Bot testing in progress
- [ ] Bot tuning
- [ ] Deploy the bot on Cloud Compute
