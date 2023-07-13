from bs4 import BeautifulSoup

path = "mainSites"

with open(f'{path}/krebs.html') as krebs:
    krebsSite = krebs.read()

with open(f'{path}/cisa.html') as cisa:
    cisaSite = cisa.read()

with open(f'{path}/secweek.html') as secWeek:
    secWeekSite = secWeek.read()

with open(f'{path}/thn.html') as THN:
    thnSite = THN.read()


class Website:

    soup = None
    
    subLinks = None

    tag = None
    tagClass = None

    def __init__(self, html):
        self.assignSoup(html)

    @classmethod
    def assignSoup(cls, html):
        cls.soup = BeautifulSoup(html, 'lxml')


    @classmethod
    def getSubLinks(cls):
        subLinkElements = cls.soup.find_all(cls.tag, class_=cls.tagClass)
        for subLinkElement in subLinkElements:
           print(subLinkElement.a['href'])


class Krebs(Website):

    tag = "h2"
    tagClass = "entry-title"    

    def __init__(self, html):
        super().__init__(html)

    
    

krebs = Krebs(krebsSite)

Krebs.getSubLinks()
