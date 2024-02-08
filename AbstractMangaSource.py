import mangasources


class AbstractMangaSource:

    @staticmethod
    def getSearchResult(current_source, text):
        return getattr(mangasources, str(current_source)).getSearchResult(text)

    @staticmethod
    def listchapters(url):
        return getattr(mangasources, 'kavita').processing_chapters(url)

    @staticmethod
    def listchapterimages(url):
        return getattr(mangasources, 'kavita').image_lists(url)

    @staticmethod
    def getIconFromUrl(url):
        return getattr(mangasources, 'kavita').getmangaiconfromurl(url)

    @staticmethod
    def getImageHeader(url):
        return {}
