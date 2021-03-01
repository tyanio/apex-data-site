<template>
  <div>
    <h1>Apex Data Site</h1>
    <WeaponButtons />
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
      datasets: [ttkDatasets.r301.fullauto]
    }
  }
};
</script>