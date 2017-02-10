from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

from .models import *

BLOG_PATINATION_INTERVAL = 12


def main(request, category=None):
    # get the page from the query string,
    # default to 1 if none is provided
    page = request.GET.get('page', 1)

    posts = Post.objects.order_by("-created")

    # if they provided a category
    # art, writing, or multimedia
    if category is not None:
        # if its writing
        if category == "writing":
            # filter to any of the writing categories
            categories = [
                "Writing",
                "fiction",
                "Lyric essay",
                "Review essay",
                "Interview"
            ]
            posts = posts.filter(posted__name__in=categories)
        # otherwise filter to the provided category
        else:
            posts = posts.filter(posted__name=category)

    paginator = Paginator(posts, BLOG_PATINATION_INTERVAL)

    try:
        current_page = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        current_page = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_page = paginator.page(paginator.num_pages)

    context = {
        'posts': current_page,
        'name': category
    }

    return render(request, 'blog.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, 'blog_post.html', {'post': post})


def contributor_page(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {
        "author": author,
        "articles": Post.objects.filter(authors=author)
    }
    return render(request, 'blog_contributor.html', context)


def tag_page(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    context = {
        "tag": tag,
        "articles": Post.objects.filter(tags=tag)
    }
    return render(request, 'blog_tags.html', context)


def theme(request):
    section = request.path
    section = section.replace("/", "").replace("blog", "")
    page = request.GET.get('page', 1)

    posts_in_cat = Post.objects.filter(theme__name=theme)
    all_posts_sorted = posts_in_cat.order_by("-created")

    paginator = Paginator(all_posts_sorted, BLOG_PATINATION_INTERVAL)

    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_page = paginator.page(paginator.num_pages)

    data = {
        'posts': blog_page,
        'name': section
    }
    return render(request, 'blog_section.html', data)
