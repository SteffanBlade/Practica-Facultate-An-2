from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'post/index.html'
    context_object_name = 'Post_list'

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'

# ----------------------------------------------------------

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PostForm()

    return render(request,'post/create.html',{'form': form})

def edit(request, pk, template_name='post/edit.html'):
    Post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=Post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='post/confirm_delete.html'):
    Post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        Post.delete()
        return redirect('index')
    return render(request, template_name, {'object':Post})