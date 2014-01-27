#coding=UTF-8   
import re,sys
import urllib
from bs4 import BeautifulSoup
global r_url
type = sys.getfilesystemencoding()
print type
def hq_url():
	so_url = "http://movie.douban.com/subject_search?search_text="
	data = urllib.urlopen(so_url+gjz).read()
	r = re.findall(r'<a class="nbg" href=(.*?) onclick',data)
	
	r_url = re.sub('"','',r[0])
	
	ymdata = urllib.urlopen(r_url).read()
	
	
	soup = BeautifulSoup(ymdata,from_encoding="gbk")

	wz = soup('span',{'property':'v:summary'})
	
	print wz
if __name__=='__main__':

    gjz=raw_input("请输入电影名: ").strip()
    hq_url()