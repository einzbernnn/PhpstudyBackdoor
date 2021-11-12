from multiprocessing.dummy import Pool
import argparse
import requests
import sys
from colorama import Fore, init
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
banner='''
       _               _             _       _                _       _                  
      | |             | |           | |     | |              | |     | |                 
 _ __ | |__  _ __  ___| |_ _   _  __| |_   _| |__   __ _  ___| | ____| | ___   ___  _ __ 
| '_ \| '_ \| '_ \/ __| __| | | |/ _` | | | | '_ \ / _` |/ __| |/ / _` |/ _ \ / _ \| '__|
| |_) | | | | |_) \__ \ |_| |_| | (_| | |_| | |_) | (_| | (__|   < (_| | (_) | (_) | |   
| .__/|_| |_| .__/|___/\__|\__,_|\__,_|\__, |_.__/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   
| |         | |                         __/ |                                            
|_|         |_|                        |___/                                             
                                                        By Einzbern  
'''
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Charset': 'c3lzdGVtKCJlY2hvIGVpbnpiZSIpOw=='
}
urllist=[]
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", type=str)
parser.add_argument("-f", "--file",type=str)
parser.add_argument('-t', type=int, default=10)
args = parser.parse_args()


def urlscan():
	init(autoreset = True)
	try:
		request = requests.get(url=args.url,headers=header,verify=False,timeout=3)
		if 'einzbe' in request.text:
			#print(Fore.GREEN+'[+]{}存在漏洞'.format(args.url))
			sys.stdout.write(Fore.GREEN+'[+]{}存在漏洞\n'.format(args.url))
		else:
			#print(Fore.RED+'[-]{}不存在漏洞'.format(args.url))
			sys.stdout.write(Fore.RED+'[-]{}不存在漏洞\n'.format(args.url))
	except:
		sys.stdout.write(Fore.RED+'[-]{}不存在漏洞\n'.format(args.url))

def filelist():
	with open(args.file,'r') as f:
		for line in f:
			urllist.append(line.strip('\n'))
def poolfilescan():
	filelist()
	pool = Pool(processes=args.t)  
	pool.map(filescan, urllist)



def filescan(url):
	init(autoreset = True)
	try:
		request = requests.get(url=url,headers=header,verify=False,timeout=3)
		if 'einzbe' in request.text:
			sys.stdout.write('[+]{}************存在漏洞************\n'.format(url))
		else:
			sys.stdout.write('[-]{}不存在漏洞\n'.format(url))
	except:
		sys.stdout.write('[-]{}不存在漏洞\n'.format(url))


if __name__=="__main__":
	print(banner)
	if args.url:
		urlscan()
	elif args.file:
		poolfilescan()

