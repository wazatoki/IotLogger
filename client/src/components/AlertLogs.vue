<template>
  <div class="alert-logs">
    <el-table :data="alertData" height="400" style="width: 100%" cell-class-name="alert-item">
      <el-table-column prop="datetime" :formatter="dateformat" label="日時" width="160"></el-table-column>
      <el-table-column prop="category" label="カテゴリー" width="100"></el-table-column>
      <el-table-column prop="name" label="イベント情報"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "AlertLogs",
  props: {
    alertData: Array
  },
  methods: {
    dateformat: function(row, column, value){
      const d = Date.parse(value);
      if (!isNaN(d)) {
        const dt = new Date(d);
        const year = dt.getFullYear();
        const month = dt.getMonth();
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
        return "";
      }
    },
  }
};
</script>

<style scoped>
.alert-logs >>> .alert-item {
  color: red;
}
</style>