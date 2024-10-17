from django.shortcuts import render
from .models import Student 
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 

# default template is student_detail, default context is student 
class StudentDetailView(DetailView):
    model = Student 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_student'] = self.model.objects.all()
        return context 

# custom template and default context is student
class StudentDetailCustomTemplateView(DetailView):
    model = Student 
    # if you don't mention template_name student_detail.html will render
    template_name = 'school/student.html'

# custom context is stu  
class StudentDetailCustomContextView(DetailView):
    model = Student 
    template_name = 'school/student_context.html'
    context_object_name = 'stu'
    """
    change the object pk in url into id
    pk_urk_kwarg = 'id'
    url 
    path('customcontextstudent/<int:id>/', views.StudentDetailCustomContextView.as_view(), name='customcontext'),
    """

# creating a list view 
class StudentListView(ListView):
    model = Student 
