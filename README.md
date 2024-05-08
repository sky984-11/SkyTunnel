
# SkyTunnel

SkyTunnel 是一个可以让用户在外地随时访问家中设备和服务的软件。

## 简介

SkyTunnel 目前基于 Lucky 实现(后续将会自己开发客户端)。它通过 Lucky 的 Webhook 将设备的 IP 地址和端口号变化信息发送到中继器中，然后中继器通过 API 接口将 IP 地址和端口号提供给 Web 或 App 端用户。

## 功能特点

- 远程访问：用户可以随时随地通过 SkyTunnel 访问家中设备和服务。
- 动态 IP 支持：SkyTunnel 可以处理设备 IP 地址和端口号的变化，确保用户始终能够访问到设备。
- 部署：支持私有化部署，用户可以将 SkyTunnel 部署在自己的服务器中

## 如何使用

1. 在家中设备上安装并配置 [lucky](https://www.lucky666.cn/docs/install/)。
2. 在luccky中添加穿透规则(如下图)
![image](https://github.com/sky984-11/SkyTunnel/assets/58068214/fdb48fc2-6aea-4621-9738-f7603c43670e)
![image](https://github.com/sky984-11/SkyTunnel/assets/58068214/12b9a544-3753-4a72-a590-d924698b302f)
![image](https://github.com/sky984-11/SkyTunnel/assets/58068214/fe977b8c-f412-4ccb-a025-3350ac056ec3)
3. skytunnel web端即可同步服务
![image](https://github.com/sky984-11/SkyTunnel/assets/58068214/13a1beca-db5e-4af3-b40a-4856f040ebf4)
4. 尝试一下把
![image](https://github.com/sky984-11/SkyTunnel/assets/58068214/fb0748e5-26ed-42d7-88bc-a92244b1fc6e)


## 私有化部署

1. 下载源代码

```sh
git clone https://github.com/sky984-11/SkyTunnel.git
```

2. 修改Setting.json.tmp -> Setting.json,并根据调整其中的服务端地址和sqlite地址
3. 下载相关python依赖

```sh
pip3 install -r requirements.txt

```


## 技术实现

- 前端：vue + elementui
- 后端：flask + sqlite3


## 安装要求

*以下版本为本人使用并且测试过的版本，其他版本自己也可以尝试下*

- Python3.10+ 
- Node21.6

## TODO

- [ ] 增加脚本中心功能(提供一些脚本来支持一些服务的定制化需求，例如webdav挂载)
- [ ] SkyTunnel客户端开发(目前实现是基于lucky来的，后面会自己开发)


## 贡献

我们欢迎任何形式的贡献！如果您发现了 Bug 或者有改进的建议，请提交 Issue 或 Pull Request。

## 联系我们

如果您有任何问题或反馈意见，请通过以下方式联系我们：

 - Email: 1269861316@qq.com
