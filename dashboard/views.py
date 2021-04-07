from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm 
from post.models import Post
from django.views.generic import View
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'dashboard/index.html')


class PostView(generic.ListView):
    template_name="dashboard/view_post.html"  

    def get_queryset(self):
        queryset=Post.objects.filter(author=self.request.user).order_by('-id')
        print(queryset)
        return queryset

class CreatePostView(SuccessMessageMixin,generic.CreateView):
    form_class = PostForm
    model = Post
    template_name = "dashboard/create_post.html"
    success_url ="/dashboard/view_post/"
    success_message = "Post was Created successfully"
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(CreatePostView, self).form_valid(form)

# class DeletePost(View):
#     def get(self,request,id):
#         post = Post.object.get(id=id)
#         post.delete()
#         messages.success(request,"Deleted Successfully")
#         return HttpResponseRedirect('/dashboard/view_post')

class DeletePost(generic.DeleteView):
    model = Post
    Template_name = 'dashboard/delete_post.html'
     