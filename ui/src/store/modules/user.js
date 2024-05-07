
import { login, logout, getInfo, register, RangeUserImage } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'
import { Message } from 'element-ui'

const getDefaultState = () => {
  return {
    token: getToken(),
    username: '',
    user_id: '',
    nickname: '',
    avatar: '',
    ctime: '',
    utime: '',
    role: '',
    qq: ''
  }
}

const state = getDefaultState()
const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_USERNAME: (state, username) => {
    state.username = username
  },
  SET_USERID: (state, user_id) => {
    state.user_id = user_id
  },
  SET_NICKNAME: (state, nickname) => {
    state.nickname = nickname
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_CTIME: (state, ctime) => {
    state.ctime = ctime
  },
  SET_QQ: (state, qq) => {
    state.qq = qq
  },
  SET_ROLE: (state, role) => {
    state.role = role
  },
  SET_UTIME: (state, utime) => {
    state.utime = utime
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then((response) => {
        commit('SET_TOKEN', response.token)
        setToken(response.token)

        localStorage.setItem('STusername', username.trim())
        localStorage.setItem('STpassword', password)

        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo({ token: state.token }).then((response) => {
        if (!response) {
          return reject('Verification failed, please Login again.')
        }
        commit('SET_USERNAME', response.username)
        commit('SET_USERID', response.user_id)
        commit('SET_NICKNAME', response.nickname)
        commit('SET_AVATAR', process.env.VUE_APP_BASE_API.replace(/\/api\/v1/, '') + response.avatar)
        commit('SET_QQ', response.qq)
        commit('SET_CTIME', response.ctime)
        commit('SET_ROLE', response.role)
        commit('SET_UTIME', response.utime)
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  // user register
  register({ commit }, userInfo) {
    return new Promise((resolve, reject) => {
      
      RangeUserImage().then((response) => {
        userInfo.avatar = response.msg
        register(userInfo).then((response) => {
          // console.log(response)
          if (response.code === 200) {
            Message({
              message: response.msg || 'Success',
              type: 'success',
              duration: 5 * 1000
            })
          }
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

