#!/bin/bash

# 检测davfs2是否已安装的函数
check_davfs2_installation() {
    local os_type=$(lsb_release -is | cut -f2)

    # 检查输出是否为空，如果为空则使用另一种方法确定系统类型
    if [ -z "$os_type" ]; then
        if [ -f /etc/redhat-release ]; then
            os_type="redhat"
        elif [ -f /etc/debian_version ]; then
            os_type="debian"
        else
            echo "无法识别系统类型"
            return 1
        fi
    fi

    # 根据系统类型检查davfs2是否已安装
    case "$os_type" in
        debian)
            dpkg -l | grep -q davfs2
            ;;
        redhat)
            rpm -qa | grep -q davfs2
            ;;
        *)
            echo "不支持的系统类型"
            return 1
            ;;
    esac

    # 如果grep找到davfs2，返回0（成功），否则返回1（失败）
    return $?
}

# 调用函数检查davfs2是否已安装
if check_davfs2_installation; then
    sleep 10
    # 调用api获取ip和端口(待调整)
    sudo mount -t davfs  http://ugreen-e22d:5081/dav/sky/ /home/sky/data/webdav
else
    echo "davfs2未安装"
fi

