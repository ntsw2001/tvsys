<template>
  <div id="app">
    <el-container style="height: 100vh"><!-- el-cointainer高度设置为100%铺满页面 -->
            <el-menu default-active="" class="el-menu-vertical-demo" @open="menuOpen" @close="menuClose" :collapse="menuStatu"><!-- defule-active默认打开的menu -->
            <el-button round @click="homepage">主页</el-button>

            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-s-home"></i>
                <span slot="title">设备借还</span>
              </template>

              <el-menu-item-group>
                <el-menu-item index="1-1" @click="lend">借设备</el-menu-item>
                <el-menu-item index="1-2" @click="Return">还设备</el-menu-item>
              </el-menu-item-group>
            </el-submenu>

            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-s-help"></i>
                <span slot="title">管理功能</span>
              </template>

              <el-menu-item-group>
              <el-submenu index="2-1">
                  <span slot="title">设备</span>
                    <el-menu-item index="2-1" @click="device">设备列表</el-menu-item>
                    <el-menu-item index="2-1-2" @click="NewDevicedialogVisible = true">添加设备</el-menu-item>
                  </el-submenu>

                  <el-submenu index="2-2">
                  <span slot="title">用户</span>
                    <el-menu-item index="2-2-1" @click="user">用户列表</el-menu-item>
                    <el-menu-item index="2-2-2" @click="NewUserdialogVisible = true">添加用户</el-menu-item>
                  </el-submenu>
                
                <el-submenu index="2-3">
                  <span slot="title">借还记录</span>
                    <el-menu-item index="2-3-1" @click="record">借用记录列表</el-menu-item>
                    <el-menu-item index="2-3-2" @click="NewRecorddialogVisible = true">添加借用记录</el-menu-item>
                  </el-submenu>
              </el-menu-item-group>
            </el-submenu>

            <el-submenu index="3">
              <template slot="title">
                <i class="el-icon-s-home"></i>
                <span slot="title">个人功能</span>
              </template>

              <el-menu-item-group>
                <el-menu-item index="1-1" @click="modifydialogVisible = true">修改密码</el-menu-item>
                <el-menu-item index="1-2" disabled>个人主页</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="6" @click="returnFun">登出</el-menu-item>
            <!-- 展开开关 -->
              <el-switch
              v-model="menuStatu"
              inactive-color="#808080"
              active-color="#808080">
            </el-switch>

          </el-menu>
          <el-container>  
                <el-header style="text-align: right; font-size: 12px ">
                    <div>{{ nowDate }}</div><!-- el-header时钟 -->
                </el-header>

                    <el-main>
                    <router-view>
                      <!-- main二级路由窗口 -->
                    </router-view>
                    </el-main>

              <el-footer style="text-align: center; font-size: 12px "> 
