<!--
 * @Date: 2024-04-28 16:59:26
 * @LastEditors: sky
 * @LastEditTime: 2024-05-08 10:13:20
 * @FilePath: /SkyTunnel/ui/src/views/homepage/index.vue
 * @Desc: 
-->

<template>
  <el-row justify="center" :gutter="24" style="padding: 10px;">
    <el-col
      :xs="24"
      :sm="12"
      :md="8"
      :lg="7"
      v-for="item in tunnelList"
      :key="item.id"

    >
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-weight: bold; font-size: 25px">{{
            item.name
          }}</span>
          <el-button
            class="button"
            type="success"
            icon="el-icon-s-promotion"
            @click="toService(item)"
            >访问</el-button
          >
          <el-button
            class="button"
            type="warning"
            icon="el-icon-edit"
            @click="showEditDialog(item)"
            >编辑</el-button
          >
          <el-button
            class="button"
            type="danger"
            icon="el-icon-delete"
            @click="delService(item)"
            >删除</el-button
          >
        </div>
        <div class="text item">
          {{ "访问地址： " + "http://" + item.ip + ":" + item.port }}
        </div>
        <div class="text item">
          {{ "域名： " + item.domain }}
        </div>
        <div class="text item">
          {{ "地址后缀： " + item.suffix }}
        </div>
        <div class="text item">创建时间: {{ item.ctime }}</div>
        <div class="text item">触发时间: {{ item.otime }}</div>
      </el-card>
    </el-col>

    <el-dialog title="修改" :visible.sync="dialog.edit.show">
      <el-form
        :model="dialog.edit.form"
        :label-width="dialog.edit.formLabelWidth"
        :rules="dialog.edit.rules"
      >
        <el-form-item label="域名" prop="domain">
          <el-input
            v-model="dialog.edit.form.domain"
            autocomplete="off"
            placeholder="填写域名后优先使用域名进行访问，格式：www.baidu.com"
          ></el-input>
        </el-form-item>
        <el-form-item label="后缀" prop="suffix">
          <el-input
            v-model="dialog.edit.form.suffix"
            autocomplete="off"
            placeholder="可以给访问地址添加后缀，例如 http://192.168.3.1/test，其中 /test 为后缀部分"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editServiceClose">取消</el-button>
        <el-button type="primary" @click="editService">确定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
import { list, del, edit } from "@/api/lucky";

export default {
  data() {
    return {
      tunnelList: [],
      listLoading: true,
      dialog: {
        edit: {
          show: false,
          formLabelWidth: "80px",
          form: {},
          rules: {
            // domain:[{ pattern: /^(www\.)?[a-zA-Z0-9]+\.[a-zA-Z]{2,}$/, message: '请输入正确的域名格式' }],
            // suffix:[{ pattern: /^\/.*/, message: '后缀必须以/开头' }]
          },
        },
      },
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.listLoading = true;
      list().then((res) => {
        if (res.code === 200) {
          this.tunnelList = res.msg;
        }

        this.listLoading = false;
      });
    },
    toService(item) {
      const domain = item.domain || item.ip;
      const suffix = item.suffix ? item.suffix : "";
      const link = `http://${domain}:${item.port}${suffix}`;
      window.open(link, "_blank");
    },

    delService(item) {
      console.log(item);
      del(item.id).then((res) => {
        if (res.code === 200) {
          this.fetchData();
          this.$message.success(res.msg);
        }
      });
    },

    editService() {
      edit(this.dialog.edit.form).then((res) => {
        if (res.code === 200) {
          this.fetchData();
          this.$message.success(res.msg);
          this.dialog.edit.show = false;
        }
      });
    },

    showEditDialog(item) {
      this.dialog.edit.form = item;
      this.dialog.edit.show = true;
    },
    editServiceClose() {
      this.fetchData();
      this.dialog.edit.show = false;
    },
  },
};
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
  clear: both;
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

.el-card__header{
 background-color: rgb(42, 177, 177);
}

.el-card__body{
  background-color: rgb(180, 184, 184);
}
</style>
