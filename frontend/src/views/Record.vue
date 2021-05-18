<template>
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
      <el-table-column align="center" prop="r_date" label="归还时间" width="180" sortable>
      </el-table-column>
      <el-table-column align="center" prop="r_place" label="归还地点" width="90"
      :filters="[{text: '114', value: '114'}, {text: '735', value: '735'}]"
      :filter-method="filterHandler">
      </el-table-column>
      <el-table-column align="center" prop="b_user" label="用户ID" width="100">
      </el-table-column>
      <el-table-column align="center" prop="b_device" label="设备ID" width="120">
      </el-table-column>
      <el-table-column  fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <el-button @click="ConfirmDR(scope.row)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
  </el-table>      
</template>
<script>
export default {
    data() {
      return {
        count: null,
        next: "",
        previous: null,
        DeleteRecord_ID:"",
        results: [],
        multipleSelection: [],    
      }
    },
    methods: {
      
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      DeleteRecord(row){
        this.axios
        .delete('manage/records/'+this.DeleteRecord_ID+'/',{ })
        .then(res => {
            console.log(res)
            if (res.data.code === 404){
              this.$message({type: 'info',message: res.data.msg});
              this.checkRecords();
            }
            else{
              this.$message({type: 'success',message: "删除成功"});
              this.checkDevices();
            }
          })
        .catch(failResponse => {
          })
        },
        ConfirmDR(row) {
        this.DeleteRecord_ID = row.b_ID
        this.$confirm('此操作将删除该记录, 是否继续?', '提示', {
          confirmButtonText: '确定删除',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.DeleteRecord()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消删除'
          });          
        });
      },
      checkRecords(){
        this.axios
          .get('manage/records/', {})
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
      handleSelectionChange(val) {
        this.multipleSelection = val;
        },
   
    },
    
     mounted:function () {   //自动触发写入的函数，打开页面自动查询
          this.checkRecords();
        },
}
</script>

<style>

</style>