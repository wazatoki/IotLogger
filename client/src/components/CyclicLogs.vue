<template>
  <div class="cyclic-logs">
    <el-row>
      <el-col :span="24">
        <el-row>
          <el-col :span="3">
            <p>{{ currentStateDateTime }}</p>
          </el-col>
        </el-row>

        <el-row v-for="(data, index) in itemData" :key="index">
          <div v-if="data.deviceItem.isVisible">
            <el-col :span="3">
              <p>{{ data.deviceItem.name }}</p>
              <p>
                <span class="current-state">{{ currentState['item'+index] }}</span>
                <span>{{ data.deviceItem.unit }}</span>
              </p>
            </el-col>
            <el-col :span="21">
              <general-chart :chartData="data.chartData" :options="chartOption" :height="chartHeight"></general-chart>
            </el-col>
          </div>
        </el-row>
      </el-col>
    </el-row>
    <el-dialog :visible.sync="noticeDialogVisible" width="40%">
      <span>{{ noticeMessage }}</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialogVisible = false">OK</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import GeneralChart from "./charts/GeneralChart";

export default {
  name: "CyclicLogs",
  components: {
    GeneralChart
  },
  props: {
    deviceItems: Array,
    cyclickData: Array,
    currentState: Object,
    device: String,
    fromDate: Date,
    toDate: Date
  },
  methods: {
    createChartDataObj() {
      return {
        datasets: [
          {
            label: "",
            borderColor: "#550000",
            fill: false,
            radius: 0,
            borderJoinStyle: "round",
            borderWidth: 1,
            data: []
          },
          {
            label: "",
            borderColor: "#000055",
            fill: false,
            radius: 0,
            borderJoinStyle: "round",
            borderWidth: 1,
            data: []
          }
        ]
      };
    }
  },
  computed: {
    currentStateDateTime: function() {
      const d = Date.parse(this.currentState.datetime);
      if (!isNaN(d)) {
        const dt = new Date(d);
        const year = dt.getFullYear();
        const month = dt.getMonth() + 1;
        const day = dt.getDate();
        const hours = dt.getHours();
        const minutes = dt.getMinutes();
        const seconds = dt.getSeconds();
        return (
          year +
          "/" +
          month +
          "/" +
          day +
          " " +
          hours +
          ":" +
          minutes +
          ":" +
          seconds
        );
      } else {
        return "0/0/0 0:0:0";
      }
    },
    itemData: function() {
      const result = [];

      this.deviceItems.forEach((deviceItem, deviceItemIndex) => {
        const chartDataObj = this.createChartDataObj();
        this.cyclickData.forEach(cData => {
          chartDataObj.datasets[0].data.push({
            x: cData['datetime'],
            y: cData['item' + deviceItemIndex + 'Max']
          });
          chartDataObj.datasets[1].data.push({
            x: cData['datetime'],
            y: cData['item' + deviceItemIndex + 'Min']
          });
        });
        result.push({ deviceItem: deviceItem, chartData: chartDataObj });
      });

      return result;
    },
  },
  data() {
    return {
      chartOption: {
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              type: "time",
              time: {
                unit: "hour",
                unitStepSize: 4,
                displayFormats: {
                  hour: "DD HH:mm"
                },
                tooltipFormat: "MM/DD HH:mm"
              }
            }
          ]
        },
        animation: false
      },
      chartHeight: 80,
      devices: [],
      noticeDialogVisible: false,
      noticeMessage: ""
    };
  }
};
</script>

<style scoped>
div.select-chart {
  width: 7em;
  float: left;
  text-align: left;
}

div.clear {
  clear: both;
}

div.master-maintenance-button,
div.csv-download-button {
  margin-top: 3em;
}

span.current-state {
  font-size: x-large;
}
</style>