import json

from numpy import void


def login_detector():
    f = open("auth_data.json")
    auth_json_data = json.load(f)
    if isinstance(auth_json_data, dict):
        try:
            if auth_json_data["auth"] == auth_json_data["auth"]:
                pass
            else:
                with open("errors.txt", "w") as f:
                    f.write("Authentication Failed due to Missmatch of data")
            pass
        except Exception as e:
            with open("errors.txt", "w") as f:
                f.write(e)
    else:
        pass
    pass

