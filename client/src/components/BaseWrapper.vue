<template>
  <div class="base-wrapper">
    <el-row>
      <el-col :span="24">
        <select-date></select-date>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="18">
        <cyclic-logs v-bind:cyclickData="cyclickData"></cyclic-logs>
      </el-col>
      <el-col :span="6">
        <alert-logs v-bind:alertData="alertData"></alert-logs>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SelectDate from "./SelectDate";
import AlertLogs from "./AlertLogs";
import CyclicLogs from "./CyclicLogs";
export default {
  name: "BaseWrapper",
  components: {
    SelectDate,
    AlertLogs,
    CyclicLogs
  },
  data() {
    return {
      alertData: [{ date: "2020/12/12 12:12:12", name: "aaaaaaaaaaaa" }],
      cyclickData: [{ datetime:"2020/12/12 12:12:12", speed: 10, flow: 100, pven: 1000 },{ datetime:"2020/12/12 12:12:13", speed: 0, flow: 300, pven: 3000 },{ datetime:"2020/12/12 12:12:14", speed: 20, flow: 200, pven: 2000 }, { datetime:"2020/12/12 12:12:15", speed: 50, flow: 200, pven: 2000 }]
    };
  }
};
</script>