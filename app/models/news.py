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
