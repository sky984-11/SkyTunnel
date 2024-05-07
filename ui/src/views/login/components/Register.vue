<template>
  <div class="register-container">

    <el-form ref="registerForm" :model="registerForm" :rules="registerRules" label-position="top" class="register-form">
      <h2>欢迎注册</h2>
      <el-form-item prop="username">
        <el-input v-model="registerForm.username" clearable placeholder="手机号或邮箱" />
      </el-form-item>
      <el-form-item prop="password">
        <el-input v-model="registerForm.password" clearable placeholder="设置密码" type="password" />
      </el-form-item>
      <el-form-item prop="confirmPassword">
        <el-input v-model="registerForm.confirmPassword" clearable placeholder="确认密码" type="password" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" class="register-button" @click="submitRegisterForm">注册</el-button>
      </el-form-item>
      <el-form-item>
        <span>点击注册即表示同意并接受<a href="#">《BillEase使用协议》</a>和<a href="#">《隐私政策》</a></span>
      </el-form-item>
      <el-form-item>
        <span>已有帐号？</span>
        <router-link to="/login">去登录</router-link>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'

export default {
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      registerForm: {
        username: '',
        password: '',
        confirmPassword: ''
      },
      registerRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 6,
            max: 20,
            message: '密码长度在6~20个字符之间',
            trigger: 'blur'
          }
        ],
        confirmPassword: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (value !== this.registerForm.password) {
                callback(new Error('两次输入密码不一致'))
              } else {
                callback()
              }
            },
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    // 提交注册表单
    submitRegisterForm() {
      this.$refs.registerForm.validate((valid) => {
        if (valid) {
          // 表单校验通过，可以提交表单到后端进行注册操作
          this.$store
            .dispatch('user/register', this.registerForm)
            .then(() => {
              this.$router.push('/login')
            })
            .catch(() => {
            })
        }
      })
    }
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f5f7f9;
}

.register-form {
  width: 400px;
  background-color: #fff;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
}

.el-input {
  margin-bottom: 20px;
}

.register-button {
  width: 100%;
  background-color: #42bd56;
  border-color: #42bd56;
}

.register-button:hover {
  background-color: #3ea653;
  border-color: #3ea653;
}

.el-form-item:last-child {
  text-align: right;
}

@media (max-width: 768px) {
  .register-form {
    width: 100%;
  }
}
</style>
