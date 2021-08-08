from blog.forms import CommentForm
from django.shortcuts import redirect, render
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    print(post)
    #quit()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_details.html', {'post': post, 'form': form})