class Article:
    '''
    class to define article objects
    '''
    def __init__(self,author,description,url,urlToImage,publishedAt,content):
        '''
        method to initialize article objects
        '''
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Sources:
    '''
    class to define Sources Objects
    '''
    def __init__(self,id,url,name,description,category,language,country):
        '''
        method to initialize sources objects
        '''
        self.id =id
        self.url = url
        self.name = name
        self.description = description
        self.category = category
        self.language = language
        self.country = country
        