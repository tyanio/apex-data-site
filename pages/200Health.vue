<template>
  <BarChart v-bind:chart-data="dataCollection" />
</template>

<script>
import BarChart from "@/components/BarChart.vue";

export default {
  components: {
    BarChart,
  },
  data() {
    return {
      dataCollection: {
        labels: ["flatline", "R-301", "G7"],
        datasets: [
          {
            data: [
              (Math.ceil(200 / 19) * 60) / 600,
              (Math.ceil(200 / 14) * 60) / 810,
              (Math.ceil(200 / 34) * 60) / 240,
            ],
            backgroundColor: ["#6acea8", "#f49a4a", "#f49a4a"],
          },
        ],
      },
    };
  },
};
</script>