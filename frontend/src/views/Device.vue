<template>
  <div class="device">
    <el-container height="100vh">
      <el-main>
        <el-table
          :data="results"
          border
          cell-class-name=""
          stripe
          style="width: 100%"
          @selection-change="handleSelectionChange"
          :default-sort="{ prop: 'd_ID', order: 'descending' }"
        >
          <el-table-column type="selection" width="55"> </el-table-column>
          <el-table-column fixed="left" prop="d_ID" label="设备ID" width="120" align="center">
          </el-table-column>
          <el-table-column align="center"
            prop="d_see"
            label="可见等级"
            width="100"
            :formatter="D_SEE"
            :filters="[
              { text: '所有人可见（1）', value: 1 },
              { text: '管理员可见（9）', value: 9 },
            ]"
            :filter-method="filterHandler"
          >
          </el-table-column>
          <el-table-column align="center"
            prop="d_type"
            label="类型"
            width="100"
            :formatter="D_TYPE"
            :filters="[
            {text: '存储卡式摄录一体机(1)', value: 1},{text: '微单或单反(2)', value: 2},
            {text: '镜头(3)', value: 3},{text: '监视器(4)', value: 4},
            {text: '导播台(5)', value: 5},{text: '麦克风(6)', value: 6},
            {text: '图传(7)', value: 7},{text: '灯(8)', value: 8},
            {text: '服务器(9)', value: 9},{text: '计算机(10)', value: 10},
            {text: '稳定器(11)', value: 11},{text: '三脚架(12)', value: 12},
            {text: '三脚架脚轮(13)', value: 13},{text: '电池(14)', value: 14},
            {text: '充电器(15)', value: 15},{text: '存储卡(16)', value: 16},
            {text: '存储卡(17)', value: 17},{text: '包(18)', value: 18},
            {text: '手柄(19)', value: 19},{text: '电缆(20)', value: 20},]"
            :filter-method="filterHandler"
          >
          </el-table-column>
          <el-table-column prop="d_name" label="名称" width="200" align="center">
          </el-table-column>
          <el-table-column prop="d_date" label="创建设备时间" width="120" align="center">
          </el-table-column>
          <el-table-column align="center"
            prop="d_status"
            label="状态"
            width="80"
            :formatter="D_STATUS"
            :filters="[
              { text: '未借出且完好（1）', value: 1 },
              { text: '借出（0）', value: 0 },
            ]"
            :filter-method="filterHandler"
          >
          </el-table-column>
          <el-table-column align="center"
            prop="d_place"
            label="位置"
            width="80"
            :filters="[
              { text: '114', value: '114' },
              { text: '735', value: '735' },
            ]"
            :filter-method="filterHandler"
          >
          </el-table-column>
          <el-table-column prop="d_others" label="备注" width="140" align="center">
          </el-table-column>
          <el-table-column fixed="right" label="操作" width="180" align="center">
            <template slot-scope="scope">
              <!-- <template> -->
              <el-button @click="ConfirmDD(scope.row)" type="text" size="small"
                >删除</el-button
              >
              <el-button
                @click="handleEditDeviceDialogOpen(scope.row)"
                type="text"
                size="small"
                >编辑</el-button
              >
            </template>
          </el-table-column>
        </el-table>

        <!-- 编辑设备信息dialog -->
        <el-dialog
          title="编辑设备信息"
          :visible.sync="EditDevicedialogVisible"
          width="30%"
          :before-close="handleEditDeviceDialogClose"
          :lock-scroll="true"
        >
          <el-form>
            <el-form-item
              label="设备名称"
              :label-width="'120px'"
              placeholder="请填写名称"
            >
              <el-input
                v-model="EditDeviceForm.d_name"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item label="设备类型" :label-width="'120px'">
              <el-select
                v-model="EditDeviceForm.d_type"
                placeholder="请选择设备类型"
              >
                <el-option label="存储卡式摄录一体机" value="1"></el-option>
                <el-option label="微单或单反" value="2"></el-option>
                <el-option label="镜头" value="3"></el-option>
                <el-option label="监视器" value="4"></el-option>
                <el-option label="导播台" value="5"></el-option>
                <el-option label="麦克风" value="6"></el-option>
                <el-option label="图传" value="7"></el-option>
                <el-option label="灯" value="8"></el-option>
                <el-option label="服务器" value="9"></el-option>
                <el-option label="计算机" value="10"></el-option>
                <el-option label="稳定器" value="11"></el-option>
                <el-option label="三脚架" value="12"></el-option>
                <el-option label="三脚架脚轮" value="13"></el-option>
                <el-option label="电池" value="14"></el-option>
                <el-option label="充电器" value="15"></el-option>
                <el-option label="存储卡" value="16"></el-option>
                <el-option label="读卡器" value="17"></el-option>
                <el-option label="包" value="18"></el-option>
                <el-option label="手柄" value="19"></el-option>
                <el-option label="电缆" value="20"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="设备可见等级" :label-width="'120px'">
              <el-select
                v-model="EditDeviceForm.d_see"
                placeholder="请选择设备可见等级"
              >
                <el-option label="所有人可见（1）" value="1"></el-option>
                <el-option label="管理员可见（9）" value="9"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="设备状态" :label-width="'120px'">
              <el-select
                v-model="EditDeviceForm.d_status"
                placeholder="请选择设备状态"
              >
                <el-option label="未借出且完好（1）" value="1"></el-option>
                <el-option label="借出（0）" value="0"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="设备所在地点" :label-width="'120px'">
              <el-select
                v-model="EditDeviceForm.d_place"
                placeholder="请选择设备所在地点"
              >
                <el-option label="114" value="114"></el-option>
                <el-option label="735" value="735"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="新建设备时间" :label-width="'120px'">
              <el-date-picker
                v-model="EditDeviceForm.d_date"
                type="date"
                placeholder="选择日期"
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
              >
              </el-date-picker>
            </el-form-item>
            <el-form-item
              label="备注"
              :label-width="'120px'"
              placeholder="可空"
            >
              <el-input
                v-model="EditDeviceForm.d_others"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button
                type="primary"
                @click="EditDevice(), (EditDevicedialogVisible = false)"
                >确 定</el-button
              >
              <el-button @click="EditDevicedialogVisible = false"
                >取 消</el-button
              >
              <!-- <el-button @click="listen11()">11</el-button> -->
              <!-- <el-button @click="listen()">111</el-button>  -->
            </el-form-item>
          </el-form>
        </el-dialog>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: "",
      results: [],
      multipleSelection: [],
      EditDevicedialogVisible: false,
      DeleteDevice_ID: "",
      EditDeviceForm: {
        d_ID: "",
        d_see: "", //可见等级1/9
        d_type: "", //大类1/2/3
        d_name: "", //名字
        d_date: "", //注意！这里必须要补全到 日，以yyyy-mm-dd形式传回
        d_status: "", //状态，默认1为未借出且完好，0为借出
        d_place: "", //地点
        d_others: "", //设备备注，可为空
      },
    };
  },

  methods: {
    D_TYPE(row){
        if (row.d_type === 1) {
          return '存储卡式摄录一体机'
        } else if(row.d_type === 2)  {
          return '微单或单反'
        } else if(row.d_type === 3)  {
          return '镜头'
        } else if(row.d_type === 4)  {
          return '监视器'
        } else if(row.d_type === 5)  {
          return '导播台'
        } else if(row.d_type === 6)  {
          return '麦克风'
        } else if(row.d_type === 7)  {
          return '图传'
        } else if(row.d_type === 8)  {
          return '灯'
        } else if(row.d_type === 9)  {
          return '服务器'
        } else if(row.d_type === 10)  {
          return '计算机'
        } else if(row.d_type === 11)  {
          return '稳定器'
        } else if(row.d_type === 12)  {
          return '三脚架'
        } else if(row.d_type === 13)  {
          return '三脚架脚轮'
        } else if(row.d_type === 14)  {
          return '电池'
        } else if(row.d_type === 15)  {
          return '充电器'
        } else if(row.d_type === 16)  {
          return '存储卡'
        } else if(row.d_type === 17)  {
          return '读卡器'
        } else if(row.d_type === 18)  {
          return '包'
        } else if(row.d_type === 19)  {
          return '手柄'
        } else if(row.d_type === 20)  {
          return '电缆'
        } 
      },
    D_SEE(row, column) {
        if (row.d_see === 1) {
          return '所有人可见'
        } else if(row.d_see === 9)  {
          return '管理员可见'
        } 
      },
    D_STATUS(row){
      if (row.d_status === 1) {
        return '完好'
      } else if(row.d_status === 3)  {
        return '维护中'
      } else if(row.d_status === 0)  {
        return '借出'
      } 
    },
    /* listen11() {
      console.log(this.EditDeviceForm);
    }, */
    checkDevices() {
      this.axios
        .get("manage/devices/", {})
        .then((res) => {
          //console.log(res)
          this.count = res.data.count;
          this.results = res.data;
        })
        .catch((failResponse) => {});
    },
    EditDevice() {
      this.axios
        .put(
          "manage/devices/" +
            this.EditDeviceForm.d_ID +
            "/",
          {
            d_see: this.EditDeviceForm.d_see,
            d_type: this.EditDeviceForm.d_type,
            d_name: this.EditDeviceForm.d_name,
            d_date: this.EditDeviceForm.d_date,
            d_status: this.EditDeviceForm.d_status,
            d_place: this.EditDeviceForm.d_place,
            d_others: this.EditDeviceForm.d_others,
          }
        )
        .then((res) => {
          //console.log(res)
          if (res.data.code === 404) {
            this.$message({ type: "info", message: res.data.msg });
            this.checkDevices();
          } else {
            this.$message({ type: "success", message: "修改成功" });
            this.checkDevices();
          }
        })
        .catch((failResponse) => {});
    },
    DeleteDevice() {
      this.axios
        .delete(
          "manage/devices/" +
            this.DeleteDevice_ID +
            "/",
          {}
        )
        .then((res) => {
          //console.log(res)
          if (res.data.code === 404) {
            this.$message({ type: "error", message: res.data.msg });
            this.checkDevices();
          } else {
            this.$message({ type: "success", message: "删除成功" });
            this.checkDevices();
          }
        })
        .catch((failResponse) => {});
    },
    ConfirmDD(row) {
      this.DeleteDevice_ID = row.d_ID;
      this.$confirm("此操作将删除该设备, 是否继续?", "提示", {
        confirmButtonText: "确定删除",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.DeleteDevice();
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消删除",
          });
        });
    },
    handleEditDeviceDialogOpen(row) {
      this.EditDevicedialogVisible = true;
      this.EditDeviceForm.d_ID = row.d_ID;
      this.EditDeviceForm.d_see = row.d_see;
      this.EditDeviceForm.d_name = row.d_name;
      this.EditDeviceForm.d_type = row.d_type;
      this.EditDeviceForm.d_date = row.d_date + "-01";
      this.EditDeviceForm.d_status = row.d_status;
      this.EditDeviceForm.d_place = row.d_place;
      this.EditDeviceForm.d_others = row.d_others;
      //console.log(this.EditDeviceForm)
    },
    handleEditDeviceDialogClose(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    filterHandler(value, row, column) {
      const property = column["property"];
      return row[property] === value;
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    /* listen(){
        console.log(this.EditDeviceForm)
      }, */
  },

  mounted: function () {
    //自动触发写入的函数
    this.checkDevices();
  },
};
</script>

<style>
</style>