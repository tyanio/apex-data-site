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

_names = wdata.keys()

_shields = [0, 50, 75, 100, 125]
_health = 100


def cal_time_to_defeat(health, shield, basic_damage, rpm, magagine_rounds, reload_time):
    # todo リロード時間が分からないデータが多いのでひとまずデフォルトで0にしておく
    if reload_time == None:
        reload_time = 0

    _needs_rounds = math.ceil((health + shield) / basic_damage)
    _needs_magagines = _needs_rounds // magagine_rounds

    if _needs_magagines > 1:
        return round((_needs_rounds - 1) * 60 / rpm + reload_time * _needs_magagines, 3)
    else:
        return round((_needs_rounds - 1) * 60 / rpm, 3)


for _shield in _shields:

    _unsorted_data = []

    for _name in _names:

        _firemodes = wdata[_name].keys()

        for _firemode in _firemodes:
            # 現在使えない武器は飛ばす
            if wdata[_name][_firemode]["isAvailable"] == False:
                continue
            # データが抜けているところは飛ばす
            if wdata[_name][_firemode]["basicDamage"] == None or wdata[_name][_firemode]["rpm"] == None:
                continue

            _basic_damage = 0
            _rpm = 0

            # 弾がいっぱい出るやつはかける
            if "bulletsPerShot" in wdata[_name][_firemode]:
                _basic_damage = wdata[_name][_firemode]["basicDamage"] * wdata[_name][_firemode]["bulletsPerShot"]
            else:
                _basic_damage = wdata[_name][_firemode]["basicDamage"]

            # shotgunはショットガンボルトによってRPMが変わるためとりあえずボルトなしの状態を_rpmに代入
            # ショットガンはマガジンサイズが固定のためそのまま取り出す
            # リロードタイムも同様
            if wdata[_name][_firemode]["type"] == "SG":
                _rpm = wdata[_name][_firemode]["rpm"][0]
                _magazine_size = wdata[_name][_firemode]["magazineSize"]
                _reload_time = wdata[_name][_firemode]["reloadTime"]
            else:
                _rpm = wdata[_name][_firemode]["rpm"]
                # ひとまず拡張マガジンなしの状態で考える
                _magazine_size = wdata[_name][_firemode]["magazineSize"][0]
                _reload_time = wdata[_name][_firemode]["reloadTime"][0]

            _each_weapon_data = [wdata[_name][_firemode]["jpName"],
                                 cal_time_to_defeat(_health, _shield, _basic_damage, _rpm, _magazine_size, _reload_time),
                                 select_color(wdata[_name][_firemode]["ammo"])]

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

    with open("../assets/" + str(_shield + _health) + "damage.json", "w", encoding="utf-8") as fw:
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
