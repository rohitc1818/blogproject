from django.shortcuts import render,get_object_or_404,redirect
from fApp.models import Post,Comment
from django.views.generic import ListView,DetailView,CreateView,TemplateView
from fApp.forms import CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def Likeview(request,pk):
    post = get_object_or_404(Post, id = request.POST.get('post.id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('list',args=[str(pk)]))

#def Commentview(request):
 #   form = CommentForm()
  #  if request.method=='POST':
   #     form = CommentForm(request.POST)
    #    if form.is_valid():
     #       form.save(commit=True)
      #  return redirect('/1/detail')
    #return render(request,'fApp/add_comment.html',{'form':form})

def Post_detail_view(request,pk):
    form = CommentForm()
    post = get_object_or_404(Post,id=pk)
    Comment_list = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/1/detail')
    return render(request,'fApp/post_detail.html',{'Comment_list':Comment_list,'post':post,'form':form})



class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post_list.html'

    #def get_context_data(self, *args, **kwargs):
    #    context = super(PostListView,self).get_context_data()
     #   stuff = get_object_or_404(Post,id=self.kwargs['pk'])
      #  total_likes = stuff.total_likes()
       # context['total_likes'] = total_likes
        #return context

#class PostDetailView(DetailView):
#    model = Post

#class AddCommentview(CreateView):
 #   model = Comment
  #  form_class = CommentForm
   # template_name = 'fApp/add_comment.html'
    #template_name = 'add_comment.html'
   # success_url = reverse_lazy('detail')
    #fields = '__all__'








