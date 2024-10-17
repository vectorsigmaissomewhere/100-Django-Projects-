from django.shortcuts import render
from .models import Post 
from django.core.paginator import Paginator 

# Create your views here.
def post_list(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post, 2, orphans=1) # 2 items in one page # orphans = 1 cause there was 1 item in last page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print('All_Post=', all_post)
    print()
    print('Paginator=', paginator)
    print()
    print('Page_Number=', page_number)
    print()
    print('Page_obj=', page_obj)
    return render(request, 'blog/home.html', {'page_obj':page_obj})
