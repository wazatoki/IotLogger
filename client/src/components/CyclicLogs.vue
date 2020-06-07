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
            <p>{{ speed }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="speedData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isFlow">
          <el-col :span="3">
            <p>flow</p>
            <p>{{ flow }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="flowData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isPven">
          <el-col :span="3">
            <p>pven</p>
            <p>{{ pven }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="pvenData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isPint">
          <el-col :span="3">
            <p>pint</p>
            <p>{{ pint }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="pintData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isDeltap">
          <el-col :span="3">
            <p>⊿p</p>
            <p>{{ deltap }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="deltapData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isPart">
          <el-col :span="3">
            <p>part</p>
            <p>{{ part }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="partData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isTven">
          <el-col :span="3">
            <p>tven</p>
            <p>{{ tven }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="tvenData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isTart">
          <el-col :span="3">
            <p>tart</p>
            <p>{{ tart }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="tartData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isSvo2">
          <el-col :span="3">
            <p>svo2</p>
            <p>{{ svo2 }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="svo2Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isHct">
          <el-col :span="3">
            <p>hct</p>
            <p>{{ hct }}</p>
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
    cyclickData: Array
  },
  computed: {
    speedData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    flowData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["flow"]
        });
      }
      return result;
    },
    pvenData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["pven"]
        });
      }
      return result;
    },
    pintData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    deltapData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    partData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    tvenData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    tartData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    svo2Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
        });
      }
      return result;
    },
    hctData: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["speed"]
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
            backgroundColor: "#557979",
            data: []
          }
        ]
      };
    }
  },
  data() {
    return {
      speed: 0,
      flow: 0,
      pven: 0,
      pint: 0,
      deltap: 0,
      part: 0,
      tven: 0,
      tart: 0,
      svo2: 0,
      hct: 0,
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
                unitStepSize: 2,
                displayFormats: {
                  hour: "h:mm"
                },
                tooltipFormat: "MM/DD h:mm:ss"
              }
            }
          ]
        },
        animation: false
      },
      chartHeight: 35
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