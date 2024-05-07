<!--
 * @Date: 2024-04-28 16:59:26
 * @LastEditors: liupeng
 * @LastEditTime: 2024-05-07 09:10:26
 * @FilePath: /SkyTunnel/ui/src/views/homepage/index.vue
 * @Desc: 
-->

<template>
  <el-row justify="center" :gutter="20">
     <el-col :xs="24" :sm="12" :md="8" :lg="6" v-for="item in tunnelList" :key="item.id" style="margin-right: 10px;margin-top:10px">
    <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span style="font-weight: bold;font-size:25px">{{item.name}}</span>
    <el-button class="button" type="success" icon="el-icon-s-promotion" @click="toService(item)" >访问</el-button>
    <el-button class="button" type="warning" icon="el-icon-edit" @click="editService(item)" >编辑</el-button>
    <el-button class="button" type="danger" icon="el-icon-delete" @click="delService(item)" >删除</el-button>
  </div>
  <div class="text item">
    {{'访问地址： ' + 'http://' + item.ip + ':' + item.port +  '/' + item.suffix }}
  </div>
    <div class="text item">
    {{'域名： ' + item.domain }}
  </div>
  <div class="text item ">创建时间: {{ item.ctime }}</div>
  <div class="text item ">触发时间: {{ item.otime }}</div>
</el-card>

     </el-col>
  </el-row>
</template>

<script>
import {list,del} from '@/api/lucky'

export default {
  data() {
    return {
      tunnelList: [],
      listLoading: true,
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      list().then(res => {
        // console.log(res)
        if(res.code === 200){
          this.tunnelList = res.msg
        }
        
        this.listLoading = false
      })
    },
    toService(item) {
      const link = 'http://' + item.ip + ':' + item.port+  '/' + item.suffix
      window.open(link, '_blank');
    },

    delService(item){
      console.log(item)
      del(item.id).then(res => {
        if(res.code === 200){
          this.fetchData()
          this.$message.success(res.msg)
        }
      })
    },

    editService(item){
      console.log(item)
      // edit(item).then(res => {
      //   if(res.code === 200){
      //     this.fetchData()
      //     this.$message.success(res.msg)
      //   }
      // })
    },
  }
}
</script>




<style>
.text {
    font-size: 14px;
  }
.item {
    margin-bottom: 18px;
  }
.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
  }
.clearfix:after {
    clear: both
  }

.box-card {
    width: 480px;
  }

.button {
    padding: 3px 0;
    float: right;
    margin: 3px;
  }
.time {
    font-size: 13px;
    color: #999;
  }

</style>