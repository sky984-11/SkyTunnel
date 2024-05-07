/*
 * @Date: 2024-04-29 08:12:23
 * @LastEditors: liupeng
 * @LastEditTime: 2024-05-07 10:18:42
 * @FilePath: /SkyTunnel/ui/src/api/lucky.js
 * @Desc: 
 */
import request from '@/utils/request'



export function list(data) {
    return request({
      url: '/lucky/stunrule/list',
      method: 'get',
      data
    })
  }

  export function del(stun_id) {
    return request({
      url: '/lucky/del/' + stun_id,
      method: 'delete'
    })
  }

  export function edit(data) {
    return request({
      url: '/lucky/edit',
      method: 'post',
      data
    })
  }