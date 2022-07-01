import pass_generator
import datetime
import json

data = {
    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "auth": pass_generator.authquator(""),
}
data_main = json.dumps(data, indent=4)
with open("auth_data.json", "w") as f:
    f.write(data_main)
