stocks_dict = {
    "AAPL": "$217.49" ,
    "NVDA": "$112.28" ,
    "GOOG": "$169.16" ,
    "AMZN": "$179.85" ,
    "META": "$453.41" ,
    "BRK/A": "$649950" ,
    "TSLA": "$220.25" ,
    "JPM": "$208.67" ,
    "WMT": "70.02" ,
    "TGT": "$146.29"
}

WELCOME_MSG = "Hello! Welcome to the stock information exchange!\n"

def getstockinfo(stock):
    ERROR_MSG = f"\nSorry! Stock {stock} is not currently in our database. Please try again.\n"
    stock_price = stocks_dict.get(stock, ERROR_MSG)
    if stock_price == ERROR_MSG:
        return stock_price
    else:
        return f'{stock}\'s current stock price is: {stock_price}'

def main():
    print(WELCOME_MSG)

    while True:
        userStock = input(
            '\nTo begin, please enter a ticker symbol for the stock you would like to search up. For an entire list of '
            'our current database, please type LIST. To end the program, type END\n').upper()
        if userStock == "LIST":
            for stock in stocks_dict:
                print(stock)
        elif userStock == 'END':
            print('\nGoodbye!')
            exit()
        else:
            print(getstockinfo(userStock))

main()
