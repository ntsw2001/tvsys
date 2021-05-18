<template>
  <div>
    <el-container height="100vh">
      <el-main>
        <el-table :data="results"  border cell-class-name="" stripe style="width: 100%" @selection-change="handleSelectionChange" :default-sort = "{prop: 'u_ID', order: 'descending'}">
          <el-table-column type="selection" width="55">
          </el-table-column>
          <el-table-column align="center" fixed="left" prop="u_ID" label="ID" width="200" sortable>
          </el-table-column>
          <el-table-column align="center" prop="u_name" label="用户名" width="200" sortable>
          </el-table-column>
          <el-table-column align="center" prop="u_auth" label="权限" width="200" :formatter="U_AUTH"
          :filters="[{text: '普通用户（1）', value: 1}, {text: '管理员（6）', value: 6}]"
          :filter-method="filterHandler">
          </el-table-column>
          <el-table-column  fixed="right" label="操作" width="230">
              <template slot-scope="scope">
                <el-button @click="handleEditUserDialogOpen(scope.row)" type="text" size="small">编辑</el-button>
                <el-button @click="ConfirmDU(scope.row)" type="text" size="small">删除</el-button>
                <el-button @click="resetPass(scope.row)" type="text" size="small">重置密码</el-button>
              </template>
          </el-table-column>
        </el-table>

<!-- 编辑用户信息dialog -->
      <el-dialog title="编辑用户信息" :visible.sync="EditUserdialogVisible" width="30%" :before-close="handleEditUserDialogClose">
          <el-form>
            <el-form-item label="用户ID" :label-width="'120px'" placeholder="请填写学号/工号">
              <el-input v-model="EditUserForm.u_ID" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户名" :label-width="'120px'">
              <el-input v-model="EditUserForm.u_name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" :label-width="'120px'" placeholder="请填写密码">
              <el-input v-model="EditUserForm.u_pass" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户权限" :label-width="'120px'">
              <el-select v-model="EditUserForm.u_auth" placeholder="请选择用户权限">
                <el-option label="1(普通用户）" value="1"></el-option>
                <el-option label="6（管理员）" value="6"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button @click="EditUserdialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="EditUser(),EditUserdialogVisible = false">确 定</el-button>
              <!-- <el-button @click="listen()">111</el-button> -->
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
        count: null,
        next: "",
        previous: null,
        results: [],
        multipleSelection: [],
        EditUserdialogVisible: false,
        DeleteUser_ID:"",
        EditUserForm:{
          Old_u_ID:"",
          u_ID: "", // 用户ID
          u_name: "", // 用户名
          u_pass: "", // 默认密码
          u_auth: "" // 用户权限，默认为1
        },
      }
    },
   methods: {
     U_AUTH(row){
        if (row.u_auth === 1) {
          return '普通用户'
        } else if(row.u_auth === 6)  {
          return '管理员'
        } 
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      listen(){
        console.log(this.EditUserForm)
      },
      resetPass(row){
        this.axios
        .post('reset/',{
          u_ID : row.u_ID
        })
        .then(res => {
            console.log(res)
            if (res.data.code === 200){
              this.$message({type: 'info',message: res.data.msg});
            }
            else{
              this.$message({type: 'info',message: "重置时发生错误，请联系管理员"});
            }
          })
        .catch(failResponse => {
          })
      },
      EditUser() {
      this.axios
        .put('manage/users/'+this.EditUserForm.Old_u_ID+'/',{
          u_ID : this.EditUserForm.u_ID,
          u_name : this.EditUserForm.u_name,
          u_pass : this.EditUserForm.u_pass,
          u_auth : this.EditUserForm.u_auth
        })
        .then(res => {
            console.log(res)
            if (res.data.code === 404){
              this.$message({type: 'info',message: res.data.msg});
              this.checkUsers();
            }
            else{
              this.$message({type: 'success',message: "修改成功"});
              this.checkUsers();
            }
          })
        .catch(failResponse => {
          })
      },
      handleEditUserDialogOpen(row){
        this.EditUserdialogVisible = true 
        this.EditUserForm.Old_u_ID = row.u_ID
        this.EditUserForm.u_ID = row.u_ID
        this.EditUserForm.u_name = row.u_name
        this.EditUserForm.u_pass = row.u_pass
        this.EditUserForm.u_auth = row.u_auth
        //console.log(this.EditUserForm)
      },
      handleEditUserDialogClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      DeleteUser(){
        this.axios
        .delete('manage/users/'+this.DeleteUser_ID+'/',{ })
        .then(res => {
            console.log(res)
            if (res.data.code === 404){
              this.$message({type: 'info',message: res.data.msg});
              this.checkUsers();
            }
            else{
              this.$message({type: 'success',message: "删除成功"});
              this.checkUsers();
            }
          })
        .catch(failResponse => {
          })
        },
        ConfirmDU(row) {
        this.DeleteUser_ID = row.u_ID
        this.$confirm('此操作将删除该用户, 是否继续?', '提示', {
          confirmButtonText: '确定删除',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.DeleteUser()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消删除'
          });          
        });
      },
      checkUsers(){
        this.axios
          .get('manage/users/', {})
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
          this.checkUsers();
        },
}

</script>

<style>

</style>