<template>
  <div>
    <h1>Apex Data Site</h1>
    <v-item-group multiple>
      <v-container>
        <v-row>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'energyDark' : ''"
                class="d-flex align-center pa-2"
                dark
                height="100"
                @click="toggle(), toggleWeapons('havoc.fullauto', active)"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/Havoc_Icon.png"
                ></v-img>
                <!-- <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition> -->
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'heavyDark' : ''"
                class="d-flex align-center pa-2"
                dark
                height="100"
                @click="toggle(), toggleWeapons('flatline.fullauto', active)"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/Flatline_Icon.png"
                ></v-img>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'lightDark' : ''"
                class="d-flex align-center pa-2"
                dark
                height="100"
                @click="toggle(), toggleWeapons('g7.semiauto', active)"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/G7_Scout_Icon.png"
                ></v-img>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'heavyDark' : ''"
                class="d-flex align-center pa-2"
                dark
                height="100"
                @click="toggle(), toggleWeapons('hemlok.semiauto', active)"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/Hemlok_Icon.png"
                ></v-img>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'lightDark' : ''"
                class="d-flex align-center pa-2"
                dark
                height="100"
                @click="toggle(), toggleWeapons('r301.fullauto', active)"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/R-301_Icon.png"
                ></v-img>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'heavyDark' : ''"
                class="d-flex align-center pa-5"
                dark
                height="100"
                @click="toggle(), toggleWeapons('repeater.semiauto', active)"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/30-30_Repeater_Icon.png"
                ></v-img>
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
    <StepChart v-bind:chart-data="dataCollection" />
  </div>
</template>

<script>
import StepChart from "@/components/StepChart.vue";
import ttkDatasets from "@/assets/ttk.json";

export default {
  components: {
    StepChart,
  },
  data() {
    return {
      dataCollection: {},
    };
  },
  methods: {
    toggleWeapons: function (name, active) {
      var _dataCollection = { ...this.dataCollection };
      if (name == "havoc.fullauto") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.havoc.fullauto);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.havoc.fullauto),
            1
          );
        }
      }
      if (name == "flatline.fullauto") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.flatline.fullauto);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.flatline.fullauto),
            1
          );
        }
      }
      if (name == "flatline.anvilReceiver") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.flatline.anvilReceiver);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(
              ttkDatasets.flatline.anvilReceiver
            ),
            1
          );
        }
      }
      if (name == "g7.semiauto") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.g7.semiauto);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.g7.semiauto),
            1
          );
        }
      }
      if (name == "hemlok.semiauto") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.hemlok.semiauto);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.hemlok.semiauto),
            1
          );
        }
      }
      if (name == "r301.fullauto") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.r301.fullauto);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.r301.fullauto),
            1
          );
        }
      }
      if (name == "r301.anvilReceiver") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.r301.anvilReceiver);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.r301.anvilReceiver),
            1
          );
        }
      }
      if (name == "repeater.semiauto") {
        if (!active) {
          _dataCollection.datasets.push(ttkDatasets.repeater.semiauto);
        } else {
          _dataCollection.datasets.splice(
            _dataCollection.datasets.indexOf(ttkDatasets.repeater.semiauto),
            1
          );
        }
      }

      this.dataCollection = _dataCollection;
    },
    // setData: function () {
    //   var _dataCollection = {
    //     datasets: [],
    //   };
    //   if (this.isAcitive["r301.fullauto"]) {
    //     _dataCollection.datasets.push(ttkDatasets.r301.fullauto);
    //   } else {
    //     delete _dataCollection.datasets.indexOf(ttkDatasets.r301.fullauto);
    //   }
    //   this.dataCollection = _dataCollection;
    // },
  },
};
</script>