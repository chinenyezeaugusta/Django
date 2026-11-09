from django.shortcuts import HttpResponse, render

POSTS = [
    { "id": 1, "title": "First Post", "content": "This is the content of the first post."},
    { "id": 2, "title": "Second Post", "content": "This is the content of the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the content of the third post."}, 

]

def home(request):
    context = {"posts": POSTS}
    return render(request, 'home.html', context)


def post_detail(request, post_id):
    return render(request, 'post_detail.html', {'post_id': post_id})

