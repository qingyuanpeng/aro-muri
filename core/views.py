from django.shortcuts import render
from core.models import Comment
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, "index.html", {})


def overview(request):
    return render(request, "project-overview.html", {})


def people(request):
    return render(request, "people.html", {})


def events(request):
    return render(request, "meetings-events.html", {})


def readingGroup(request):
    return render(request, "reading-group.html", {})


# def internalDiscussion(request):
#     return render(request, "reading-group.html", {})


def internalDiscussion(request):
    if request.method == "POST":
        if str(request.user) != "AnonymousUser":
            body = request.POST["body"]
            comments = Comment.objects.create(body=body, author=request.user)
        else:
            comments = comments.objects.order_by("created_at").reverse()
            return render(request, "internal-discussion.html", {"comments": comments, "user": request.user, "valid": False})
    comments = Comment.objects.order_by("created_at").reverse()
    return render(request, "internal-discussion.html", {"comments": comments, "user": request.user, "valid": True})
