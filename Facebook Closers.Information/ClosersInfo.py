import requests,hashlib,time,re,os
from bs4 import BeautifulSoup
from discord_hooks import Webhook

def check(filename,str):
    if not( os.path.exists(filename)):
        File = open(filename,'w')
        File.write(str)
        File.close()
        return 0
    else:
        with open(filename,'r+') as File:
            DataList = File.readlines()
            line = len(DataList)
            if line<2 and line>0:
                Data = DataList[0]
                if not(Data == str):
                    File.seek(0)
                    File.truncate()
                    File.write(str)
                    return 0
                else:
                    return 1
            else:
                File.write(str)
                return 0

def getImgUrl(PostCount):
    try:
        ImgUrl = Posts[PostCount].find('img',{'class':'scaledImageFitWidth img'})['src']
    except TypeError:
        ImgUrl = Posts[PostCount].find('img',{'class':'_4lpf'})['src']
    finally:
        return ImgUrl

def getMessages(PostCount):
    Messages = (Posts[PostCount].find('div',{'class':'_5pbx userContent _3576'}).text).replace('⋯⋯','')
    if Messages[-2:] == '更多':
        Messages = Messages[:-2]
    return Messages

def getPostUrl(PostCount):
    PostUrl = 'https://www.facebook.com'+Posts[PostCount].find('a',{'class':'_5pcq'})['href']
    return PostUrl


def getHTMLCode(WebsiteUrl):
    try:
        html = requests.get(url=WebsiteUrl)
        html.encoding = 'utf-8'
        htmlcode = BeautifulSoup(html.text, "html.parser")
        return htmlcode
    except:
        print('getHTMLCode Error')
        


BotWebHook = 'Your webhook url'


HTMLCode = getHTMLCode('https://www.facebook.com/pg/Closers.Information/posts/?ref=page_internal')
PostsLists = HTMLCode.find('div',{'class':'_2pie _14i5 _1qkq _1qkx'})
PostList = PostsLists.find('div',{'class':'_1xnd'})
Posts = PostList.find_all('div',{'class':'_1dwg _1w_m _q7o'})


try:
    Img = getImgUrl(1)
except:
    Img = 'https://i.imgur.com/08ovhYT.png'
finally:
    Messages = getMessages(1)
    PostUrl = getPostUrl(1)

sha1 = hashlib.sha1((PostUrl).encode("utf-8")).hexdigest()
if check('ClosersInfo',sha1)==0:
    embed = Webhook(BotWebHook, color=123123)
    embed.set_author(name=Messages, icon='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-1/p200x200/25498185_1451951624922509_2329157679259274468_n.jpg?_nc_cat=0&oh=adae6bb11de458c0ef8bd63cd4c6b1cd&oe=5BD7BB91')
    embed.set_desc(PostUrl)
    #embed.add_field(name='Test Field',value='Value of the field \U0001f62e')
    #embed.add_field(name='Another Field',value='1234 😄')
    #embed.set_thumbnail('https://i.imgur.com/rdm3W9t.png')
    embed.set_image(Img)
    #embed.set_footer(text='發文時間 '+post_time,icon='',ts=True)
    embed.post()