<template>
  <div class="device-master">
    <span>空白行は保存されません。</span>
    <ul class="device-list">
      <li v-for="(device, index) in devices" :key="index">
        <el-input v-model="device.id"></el-input>
      </li>
    </ul>
    <div class="add-button">
      <el-button type="primary" v-on:click="addDevice">device追加</el-button>
    </div>
    <div class="commit-button">
      <el-button type="warning" v-on:click="commitData">データ送信</el-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DeviceMaster",
  mounted: function() {
    this.fetchAllDevices();
  },
  data() {
    return {
      devices: []
    };
  },
  methods: {
    addDevice() {
      this.devices.push({id: ''})
    },
    commitData() {
      const data = []
      this.devices.forEach(device => {
        data.push(device.id)
      });
      axios.post("api/device/save", data).then(() => {
        this.devices = []
        this.fetchAllDevices()
        this.$emit("device-data-saved");
      });
    },
    fetchAllDevices() {
      const self = this;
      axios.get("api/find_all_devices").then(res => {
        if (res.data && res.data.length > 0) {
          res.data.forEach(item => {
            self.devices.push({ id: item });
          });
        }
      });
    }
  }
};
</script>

<style scoped>
div.commit-button, div.add-button {
  margin: 2em;
}
</style>