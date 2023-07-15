from bs4 import BeautifulSoup
from OurRequests import Requests as request
from CRUD import addSource

path = "subSites"

with open(f'{path}/krebs.html') as krebs:
    krebsSite = krebs.read()

with open(f'{path}/cisa.html') as cisa:
    cisaSite = cisa.read()

with open(f'{path}/secweek.html') as secWeek:
    secWeekSite = secWeek.read()

with open(f'{path}/thn.html') as THN:
    thnSite = THN.read()



class Subroute():

    soup = None
    
    source = None

    #The sub route's title
    titleTag = None
    titleClass = None

    #The sub route's content
    contentTag = None
    contentClass = None

    #Filtering of unnecassry content
    shouldFilter = False
    
    shouldFilterByTags = False
    shouldFilterByKeywords = False

    filters = []



    def __init__(self, link):
        self.link = link
        html = request.get(link).text
        self.assignSoup(html)

    @classmethod
    def assignSoup(cls, html):
        cls.soup = BeautifulSoup(html, 'lxml')
    
    @classmethod
    def getTitle(cls):
        title = cls.soup.find(cls.titleTag, class_=cls.titleClass)
        return title.get_text()


    @classmethod
    def getContent(cls):
        content = cls.soup.find(cls.contentTag, class_=cls.contentClass)
        filterdContent = None

        if cls.shouldFilter:
            if cls.shouldFilterByTags and cls.shouldFilterByKeywords:
                filterdContent = cls.filterByTags(content)
                filterdContent = cls.filterByKeywords(filterdContent)

            elif cls.shouldFilterByTags:
                filterdContent = cls.filterByTags(content)
            
            elif cls.shouldFilterByKeywords:
                filterdContent = cls.filterByKeywords(content)
            
            content = filterdContent

        return content.get_text()
    

    @classmethod
    def filterByTags(cls, content):
        for filter in cls.filters:
            excludedTags = content.find_all(filter['tag'], class_=filter["class"])   
            if excludedTags is not None:
                for excludedTag in excludedTags:
                    excludedTag.extract()
            else:
                continue
        
        return content
    
    @classmethod
    def filterByKeywords(cls):
        pass

    def saveArticle(self):
        title = self.getTitle()
        content = self.getContent()
        data = {"title":title, "content":content, "link":self.link, "type":self.source}
        addSource(data)

class KrebsSubroute(Subroute):

    source = "krebs"

    titleTag = "h1"
    titleClass = "entry-title"

    contentTag = "div"
    contentClass = "entry-content"

    shouldFilter = True
    shouldFilterByTags = True

    filters = [
        {"tag":"div", "class":"wp-caption"},
    ]


    def __init__(self, link):   
        super().__init__(link)

class ThnSubroute(Subroute):
    
    source = "thn"

    
    titleTag = "h1"
    titleClass = "story-title"

    contentTag ="div"
    contentClass = "articlebody"

    shouldFilter = True
    shouldFilterByTags = True

    filters = [
        {"tag":"section", "class":"badbox"},
        {"tag":"div", "class":"note-b"}
    ]


    def __init__(self, link):
        super().__init__(link)

class SecWeekSubroute(Subroute):

    source = "secweek"

    titleTag = "h1"
    titleClass = "entry-title"
    
    contentTag = "div"
    contentClass = "theiaPostSlider_preloadedSlide"

    shouldFilter = True
    shouldFilterByTags = True
    shouldFilterByKeywords = True

    filters = [{"tag":"div", "class":"zox-post-ad-wrap"}]

    def __init__(self, link):
        super().__init__(link)

    @classmethod
    def filterByKeywords(cls, content): # Overriding to remove 'Related:' element
    
        excludeElements = content.find_all("strong", string="Related")

        for element in excludeElements:
            element = element.parent
            elementText = element.text[:8]
            if(elementText == "Related:"):
                element.extract()

        return content

class CisaSubroute(Subroute):

    source = "cisa"


    titleTag = "h1"
    titleClass = "c-page-title__title"

    contentTag = "div"
    contentClass = "c-field--type-text-long"

    shouldFilter = True
    shouldFilterByTags = True

    def __init__(self, link):
        super().__init__(link)

    @classmethod
    def filterByTags(cls, content): # Overriding to remove the bottom segments

        hashes = content.find(string="###") #To remove hashes
        lastElement = content.find_all("p")[-1] #To remove the bottom paragraphs

        if hashes is not None:
            hashes.extract()

        if lastElement is not None: 
            secondLastElement = lastElement.previous_sibling
            thirdLastElemenet = secondLastElement.previous_sibling

            lastElement.extract()  
            secondLastElement.extract()
            thirdLastElemenet.extract()

        return content


