<template>
  <div class="select-date">
    <el-date-picker v-model="fromDate" type="date" placeholder="開始日"></el-date-picker>
    <span>〜</span>
    <el-date-picker v-model="toDate" type="date" placeholder="終了日"></el-date-picker>
    <el-button type="primary" v-on:click="getData">データ取得</el-button>
  </div>
</template>

<script>
import axios from "axios"

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
    },
    getData() {
      axios.get('api/find_cyclic_by_event_date',{
        params: {
          from: this.fromDate,
          to: this.toDate
        }
      }).then( (res) => {
        console.log(res.data.length)
      });
    }
  }
};
</script>

<style scoped>
span {
  color: darkgray;
}
</style>