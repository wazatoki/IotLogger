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
        <el-row>
          <el-col :span="3">
            <p>speed</p>
            <p>{{ speed }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="speedData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>flow</p>
            <p>{{ flow }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="flowData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>pven</p>
            <p>{{ pven }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="pvenData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>pint</p>
            <p>{{ pint }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="pintData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>⊿p</p>
            <p>{{ deltap }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="deltapData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>part</p>
            <p>{{ part }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="partData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>tven</p>
            <p>{{ tven }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="tvenData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>tart</p>
            <p>{{ tart }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="tartData" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>svo2</p>
            <p>{{ svo2 }}</p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="svo2Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row>
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
        animation: false
      },
      chartHeight: 35,
      speedData: {
        datasets: [
          {
            label: "",
            backgroundColor: "#f87979",
            data: [20, 30, 25]
          }
        ]
      },
      flowData: {
        datasets: [
          {
            label: "",
            backgroundColor: "#557979",
            data: [20, 30, 25]
          }
        ]
      }
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

div.chart-area {
  max-height: 100px;
}
</style>