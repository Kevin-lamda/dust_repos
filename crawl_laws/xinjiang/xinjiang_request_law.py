#/usr/bin/python3

# 辽宁省

import urllib.request
import urllib.error
import urllib

from bs4 import BeautifulSoup
import urllib3

def create_header():
	head = urllib3.util.make_headers(keep_alive=True, accept_encoding="gzip, deflate", user_agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36', basic_auth=None)
	head['Host'] = 'oa.xjlx.org'
	head['Referer'] = 'http://oa.xjlx.org/html/lscx1.asp'
	head['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	head['Accept-Encoding'] = 'gzip, deflate, sdch'
	head['Accept-Language'] = 'zh-CN,zh;q=0.8'
	return head


def track_info(tbody, fp):
	for people in tbody.findAll('tr')[1:]:
		tds = people.findAll('td')
		if len(tds) == 4:
			fp.write("执业律师姓名：%s  执业证号：%s  联系电话：%s \n" %(tds[1].string, tds[2].string, tds[3].string, ))
	return	
	
	
if __name__ == "__main__":
	
	url_prefix = 'http://oa.xjlx.org/html/lscx1.asp?page='	
	result_file = 'xinjiang_law.txt'	
	
	fp = open(result_file, 'w')
	header = create_header()
	
	page_id = 1
	while True:
		print("Current page: %d" % page_id)
		url = url_prefix + repr(page_id)
		req = urllib.request.Request(url, headers=header)
		response = urllib.request.urlopen(req)
		soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'), 'lxml')
		info_soup = soup.find('table', attrs={"width":"100%"})
		if info_soup:
			track_info(info_soup, fp)
		
		page_id += 1
		if page_id > 454:
			break
	
	fp.close()
	print("Done!")
