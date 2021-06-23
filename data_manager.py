import http.client

conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "31e34b8aacmshadf6e5c6aef3fc0p10ef54jsn410a3ed8c725",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

conn.request("GET", "/market/get-charts?symbol=HYDR.ME&interval=5m&range=1d&region=US&comparisons=%5EGDAXI%2C%5EFCHI", headers=headers)
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
