from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery

def query_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    return Products.objects.annotate(search=SearchVector('title', 'description')).filter(search=SearchQuery(query))

