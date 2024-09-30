# 100-Django-Concepts 

# what in where 
```text
med : nothing here
authenticationusercreationform: check authentication and authorization cookies , session, page session and cache and many more 
aboutcookies: learn about cookies from this project
E-Commerce Project: Creating an e-commerce website using react js and django rest framework
```

## Limiting QuerySets
```text
Use a subset of Python's array-slicing to limit over QuerySet to a certain number of results.
This is the equivalent of SQL's LIMIT and OFFSET clauses.

Student.objects.all()[:5] - This returns First 5 objects
Student.objects.all()[5:100] - This returns sixth through tenth objects
Student.objects.all()[-1] - This is not valid
Student.objects.all()[:10:2] - This returns a list of every second object of first 10
```