<template>
  <div>
    <h1>Apex Data Site</h1>
    <v-item-group multiple>
      <v-container>
        <v-row>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'heavyDark' : ''"
                class="d-flex align-center pa-5"
                dark
                height="100"
                @click="toggle"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/30-30_Repeater_Icon.png"
                ></v-img>
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition>
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
                @click="toggle"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/Flatline_Icon.png"
                ></v-img>
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition>
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
                @click="toggle"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/G7_Scout_Icon.png"
                ></v-img>
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="6" md="2">
            <v-item v-slot="{ active, toggle }">
              <v-card
                :color="active ? 'energyDark' : ''"
                class="d-flex align-center pa-2"
                dark
                height="100"
                @click="toggle"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/Havoc_Icon.png"
                ></v-img>
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition>
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
                @click="toggle"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/Hemlok_Icon.png"
                ></v-img>
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition>
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
                @click="toggle"
              >
                <v-img
                  max-height="90"
                  contain
                  src="/icon_weapons/R-301_Icon.png"
                ></v-img>
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">
                    Active
                  </div>
                </v-scroll-y-transition>
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
    <BarChart v-bind:datasets="datasets" />
  </div>
</template>

<script>
import BarChart from "@/components/BarChart.vue";
import ttkDatasets from "@/assets/ttk.json";

export default {
  components: {
    BarChart,
  },
  data() {
    return {
      datasets: [ttkDatasets.r301.fullauto, ttkDatasets.flatline.fullauto],
    };
  },
};
</script>