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
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>flow</p>
            <p>{{ flow }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>pven</p>
            <p>{{ pven }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>pint</p>
            <p>{{ pint }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>⊿p</p>
            <p>{{ deltap }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>part</p>
            <p>{{ part }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>tven</p>
            <p>{{ tven }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>tart</p>
            <p>{{ tart }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>svo2</p>
            <p>{{ svo2 }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>

        <el-row>
          <el-col :span="3">
            <p>hct</p>
            <p>{{ hct }}</p>
          </el-col>
          <el-col :span="21"></el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "CyclicLogs",
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
      isHct: true
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
</style>