<template>
  <div class="cyclic-current-state-mode">
    <el-row>
      <el-col :span="24">
        <el-row>
          <el-col :span="3">
            <p>{{ currentStateDateTime }}</p>
          </el-col>
        </el-row>

        <el-row>
          <div v-for="(deviceItem, index) in deviceItems" :key="index">
            <div v-if="deviceItem.isVisible">
              <el-col :span="8">
                <p>{{ deviceItem.name }}</p>
                <p>
                  <span class="current-state">{{ currentState['item'+index] }}</span>
                  <br/>
                  <span>{{ deviceItem.unit }}</span>
                </p>
              </el-col>
            </div>
          </div>
        </el-row>
      </el-col>
    </el-row>
    <el-dialog :visible.sync="noticeDialogVisible" width="40%">
      <span>{{ noticeMessage }}</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialogVisible = false">OK</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>

export default {
  name: "CyclicCurrentStateMode",
  props: {
    deviceItems: Array,
    currentState: Object
  },
  methods: {
  },
  computed: {
    currentStateDateTime: function() {
      const d = Date.parse(this.currentState.datetime);
      if (!isNaN(d)) {
        const dt = new Date(d);
        const year = dt.getFullYear();
        const month = dt.getMonth() + 1;
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
        return "0/0/0 0:0:0";
      }
    },
  },
  data() {
    return {
      noticeDialogVisible: false,
      noticeMessage: ""
    };
  }
};
</script>

<style scoped>

span.current-state {
  font-size: xx-large;
}

</style>