import os
import youtube_dl

class YouTubeDownloader:
    def __init__(self, download_path=None):
        """
        初始化下载器
        :param download_path: 下载路1径，默认为当前目录下的 'downloads' 文件夹
        """
        if download_path is None:
            download_path = os.path.join(os.getcwd(), 'downloads')

        # 确保下载目录存在
        os.makedirs(download_path, exist_ok=True)
        self.download_path = download_path

    def download_video(self, url, download_type='best'):
        """
        下载YouTube视频
        :param url: 视频链接
        :param download_type: 下载类型
            'best': 最佳质量
            'audio': 仅下载音频
            'video': 仅下载视频
        """
        try:
            # 配置下载选项
            ydl_opts = {
                'format': self._get_format(download_type),
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [self._download_progress],
                'no_warnings': False,
                'ignoreerrors': False,
                'no_color': True,
            }

            # 创建下载器
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # 获取视频信息
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', None)

                print(f"正在下载: {video_title}")

                # 开始下载
                ydl.download([url])

                print(f"下载完成: {video_title}")

        except youtube_dl.utils.DownloadError as e:
            print(f"下载错误: {e}")
        except youtube_dl.utils.ExtractorError as e:
            print(f"视频提取错误: {e}")
        except Exception as e:
            print(f"未知错误: {e}")

    def _get_format(self, download_type):
        """
        根据下载类型选择格式
        """
        format_map = {
            'best': 'bestvideo+bestaudio/best',  # 最佳画质
            'audio': 'bestaudio/best',  # 仅音频
            'video': 'bestvideo/best'  # 仅视频
        }
        return format_map.get(download_type, 'bestvideo+bestaudio/best')

    def _download_progress(self, d):
        """
        下载进度回调
        """
        if d['status'] == 'finished':
            print('下载完成，正在处理文件...')
        elif d['status'] == 'downloading':
            # 显示下载进度
            downloaded_bytes = d.get('downloaded_bytes', 0)
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            if total_bytes > 0:
                percent = downloaded_bytes * 100. / total_bytes
                print(f'下载中: {percent:.1f}%', end='\r')


def main():
    # 创建下载器实例
    downloader = YouTubeDownloader()

    # 菜单
    print("YouTube 视频下载器")
    print("1. 下载最佳质量视频")
    print("2. 仅下载音频")
    print("3. 仅下载视频")

    choice = input("请选择下载类型(1/2/3): ")

    # 对应选择
    download_type_map = {
        '1': 'best',
        '2': 'audio',
        '3': 'video'
    }

    download_type = download_type_map.get(choice, 'best')

    # 获取视频链接
    url = input("请输入YouTube视频链接: ")

    # 下载
    downloader.download_video(url, download_type)


if __name__ == '__main__':
    main()