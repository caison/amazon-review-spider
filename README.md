# 亚马逊评论爬取工具

## 打包exe
基于python3.7 使用命令：pyinstaller -F --hidden-import=queue main_spider.py 
## 功能
爬取亚马逊评论，基于百度翻译接口把英文评论翻译成中文，输出excel
## 使用说明
在输入信息/商品地址文件.txt 输入要爬取的亚马逊网站的地址，每行一个地址
