<template>
  <el-form class="login-container" label-position="left"
           label-width="0px">
    <h3 class="login_title">系统登录</h3>
    <el-form-item>
      <el-input type="text" v-model="loginForm.u_ID"
                auto-complete="off" placeholder="学号/工号"></el-input>
    </el-form-item>
    <el-form-item>
      <el-input type="password" v-model="loginForm.u_pass"
                auto-complete="off" placeholder="密码"></el-input>
    </el-form-item>
    <el-form-item style="width: 100%">
      <el-button type="primary" style="width: 100%;background: #505458;border: none" v-on:click="login">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        u_ID: '',
        u_pass: ''
      }
    }
  },
  methods: {
    login () {
      this.axios
        .post('', {
          u_ID: this.loginForm.u_ID,
          u_pass: this.loginForm.u_pass
        })
        .then(res => {
          const data = res.data
          if (res.data.code === 200) {
            const u_ID = data.u_ID
            const u_name = data.u_name
            const u_auth = data.u_auth
            const token = data.token
            this.$auth.setUserToken(u_ID, u_name, u_auth, token)
            /* this.$router.replace('/main') */
            console.log(u_ID,u_name,u_auth,token)
          } else {
            console.log(data.code, data.msg)
          }
        })
        .catch(failResponse => {
        })
    }
  }
}
</script>

<style>
  .login-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }

  .login_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }
</style>
