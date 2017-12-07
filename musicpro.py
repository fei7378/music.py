import requests
import os
primary_url="http://kg.qq.com/node/play?s=AFtGvaAm-2lylAEJ&g_f=share_html"
try:
	p=requests.get(primary_url)
except:
	print("分享链接抓取失败")
primary_number=p.text.find('playurl')+10
primary_number_end=p.text[primary_number:].find('"')
url=p.text[primary_number:][:primary_number_end]
print("解析获得下载链接为："+url)
original_number=p.text.find("singer_name")+14
original_number_end=p.text[original_number:].find("song_name")-3
original_name=p.text[original_number:][:original_number_end]
print("解析原唱歌手为："+original_name)
song_name_number=p.text.find("song_name")+12
song_name_number_end=p.text[song_name_number:].find("tail_name")-3
song_name=p.text[song_name_number:][:song_name_number_end]
print("解析歌名为："+song_name)
singer_number=p.text.find('kg_nick')+10
singer_number_end=p.text[singer_number:].find('ksong_mid')-3
singer=p.text[singer_number:][:singer_number_end]
print("解析翻唱歌手名为："+singer)
singer_number1=p.text.find('在全民k歌录制了一首')
singer1=p.text[:singer_number1].split('"')[-1]
print("备用解析翻唱歌手名为："+singer1)
if len(singer)>len(singer1):
    singer=singer1
else:
    print("翻唱歌手名解析正确")
root="C:\\Users\\飞云川\\Desktop\\"
path=root+song_name+"-"+singer+"(cover"+original_name+").m4a"

print("保存位置为"+path)
try:
    if not os.path.exists(root):
    
        os.mkdir(root)
    if not os.path.exists(path):
    
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        print(r.status_code)
        with open (path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件已保存")
    else:print("文件已存在")
except:print("爬取失败")

