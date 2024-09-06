from django.shortcuts import render
from django.core.cache import cache

# Long code
"""
def home(request):
    mv = cache.get('movie','has_expired') # if there is any value in movie then returns movie value else returns has_expired
    if mv == 'has_expired':
        cache.set('movie','The Manjhi', 30)
        mv = cache.get('movie')
    return render(request, 'enroll/course.html', {'fm':mv})
"""

# Short code
"""
def home(request):
    mv = cache.get_or_set('movie',2000,30, version=2)
    return render(request, 'enroll/course.html',{'fm':mv})
"""

# Set key
"""
def home(request):
    data = {'name':'Sonam', 'roll':101}
    cache.set_many(data,30)
    sv = cache.get_many(data)
    print(sv)
    return render(request, 'enroll/course.html', {'stu':sv})
"""
    
# Delete Key
"""
def home(request):
    cache.delete('roll') # check the database to see the key
    cache.delete('fees', version=2) 
    return render(request, 'enroll/course.html')
"""

# incrementing decrementing keys
def home(request):
    #cache.set('roll', 101, 600)
    #rv = cache.get('roll')
    #print(rv)
    dv = cache.decr('roll',delta=1)
    # dv = cache.incr('roll', delta = 3)
    print(dv)
    return render(request, 'enroll/course.html')

# delete all the keys
"""
def home(request):
    cache.clear()
    return render(request, 'enroll/course.html')
"""