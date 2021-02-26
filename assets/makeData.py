import json

# encodingのところは後で消す
# file = open("../static/weapons.json", "r", encoding="utf-8_sig")

file = open("../static/weapons.json", "r")
w_data = json.load(file)

# print("{}".format(json.dumps(w_data["g7"]["semiauto"], indent=4)))

i = 0
data = []
while True:
    time = i / w_data["g7"]["semiauto"]["rpm"] * 60
    total_damage = (i + 1) * w_data["g7"]["semiauto"]["basicDamage"]
    damage_data = {"x": time, "y": total_damage}
    data.append(damage_data)
    i += 1
    if total_damage >= 225:
        break

# print(data)

ttk_data = {"label": w_data["g7"]["semiauto"]["jpName"],
            "borderColor": "#6ACEA8",
            "steppedLine": True,
            "data": data}

# print(ttk_data)

fs = open("../static/havoc-ttk.json", "w")
json.dump(ttk_data, fs)