import requests
from bs4 import BeautifulSoup

class WebScrape:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://dir.indiamart.com/'

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words

  def search(self, keywords):
    global anylink
    anylink = True
    response = requests.get(self.url+keywords+ '/24-hours-ambulance-service.html', headers = self.headers)
    #print(self.url+keywords+ '/24-hours-ambulance-service.html')
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_links = soup.findAll('a',attrs={'class':'read wh mlin'})
    #print(result_links)
    no_link = soup.findAll('p',attrs={'class':'dinw'})
    #print(no_link)
    if no_link:
      anylink = False
    #print(no_link,anylink)
    return result_links,anylink
      
  def send_link(self, result_links, search_words,anylink): 
    #no_link = soup.findAll('p',attrs={'class':'dinw'})
    send_link = set()
    for link in result_links:
        text = link.text.lower()
        if (anylink==True) :  #search_words in text
          send_link.add(link.get('href'))
        else:
          send_link = set()
    #print(send_link)
    return send_link
