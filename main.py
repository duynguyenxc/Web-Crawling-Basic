import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'books.toscrape'
HOMEPAGE = 'http://books.toscrape.com'
DOMAIN_NAME = get_sub_domain_name(HOMEPAGE)