/*
 * @Date: 2024-04-28 16:59:26
 * @LastEditors: liupeng
 * @LastEditTime: 2024-05-07 13:32:33
 * @FilePath: /SkyTunnel/ui/tests/unit/utils/validate.spec.js
 * @Desc: 
 */
import { validUsername, isExternal } from '@/utils/validate.js'

describe('Utils:validate', () => {
  it('validUsername', () => {
    expect(validUsername('admin')).toBe(true)
    expect(validUsername('editor')).toBe(true)
    expect(validUsername('xxxx')).toBe(false)
  })
  it('isExternal', () => {
    expect(isExternal('https://github.com/PanJiaChen/vue-element-admin')).toBe(true)
    expect(isExternal('http://github.com/PanJiaChen/vue-element-admin')).toBe(true)
    expect(isExternal('github.com/PanJiaChen/vue-element-admin')).toBe(false)
    expect(isExternal('/service')).toBe(false)
    expect(isExternal('./service')).toBe(false)
    expect(isExternal('service')).toBe(false)
  })
})
