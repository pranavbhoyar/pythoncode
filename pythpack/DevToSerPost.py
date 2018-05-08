import json
import urllib3

class DevToSerPost:

    def __init__(self):
        self.url = "http://192.168.0.113:8000/recreq/"

    def getrequest(self, App_Id, API_Key, Website_name, username, Phone_No, Email, City, State, Country):
        try:
            isinstance(username, bool)
            isinstance(Phone_No, bool)
            isinstance(Email, bool)
            isinstance(City,  bool)
            isinstance(State, bool)
            isinstance(Country, bool)
            encoded_body = json.dumps({
                    "apikey": str(API_Key),
                    "appid": str(App_Id),
                    "websitename": str(Website_name),
                    "username": str(username),
                    "phoneno": str(Phone_No),
                    "email": str(Email),
                    "city": str(City),
                    "state": str(State),
                    "country": str(Country)
                })
            #print(encoded_body.get("appid"))
            http = urllib3.PoolManager()
            r=http.request('POST',self.url,
                           headers={'Content-Type':'application/json'},
                           body=encoded_body)
            #print(r.data)
        except Exception as e:
            print(format(e))
            print("Developer must send request arguments as boolean values only")
        else:
            print("Post request sent to server")
            
