import pass_generator
import datetime
import json

passw = pass_generator.authquator("passw")

auth_data = {"time": int(datetime.datetime.now().hour), "authcode": passw}
with open("auth_data.json", "a+") as f:
    json.dump(auth_data, f)
