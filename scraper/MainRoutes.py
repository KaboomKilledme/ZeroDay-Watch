from bs4 import BeautifulSoup
from OurRequests import Requests as request
from SubRoutes import KrebsSubroute, ThnSubroute, CisaSubroute, SecWeekSubroute
import time 

path = "mainSites"

# with open(f'{path}/krebs.html') as krebs:
#     krebsSite = krebs.read()

# with open(f'{path}/cisa.html') as cisa:
#     cisaSite = cisa.read()

# with open(f'{path}/secweek.html') as secWeek:
#     secWeekSite = secWeek.read()

# with open(f'{path}/thn.html') as THN:
#     thnSite = THN.read()


class Website:

    soup = None
    
    subLinks = []

    tag = None
    tagClass = None

    def __init__(self, link):
        html = request.get(link).text
        self.assignSoup(html)

    @classmethod
    def assignSoup(cls, html):
        cls.soup = BeautifulSoup(html, 'lxml')

    @classmethod
    def getSubLinks(cls): # Method is used to get sub route links
        subLinkElements = cls.soup.find_all(cls.tag, class_=cls.tagClass)
        for subLinkElement in subLinkElements:
           cls.subLinks.append(subLinkElement.a['href'])   

    

class Krebs(Website):

    tag = "h2"
    tagClass = "entry-title"    

    def __init__(self, html):
        super().__init__(html) 

    @classmethod
    def saveArticles(cls):
        cls.subLinks = []
        cls.getSubLinks()
        
        for link in cls.subLinks:
            subSite = KrebsSubroute(link)
            try:
                subSite.saveArticle()
                time.sleep(20)
            except:
                break
            

class THN(Website):
    tag = "a"
    tagClass = "story-link"    

    def __init__(self, html):
        super().__init__(html)    

    @classmethod
    def getSubLinks(cls): # Overriding method to filter out advertisements
        subLinkElements = cls.soup.find_all(cls.tag, class_=cls.tagClass)

        for subLinkElement in subLinkElements:
            parentTag = subLinkElement.parent

            if(parentTag.name == "section"):
                subLinkElement.extract()
            else:
                cls.subLinks.append(subLinkElement['href'])

    @classmethod
    def saveArticles(cls):
        cls.subLinks = []
        cls.getSubLinks()
        
        for link in cls.subLinks:
            subSite = ThnSubroute(link)
            try:
                subSite.saveArticle()
                time.sleep(20)
            except:
                break
            

class SecWeek(Website):

    tag = "div"
    tagClass = "zox-art-title"

    def __init__(self, html):
        super().__init__(html)

    @classmethod
    def getSubLinks(cls): # Overriding method to target specific container
        latestContainer = cls.soup.find('div', id='zox_side_trend_widget-1')
        subLinkElements = latestContainer.find_all(cls.tag, class_=cls.tagClass)

        for subLinkElement in subLinkElements:
            cls.subLinks.append(subLinkElement.a['href'])

    @classmethod
    def saveArticles(cls):
        cls.subLinks = []
        cls.getSubLinks()
        
        for link in cls.subLinks:
            subSite = SecWeekSubroute(link)
            try:
                subSite.saveArticle()
                time.sleep(20)
            except:
                break
            
    
class CISA(Website):

    tag = "h3"
    tagClass = "c-teaser__title"
    
    def __init__(self, link):
        super().__init__(link)
    
    @classmethod
    def getSubLinks(cls): # Overriding method to format urls
        subLinkElements = cls.soup.find_all(cls.tag, class_=cls.tagClass)
        for subLinkElement in subLinkElements:
            link = f"https://www.cisa.gov{subLinkElement.a['href']}"
            cls.subLinks.append(link) 

    @classmethod
    def saveArticles(cls):
        cls.subLinks = []
        cls.getSubLinks()
        
        for link in cls.subLinks:
            subSite = CisaSubroute(link)
            try:
                subSite.saveArticle()
                time.sleep(20)
            except:
                break
              




#cisa = CISA('https://www.cisa.gov')
##krebs = Krebs('https://krebsonsecurity.com')
#thn = THN('https://thehackernews.com/')
#secweek = SecWeek('https://www.securityweek.com')

#krebs.saveArticles()
#thn.saveArticles()
#secweek.saveArticles()
#cisa.saveArticles()

print('Ran')