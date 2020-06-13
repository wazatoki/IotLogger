<template>
  <div class="base-wrapper">
    <el-row>
      <el-col :span="24">
        <select-date
          v-on:parsed-data-fetched="setCyclicData"
          v-on:asynchronous-data-fetched="setAlertData"
        ></select-date>
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
      cyclickData: []
    };
  },
  methods: {
    setCyclicData(data) {
      this.cyclickData = data;
    },
    setAlertData(data) {
      this.alertData = data;
    }
  }
};
</script>