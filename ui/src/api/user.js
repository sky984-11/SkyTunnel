/*
 * @Date: 2024-04-28 16:59:26
 * @LastEditors: liupeng
 * @LastEditTime: 2024-05-06 14:57:51
 * @FilePath: /SkyTunnel/ui/src/api/user.js
 * @Desc: 
 */


import request from '@/utils/request'

export function login(data) {
  var formdata = new FormData()
  formdata.append('username', data['username'])
  formdata.append('password', data['password'])
  return request({
    url: '/user/login',
    method: 'post',
    data: formdata
  })
}

export function register(data) {
  var formdata = new FormData()
  formdata.append('username', data['username'])
  formdata.append('password', data['password'])
  formdata.append('avatar', data['avatar'])
  return request({
    url: '/user/register',
    method: 'post',
    data: formdata
  })
}

export function getInfo(data) {
  return request({
    url: '/user/info',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/user/logout',
    method: 'get'
  })
}

export function RangeUserImage() {
  return request({
    url: '/user/image/random',
    method: 'get'
  })
}
