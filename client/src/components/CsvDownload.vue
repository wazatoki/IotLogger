<template>
  <div class="csv-download">
    <div class="small-margin">
      <el-select
        v-model="selectedDevice"
        placeholder="Device Select"
        class="device-select"
      >
        <el-option
          v-for="item in devices"
          :key="item"
          :label="item"
          :value="item"
        ></el-option>
      </el-select>
    </div>
    <div class="small-margin">
      <el-radio v-model="selectedDataType" label="cyclic">Cyclic Data</el-radio>
      <el-radio v-model="selectedDataType" label="asynchronous"
        >Asynchronous Data</el-radio
      >
    </div>
    <div class="small-margin">
      <el-checkbox v-model="isDeleteData"
        >データを取得した後に期間内データを削除する。</el-checkbox
      >
    </div>
    <div class="small-margin">
      <el-date-picker
        v-model="fromDateTime"
        type="datetime"
        placeholder="開始日時"
      ></el-date-picker>
      <span>〜</span>
      <el-date-picker
        v-model="toDateTime"
        type="datetime"
        placeholder="終了日時"
      ></el-date-picker>
      <el-button type="primary" v-on:click="getData">データ取得</el-button>
    </div>

    <el-dialog :visible.sync="confirmDialogVisible" width="30%" append-to-body>
      <span>指定期間内のデータの消去を行いますか？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="confirmDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="deleteData"
          >消去する</el-button
        >
      </span>
    </el-dialog>

    <el-dialog :visible.sync="noticeDialogVisible" width="30%" append-to-body>
      <span>指定期間内のデータを消去しました。</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialogVisible = false">OK</el-button>
      </span>
    </el-dialog>
    
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "csvDownload",
  props: {
    device: String,
    devices: Array,
    fromDate: Date,
    toDate: Date,
  },
  mounted: function () {
    this.selectedDevice = this.device;
    this.fromDateTime = this.fromDate;
    this.toDateTime = this.toDate;
  },
  watch: {
    device: function (val) {
      this.selectedDevice = val;
    },
    fromDate: function (val) {
      this.fromDateTime = val;
    },
    toDate: function (val) {
      this.toDateTime = val;
    },
  },
  data() {
    return {
      selectedDevice: "",
      selectedDataType: "cyclic",
      fromDateTime: "",
      toDateTime: "",
      isDeleteData: false,
      confirmDialogVisible: false,
      noticeDialogVisible: false,
    };
  },
  methods: {
    getData() {
      switch (this.selectedDataType) {
        case "cyclic":
          this.fetchCyclicData();
          break;
        case "asynchronous":
          this.fetchAsynchronousData();
          break;

        default:
          this.fetchCyclicData();
          break;
      }
    },
    fetchAllDevices() {
      axios.get("api/find_all_devices").then((res) => {
        if (res.data && res.data.length > 0) {
          this.options = res.data;
        }
      });
    },
    fetchAsynchronousData() {
      axios
        .get("api/asynchronous/csv/filename", {
          params: {
            from: this.fromDateTime,
            to: this.toDateTime,
            selectedDevice: this.selectedDevice,
          },
        })
        .then((res) => {

          if (this.isDeleteData) {
            this.confirmDialogVisible = true;
          }

          window.location.href =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/asynchronous/csv/download?fileName=" +
            res.data.fileName;
          
        });
    },
    fetchCyclicData() {
      axios
        .get("api/cyclic/csv/filename", {
          params: {
            from: this.fromDateTime,
            to: this.toDateTime,
            selectedDevice: this.selectedDevice,
          },
        })
        .then((res) => {

          if (this.isDeleteData) {
            this.confirmDialogVisible = true;
          }

          window.location.href =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/cyclic/csv/download?fileName=" +
            res.data.fileName;

        });
    },
    deleteData() {
      switch (this.selectedDataType) {
        case "cyclic":
          this.deleteCyclicData();
          break;
        case "asynchronous":
          this.deleteAsynchronousData();
          break;

        default:
          this.deleteCyclicData();
          break;
      }
    },
    deleteAsynchronousData() {
      axios
        .delete("api/asynchronous/delete", {
          data: {
            from: this.fromDateTime,
            to: this.toDateTime,
            selectedDevice: this.selectedDevice,
          },
        })
        .then((res) => {
          if (res && res.data.result){
            this.confirmDialogVisible = false;
            this.noticeDialogVisible = true;
          }
        });
    },
    deleteCyclicData() {
      axios
        .delete("api/cyclic/delete", {
          data: {
            from: this.fromDateTime,
            to: this.toDateTime,
            selectedDevice: this.selectedDevice,
          },
        })
        .then((res) => {
          if(res && res.data.result){
            this.confirmDialogVisible = false;
            this.noticeDialogVisible = true;
          }
        });
    },
  },
};
</script>

<style scoped>
span {
  color: darkgray;
}
.device-select {
  margin-right: 2em;
}

.small-margin {
  margin: 1em;
}
</style>