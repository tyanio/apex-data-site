<script>
import { Line } from "vue-chartjs";
import g7Datasets from "../assets/g7-ttk.json"
export default {
  extends: Line,
  data() {
    return {
      chartdata: {
        datasets: [
          {
            label: "Flatline",
            borderColor: "#6ACEA8",
            steppedLine: true,
            data: [
              {
                x: 0,
                y: 19,
              },
              {
                x: 0.1,
                y: 38,
              },
              {
                x: 0.2,
                y: 57,
              },
              {
                x: 0.3,
                y: 76,
              },
              {
                x: 0.4,
                y: 95,
              },
              {
                x: 0.5,
                y: 114,
              },
              {
                x: 0.6,
                y: 133,
              },
              {
                x: 0.7,
                y: 152,
              },
              {
                x: 0.8,
                y: 171,
              },
              {
                x: 0.9,
                y: 190,
              },
              {
                x: 1.0,
                y: 209,
              },
              {
                x: 1.1,
                y: 228,
              },
            ],
          },
          {
            label: "R-301",
            borderColor: "#F49A4A",
            steppedLine: true,
            data: [
              {
                x: (1 - 1) / 13.5,
                y: 1 * 14,
              },
              {
                x: (2 - 1) / 13.5,
                y: 2 * 14,
              },
              {
                x: (3 - 1) / 13.5,
                y: 3 * 14,
              },
              {
                x: (4 - 1) / 13.5,
                y: 4 * 14,
              },
              {
                x: (5 - 1) / 13.5,
                y: 5 * 14,
              },
              {
                x: (6 - 1) / 13.5,
                y: 6 * 14,
              },
              {
                x: (7 - 1) / 13.5,
                y: 7 * 14,
              },
              {
                x: (8 - 1) / 13.5,
                y: 8 * 14,
              },
              {
                x: (9 - 1) / 13.5,
                y: 9 * 14,
              },
              {
                x: (10 - 1) / 13.5,
                y: 10 * 14,
              },
              {
                x: (11 - 1) / 13.5,
                y: 11 * 14,
              },
              {
                x: (12 - 1) / 13.5,
                y: 12 * 14,
              },
              {
                x: (13 - 1) / 13.5,
                y: 13 * 14,
              },
              {
                x: (14 - 1) / 13.5,
                y: 14 * 14,
              },
              {
                x: (15 - 1) / 13.5,
                y: 15 * 14,
              },
              {
                x: (16 - 1) / 13.5,
                y: 16 * 14,
              },
              {
                x: (17 - 1) / 13.5,
                y: 17 * 14,
              },
            ],
          },
          g7Datasets
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
