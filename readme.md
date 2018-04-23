# DOMJudge 安装指南 (以Ubuntu 17.10为例，其他系统可能不同)

Author: Yulin Shen (sylxjtu@outlook.com)

## 安装docker

运行命令

```bash
sudo apt-get install docker.io docker-compose
```

## 开启cgroups

打开`/etc/default/grub`，在`GRUB_CMDLINE_LINUX=`后加上以下参数

```
cgroup_enable=memory swapaccount=1
```

运行命令

```
sudo update-grub
sudo update-grub2
```

重启，之后运行以下命令

```
sudo docker info
```

确认没有关于swap的WARNING

## 修改`docker-compose.yml`文件

1. `mariadb.volumes`: 数据持久化的目录，修改成合适目录名，之后会创建这个目录

2. `MYSQL_ROOT_PASSWORD`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`: 可以根据需要修改，注意保持一致

3. `domserver.ports`: 网页端端口，可以根据需要修改

4. `judgehost_[0-9]`: 评测进程的数量，每个评测进程会绑定到`CPU{DAEMON_ID}`，因此必须确保每个评测进程的`DAEMON_ID`不同

## 创建`mariadb.volumes`对应的目录

## 启动

```
sudo docker-compose up -d
```

如果没有修改端口的话，访问`http://localhost:12345`进入网页端，用户名和密码均为`admin`

## 添加评测机

在网页端添加评测机用户并设置密码，与`docker-compose.yml`一致

## 修改管理员密码

