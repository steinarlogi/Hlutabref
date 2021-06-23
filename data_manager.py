import http.client
import json


class DataConnection:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

        self.headers = {
            'x-rapidapi-key': "31e34b8aacmshadf6e5c6aef3fc0p10ef54jsn410a3ed8c725",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }


    def get_headers(self):
        return self.headers


    def get_connection(self):
        return self.conn


    """
    symbol:
    """
    def get_statistics(self, symbol="JD"):

        if symbol == None or symbol == "":
            return -1

        req = "/stock/v3/get-statistics?symbol=" + symbol
        self.conn.request("GET", req, headers=self.headers)
        res = self.conn.getresponse()

        return json.loads(res.read().decode("utf-8"))


    def get_auto_complete(query="nbe", region="US"):
        self.conn.request("GET", "/market/auto-complete?query="+query+"&region="+region, headers=self.headers)

        res = self.conn.getresponse()
        data = res.read()

        return json.loads(data.decode("utf-8"))

    ################################################################
    #       Getum bætt inn föllum hér sem sækja fleiri hluti       #
    ################################################################
