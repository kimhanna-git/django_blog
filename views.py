from django.shortcuts import render

##request. home. handle these things. return what users want to see
posts = [
    {
        'author': 'Hanna',
        'title': 'Blog Post 1',
        'content': 'first post',
        'date': 'Dec 3, 2021'
    },
    {
        'author': 'Hitesh',
        'title': 'Blog Post 2',
        'content': 'second post',
        'date': 'Dec 4, 2021'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render (request, 'blog/home.html', context)
def about(request) :
    return render (request, 'blog/about.html', {'title': 'About'})
##we need url pattern! ets creat urls.py and map the url for each view functionl