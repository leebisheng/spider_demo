import requests
import os
from bs4 import BeautifulSoup
import re
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}



def save_binary_data(file_path, binary_data):
    """将二进制数据保存到指定路径的文件中，如果文件已存在则不保存，不存在的目录会自动创建"""
    try:
        # 检查文件是否已存在
        if os.path.exists(file_path):
            print(f"文件 {file_path} 已存在，未执行保存")
            return False

        # 创建目录（如果不存在）
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as file:  # 使用 'wb' 模式写入二进制数据
            file.write(binary_data)
        print(f"数据已成功保存到 {file_path}")
        return True
    except Exception as e:
        print(f"保存文件时发生错误: {e}")
        return False
def scrape_163_top(id):
    url_hot_list = f"https://music.163.com/discover/toplist?id={id}"
    print(f'url_hot_list:{url_hot_list}')
    response = requests.get(f"{url_hot_list}", headers=headers)
    if response.ok:
        html = response.text
        # print(f'html text:{html}')
        html_data = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', html)
        print(f'html_data:{html_data}')
        for num_id, title in html_data:
            music_url = f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
            music_content = requests.get(url=music_url, headers=headers).content
            file_path = f'E:\音乐\网易音乐\\{title}.mp3'
            save_binary_data(file_path, music_content)
    else:
        print(response.status_code)
def scrape_163_classic(id):
    url_hot_list = f"https://music.163.com/discover/toplist?id={id}"
    print(f'url_hot_list:{url_hot_list}')
    response = requests.get(f"{url_hot_list}", headers=headers)
    if response.ok:
        html = response.text
        # print(f'html text:{html}')
        html_data = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', html)
        print(f'html_data:{html_data}')
        for num_id, title in html_data:
            music_url = f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
            music_content = requests.get(url=music_url, headers=headers).content
            file_path = f'E:\音乐\网易音乐\古典音乐\\{title}.mp3'
            save_binary_data(file_path, music_content)
    else:
        print(response.status_code)
def scrape_163(id,top_name):
    url_hot_list = f"https://music.163.com/discover/toplist?id={id}"
    print(f'url_hot_list:{url_hot_list}')
    response = requests.get(f"{url_hot_list}", headers=headers)
    if response.ok:
        html = response.text
        # print(f'html text:{html}')
        html_data = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', html)
        print(f'html_data:{html_data}')
        for num_id, title in html_data:
            music_url = f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
            music_content = requests.get(url=music_url, headers=headers).content
            file_path = f'E:\音乐\网易音乐\\{top_name}\\{title}.mp3'
            save_binary_data(file_path, music_content)
    else:
        print(response.status_code)
def scrape_163_url(url,top_name):
    url_hot_list = url
    response = requests.get(f"{url_hot_list}", headers=headers)
    if response.ok:
        html = response.text
        # print(f'html text:{html}')
        html_data = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', html)
        print(f'html_data:{html_data}')
        for num_id, title in html_data:
            music_url = f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
            music_content = requests.get(url=music_url, headers=headers).content
            file_path = f'E:\音乐\网易音乐\\{top_name}\\{title}.mp3'
            save_binary_data(file_path, music_content)
    else:
        print(response.status_code)

def main():
    # scrape_163_top('3778678')
    # scrape_163_top('19723756')
    # scrape_163_top('3779629')
    #scrape_163_classic("71384707")
    # scrape_163('6845908342','影视金曲')
    # scrape_163('6847295283', '国语流行')
    # scrape_163('12650425817', '欧美精选')
    scrape_163_url('https://music.163.com/playlist?id=9493371200','80年代经典流行')
if __name__ == "__main__":
    main()