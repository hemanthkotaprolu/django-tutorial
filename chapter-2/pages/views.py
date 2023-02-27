from django.shortcuts import HttpResponse

# Create your views here.

#Technically there are 3 different ways to write a view in django
# 1. CLass-Based views
# 2. Function-Based views
# 3. Generic Class-Based views
def homePageView(request):
    return HttpResponse("Hello, world!")
