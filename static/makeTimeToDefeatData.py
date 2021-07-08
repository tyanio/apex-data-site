import json
import math
import numpy
from enum import Enum

# class AmmoColor(Enum):
#     LIGHT = "#f49a4a"
#     HEAVY = "#6acea8"
#     ENERGY = "#C6DB3A"
#     SHOTGUN = "#FE2C00"
#     SNIPER = "#7E85F4"
#     SPECIAL = "#EE0047"


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

shields = [0, 50, 75, 100, 125]
health = 100

for shield in shields:

    _unsorted_data = []

    for name in names:

        firemodes = wdata[name].keys()
        # data_200health_firemodes = {}

        for firemode in firemodes:
            # 現在使えない武器は飛ばす
            if wdata[name][firemode]["isAvailable"] == False:
                continue
            # データが抜けているところは飛ばす
            if wdata[name][firemode]["basicDamage"] == None or wdata[name][firemode]["rpm"] == None:
                continue

            _basic_damage = 0
            _rpm = 0

            # 弾がいっぱい出るやつはかける
            if "bulletsPerShot" in wdata[name][firemode]:
                _basic_damage = wdata[name][firemode]["basicDamage"] * wdata[name][firemode]["bulletsPerShot"]
            else:
                _basic_damage = wdata[name][firemode]["basicDamage"]

            # shotgunはショットガンボルトによってRPMが変わるためとりあえずボルトなしの状態を_rpmに代入
            if wdata[name][firemode]["type"] == "SG":
                _rpm = wdata[name][firemode]["rpm"][0]
            else:
                _rpm = wdata[name][firemode]["rpm"]

            _each_weapon_data = [wdata[name][firemode]["jpName"],
                                 round((math.ceil((health + shield) / _basic_damage) - 1) * 60 / _rpm, 3),
                                 select_color(wdata[name][firemode]["ammo"])]

            _unsorted_data.append(_each_weapon_data)

    sorted_data = sorted(_unsorted_data, key=lambda i: i[1])

    processed_data_t = numpy.array(sorted_data).T.tolist()

    data_time_to_defeat = {
        "labels": processed_data_t[0],
        "datasets": [{
            "data": processed_data_t[1],
            "backgroundColor": processed_data_t[2]
        }]
    }

    with open("../assets/" + str(shield + health) + "damage.json", "w", encoding="utf-8") as fw:
        json.dump(data_time_to_defeat, fw, ensure_ascii=False)

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
