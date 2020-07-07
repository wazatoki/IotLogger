<template>
    <div class="chart-select">

      <div class="select-chart" v-for="(item, index) in deviceItems" :key="index">
        <el-checkbox v-model="item.isVisible">{{ item.name }}</el-checkbox>
      </div>

        <div class="clear"></div>
    </div>
</template>

<script>

export default {
  name: "ChartSelect",
  props: {
    deviceItems: Array,
  },
}
</script>

<style scoped>
div.select-chart {
  width: 7em;
  float: left;
  text-align: left;
}

div.clear {
  clear: both;
}
</style>