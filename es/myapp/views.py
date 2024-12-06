from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from .documents import BookDocument 


# Create your views here.
def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        query = MultiMatch(query=q, fields=["title", "description"], fuzziness="AUTO")
        s = BookDocument.search().query(query)
        context['books'] = s
    return render(request, 'index.html', context)