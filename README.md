# HeXunSpider

#### 项目介绍
使用 scrapy 编写的讯博客全站文章内容爬虫，可以爬取全站的文章标题、文章链接、点击数和评论数。

#### 软件架构
采用 scrapy 爬取后再使用 MongoDB 数据库来存储爬取的数据


#### 安装教程

1. 使用 python3 安装 scrapy 命令为：pip install scrapy
2. 安装 MongoDB 数据库并创建数据库名为"hexun"

#### 使用说明

1. 下载项目

git clone https://gitee.com/cix/HeXunSpider

2. 进入项目文件夹

cd HeXunSpider/

3. 执行项目

scrapy crawl hexun

4. 最终效果

![输入图片说明](https://images.gitee.com/uploads/images/2018/0911/170557_616c0967_1577043.png "Snip20180911_18.png")