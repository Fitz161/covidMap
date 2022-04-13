<div align="center">

# 疫情地图

基于[ Flask ](https://github.com/pallets/flask)框架以及[ echarts ](https://github.com/apache/echarts/)开发的疫情可视化网页

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
</div>
</br>
<div align="center">

### 项目介绍
</div>

本项目基于[ Python爬取疫情实战 ](https://www.bilibili.com/video/BV177411j7qJ)开发。可点击 [此处](http://yorushika.xyz:8888/) 预览成功部署后的页面。本项目使用Flask作为web服务框架，提供后台数据接口，利用python实现公开数据的抓取并插入数据库，前端基于jquery使用ajax异步加载数据，echarts根据填充的数据进行可视化。
<br>

<div align="center">

### 安装使用
</div>

- 按照 `database.txt` 中的内容配置好mysql数据库
- 安装 Google Chrome 和 chromedriver
- 克隆项目到本地 `git clone https://gitee.com/fitz161/covidMap.git`，或者下载源码压缩包并解压
- 切换到项目所在目录 `cd covidMap/`
- 安装依赖的包 `pip insatll -r requirments.txt -i https://pypi.douban.com/simple`
- 打开config.py文件配置数据库账号
- 开启服务 `python main.py`

<div align="center">

### 注意事项
</div>

- 项目中chromedriver适用于Google Chrome98版本，其他版本请前往 [此处](https://chromedriver.storage.googleapis.com/index.html) 下载并复制到项目所在目录。
- 仅需本地部署服务时，需删去`main.py`最后一行的`host`参数