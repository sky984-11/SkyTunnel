/*
 * @Date: 2024-04-28 16:59:26
 * @LastEditors: sky
 * @LastEditTime: 2024-05-08 10:13:03
 * @FilePath: /SkyTunnel/ui/src/utils/validate.js
 * @Desc: 
 */


/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validUsername(str) {
  const valid_map = ['admin', 'editor']
  return valid_map.indexOf(str.trim()) >= 0
}
