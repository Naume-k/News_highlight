from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles
from ..models import Sources


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = get_sources('general')
   
    title = 'News feed'
    return render_template('index.html', title = title, general = general)


@main.route('/articles/<id>')
def source(id):
    '''
    Function that returns articles based on their sources
    '''
    articles = get_articles(id)
   

    return render_template('articles.html', id=id, articles=articles)