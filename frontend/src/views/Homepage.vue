<template>
    <div>
        <el-container>
            <el-main>
              <el-card>
                <el-carousel indicator-position="outside" >
                    <el-carousel-item v-for="item in imgList1" :key="item.name">
                    <img :src="item.src" style="height:100%;width:100%;" alt="图片丢失了" :title="item.title" />
                    </el-carousel-item>
                </el-carousel>
              </el-card> 

              <el-row>
                <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
                <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
              </el-row>

              <el-card>
                <a href="http://zqb.cyol.com/html/2021-04/12/nw.D110000zgqnb_20210412_1-07.htm">
                <img src='../assets/paper1.png' width='100%'></a>
              </el-card>    
            </el-main>

            <el-main>
              <el-card>
                <a href="http://www.njtech.edu.cn/info/1061/2303216.htm">
                <img src='../assets/paper2.png' width='100%'></a>
              </el-card>
              <el-row>
                <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
                <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
              </el-row>
              <el-card>
                <a href="http://www.njtech.edu.cn/info/1061/2114905.htm">
                <img src='../assets/paper3.png' width='100%'></a>
              </el-card>
            </el-main>
        </el-container>
    </div>
</template>

<script>
export default {
name:'Homepage',
    data() {
        return {
            imgList1: [
            {
            name: "jpg1",
            src: require("../assets/1.jpg"),
            title: "1"
            },
            {
            name: "jpg2",
            src: require("../assets/2.jpg"),
            title: "2"
            },
            /* {
            name: "jpg3",
            src: require("@/assets/3.jpg"),
            title: "3"
            },
            {
            name: "jpg4",
            src: require("@/assets/4.jpg"),
            title: "4"
            }, */
            ]   
        }
    },
}
</script>

<style scope>
.el-card{
    border-radius:30px;
    height: 350px;
    width: 800px;
    box-shadow: 0 2px 12px 0 rgb(243, 102, 102);
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);    
  }
/* .el-card-text{
    border-radius:30px;
    height: 500px;
    width: 300px;
    box-shadow: 0 2px 12px 0 rgb(243, 102, 102);
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);    
  } */
.bg-purple-dark {
    background: #99a9bf;
  }

.grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

   .el-carousel {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
</style>