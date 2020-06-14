<template>
  <div class="base-wrapper">
    <el-row>
      <el-col :span="24">
        <select-date
          v-on:parsed-data-fetched="setCyclicData"
          v-on:asynchronous-data-fetched="setAlertData"
          v-on:current-state-fetched="setCurrentState"
        ></select-date>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="18">
        <cyclic-logs v-bind:cyclickData="cyclickData" v-bind:currentState="currentState"></cyclic-logs>
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
      alertData: [],
      cyclickData: [],
      currentState: {}
    };
  },
  methods: {
    setCyclicData(data) {
      this.cyclickData = data;
    },
    setAlertData(data) {
      this.alertData = data;
    },
    setCurrentState(data) {
      if (data == null) {
        data = {};
      }
      this.currentState = data;
    }
  }
};
</script>