<template>
  <div class="cyclic-logs">
    <el-row>
      <el-col :span="2">
        <div class="select-chart">
          <el-checkbox v-model="isSpeed">speed</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isFlow">flow</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isPven">pven</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isPint">pint</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isDeltap">⊿p</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isPart">part</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isTven">tven</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isTart">tart</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isSvo2">svo2</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isHct">hct</el-checkbox>
        </div>
      </el-col>
      <el-col :span="22">
        <el-row v-if="isSpeed">
          <el-col :span="3">
            <p>speed</p>
            <p>{{ currentState.speed }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="speedData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isFlow">
          <el-col :span="3">
            <p>flow</p>
            <p>{{ currentState.flow }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="flowData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isPven">
          <el-col :span="3">
            <p>pven</p>
            <p>{{ currentState.pven }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="pvenData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isPint">
          <el-col :span="3">
            <p>pint</p>
            <p>{{ currentState.pint }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="pintData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isDeltap">
          <el-col :span="3">
            <p>⊿p</p>
            <p>{{ currentState.deltap }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="deltapData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isPart">
          <el-col :span="3">
            <p>part</p>
            <p>{{ currentState.part }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="partData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isTven">
          <el-col :span="3">
            <p>tven</p>
            <p>{{ currentState.tven }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="tvenData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isTart">
          <el-col :span="3">
            <p>tart</p>
            <p>{{ currentState.tart }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="tartData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isSvo2">
          <el-col :span="3">
            <p>svo2</p>
            <p>{{ currentState.svo2 }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="svo2Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isHct">
          <el-col :span="3">
            <p>hct</p>
            <p>{{ currentState.hct }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="hctData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
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
    cyclickData: Array,
    currentState: Object
  },
  computed: {
    speedData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speedMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speedMin"]
        });
      }
      return result;
    },
    flowData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["flowMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["flowMin"]
        });
      }
      return result;
    },
    pvenData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["pvenMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["pvenMin"]
        });
      }
      return result;
    },
    pintData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["pintMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["pintMin"]
        });
      }
      return result;
    },
    deltapData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["deltapMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["deltapMin"]
        });
      }
      return result;
    },
    partData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["partMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["partMin"]
        });
      }
      return result;
    },
    tvenData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["tvenMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["tvenMin"]
        });
      }
      return result;
    },
    tartData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["tartMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["tartMin"]
        });
      }
      return result;
    },
    svo2Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["svo2Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["svo2Min"]
        });
      }
      return result;
    },
    hctData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["hctMax"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["hctMin"]
        });
      }
      return result;
    }
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
  data() {
    return {
      isSpeed: true,
      isFlow: true,
      isPven: true,
      isPint: true,
      isDeltap: true,
      isPart: true,
      isTven: true,
      isTart: true,
      isSvo2: true,
      isHct: true,
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
      chartHeight: 80
    };
  }
};
</script>

<style scoped>
div.select-chart {
  width: 5em;
  float: left;
  text-align: left;
}
</style>