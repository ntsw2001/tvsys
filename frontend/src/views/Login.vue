<template>
  <div id="login">
    <div class="homepage-hero-module">
      <div class="video-container">
        <div :style='"fixStyle"' class="filter">
          <!--内容-->
          <el-row type="flex" justify="left">
            <el-col :span="4">
              <div class="grid-content">
                <img src="src/assets/logo.png" width="258" height="100">
              </div>
            </el-col>
          </el-row>

          <el-row type="flex" justify="center">
                <el-col :span="6">
                    <el-card shadow="always">
                      <h1 style="text-align: center;">欢迎登录<br>设备管理系统</h1>
                      <el-divider></el-divider>
                      <el-form  :model="nameValidateForm" ref="nameValidateForm" label-width="100px" class="demo-ruleForm">
                        <el-form-item label="用户ID" prop="u_ID" :rules="[{ required: true, message: '用户ID不能为空！'},]">
                          <el-input placeholder="请输入用户ID" type="text" v-model="nameValidateForm.u_ID" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="u_pass" :rules="[{ required: true, message: '密码不能为空！'},]">
                          <el-input placeholder="请输入密码" v-model="nameValidateForm.u_pass" show-password></el-input>
                        </el-form-item>
                        <el-form-item>
                          <el-button type="primary" @click="login('nameValidateForm')">提交</el-button>
                          <el-button @click="resetForm('nameValidateForm')">清空</el-button>
                        </el-form-item>
                      </el-form>
                    </el-card>
                    <br><br>
                    <a style="color:rgb(255, 255, 255)">本网站仅为个人或团队项目演示或实验</a><br>
                    <a style="color:rgb(255, 255, 255)">©2021版权所有</a><br>
                    <a href="https://beian.miit.gov.cn/" target="_blank" style="color:rgb(255, 255, 255)">苏ICP备2021018238号</a>
                    <br><br><br><br><br><br><br><br><br>
                </el-col>   
          </el-row>
           
        </div>
    <video :style='"fixStyle"' autoplay loop muted class="fillWidth" v-on:canplay="canplay">
      <source src="src/assets/01.mp4" type="video/mp4"/>
      浏览器不支持 video 标签，建议升级浏览器。
    </video>
       <!--  关于fixstyle：
        此页开头div style与这句话上面的video style里面定义了一个动态添加根级反应属性，由于Vue不允许动态添加根级反应属性，
        因此必须通过预先声明所有根级反应数据属性来初始化Vue实例，即使是空值：
        如果未在数据选项中声明，Vue将警告您渲染功能正在尝试访问不存在的属性。
        这种限制背后有技术原因 - 它消除了依赖性跟踪系统中的一类边缘情况，并且还使Vue实例在类型检查系统中发挥更好的作用。
        但是在代码可维护性方面也有一个重要的考虑因素：data对象就像组件状态的模式一样。
        预先声明所有反应属性使得组件代码在以后重新访问或由其他开发人员阅读时更容易理解。
        解决方法：给原有的"fixstyle"再套一对单引号变成：'"fixstyle"'就好了 -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
      name:"Login",
        data() 
        {
            return {
                nameValidateForm: {
                  u_ID: '',
                  u_pass: '',
                },
            };
        },
        methods: {
            resetForm(formName) {//reset button
                this.$refs[formName].resetFields();
            },
            canplay() {//background video
            this.vedioCanPlay = true
            },
            login() {
                this.axios
                  .post('login/', {
                    u_ID: this.nameValidateForm.u_ID,
                    u_pass: this.nameValidateForm.u_pass
                  })
                  .then(res => {
                    const data = res.data
                    if (res.data.code === 200) {
                      this.$message({type: 'success',message: "登录成功"});
                      const u_name = data.u_name
                      const token = data.token
                      console.log(res)
                      this.$store.commit('$_setToken', token);
                      this.$store.commit('$_setUname',u_name);
                      this.$router.push('/homepage')
                    } else {
                      this.$message({type: 'info',message: res.data.msg});
                    }
                  })
                  .catch(failResponse => {
                  })
            },
            mounted: function() {   //屏幕自适应
              window.onresize = () => {
                const windowWidth = document.body.clientWidth
                const windowHeight = document.body.clientHeight
                const windowAspectRatio = windowHeight / windowWidth
                let videoWidth
                let videoHeight
                if (windowAspectRatio < 0.5625) {
                  videoWidth = windowWidth
                  videoHeight = videoWidth * 0.5625
                  this.fixStyle = {
                    height: windowWidth * 0.5625 + 'px',
                    width: windowWidth + 'px',
                    'margin-bottom': (windowHeight - videoHeight) / 2 + 'px',
                    'margin-left': 'initial'
                  }
                } else {
                  videoHeight = windowHeight
                  videoWidth = videoHeight / 0.5625
                  this.fixStyle = {
                    height: windowHeight + 'px',
                    width: windowHeight / 0.5625 + 'px',
                    'margin-left': (windowWidth - videoWidth) / 2 + 'px',
                    'margin-bottom': 'initial'
                  }
                }
              }
              window.onresize()
            }
        }
}
</script>

<style>
  .el-radio-group{
    display: flex;
    margin: 20px;
    justify-content: center;
  }
  .el-card{
    border-radius:30px;
    width: 380px;
    box-shadow: 0 2px 12px 0 rgb(243, 102, 102);
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);    
  }
  .grid-content {
    border-radius: 4px;
    min-height: 80px;
  }
  .el-row {
    margin-bottom: 20px;
  }
/* 背景视频↓ */
.homepage-hero-module,
  .video-container {
    position: relative;
    height: 100vh;
    overflow: hidden;
  }
  .video-container .poster img{
    z-index: 0;
    position: absolute;
  }
  .video-container .filter {
    z-index: 1;
    position: absolute;
    background: rgba(0, 0, 0, 0.4);
    width: 100%;
  }
  .fillWidth {
    width: 100%;
  }
</style>