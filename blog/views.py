from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request,'blog/post_list.html',{})
    # A function called post_list is created that takes request and will return render that will render(put together) our template blog/post_list.html