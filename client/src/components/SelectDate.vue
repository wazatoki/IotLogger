<template>
  <div class="select-date">
    <el-date-picker v-model="fromDate" type="date" placeholder="開始日"></el-date-picker>
    <span>〜</span>
    <el-date-picker v-model="toDate" type="date" placeholder="終了日"></el-date-picker>
  </div>
</template>

<script>
export default {
  name: "SelectDate",
  data() {
    return {
      fromDate: this.getDefaultFromDate(),
      toDate: new Date()
    };
  },
  methods: {
    getDefaultFromDate() {
      let d;
      d = new Date();
      d.setDate(d.getDate() - 2);
      return d;
    }
  }
};
</script>

<style scoped>
span {
  color: darkgray;
}
</style>