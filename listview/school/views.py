from django.shortcuts import render
from django.views.generic.list import ListView 
from .models import Student 


# this view shows listview 
class StudentListView(ListView):
    model = Student 

    # Use of ListView is I don't need to write the below lines of code
    """
    stud = Student.object.all()
    context = {'student_list':stud}
    return render(request, 'school/student_list.html', context)
    """

# custom listview 
class StudentSecondListView(ListView):
    model = Student 
    # the above search for student_list.html while this view search for student_get.htmk
    template_name_suffix = '_get'
    # orders by name 
    ordering = ['name']

# in previous view we must have student_list.html or student_get.html as template name 
# custom listview where we gonna change the template name 
class StudentThirdListView(ListView):
    model = Student
    template_name = 'school/studentthird.html'

# change context name 
# that is our default context name is student_list in template page
# but we are change it into students
class StudentFourthListView(ListView):
    model = Student 
    template_name = 'school/studentfourth.html'
    context_object_name = 'students'

# filter data 
# get only data whose course is Python from get_queryset method
# get data with order of name but with context name freshers 
class StudentFifthListView(ListView):
    model = Student 
    template_name = 'school/studentfifth.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Python')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context
    
    
    


