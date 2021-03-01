<template>
  <div>
    <h1>Apex Data Site</h1>
    <WeaponButtons />
    <BarChart />
  </div>
</template>

<script>
import BarChart from "@/components/BarChart.vue";

export default {
  components: {
    BarChart,
  },
};
</script>