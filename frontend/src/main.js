import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router/router'
import store from './store/store'
// import axios from 'axios'

var axios = require('axios')
axios.defaults.baseURL = 'http://127.0.0.1:61925/'

Vue.prototype.$http = axios;
Vue.prototype.axios = axios;
Vue.use(ElementUI);
Vue.use(VueRouter);

//请求拦截器，在请求头中加token
axios.interceptors.request.use(
  config => {
    if (localStorage.getItem('token')) {
      config.headers.Authorization = 'JWT '+localStorage.getItem('token');
      config.headers.Referer = localStorage.getItem('token');
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  });
//http reponse响应拦截器
axios.interceptors.response.use(
  response =>{
    return response;
  },
  error=>{
    if(error.response){
      switch(error.response.status){
        case '':
          localStorage.removeItem('token');
          router.replace({
            path: '/',
            query: {redirect: router.currentRoute.fullPath}//登录成功后跳入浏览的当前页面
          })
      }
    }
  })

new Vue({
  el: '#app',
  
// 启用路由
  router,
// 启用 ElementUI
  render: h => h(App),
//
  store,
  
})
