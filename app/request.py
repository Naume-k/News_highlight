import urllib.request,json
from .models import Sources,Article
from datetime import datetime

# # Getting api key
# api_key = None
# base_url = None
# base_articles_url = None

# def configure_request(app):
#     global api_key,base_url,base_articles_url
#     api_key = app.config['SOURCES_API_KEY']
#     base_url = app.config['SOURCES_BASE_URL']
#     base_articles_url = app.config['ARTICLES_BASE_URL']

#     print(api_key)
#     print(base_url)

# def get_sources(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_sources_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         sources_results = None

#         if get_sources_response['sources']:
#             sources_results_list = get_sources_response['sources']
#             sources_results = process_sources(sources_results_list)
    
#     return sources_results

# def process_sources(sources_list):
#     '''
#     Function that processes the json results
#     '''
#     sources_results = []

#     for source_item in sources_list:
#         id = source_item.get('id')
#         name = source_item.get('name')
#         description = source_item.get('description')
#         url = source_item.get('url')
#         category = source_item.get('category')
#         country = source_item.get('country')

#         if id:
#             sources_object = Sources(id,name,description,url,category,country)
#             sources_results.append(sources_object)
    
#     return sources_results

# def get_articles(id):
#     '''
#     Function that gets articles based on the source id
#     '''
#     get_articles_url = base_articles_url.format(id,api_key)

#     print(get_articles_url)
#     with urllib.request.urlopen(get_articles_url) as url:
#         get_articles_data = url.read()
#         get_articles_response = json.loads(get_articles_data)

#         articles_results = None

#         if get_articles_response['articles']:
#             articles_results_list=get_articles_response['articles']
#             articles_results = process_articles(articles_results_list)
        
#     return articles_results

# def process_articles(articles_list):
#     '''
#     Function that processes the json results for the articles
#     '''
#     articles_results = []
    
#     for article in articles_list:
#         id = article.get('id')
#         title = article.get('title')
#         author = article.get('author')
#         description = article.get('description')
#         url = article.get('url')
#         urlToImage = article.get('urlToImage')
#         date_published = article.get('publishedAt')

#         publishedAt = datetime(year=int(date_published[0:4]),month=int(date_published[5:7]),day=int(date_published[8:10]),hour=int(date_published[11:13]),minute=int(date_published[14:16]))

#         if urlToImage:
#             articles_object = Article(id,title,author,description,url,urlToImage,publishedAt)
#             articles_results.append(articles_object)
        
#     return articles_results