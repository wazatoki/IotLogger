<template>
  <div class="cyclic-logs">
    <el-row>
      <el-col :span="24">
        <el-row v-if="deviceItems[0].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[0].name }}</p>
            <p>
              <span>{{ currentState.item0 }}</span>
              <span>{{ deviceItems[0].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item0Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[1].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[1].name }}</p>
            <p>
              <span>{{ currentState.item1 }}</span>
              <span>{{ deviceItems[1].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item1Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[2].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[2].name }}</p>
            <p>
              <span>{{ currentState.item2 }}</span>
              <span>{{ deviceItems[2].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item2Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[3].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[3].name }}</p>
            <p>
              <span>{{ currentState.item3 }}</span>
              <span>{{ deviceItems[3].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item3Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[4].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[4].name }}</p>
            <p>
              <span>{{ currentState.item4 }}</span>
              <span>{{ deviceItems[4].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item4Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[5].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[5].name }}</p>
            <p>
              <span>{{ currentState.item5 }}</span>
              <span>{{ deviceItems[5].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item5Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[6].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[6].name }}</p>
            <p>
              <span>{{ currentState.item6 }}</span>
              <span>{{ deviceItems[6].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item6Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[7].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[7].name }}</p>
            <p>
              <span>{{ currentState.item7 }}</span>
              <span>{{ deviceItems[7].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item7Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[8].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[8].name }}</p>
            <p>
              <span>{{ currentState.item8 }}</span>
              <span>{{ deviceItems[8].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item8Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="deviceItems[9].isVisible">
          <el-col :span="3">
            <p>{{ deviceItems[9].name }}</p>
            <p>
              <span>{{ currentState.item9 }}</span>
              <span>{{ deviceItems[9].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item9Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
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
    GeneralChart,
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
    item0Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item0Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item0Min"]
        });
      }
      return result;
    },
    item1Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item1Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item1Min"]
        });
      }
      return result;
    },
    item2Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item2Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item2Min"]
        });
      }
      return result;
    },
    item3Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item3Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item3Min"]
        });
      }
      return result;
    },
    item4Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item4Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item4Min"]
        });
      }
      return result;
    },
    item5Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item5Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item5Min"]
        });
      }
      return result;
    },
    item6Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item6Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item6Min"]
        });
      }
      return result;
    },
    item7Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item7Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item7Min"]
        });
      }
      return result;
    },
    item8Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item8Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item8Min"]
        });
      }
      return result;
    },
    item9Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item9Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item9Min"]
        });
      }
      return result;
    }
  },
  data() {
    return {
      isItem0: true,
      isItem1: true,
      isItem2: true,
      isItem3: true,
      isItem4: true,
      isItem5: true,
      isItem6: true,
      isItem7: true,
      isItem8: true,
      isItem9: true,
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

div.master-maintenance-button, div.csv-download-button {
  margin-top: 3em;
}
</style>