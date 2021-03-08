import json
import math
import numpy


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
    elif ammo_type == "special":
        return "#EE0047"
    else:
        return "#FFFFFF"


with open("weapons.json", "r", encoding="utf-8") as fr:
    wdata = json.load(fr)

names = wdata.keys()

health = 200

_labels = []
_data = []
_backgroundColor = []

_unprocessed_data = []

for name in names:

    firemodes = wdata[name].keys()
    # data_200health_firemodes = {}

    for firemode in firemodes:
        # データが抜けているところは飛ばす
        if wdata[name][firemode]["basicDamage"] == None or wdata[name][firemode]["rpm"] == None:
            continue

        _basic_damage = wdata[name][firemode]["basicDamage"]

        # 弾がいっぱい出るやつはかける
        if "bulletsPerShot" in wdata[name][firemode]:
            _basic_damage *= wdata[name][firemode]["bulletsPerShot"]

        _each_weapon_data = [wdata[name][firemode]["jpName"], (math.ceil(
            health / _basic_damage) - 1) * 60 / wdata[name][firemode]["rpm"], select_color(wdata[name][firemode]["ammo"])]

        # _labels.append(wdata[name])
        # _data.append(math.ceil(health / wdata[name][firemode]["basicDamage"]) * 60 / wdata[name][firemode]["rpm"])
        # _backgroundColor = select_color(wdata[name][firemode]["ammo"])

        _unprocessed_data.append(_each_weapon_data)

processed_data = sorted(_unprocessed_data, key=lambda i: i[1])

processed_data_t = numpy.array(processed_data).T.tolist()

data_200health = {
    "labels": processed_data_t[0],
    "datasets": [{
        "data": processed_data_t[1],
        "backgroundColor": processed_data_t[2]
    }]
}

with open("../assets/200health.json", "w", encoding="utf-8") as fw:
    json.dump(data_200health, fw, ensure_ascii=False)

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
