import requests
import lxml
from bs4 import BeautifulSoup
import os
import time
import urllib.request

root_ip = 'http://211.86.241.19'
root_url = 'http://211.86.241.19/s/77/t/181/p/99/c/4645/d/4724/list.htm'

def get_year():
	year_dict={}
	r = requests.get(root_url)
	soup = BeautifulSoup(r.text, 'lxml')
	# 将年级和年级对应链接保存
	for i in soup.find_all('a',class_="clink"):
		year_dict[i.get_text()] = i.get('href')
	# print(year_dict)
	return year_dict

def get_xueyuan(year_url):
	xueyuan_dict={}
	r = requests.get(root_ip+year_url)
	soup = BeautifulSoup(r.text, 'lxml')
	for i in soup.find('div',class_='z14').table.find_all('a'):
		# print(i.get('href'))
		# print(i.get_text())
		xueyuan_dict[i.get_text()] = i.get('href')
	return xueyuan_dict

def get_major(xueyuan_url):
	major_dict={}
	r = requests.get(root_ip+xueyuan_url)
	soup = BeautifulSoup(r.text, 'lxml')
	for i in soup.find('div',class_='z14').find_all('a'):
		if len(i.get_text())>2:
			# print(i.get('href'))
			# print(i.get_text())
			# print('888888888888')
			major_dict[i.get_text()] = i.get('href')
	return major_dict

def dow_file():
	aaa = ''
	year_dict = get_year()
	time.sleep(5)
	for k,v in year_dict.items():
		year_name = k
		xueyuan_dict = get_xueyuan(year_dict[k])
		time.sleep(1)
		for kk,vv in xueyuan_dict.items():
			xueyuan_name = kk
			major_dict = get_major(xueyuan_dict[kk])
			time.sleep(1)
			for kkk,vvv in major_dict.items():
				major_name = kkk
				major_url = vvv
				# print(year_name)
				# print(xueyuan_name)
				# print(major_name)
				aaa = './'+year_name+'/'+xueyuan_name
				# print(aaa)
			    # print(aaa)
			    # if not os.path.exists(aaa):
			    # os.makedirs(aaa)
			    # os.makedirs(aaa)
				if not os.path.exists(aaa):
					os.makedirs(aaa)
				urllib.request.urlretrieve(root_ip+major_url,aaa+'/'+major_name)	
				time.sleep(1)
	# urllib.request.urlretrieve()
	return 0


if __name__ == '__main__':
	dow_file()

# C:/DDD/files/gitdata/mycodemanager/sublime666/爬取安财培养方案/2016/一、经济学