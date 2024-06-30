from .models import CustomUser


def register_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        phonenumber = request.POST.get('phonenumber')

        userObj = CustomUser.objects.filter(email = email)
        if userObj.exists():
            messages.warning(request)
