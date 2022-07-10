import json

data = {"abhay": "lmaoaa"}


def data_commit():
    with open("user_data.json", "w") as f:
        json.dump(data, f)


data.update({"abhayss": "lmaoaa"})
data_commit()
data.update({"abhaaaayss": "lmaoaa"})
data_commit()
