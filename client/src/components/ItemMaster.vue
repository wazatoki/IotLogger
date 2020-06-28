<template>
  <div class="item-master">
    <div class="form-element">
      <el-select
        v-model="selectedDevice"
        v-on:change="deviceSelected"
        placeholder="Device Select"
        class="device-select"
      >
        <el-option v-for="item in devices" :key="item" :label="item" :value="item"></el-option>
      </el-select>
    </div>

    <div class="form-element">
      <el-row>
        <el-col :span="3">ID</el-col>
        <el-col :span="8">device用項目ID</el-col>
        <el-col :span="8">表示名称</el-col>
        <el-col :span="4">単位</el-col>
      </el-row>
      <el-row v-for="(item, index) in items" :key="index">
        <el-col :span="3">{{ item.id }}</el-col>
        <el-col :span="8">
          <el-input v-model="item.deviceItemID"></el-input>
        </el-col>
        <el-col :span="8">
          <el-input v-model="item.name"></el-input>
        </el-col>
        <el-col :span="4">
          <el-input v-model="item.unit"></el-input>
        </el-col>
      </el-row>
    </div>

    <div class="form-element">
      <el-button type="warning" v-on:click="commitData">データ送信</el-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ItemMaster",
  props: {
    devices: Array
  },
  methods: {
    deviceSelected() {
      axios
        .get("api/find_device_items_by_deviceID", {
          params: {
            selectedDevice: this.selectedDevice
          }
        })
        .then(res => {
          if (res.data && res.data.length > 0) {
            this.items = res.data;
          } else {
            this.items = this.createDefaultItems();
          }
        });
    },
    commitData() {
      this.items.forEach(item => {
        item.deviceID = this.selectedDevice;
      });
      axios.post("api/device_item/save", this.items).then(() => {
        this.selectedDevice = "";
        this.items = this.createDefaultItems();
        this.$emit("device-item-data-saved");
      });
    },
    createDefaultItems() {
      return [
        {
          id: "item0",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item1",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item2",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item3",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item4",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item5",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item6",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item7",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item8",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        },
        {
          id: "item9",
          deviceID: "",
          deviceItemID: "",
          name: "",
          unit: ""
        }
      ];
    }
  },
  data() {
    return {
      selectedDevice: "",
      items: []
    };
  }
};
</script>

<style scoped>
div.form-element {
  margin: 2em;
}
div.el-col {
  height: 3em;
  line-height: 3em;
}
</style>