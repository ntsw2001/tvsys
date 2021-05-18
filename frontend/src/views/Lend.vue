<template>
  <div id="app">
    <el-container>
      <el-card class="lendtable" width='500px'>         
        <el-form>
          <el-form-item label="借用设备ID" :label-width="'120px'" placeholder="请填写ID">
          <el-input v-model="LendForm.b_device" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="借用设备时间" :label-width="'120px'">
            <el-date-picker v-model="LendForm.b_date" type="datetime" placeholder="选择借用日期时间" value-format="yyyy-MM-ddTHH:mm:ss">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="借用缘由" :label-width="'120px'" placeholder="请填写缘由">
          <el-input v-model="LendForm.b_reason" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="借用设备地点" :label-width="'120px'">
            <el-input v-model="LendForm.b_place" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item>
          <el-button type="primary" @click="Lend()">立即借用</el-button>
          <el-button @click="resetLendForm()">重置</el-button>
          <!-- <el-button @click="receiptDialog = true">测试回执单</el-button> -->
          <!-- <el-button @click="listen0()">111</el-button> --> 
          </el-form-item>
        </el-form>
      </el-card>


      <el-main>
        <el-table :data="results" border  cell-class-name="" style="width: 100% "  @selection-change="handleSelectionChange" :default-sort = "{prop: 'd_ID', order: 'descending'}">
        <el-table-column type="selection" width="55">
        </el-table-column>
        <el-table-column fixed="left" prop="d_ID" label="设备ID" width="120" align="center">
        </el-table-column>
        <el-table-column prop="d_see" label="可见等级" width="95" align="center" :formatter="D_SEE"
        :filters="[{text: '所有人可见（1）', value: 1}, {text: '管理员可见（9）', value: 9}]"
        :filter-method="filterHandler">
        </el-table-column>
        <el-table-column prop="d_type" label="类型" width="150" align="center" :formatter="D_TYPE"
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
        :filter-method="filterHandler">
        </el-table-column>
        <el-table-column prop="d_name" label="名称" width="180" align="center">
        </el-table-column>
        <el-table-column prop="d_data" label="时间" width="40" align="center">
        </el-table-column>
        <el-table-column prop="d_status" label="状态" width="50" align="center" :formatter="D_STATUS">
        </el-table-column>
        <el-table-column prop="d_place" label="位置" width="80" align="center"
        :filters="[{text: '114', value: '114'}, {text: '735', value: '735'}]"
        :filter-method="filterHandler">
        </el-table-column>
        <el-table-column prop="d_others" label="备注" width="140" align="center">
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="230" align="center">
          <template slot-scope="scope">
            <el-button @click="readytoLend(scope.row)" type="text" size="small">借用</el-button>
          </template>
        </el-table-column>
        </el-table>
    </el-main>

      <!-- 借用回执dialog -->
<!--       <el-dialog title="借用成功！看看回执单吧" :visible.sync="receiptDialog">
      <el-table :data="receipt">
        <el-table-column property="b_ID" label="流水号" width="150"></el-table-column>
        <el-table-column property="b_user" label="借用者" width="200"></el-table-column>
        <el-table-column property="b_data" label="借用时间"></el-table-column>
        <el-table-column property="b_device" label="借用设备"></el-table-column>
        <el-table-column property="b_reason" label="借用缘由"></el-table-column>
        <el-table-column property="b_place" label="借用地址"></el-table-column>
      </el-table>
      <el-button @click="receiptDialog = false">我知道了</el-button>
    </el-dialog> -->


    </el-container>
  </div>
</template>

<script>

  export default 
  {
    data() {
      return {
        count: '',
        next: '',
        previous: '',
        results: [],
        multipleSelection: [],
        receiptDialog : false,
        LendForm:{
          b_device: "",
          b_date: "", //补全
          b_reason: "",
          b_place: "",
          r_assign: null,
          r_date: null,
          r_place: null
        },
        receipt:{
          b_ID: "",
          b_user: "",
          b_device: "",
          b_date: "",
          b_reason: "",
          b_place: "",
          r_assign: null,
          r_date: null,
          r_place: null
        }
      }
    },
    methods:
    {
      D_SEE(row, column) {
        if (row.d_see === 1) {
          return '所有人可见'
        } else if(row.d_see === 9)  {
          return '管理员可见'
        } 
      },
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
      D_STATUS(row){
        if (row.d_status === 1) {
          return '完好'
        } else if(row.d_status === 3)  {
          return '维护中'
        } else if(row.d_status === 0)  {
          return '借出'
        } 
      },
      readytoLend(row){
        this.LendForm.b_device = row.d_ID
        this.LendForm.b_place = row.d_place
        
      },
      Lend(){
        this.axios
          .post('lend/', {
            b_device: this.LendForm.b_device,
            b_date: this.LendForm.b_date, //补全
            b_reason: this.LendForm.b_reason,
            b_place: this.LendForm.b_place,
            r_assign: this.LendForm.r_assign,
            r_date: this.LendForm.r_date,
            r_place: this.LendForm.r_place
          })
          .then(res => {
            if(res.data.code === 404){
              this.$message({type: 'info',message: res.data.msg});
            }
            else if(res.data.code === 500){
              this.$message({type: 'info',message: res.data.msg});
            }
            else{
              this.$message({type: 'success',message: "借用成功"});
              this.resetLendForm()
              this.openrecepitdialog()
              //this.trans()
              //console.log(res)
              //this.receiptDialog = true
              //console.log(this.receipt)
            }
          })
          .catch(failResponse => {
          })
      },
      /* trans(){
        this.receipt.b_ID = res.data.b_ID,
        this.receipt.b_user = res.data.b_user,
        this.receipt.b_device = res.data.b_device,
        this.receipt.b_date = res.data.b_date,
        this.receipt.b_reason = res.data.b_reason,
        this.receipt.b_place = res.data.b_place,
        this.receipt.r_assign = res.data.r_assign,
        this.receipt.r_date = res.data.r_date,
        this.receipt.r_place = res.data.r_place
      }, */
      openrecepitdialog(){
        this.receiptDialog = true
      },
      checkAvailableDevices(){
        this.axios
          .post('api/q_d/', {
            d_ID: null,
            d_see: "1,9", // 可以传"1,2,3"或者"1,6"或者别的数字字符串，逗号分隔实现多选，默认1
            d_type: null, // 同上，默认所有类别
            d_name: null,
            d_date_start: null, // 可为空，默认1970-01-01
            d_date_end: null, // 可为空，默认为发起查询的日子
            d_status: null, // 同上，默认1
            d_place: null,
            d_others: null
          })
          .then(res => {
            //console.log(res)
            this.count = res.data.count;
            this.next = res.data.next;
            this.previous = res.data.previous;
            this.results = res.data;
          })
          .catch(failResponse => {
          })
      },   
      resetLendForm() {
        this.LendForm.b_device = null,
        this.LendForm.b_date = null, 
        this.LendForm.b_reason ='',
        this.LendForm.b_place = null,
        this.LendForm.r_assign = null,
        this.LendForm.r_date = null,
        this.LendForm.r_place = null
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      /* listen0(){
        console.log(this.LendForm)
      },
      listen2(){
        console.log(this.results,this.count)
      }, */
    },
    
    mounted:function () {   //自动触发写入的函数
      this.checkAvailableDevices();
    },    
  }

</script>

<style>
.el-aside {
    background-color: #D3DCE6;
    color: rgb(255, 255, 255);
  }
.lendtable{
    border-radius:30px;
    width: 380px;
    box-shadow: 0 2px 12px 0 rgb(243, 102, 102);
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); 
    height: 600px;   
  }
</style>