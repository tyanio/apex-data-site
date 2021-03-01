import json


def select_color(ammo_type):
    if ammo_type == "light":
        return "#f49a4a"
    elif ammo_type == "heavy":
        return "#6acea8"
    elif ammo_type == "energy":
        return "#C6DB3A"
    elif ammo_type == "shotgun":
        return "#FE2C00"
    elif ammo_type == "sniper":
        return "#7E85F4"
    else:
        return "#FFFFFF"


with open("weapons.json", "r", encoding="utf-8") as fr:
    data = json.load(fr)

names = data.keys()

ttk_out_data = {}

for name in names:

    firemodes = data[name].keys()
    ttk_fires_data = {}

    for firemode in firemodes:
        # 今はバーストモードは実装しない
        if firemode == "burst":
            continue

        i = 0
        point_data = []
        while True:
            time = i / data[name][firemode]["rpm"] * 60
            total_damage = (i + 1) * data[name][firemode]["basicDamage"]
            damage_data = {"x": time, "y": total_damage}
            point_data.append(damage_data)
            i += 1
            if total_damage >= 225:
                break

        ttk_data = {"label": data[name][firemode]["jpName"],
                    "borderColor": select_color(data[name][firemode]["ammo"]),
                    "steppedLine": True,
                    "data": point_data}

        ttk_fires_data[firemode] = ttk_data

    ttk_out_data[name] = ttk_fires_data

with open("../assets/ttk.json", "w", encoding="utf-8") as fw:
    json.dump(ttk_out_data, fw, ensure_ascii=False)

# i = 0
# data = []
# while True:
#     time = i / data["g7"]["semiauto"]["rpm"] * 60
#     total_damage = (i + 1) * data["g7"]["semiauto"]["basicDamage"]
#     damage_data = {"x": time, "y": total_damage}
#     data.append(damage_data)
#     i += 1
#     if total_damage >= 225:
#         break

# ttk_data = {"label": data["g7"]["semiauto"]["jpName"],
#             "borderColor": "#6ACEA8",
#             "steppedLine": True,
#             "data": data}

# with open("../assets/g7-ttk.json", "w", encoding="utf-8") as fw:
#     json.dump(ttk_data, fw, ensure_ascii=False)
