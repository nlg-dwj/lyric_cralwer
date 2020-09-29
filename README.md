# lyric_crawler
爬取网易云音乐歌手歌词
## 需要安装的包：

 - re
 - shutil
 - gensim
 - jieba
 - requests
 - bs4
 - lxml
 ## 爬取歌词流程
 
 - 爬取网易云的歌手id，可以通过lyric_crawler.py里的find_artist_ids()函数或者get_all_singer.py来实现抓取。
 - 然后通过lyric_crawler.py来实现歌词抓取。
 - 爬取完成以后可以使用lyric_filter.py来过滤英文歌曲和获取纯净歌词文本。
 - 使用lyric_similarity.py进行去重
 ## 爬取歌曲文件流程
 
 - 运行song_download.py，输入想要爬取的歌单网址即可。
## 同时爬取歌曲和歌词文件流程
 - 运行song_and_lyric_download.py

 ## 注意事项
 
 - 在爬取歌词的过程中，爬取速度过快的话，会被网易云封锁ip，可以使用芝麻代理这个软件来使用代理ip进行爬取。

 

