<template>
  <div class="cyclic-logs">
    <el-row>
      <el-col :span="3">
        <div class="select-chart">
          <el-checkbox v-model="isItem0">{{ deviceItems[0].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem1">{{ deviceItems[1].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem2">{{ deviceItems[2].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem3">{{ deviceItems[3].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem4">{{ deviceItems[4].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem5">{{ deviceItems[5].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem6">{{ deviceItems[6].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem7">{{ deviceItems[7].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem8">{{ deviceItems[8].name }}</el-checkbox>
        </div>
        <div class="select-chart">
          <el-checkbox v-model="isItem9">{{ deviceItems[9].name }}</el-checkbox>
        </div>
        <div class="clear"></div>

        <div class="master-maintenance-button">
          <span v-on:click="deviceMasterVisible = true">device マスター</span>
        </div>
        <div class="master-maintenance-button">
          <span v-on:click="onClickItemMaster">item マスター</span>
        </div>
        <div class="csv-download-button">
          <span v-on:click="onClickCsvDownload">CSV ダウンロード</span>
        </div>
      </el-col>
      <el-col :span="21">
        <el-row v-if="isItem0">
          <el-col :span="3">
            <p>{{ deviceItems[0].name }}</p>
            <p>
              <span>{{ currentState.item0 }}</span>
              <span>{{ deviceItems[0].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item0Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem1">
          <el-col :span="3">
            <p>{{ deviceItems[1].name }}</p>
            <p>
              <span>{{ currentState.item1 }}</span>
              <span>{{ deviceItems[1].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item1Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem2">
          <el-col :span="3">
            <p>{{ deviceItems[2].name }}</p>
            <p>
              <span>{{ currentState.item2 }}</span>
              <span>{{ deviceItems[2].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item2Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem3">
          <el-col :span="3">
            <p>{{ deviceItems[3].name }}</p>
            <p>
              <span>{{ currentState.item3 }}</span>
              <span>{{ deviceItems[3].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item3Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem4">
          <el-col :span="3">
            <p>{{ deviceItems[4].name }}</p>
            <p>
              <span>{{ currentState.item4 }}</span>
              <span>{{ deviceItems[4].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item4Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem5">
          <el-col :span="3">
            <p>{{ deviceItems[5].name }}</p>
            <p>
              <span>{{ currentState.item5 }}</span>
              <span>{{ deviceItems[5].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item5Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem6">
          <el-col :span="3">
            <p>{{ deviceItems[6].name }}</p>
            <p>
              <span>{{ currentState.item6 }}</span>
              <span>{{ deviceItems[6].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item6Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem7">
          <el-col :span="3">
            <p>{{ deviceItems[7].name }}</p>
            <p>
              <span>{{ currentState.item7 }}</span>
              <span>{{ deviceItems[7].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item7Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem8">
          <el-col :span="3">
            <p>{{ deviceItems[8].name }}</p>
            <p>
              <span>{{ currentState.item8 }}</span>
              <span>{{ deviceItems[8].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item8Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>

        <el-row v-if="isItem9">
          <el-col :span="3">
            <p>{{ deviceItems[9].name }}</p>
            <p>
              <span>{{ currentState.item9 }}</span>
              <span>{{ deviceItems[9].unit }}</span>
            </p>
          </el-col>
          <el-col :span="21">
            <general-chart :chartData="item9Data" :options="chartOption" :height="chartHeight"></general-chart>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-dialog title="device マスターメンテナンス" :visible.sync="deviceMasterVisible" width="40%">
      <device-master v-on:device-data-saved="deviceDataSaved"></device-master>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deviceMasterVisible = false">Cancel</el-button>
      </span>
    </el-dialog>
    <el-dialog title="item マスターメンテナンス" :visible.sync="itemMasterVisible" width="50%">
      <item-master :devices="devices" v-on:device-item-data-saved="deviceItemDataSaved"></item-master>
      <span slot="footer" class="dialog-footer">
        <el-button @click="itemMasterVisible = false">Cancel</el-button>
      </span>
    </el-dialog>
    <el-dialog title="CSV ダウンロード" :visible.sync="csvDownloadVisible" width="70%">
      <csv-download :devices="devices" :device="device" :fromDate="fromDate" :toDate="toDate"></csv-download>
      <span slot="footer" class="dialog-footer">
        <el-button @click="csvDownloadVisible = false">Cancel</el-button>
      </span>
    </el-dialog>
    <el-dialog :visible.sync="noticeDialogVisible" width="40%">
      <span>{{ noticeMessage }}</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialogVisible = false">OK</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";
import GeneralChart from "./charts/GeneralChart";
import DeviceMaster from "./DeviceMaster";
import ItemMaster from "./ItemMaster";
import CsvDownload from './CsvDownload.vue';

export default {
  name: "CyclicLogs",
  components: {
    GeneralChart,
    DeviceMaster,
    ItemMaster,
    CsvDownload
  },
  props: {
    deviceItems: Array,
    cyclickData: Array,
    currentState: Object,
    device: String,
    fromDate: Date,
    toDate: Date
  },
  methods: {
    onClickCsvDownload() {
      this.fetchAllDevices();
      this.csvDownloadVisible = true;
    },
    onClickItemMaster() {
      this.fetchAllDevices();
      this.itemMasterVisible = true;
    },
    fetchAllDevices() {
      axios.get("api/find_all_devices").then(res => {
        if (res.data && res.data.length > 0) {
          this.devices = res.data;
        }
      });
    },
    deviceDataSaved() {
      this.fetchAllDevices();
      this.deviceMasterVisible = false;
      this.noticeMessage = "deviceデータの保存に成功しました。";
      this.noticeDialogVisible = true;
    },
    deviceItemDataSaved() {
      this.itemMasterVisible = false;
      this.noticeMessage = "itemデータの保存に成功しました。";
      this.noticeDialogVisible = true;
    },
    createChartDataObj() {
      return {
        datasets: [
          {
            label: "",
            borderColor: "#550000",
            fill: false,
            radius: 0,
            borderJoinStyle: "round",
            borderWidth: 1,
            data: []
          },
          {
            label: "",
            borderColor: "#000055",
            fill: false,
            radius: 0,
            borderJoinStyle: "round",
            borderWidth: 1,
            data: []
          }
        ]
      };
    }
  },
  computed: {
    item0Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item0Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item0Min"]
        });
      }
      return result;
    },
    item1Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item1Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item1Min"]
        });
      }
      return result;
    },
    item2Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item2Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item2Min"]
        });
      }
      return result;
    },
    item3Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item3Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item3Min"]
        });
      }
      return result;
    },
    item4Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item4Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item4Min"]
        });
      }
      return result;
    },
    item5Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item5Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item5Min"]
        });
      }
      return result;
    },
    item6Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item6Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item6Min"]
        });
      }
      return result;
    },
    item7Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item7Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item7Min"]
        });
      }
      return result;
    },
    item8Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item8Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item8Min"]
        });
      }
      return result;
    },
    item9Data: function() {
      let result = this.createChartDataObj();
      for (let i = 0; i < this.cyclickData.length; i++) {
        result.datasets[0].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item9Max"]
        });
        result.datasets[1].data.push({
          x: this.cyclickData[i]["datetime"],
          y: this.cyclickData[i]["item9Min"]
        });
      }
      return result;
    }
  },
  data() {
    return {
      isItem0: true,
      isItem1: true,
      isItem2: true,
      isItem3: true,
      isItem4: true,
      isItem5: true,
      isItem6: true,
      isItem7: true,
      isItem8: true,
      isItem9: true,
      chartOption: {
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              type: "time",
              time: {
                unit: "hour",
                unitStepSize: 4,
                displayFormats: {
                  hour: "DD HH:mm"
                },
                tooltipFormat: "MM/DD HH:mm"
              }
            }
          ]
        },
        animation: false
      },
      chartHeight: 80,
      deviceMasterVisible: false,
      itemMasterVisible: false,
      csvDownloadVisible: false,
      devices: [],
      noticeDialogVisible: false,
      noticeMessage: ""
    };
  }
};
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

div.master-maintenance-button, div.csv-download-button {
  margin-top: 3em;
}
</style>