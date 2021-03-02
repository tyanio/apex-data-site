<script>
import { Line, mixins } from "vue-chartjs";

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  props: ["chartData"],
  data() {
    return {
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
          yAxes: [
            {
              type: "linear",
              ticks: {
                beginAtZero: true,
                suggestedMax: 250,
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
    this.renderChart(this.chartData, this.options);
  },
};
</script>
