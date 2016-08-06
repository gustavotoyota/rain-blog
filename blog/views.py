from django.shortcuts import render, get_object_or_404, redirect
from models import Post, Comment
from forms import CommentForm
from django.utils import timezone

def posts(request):
    return render(request, 'blog/posts.html', {'posts': Post.objects.order_by('timestamp')})

def post(request, pk):
    current_post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=current_post).order_by('timestamp')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = current_post
            comment.timestamp = timezone.now()
            comment.save()
            return redirect('post', pk=pk)
    comment_form = CommentForm()
    return render(request, 'blog/post.html', {'post': current_post, 'comments': comments, 'comment_form': comment_form})