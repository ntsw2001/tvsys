<template>
  <div id="app">
    <router-view/>   
  </div>
</template>

<script>
  export default {
    name: 'app',
  }
</script>

<style>
#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
  width: 100%;
  height: 100%;
  position: relative;
}
</style>

<style type="text/css">
html,body,#app,.el-container{
        padding: 0px;
         
        margin: 0px;
        height: 100%;
}/*设置外部间距.内部填充为0，几个布局元素之间没有间距,统一设置高度为100%*/
</style>



