import os, ssl
from bs4 import BeautifulSoup
import re
import json
import requests


class TikTokAPI:

    def __init__(self,url):
        self.url=url
        self.isEmpty=True



    def getVideoDetails(self):

        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

        header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        proxy = {'https': Enter Proxy}

        page = requests.get(self.url, headers=header, proxies=proxy)

        soup = BeautifulSoup(page.content, 'html.parser')

        data=soup(text=re.compile(r'"videoProps":'))

        if not data:
            self.isEmpty=False
            return {"isEmpty":False}
        else:

            for script in data:

                js = json.loads(script.parent.text)

                videoURL=js["props"]["pageProps"]["videoObjectPageProps"]["videoProps"]["url"]
                videoUploadDate=js["props"]["pageProps"]["videoObjectPageProps"]["videoProps"]["uploadDate"]
                likesOnVideo=js["props"]["pageProps"]["videoData"]["itemInfos"]["diggCount"]
                viewsOnVideo=js["props"]["pageProps"]["videoData"]["itemInfos"]["playCount"]
                commentOnVideo=js["props"]["pageProps"]["videoData"]["itemInfos"]["commentCount"]
                shareOnVideo=js["props"]["pageProps"]["videoData"]["itemInfos"]["shareCount"]
                audioName=js["props"]["pageProps"]["videoObjectPageProps"]["videoProps"]["audio"]["name"]
                audioURL=js["props"]["pageProps"]["videoObjectPageProps"]["videoProps"]["audio"]["mainEntityOfPage"]["@id"]
                videoDownloadLink=js["props"]["pageProps"]["videoData"]["itemInfos"]["video"]["urls"]

                # User Details


                id = js["props"]["pageProps"]["videoData"]["authorInfos"]["userId"]
                uniqueId = js["props"]["pageProps"]["videoData"]["authorInfos"]["uniqueId"]
                profileURL = 'www.tiktok.com/@{}'.format(uniqueId)
                nickname = js["props"]["pageProps"]["videoData"]["authorInfos"]["nickName"]
                followerCount = js["props"]["pageProps"]["videoData"]["authorStats"]["followerCount"]
                heartCount = js["props"]["pageProps"]["videoData"]["authorStats"]["heartCount"]



            videoInfo={"isEmpty":False,"profileURL":profileURL,"id":id,"uniqueId":uniqueId,"nickname":nickname,"followerCount":followerCount,"heartCount":heartCount,"videoURL":videoURL,"videoUploadDate":videoUploadDate,"likesOnVideo":likesOnVideo,"viewsOnVideo":viewsOnVideo,"commentOnVideo":commentOnVideo,"shareOnVideo":shareOnVideo,"audioName":audioName,"audioURL":audioURL,"videoDownloadLink":videoDownloadLink}


            return videoInfo




    def getUserDetails(self):

        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

        header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        proxy = {'https':  Enter Proxy}

        page = requests.get(self.url, headers=header, proxies=proxy)

        soup = BeautifulSoup(page.content, 'html.parser')

        data = soup(text=re.compile(r'"shareMeta":'))

        if not data:
            self.isEmpty = False
            return {"isEmpty": False}

        else:

            for script in data:
                js = json.loads(script.parent.text)


                profileURL=js["props"]['initialProps']['$pageUrl']
                profileURL='www.tiktok.com{}'.format(profileURL)
                id=js["props"]["pageProps"]["userInfo"]["user"]["id"]
                uniqueId=js["props"]["pageProps"]["userInfo"]["user"]["uniqueId"]
                nickname=js["props"]["pageProps"]["userInfo"]["user"]["nickname"]
                avatarThumb=js["props"]["pageProps"]["userInfo"]["user"]["avatarThumb"]
                avatarMedium=js["props"]["pageProps"]["userInfo"]["user"]["avatarMedium"]
                followingCount=js["props"]["pageProps"]["userInfo"][ "stats"]["followingCount"]
                followerCount=js["props"]["pageProps"]["userInfo"][ "stats"]["followerCount"]
                heartCount=js["props"]["pageProps"]["userInfo"][ "stats"]["heartCount"]
                videoCount=js["props"]["pageProps"]["userInfo"][ "stats"]["videoCount"]
                covers=js["props"]["pageProps"]["userData"]["covers"]
                coversMedium=js["props"]["pageProps"]["userData"]["coversMedium"]



            userInfo={"profileURL":profileURL,"id":id,"uniqueId":uniqueId,"nickname":nickname,"avatarThumb":avatarThumb,"avatarMedium":avatarMedium,"followingCount":followingCount,"followerCount":followerCount,"heartCount":heartCount,"videoCount":videoCount,"covers":covers,"coversMedium":coversMedium}

            return userInfo







