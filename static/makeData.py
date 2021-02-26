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
    w_data = json.load(fr)

w_names = w_data.keys()

for w_name in w_names:

    w_firemodes = w_data[w_name].keys()

    for w_firemode in w_firemodes:
        # 今はバーストモードは実装しない
        if w_firemode == "burst":
            continue

        i = 0
        data = []
        while True:
            time = i / w_data[w_name][w_firemode]["rpm"] * 60
            total_damage = (i + 1) * w_data[w_name][w_firemode]["basicDamage"]
            damage_data = {"x": time, "y": total_damage}
            data.append(damage_data)
            i += 1
            if total_damage >= 225:
                break

        ttk_data = {"label": w_data[w_name][w_firemode]["jpName"],
                    "borderColor": select_color(w_data[w_name][w_firemode]["ammo"]),
                    "steppedLine": True,
                    "data": data}

        with open("../assets/" + w_name + "-" + w_firemode + "-ttk.json", "w", encoding="utf-8") as fw:
            json.dump(ttk_data, fw, ensure_ascii=False)

# i = 0
# data = []
# while True:
#     time = i / w_data["g7"]["semiauto"]["rpm"] * 60
#     total_damage = (i + 1) * w_data["g7"]["semiauto"]["basicDamage"]
#     damage_data = {"x": time, "y": total_damage}
#     data.append(damage_data)
#     i += 1
#     if total_damage >= 225:
#         break

# ttk_data = {"label": w_data["g7"]["semiauto"]["jpName"],
#             "borderColor": "#6ACEA8",
#             "steppedLine": True,
#             "data": data}

# with open("../assets/g7-ttk.json", "w", encoding="utf-8") as fw:
#     json.dump(ttk_data, fw, ensure_ascii=False)