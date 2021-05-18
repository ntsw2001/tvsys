<template>
  <div>
    <el-table :data="results"  border cell-class-name="" stripe style="width: 100%" @selection-change="handleSelectionChange" :default-sort = "{prop: 'b_ID', order: 'descending'}">
      <el-table-column type="selection" width="55">
      </el-table-column>
      <el-table-column align="center" fixed="left" prop="b_ID" label="流水号" width="200" sortable>
      </el-table-column>
      <el-table-column align="center" prop="b_device_name" label="设备名称" width="180">
      </el-table-column>
      <el-table-column align="center" prop="b_date" label="借用时间" width="180" sortable>
      </el-table-column>
      <el-table-column align="center" prop="b_reason" label="借用缘由" width="100">
      </el-table-column>
      <el-table-column align="center" prop="b_place" label="借用地点" width="90"
      :filters="[{text: '114', value: '114'}, {text: '735', value: '735'}]"
      :filter-method="filterHandler">
      </el-table-column>
      <el-table-column align="center" prop="b_user" label="用户ID" width="100">
      </el-table-column>
      <el-table-column align="center" prop="b_device" label="设备ID" width="120">
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <el-button @click="openRetuenDialog(scope.row),ReturndialogVisible = true" type="text" size="small">归还此设备</el-button>
        </template>
      </el-table-column>
    </el-table>


<!-- 归还设备dialog -->
    <el-dialog title="归还设备" :visible.sync="ReturndialogVisible" width="30%" :before-close="handleAllDialogClose">
        <el-form>
          <el-form-item label="归还地点" :label-width="'120px'" placeholder="请填写归还地点">
            <el-input v-model="returnForm.r_place" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="归还时间" :label-width="'120px'">
            <el-date-picker v-model="returnForm.r_date" type="datetime" placeholder="请选择归还时间" value-format="yyyy-MM-ddTHH:mm:ss">
            </el-date-picker>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="ReturnFun(),ReturndialogVisible = false">归还</el-button>
            <el-button @click="returnForm.r_data = '',returnForm.r_place = ''">重置</el-button>
          </el-form-item>
        </el-form>
    </el-dialog>

  </div>
</template>

<script>
export default {
    data() {
      return {
        ReturndialogVisible: false,
        results: [],
        returnForm:{
          b_ID:"",
          r_date: "",
          r_place: ""
        }        
      }
    },
    methods: {
      checkLentDevices(){
        this.axios
        .get('return/',{})
        .then(res => {
            //console.log(res)
            if (res.data.code === 404){
              this.$message({type: 'info',message: res.data.msg});
            }
            else{
              this.results = res.data
            }
          })
        .catch(failResponse => {
          })
      },
      ReturnFun(){
        this.axios
        .put('return/'+this.returnForm.b_ID+'/',{
          r_date: this.returnForm.r_date,
          r_place: this.returnForm.r_place
        })
        .then(res => {
            //console.log(res)
            if (res.data.code === 404){
              this.$message({type: 'info',message: res.data.msg});
            }
            else if(res.data.code === 500){
              this.$message({type: 'info',message: res.data.msg});
            }
            else{
              this.$message({type: 'success',message: "归还成功"});
            }
          })
        .catch(failResponse => {
          })
        
      },
      openRetuenDialog(row){
        this.returnForm.b_ID = row.b_ID
      },
      handleAllDialogClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
        },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
    },
    mounted:function () {   //自动触发写入的函数，打开页面自动查询
      this.checkLentDevices();
    },
}
</script>

<style>

</style>