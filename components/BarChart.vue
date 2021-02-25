<script>
import { Line } from "vue-chartjs";
export default {
  extends: Line,
  data() {
    return {
      chartdata: {
        datasets: [
          {
            label: "Flatline",
            borderColor: "#64C4A9",
            steppedLine: true,
            data: [
              {
                x: 0,
                y: 19
              },
              {
                x: 0.1,
                y: 38
              },
              {
                x: 0.2,
                y: 57
              },
              {
                y: 76,
                x: 0.3
              },
              {
                y: 95,
                x: 0.4
              },
              {
                y: 114,
                x: 0.5
              },
              {
                y: 133,
                x: 0.6
              },
              {
                y: 152,
                x: 0.7
              },
              {
                y: 171,
                x: 0.8
              },
              {
                y: 190,
                x: 0.9
              },
              {
                y: 209,
                x: 1.0
              },
              {
                y: 228,
                x: 1.1
              },
              {
                y: 247,
                x: 1.2
              },
              {
                y: 266,
                x: 1.3
              }
            ]
          }
        ]
      },
      options: {
        // scales: {
        //   xAxes: [
        //     {
        //       txpe: "linear",
        //       offset: true,
        //       ticks: {
        //         beginAtZero: true,
        //         max: 2,
        //         stepSize: 0.1
        //         }
        //     }
        //   ]
        // },
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  }
};
</script>
