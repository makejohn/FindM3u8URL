import sys
import requests
import re

#This web site is simple, u can just enter different code "like juq-071" atfer "videos/",then u get the video page.
url = "https://jable.tv/videos/"

#depends on the site you test, based on different anti-spider tech, use different methods.
headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def findM3u8():
  
    if len(sys.argv)!=2:
        print("Please enter the right code, Eg \"juq-071\"")
        exit(0)
    code = sys.argv[1]
    result = requests.get(url+code+'/',headers=headers).text
    #print(result)
    result = re.findall("https.*m3u8",result)
    return result
if __name__ == '__main__':
    print(findM3u8())% 
