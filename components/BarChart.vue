<script>
import { Line } from "vue-chartjs";
import ttkDatasets from "@/assets/ttk.json"
export default {
  extends: Line,
  data() {
    return {
      chartdata: {
        datasets: [
          ttkDatasets.r301.fullauto,
          ttkDatasets.hemlok.semiauto,
        ],
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
