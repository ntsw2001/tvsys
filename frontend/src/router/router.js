import Vue from 'vue'
import Router from 'vue-router'
import Login from "../views/Login"
import Main from '../views/Main'
import User from '../views/User'
import Lend from '../views/Lend'
import Return from '../views/Return'
import Record from '../views/Record'
import Device from '../views/Device'
import Homepage from '../views/Homepage'
import test from '../views/test'
import test2 from '../views/test2'

Vue.use(Router);

const router = new Router({
  routes: [
    {
      // 登录页
      path: '',
      name: 'Login',
      component: Login
    },
    {
      // 首页
      path: '/main',
      name: 'Main',
      component: Main,
      children: [

        {
          path: '/user',
          name: 'User',
          component: User
        },
        {
          path: '/lend',
          name: 'Lend',
          component: Lend
        },
        {
          path: '/return',
          name: 'Return',
          component: Return
        },
        {
          path: '/record',
          name: 'Record',
          component: Record
        },
        {
          path: '/device',
          name: 'Device',
          component: Device
        },
        {
          path: '/homepage',
          name: 'Homepage',
          component: Homepage
        }
      ]
    },
    /* {
      path:'/test',
      name:'test',
      component:test
    },
    {
      path:'/test2',
      name:'test2',
      component:test2
    } */
  ]
})
const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return VueRouterPush.call(this, location).catch(err => err)
}

const VueRouterReplace = Router.prototype.replace
Router.prototype.replace = function replace(location) {
  return VueRouterReplace.call(this, location).catch(err => err)
}
/* 以上
“解决 Vue 重复点击相同路由，出现 Uncaught (in promise) 
NavigationDuplicated: Avoided redundant navigation 问题” */

router.beforeEach((to, from, next) => {
  let token = window.localStorage.token;
  if (token === 'null' || token === '' || token === undefined) {
    if (to.path !== '/') {
      next({ path: '/' })
      alert('请登录后操作！')
    }
    else {
      next()
    }
  }
  else {
    next()
  }
})

export default router;