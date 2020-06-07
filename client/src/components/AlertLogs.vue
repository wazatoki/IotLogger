<template>
  <div class="alert-logs">
    <el-table :data="alertData" height="400" style="width: 100%" cell-class-name="alert-item">
      <el-table-column prop="date" label="日時" width="160"></el-table-column>
      <el-table-column prop="name" label="イベント情報"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "AlertLogs",
  props: {
    alertData: Array
  }
};
</script>

<style scoped>
.alert-logs >>> .alert-item {
  color: red;
}
</style>