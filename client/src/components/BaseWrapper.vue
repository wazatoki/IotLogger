<template>
  <div class="base-wrapper">
    <el-row>
      <el-col :span="24">
        <select-date></select-date>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="18">
        <cyclic-logs></cyclic-logs>
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
      alertData: [{ date: "2020/12/12 12:12:12", name: "aaaaaaaaaaaa" }]
    };
  }
};
</script>