import yfinance as yf
import time
import threading
import subprocess
# Define the ticker

ticker_symbol = input("Enter the yahoo finance ticker symbol")
print("insert ammount of shares")
value = int(input())

#Background thread
def background_input(stop_event):

    while not stop_event.is_set():

        if input() == 'q':

            stop_event.set()
stop_event = threading.Event()
background_thread = threading.Thread(target=background_input, args=(stop_event,))

background_thread.start()

#Clear all prints
def clear_console():

    subprocess.call('clear', shell=True)


clear_console()

#print Stocks
def printer():
    print(f"The latest price of Apple's stock is {latest_price} at {latest_time}\nPress 'q + Enter' to leave the program")


# Fetch data every 2 seconds
while True:
    apple_stock = yf.Ticker(ticker_symbol)
    historical_prices = apple_stock.history(period='1d', interval='1m')
    latest_price = historical_prices['Close'].iloc[-1]
    latest_time = historical_prices.index[-1]
    latest_price = latest_price*value
    printer()
    time.sleep(2)
    clear_console()
    if stop_event.is_set():
        break
background_thread.join()