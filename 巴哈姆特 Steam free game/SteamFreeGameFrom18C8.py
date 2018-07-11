import requests
from bs4 import BeautifulSoup
from discord_hooks import Webhook
import hashlib

def check(filename,input):
    file = open(filename)
    line = len(file.readlines())
    if(line<2 and line>0):
        file = open(filename)
        record = file.readlines()[0]
        if(record==input):
            #print("==")
            file = open(filename,'r+')
            file.write(input)
            return 1
        else:
            #print("!=")
            file = open(filename,'r+')
            file.write(input)
            return 0
    else:
        file = open(filename,'w+')
        file.write(input)
    file.close()

res = requests.get('https://forum.gamer.com.tw/B.php?bsn=60599&subbsn=10')
BotWebHook = 'Your webhook url'
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, "html.parser")


PostLists = soup.find('table',{'class':'b-list'})
Posts = PostLists.find_all('tr',{'class':'b-list__row'})
Title = Posts[0].find('td',{'class':'b-list__main'}).text
WebsiteUrl = 'https://forum.gamer.com.tw/'+Posts[0].find('td',{'class':'b-list__main'}).a['href']
sha1 = hashlib.sha1((Title).encode("utf-8")).hexdigest()
checkvalue = check('18c8',sha1)

embed = Webhook(BotWebHook, color=123123)
embed.set_author(name='Steam巴哈姆特免費遊戲情報', icon='')
embed.set_desc(Title + WebsiteUrl)
#embed.add_field(name='Test Field',value='Value of the field \U0001f62e')
#embed.add_field(name='Another Field',value='1234 😄')
#embed.set_thumbnail('https://i.imgur.com/rdm3W9t.png')
embed.set_image('https://pbs.twimg.com/profile_images/663739181231792128/58-mQCZh_400x400.png')
#embed.set_footer(text='發文時間 '+post_time,icon='',ts=True)

if(checkvalue==1):
    print("No")
elif(checkvalue==0):
    embed.post()

#embed.post()