<!--                 <img src="src\assets\logo.png" width="120" height="40" @click="returnFun"><br> -->
                <img src="src\assets\logo.png" width="120" height="40"><br>
                <a>本网站仅为个人或团队项目演示或实验</a>
                <a>©2021版权所有</a>
                <a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备2021018238号</a>
              </el-footer>
            </el-container>
    </el-container>

  <!--   新建用户 dialog -->
      <el-dialog title="添加新用户" :visible.sync="NewUserdialogVisible" width="30%" :before-close="handleAllDialogClose">
          <el-form>
            <el-form-item label="用户ID" :label-width="'120px'" placeholder="请填写学号/工号">
              <el-input v-model="NewUserForm.u_ID" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户名" :label-width="'120px'">
              <el-input v-model="NewUserForm.u_name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户权限" :label-width="'120px'">
              <el-select v-model="NewUserForm.u_auth" placeholder="请选择用户权限">
                <el-option label="1(普通用户）" value="1"></el-option>
                <el-option label="6（管理员）" value="6"></el-option>
              </el-select>
            </el-form-item>
            <!-- <span>默认密码123456请自行更改密码</span> -->
            <el-form-item>
              <el-button @click="NewUserdialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="NewUser(),NewUserdialogVisible = false">确 定</el-button>
            </el-form-item>
          </el-form>
      </el-dialog>

  <!--   新建设备 dialog -->
  <el-dialog title="添加新设备" :visible.sync="NewDevicedialogVisible" width="30%" :before-close="handleAllDialogClose">
      <el-form>
        <el-form-item label="设备名称" :label-width="'120px'" placeholder="请填写名称">
          <el-input v-model="NewDeviceForm.d_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="设备类型" :label-width="'120px'">
          <el-select v-model="NewDeviceForm.d_type" placeholder="请选择设备类型">
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
          <el-select v-model="NewDeviceForm.d_see" placeholder="请选择设备可见等级">
            <el-option label="所有人可见（1）" value="1"></el-option>
            <el-option label="管理员可见（9）" value="9"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="设备状态" :label-width="'120px'">
          <el-select v-model="NewDeviceForm.d_status" placeholder="请选择设备状态">
            <el-option label="未借出且完好（1）" value="1"></el-option>
            <el-option label="借出（0）" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="设备所在地点" :label-width="'120px'">
          <el-select v-model="NewDeviceForm.d_place" placeholder="请选择设备所在地点">
            <el-option label="114" value="114"></el-option>
            <el-option label="735" value="735"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="新建设备时间" :label-width="'120px'">
          <el-date-picker v-model="NewDeviceForm.d_date" type="date" placeholder="选择日期" format="yyyy 年 MM 月 dd 日" value-format="yyyy-MM-dd">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="备注" :label-width="'120px'" placeholder="可空">
          <el-input v-model="NewDeviceForm.d_others" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="NewDevicedialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="NewDevice(),NewDevicedialogVisible = false">确 定</el-button>
          <!-- <el-button @click="listen1()">111</el-button> -->
        </el-form-item>
      </el-form>
  </el-dialog>


  <!--   新建Record dialog -->
  <el-dialog title="添加新借用明细" :visible.sync="NewRecorddialogVisible" width="30%" :before-close="handleAllDialogClose">
    <el-form>
        <el-form-item label="借用者ID" :label-width="'120px'" placeholder="请填写ID">
          <el-input v-model="NewRecordForm.b_user" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="借用设备ID" :label-width="'120px'" placeholder="请填写ID">
          <el-input v-model="NewRecordForm.b_device" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="借用时间" :label-width="'120px'">
          <el-date-picker v-model="NewRecordForm.b_date" type="datetime" placeholder="选择日期" value-format="yyyy-MM-ddTHH:mm:ss">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="借用原因" :label-width="'120px'" placeholder="请填写原因">
          <el-input v-model="NewRecordForm.b_reason" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="借用地点" :label-width="'120px'">
          <el-select v-model="NewRecordForm.b_place" placeholder="请选择借用设备地点">
            <el-option label="114" value="114"></el-option>
            <el-option label="735" value="735"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="归还时间" :label-width="'120px'">
          <el-date-picker v-model="NewRecordForm.r_date" type="datetime" placeholder="未归还不用填写" value-format="yyyy-MM-ddTHH:mm:ss">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="归还地点" :label-width="'120px'">
          <el-select v-model="NewRecordForm.r_place" placeholder="未归还不用填写">
            <el-option label="114" value="114"></el-option>
            <el-option label="735" value="735"></el-option>
          </el-select>
        </el-form-item>
      <el-form-item>
        <el-button @click="NewRecorddialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="NewRecord(),NewRecorddialogVisible = false">确 定</el-button>
        <!-- <el-button @click="listen1()">111</el-button> -->
      </el-form-item>
    </el-form>
  </el-dialog>

