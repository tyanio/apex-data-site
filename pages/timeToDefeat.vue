<template>
  <v-container>
    <v-col>
      <v-btn-toggle v-model="selected" @change="toggleHealth()">
        <v-btn>Level0</v-btn>
        <v-btn>Level1</v-btn>
        <v-btn>Level2</v-btn>
        <v-btn>Level3</v-btn>
        <v-btn>Level4</v-btn>
        <!-- アイコンボタン -->
        <!-- <v-btn icon>
          <v-img height="36" contain src="/icon_shields/level1.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="36" contain src="/icon_shields/level1.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="36" contain src="/icon_shields/level2.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="36" contain src="/icon_shields/level3.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="36" contain src="/icon_shields/level4.png"></v-img>
        </v-btn> -->
      </v-btn-toggle>
      <v-slider v-model="hitRate" step="25" thumb-label ticks></v-slider>
      <BarChart v-bind:chart-data="dataCollection" />
    </v-col>
  </v-container>
</template>

<script>
import BarChart from "@/components/BarChart.vue";
import wdata from "@/assets/weapons.json";
import damage100Datasets from "@/assets/100damage.json";
import damage150Datasets from "@/assets/150damage.json";
import damage175Datasets from "@/assets/175damage.json";
import damage200Datasets from "@/assets/200damage.json";
import damage225Datasets from "@/assets/225damage.json";

export default {
  components: {
    BarChart,
  },
  data() {
    return {
      hitRate: undefined,
      selected: undefined,
      dataCollection: {},
    };
  },
  methods: {
    toggleHealth: function () {
      // switch (this.selected) {
      //   case 0:
      //     this.dataCollection = damage100Datasets;
      //     break;
      //   case 1:
      //     this.dataCollection = damage150Datasets;
      //     break;
      //   case 2:
      //     this.dataCollection = damage175Datasets;
      //     break;
      //   case 3:
      //     this.dataCollection = damage200Datasets;
      //     break;
      //   case 4:
      //     this.dataCollection = damage225Datasets;
      //     break;
      // }

      var sheild = 0;
      switch (this.selected) {
        case 0:
          sheild = 0;
          break;
        case 1:
          sheild = 50;
          break;
        case 2:
          sheild = 75;
          break;
        case 3:
          sheild = 100;
          break;
        case 4:
          sheild = 125;
          break;
      }

      var unsorted_data = [];

      for (var name in wdata) {
        // console.log(name);
        var firemodes = wdata[name];
        // console.log(firemodes);
        for (var firemode in firemodes) {
          // console.log(firemode);
          var weapon = wdata[name][firemode];
          // console.log(weapon);

          // 現在使えない武器は飛ばす
          if (weapon["isAvailable"] == false) {
            continue;
          }

          // データが抜けているところは飛ばす
          if (weapon["basicDamage"] == null || weapon["rpm"] == null) {
            continue;
          }

          var basicDamage = 0;

          // 弾がいっぱい出るやつはかける
          if (weapon["bulletPerShot"] != undefined) {
            basicDamage = wdata[name][firemode]["basicDamage"] * wdata;
          } else {
            basicDamage = weapon["basicDamage"];
          }

          var rpm = 0;
          var magazineSize = 0;
          var reloadTime = 1000;

          // shotgunはショットガンボルトによってRPMが変わるためとりあえずボルトなしの状態を_rpmに代入
          // ショットガンはマガジンサイズが固定のためそのまま取り出す
          // リロードタイムも同様
          if (weapon["type"] == "SG") {
            // ひとまずショットガンボルトなしの状態で考える
            rpm = weapon["rpm"][0];
            magazineSize = weapon["magazineSize"];
            reloadTime = weapon["reloadTime"];
          } else {
            rpm = weapon["rpm"];
            // ひとまず拡張マガジンなしの状態で考える
            magazineSize = weapon["magazineSize"][0];
            reloadTime = weapon["reloadTime"][0];
          }

          console.log

          // wip jsonに入れるためにデータの格納の仕方とソートを考える
          unsorted_data.push(
            weapon["jpName"],
            calTimeToDefeat(shield, basicDamage, rpm, magazineSize, reloadTime),
            selectColor(weapon['ammo'])
          );
        }
      }
    },
    calTimeToDefeat: function (
      shield,
      basicDamage,
      rpm,
      magazineRounds,
      reloadTime
    ) {
      if (reloadTime == undefined) {
        reloadTime == 1000;
      }

      var health = 100;

      var needsRounds = Math.ceil((health + shield) / basicDamage);
      var needsMagazines = Math.floor(needsRounds / magazineRounds);

      if (needsMagazines > 1) {
        return (
          Math.round(
            ((needsRounds - 1) * 60) / rpm + reloadTime * needsMagazines * 1000
          ) / 1000
        );
      } else {
        return Math.round((((needsRounds - 1) * 60) / rpm) * 1000) / 1000;
      }
    },
    selectColor: function (ammoType) {
      switch (ammoType) {
        case "light":
          return "#f49a4a";
        case "heavy":
          return "#6acea8";
        case "energy":
          return "#C6DB3A";
        case "shotgun":
          return "#FE2C00";
        case "sniper":
          return "#7E85F4";
        case "special":
          return "#EE0047";
        default:
          return "#FFFFFF";
      }
    },
  },
};
</script>