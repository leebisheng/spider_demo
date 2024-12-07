import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
cnt = 0
print("豆瓣TOP250电影\r")
for start_num in range(0,255,25):
    response=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    if response.ok:
        html=response.text
        soup=BeautifulSoup(html,"html.parser")
        all_titles=soup.find_all("span",attrs={"class":"title"})
        for title in all_titles:
            title_string=title.string
            if "/" not in title_string:
                cnt+=1
                print(f"Top{cnt}：{title.string}")
    else:
        print(response.status_code)