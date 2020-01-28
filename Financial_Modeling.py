import requests
import json

BSresponse = requests.get("https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/MSFT")
ISresponse = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/MSFT")

BS = json.loads(BSresponse.text)
IS  = json.loads(ISresponse.text)

#Net Income
print("2019 SE:",IS['financials'][0]['Net Income'])
print("2018 SE:",IS['financials'][1]['Net Income'])
print("2017 SE:",IS['financials'][2]['Net Income'])

#Sales

#Assets

#Shareholder Equity Values
print("2019 SE:",BS['financials'][0]['Total shareholders equity'])
print("2018 SE:",BS['financials'][1]['Total shareholders equity'])
print("2017 SE:",BS['financials'][2]['Total shareholders equity'])

