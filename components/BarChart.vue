<script>
import { Line } from "vue-chartjs";
import ttkDatasets from "@/assets/ttk.json";
export default {
  props: ["datasets"],
  extends: Line,
  data() {
    return {
      chartdata: {
        datasets: this.datasets,
      },
      options: {
        scales: {
          xAxes: [
            {
              type: "linear",
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
