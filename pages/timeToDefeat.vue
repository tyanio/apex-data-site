<template>
  <v-container>
    <v-col>
      <v-btn-toggle v-model="selected" @change="toggleHealth()">
        <v-btn icon>
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
        </v-btn>
      </v-btn-toggle>
      <BarChart v-bind:chart-data="dataCollection" />
    </v-col>
  </v-container>
</template>

<script>
import BarChart from "@/components/BarChart.vue";
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
      selected: undefined,
      dataCollection: {},
    };
  },
  methods: {
    toggleHealth: function () {
      console.log(this.selected);
      switch (this.selected) {
        case 0:
          this.dataCollection = damage100Datasets;
          break;
        case 1:
          this.dataCollection = damage150Datasets;
          break;
        case 2:
          this.dataCollection = damage175Datasets;
          break;
        case 3:
          this.dataCollection = damage200Datasets;
          break;
        case 4:
          this.dataCollection = damage225Datasets;
          break;
      }
    },
  },
};
</script>