from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blog_total = Blog.objects.count
    blogs = Blog.objects.all()
    return render(request, 'all_blogs.html', {'blogs': blogs, 'blog_total':blog_total})

def detail(request, blog_id):
    blog= get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog':blog})
