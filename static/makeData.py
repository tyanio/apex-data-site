import json

with open("weapons.json", "r", encoding="utf-8") as fr:
    w_data = json.load(fr)

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

ttk_data = {"label": w_data["g7"]["semiauto"]["jpName"],
            "borderColor": "#6ACEA8",
            "steppedLine": True,
            "data": data}

with open("../assets/g7-ttk.json", "w", encoding="utf-8") as fw:
    json.dump(ttk_data, fw, ensure_ascii=False)