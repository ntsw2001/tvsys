import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const state = {     // 全局管理的数据存储
	 isLogin:'0',
	 ser:null,
	 token:localStorage.getItem('token') ? localStorage.getItem('token'):'',   // token
	 u_name:localStorage.getItem('u_name') ? localStorage.getItem('u_name'):'',
};
export default new Vuex.Store({
	state,
	getters:{    // 监听数据变化的
		getStorage(state){   // 获取本地存储的登录信息
	      if(!state.token){
	        state.token =JSON.parse(localStorage.getItem(key))
	      }
	      return state.token
	    }
	},
	mutations:{
		$_setUname(state,value){//设置用户名localstorage储存
			state.u_name = value;
			localStorage.setItem('u_name',value);
		},
		$_removeuname(state,value){//删除储存的用户名
			localStorage.removeItem('u_name');
		},
		$_setToken(state, value) { // 设置存储token
	        state.token = value;
	        localStorage.setItem('token', value);
	    },
	    $_removeStorage(state, value){  // 删除token
		      localStorage.removeItem('token');
	    },
	}
})