<!--   修改密码 -->
    <el-dialog title="修改密码" :visible.sync="modifydialogVisible" width="30%" :before-close="handleAllDialogClose">
        <el-form :model="modifyForm" status-icon :rules="modifyrules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="旧密码" prop="u_pass_old">
            <el-input type="password" v-model="modifyForm.u_pass_old" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="新密码" prop="u_pass_new">
            <el-input type="password" v-model="modifyForm.u_pass_new" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认新密码" prop="check_u_pass_new">
            <el-input type="password" v-model="modifyForm.check_u_pass_new" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="modifyFun()">提交</el-button>
            <el-button @click="modifyForm.u_pass_new = null , modifyForm.u_pass_old = null , modifyForm.check_u_pass_new = null">重置</el-button>
          </el-form-item>
        </el-form>
    </el-dialog>
  
    </div>
</template>

<script>

export default {
        name: "Main",
    data() {
       var validatePass1 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入新密码'));
        } else {
          if (this.modifyForm.check_u_pass_new !== '') {
            this.$refs.modifyForm.validateField('check_u_pass_new');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入新密码'));
        } else if (value !== this.modifyForm.u_pass_new) {
          callback(new Error('两次输入的新密码不一致!'));
        } else {
          callback();
        }
      };
      var validatePass0 = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('旧密码不能为空'));
        }
      };
      return {
        nowDate: "", // 当前日期
        NewRecordForm:{
          b_user: "",
          b_device: "",
          b_date: "2021-02-26T00:00:00", //必须补全到秒，勿忘T
          b_reason: "",
          b_place: "",
          r_assign: null, //可为空
          r_date: "2021-02-26T15:00:00", //可为空
          r_place: "" //可为空
        },
        NewUserForm:{
          u_ID: "", // 用户ID
          u_name: "", // 用户名
          u_pass: "123456", // 默认密码
          u_auth: "" // 用户权限，默认为1，前端还是要传的
        },
        NewDeviceForm:{
          d_see: "", //可见等级1/9
          d_type: "", //大类1/2/3
          d_name: "", //名字
          d_date: "", //注意！这里必须要补全到 日，以yyyy-mm-dd形式传回
          d_status: "", //状态，默认1为未借出且完好，0为借出
          d_place: "", //地点
          d_others: "" //设备备注，可为空
        },
        modifyForm:{
          u_pass_old: "",
          u_pass_new: "",
          check_u_pass_new: "",
        },
        modifyrules: {
          u_pass_new: [
            { validator: validatePass1, trigger: 'blur' }
          ],
          check_u_pass_new: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          u_pass_old: [
            { validator: validatePass0, trigger: 'blur' }
          ]
        },
        menuStatu: false ,
        NewUserdialogVisible: false,
        NewDevicedialogVisible: false,
        NewRecorddialogVisible: false,
        modifydialogVisible: false,
      }
    },

    methods: {
      /* listen1(){
        console.log(this.NewRecordForm)
      }, */
      currentTime() {
        setInterval(this.formatDate, 500);
      },
      formatDate() {
        let date = new Date();
        let year = date.getFullYear(); // 年
        let month = date.getMonth() + 1; // 月
        let day = date.getDate(); // 日
        let week = date.getDay(); // 星期
        let weekArr = [ "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" ];
        let hour = date.getHours(); // 时
        hour = hour < 10 ? "0" + hour : hour; // 如果只有一位，则前面补零
        let minute = date.getMinutes(); // 分
        minute = minute < 10 ? "0" + minute : minute; // 如果只有一位，则前面补零
        let second = date.getSeconds(); // 秒
        second = second < 10 ? "0" + second : second; // 如果只有一位，则前面补零
        this.nowDate = `${year}/${month}/${day} ${hour}:${minute}:${second} ${weekArr[week]}`;
      },
      menuOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      menuClose(key, keyPath) {
        console.log(key, keyPath);
      },
      homepage(){
        this.$router.replace('./homepage')
      },
      lend(){
        this.$router.replace('./lend')
      },
      Return(){
        this.$router.replace('./return')
      },
      record(){
        this.$router.replace('./record')
      },
      user(){
        this.$router.replace('./user')
      },
      device(){
        this.$router.replace('./device')
      },
      modifyFun(){
        this.axios
          .post('modify/', {
            u_pass_old: this.modifyForm.u_pass_old, // 旧密码
            u_pass_new: this.modifyForm.u_pass_new // 新密码
          })
          .then(res => {
            if(res.data.code === 403){
              this.$message({type: 'info',message: res.data.msg});
              modifyForm.u_pass_new = null
              modifyForm.u_pass_old = null
              modifyForm.check_u_pass_new = null
            }
            else if(res.data.code === 500){
              this.$message({type: 'info',message: res.data.msg});
              modifyForm.u_pass_new = null
              modifyForm.u_pass_old = null
              modifyForm.check_u_pass_new = null
            }
            else if(res.data.code === 200){
              this.$message({type: 'success',message: "修改成功"});
            }
          })
          .catch(failResponse => {
          })
      },
      NewRecord(){
        this.$router.replace('/record');
        this.axios
          .post('manage/records/', {
            b_user:this.NewRecordForm.b_user,
            b_device:this.NewRecordForm.b_device,
            b_date:this.NewRecordForm.b_date, //必须补全到秒，勿忘T
            b_reason:this.NewRecordForm.b_reason,
            b_place:this.NewRecordForm.b_place,
            r_assign:null, //可为空
            r_date:this.NewRecordForm.r_date, //可为空
            r_place:this.NewRecordForm.r_place //可为空

          })
          .then(res => {
            this.$message({type: 'success',message: "新记录创建成功"});
            this.checkRecords();
            //this.$router.replace('/user')
          })
          .catch(failResponse => {
          })
      },
      NewUser(){
        this.$router.replace('/user');
        this.axios
          .post('manage/users/', {
            u_ID: this.NewUserForm.u_ID, // 用户ID
            u_name: this.NewUserForm.u_name, // 用户名
            u_pass: "123456", // 默认密码
            u_auth: this.NewUserForm.u_auth // 用户权限，默认为1，前端还是要传的
          })
          .then(res => {
            this.$message({type: 'success',message: "新用户创建成功"});
            this.checkUsers();
            //this.$router.replace('/user')
          })
          .catch(failResponse => {
          })
      },
      NewDevice(){
        this.$router.replace('/device');
        this.axios
          .post('manage/devices/', {
            d_see: this.NewDeviceForm.d_see, //可见等级1/9
            d_type: this.NewDeviceForm.d_type, //大类1/2/3
            d_name: this.NewDeviceForm.d_name, //名字
            d_date: this.NewDeviceForm.d_date, //注意！这里必须要补全到 日，以yyyy-mm-dd形式传回
            d_status: this.NewDeviceForm.d_status, //状态，默认1为未借出且完好，0为借出
            d_place: this.NewDeviceForm.d_place, //地点
            d_others: this.NewDeviceForm.d_others //设备备注，可为空
          })
          .then(res => {
            //console.log(res)
            this.$message({type: 'success',message: "新设备创建成功"});
            this.checkDevices();
            //this.$router.replace('/user')
          })
          .catch(failResponse => {
          })
      },
      handleAllDialogClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      returnFun(){   // 退出登录
	      //MessageBox.confirm(this.lang.logoutTip).then(action => {
	     this.$store.commit('$_removeStorage');    // 清除登录信息
       this.$store.commit('$_removeuname');
	     this.$router.push('/');
	     //Toast({message:this.lang.logoutSuccess, duration: 1500});
       this.$message({type: 'success',message: "退出登录成功"});
	     //.catch(()=>{})
      },
    },  
    mounted() {
    this.currentTime();
    },
    // 销毁定时器
    beforeDestroy() {
      if (this.formatDate) {
        clearInterval(this.formatDate); // 在Vue实例销毁前，清除时间定时器
      }
    }   
}
</script>

<style>
  .el-header{
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .el-footer{
    background-color: #b3c0d100;
    color: #333;
  }
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  .el-container{
    padding: 0%;
    height: 100vh;
    position: relative;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }

</style>