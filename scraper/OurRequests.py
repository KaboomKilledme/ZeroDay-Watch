import cloudscraper

class Requests:

    @classmethod
    def get(cls, link):
        scraper = cloudscraper.create_scraper(
            debug=False,
            browser={'browser':"chrome",'platform':"android",'desktop':False},
            disableCloudflareV1=True,
            delay=10,
        )

        request = scraper.get(link) 
        return request
