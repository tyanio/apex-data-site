<template>
  <BarChart v-bind:chart-data="dataCollection" />
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