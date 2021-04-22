from django.shortcuts import redirect, render
from .forms import CreatePostForm, CommentForm
from .models import Post, Comment



# Create your views here.
def DiscForumHome(request):
    posts = Post.objects.all().order_by('-date')

    context = {'posts':posts}
    return render(request, 'discussionforum/df_index.html', context)


def CreatePost(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            form.save()
            return redirect('DiscForumHome')


    context = {'form':form}
    return render(request, 'discussionforum/create_post.html', context)


def UpdatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = CreatePostForm(instance=post)
    update = True
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('DiscForumHome')


    context = {
        'form':form,
        'update':update,
    }
    return render(request, 'discussionforum/create_post.html', context)


def DeletePost(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('DiscForumHome')

    context = {'post':post}
    return render(request, "discussionforum/delete_post.html", context)



def ViewPost(request, slug):
    
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post_id=post.id).order_by('-date')
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_id = request.user.id
            comment.post_id = post.id
            form.save()

    context = {'post':post,'form':form,'comments':comments}
    return render(request, 'discussionforum/viewPost.html', context)