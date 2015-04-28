# -*- coding: utf-8 -*-

import json

class Kissa:
    def to_json(self):
        return "mau mau mau"

def fix_to_json(obj):
    if hasattr(obj, "to_json"):
        return obj.to_json()
    raise TypeError("Can't serialize %r" % obj)

data = {
    "kissa": "koira",
    "koira": [1, 2, 3],
    "kyllä": True,
}

print(data)
json_data = json.dumps(data, default=fix_to_json)
print(json_data[::-1])
print(data == json.loads(json_data))
data["mau"] = Kissa()
print(json.dumps(data, indent=1, default=fix_to_json))
