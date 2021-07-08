<template>
  <v-container>
    <v-col>
      <v-btn-toggle>
        <v-btn icon>
          <v-img height="48" contain src="/icon_shields/level1.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="48" contain src="/icon_shields/level2.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="48" contain src="/icon_shields/level3.png"></v-img>
        </v-btn>
        <v-btn icon>
          <v-img height="48" contain src="/icon_shields/level4.png"></v-img>
        </v-btn>
      </v-btn-toggle>
      <BarChart v-bind:chart-data="dataCollection" />
    </v-col>
  </v-container>
</template>

<script>
import BarChart from "@/components/BarChart.vue";
import ttkDatasets from "@/assets/200damage.json";

export default {
  components: {
    BarChart,
  },
  data() {
    return {
      dataCollection: ttkDatasets,
    };
  },
};
</script>