Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\user> py
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> import requests
>>> def fetch_exchange_rates():
...     url = "https://api.exchangerate-api.com/v4/latest/USD"
...     try:
...             response = requests.get(url)
...             if response.status_code == 200:
...                     data = response.json()
...                     rates = pd.DataFrame(data["rates"].items(), columns=["Currency", "Rate"])
...                     return rates
...             else:
...                     print(f"Failed to fetch data. HTTP Status: {response.status_code}")
...     except Exception as e:
...             print(f"Error fetching data:{e}")
...     return None
...
>>> def analyze_rates(rates): #process and analyze rates
...     if rates is not None:
...             top_rates = rates.nlargest(5, "Rate")
...             print("Top 5 Exchange Rates:") #get top 5 highest exchange rates
...             print(top_rates)
...     else:
...             print("No data to analyze.")
...
>>> if __name__ == "__main__": #main execution
...     exchange_rates = fetch_exchange_rates()
...     analyze_rates(exchange_rates)
...
Top 5 Exchange Rates:
    Currency      Rate
82       LBP  89500.00
66       IRR  41998.95
150      VND  25516.90
128      SLL  22856.65
81       LAK  21753.73
>>>
