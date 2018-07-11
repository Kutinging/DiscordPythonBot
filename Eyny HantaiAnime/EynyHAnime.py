import requests,hashlib,time,re
from bs4 import BeautifulSoup
from discord_hooks import Webhook

def check(filename,str):
    file = open(filename)
    line = len(file.readlines())
    if(line<2 and line>0):
        file = open(filename)
        record = file.readlines()[0]
        if(record==str):
            file = open(filename,'r+')
            file.write(str)
            return 1
        else:
            file = open(filename,'r+')
            file.write(str)
            return 0
    else:
        file = open(filename,'w+')
        file.write(str)
    file.close()


Cookie = dict([('591e55XbD_e8d7_agree','1')])
BotWebHook = 'Your webhook url'
html = requests.get(url='http://www03.eyny.com/forum.php?mod=forumdisplay&fid=431&filter=typeid&typeid=2397&orderby=dateline', cookies=Cookie)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")

ListsTable = soup.find('table',{'id':'forum_431'})
Lists = ListsTable.find_all('tbody',{'id':re.compile(r'normalthread_*')})

Title = Lists[0].find('a',{'class':'xst'}).text
PostUrl = 'http://www.eyny.com/'+Lists[0].find('a',{'class':'xst'})['href']
Img = (Lists[0].find('img',{'class':'p_pre'})['src'])
sha1 = hashlib.sha1((Title).encode("utf-8")).hexdigest()
checkvalue = check('HAnime',sha1)

if checkvalue==0:
    embed = Webhook(BotWebHook, color=123123)
    embed.set_author(name=Title, icon='')
    embed.set_desc(PostUrl)
    #embed.add_field(name='Test Field',value='Value of the field \U0001f62e')
    #embed.add_field(name='Another Field',value='1234 😄')
    #embed.set_thumbnail('https://i.imgur.com/rdm3W9t.png')
    embed.set_image(Img)
    #embed.set_footer(text='發文時間 '+post_time,icon='',ts=True)
    embed.post()