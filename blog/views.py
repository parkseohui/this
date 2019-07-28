from django.shortcuts import render
from .models import Post,Category
from django.views.generic import ListView,DetailView

class PostList(ListView): #복잡하게 쓰지않고 간단하게 리스트를 보여주려고 이걸씀
    model=Post
# Create your views here.
# def index(request):
    #posts=Post.objects.all()
    #return render(request,'blog/index.html',{'posts':posts,'hi':1+1})
    def get_queryset(self): # 이 친구는 가장최근꺼를 위로띄우는 친구야
        return Post.objects.order_by('-created')
    def get_context_data(self,*,object_list=None,**kwargs):
        context=super(PostList,self).get_context_data(**kwargs)
        context['category_list']=Category.objects.all()
        context['posts_without_category']=Post.objects.filter(category=None).count()
        return context
#def post_detail(request,pk):
    #blog_post=Post.objects.get(pk=pk)
    #return render(request,'blog/post_detail.html',{'blog_post':blog_post})
class PostDetail(DetailView):
    model=Post
