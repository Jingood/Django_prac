from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from articles.models import Article
from articles.forms import ArticleForm


def index(request):
    return render(request, 'articles/index.html')


def hello(request):
    name = "T문"
    tags = ["#귀여운", "#순수한"]
    conditions = {
        "today": "피곤",
        "yesterday": "왕피곤",
        "tomorrow": "???"
    }
    context = {
        "name": name,
        "tags": tags,
        "conditions": conditions
    }
    return render(request, 'articles/hello.html', context)


def articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'articles/articles.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        "article": article
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm()

        context = {"form": form}
    return render(request, 'articles/create.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }
    return render(request, 'articles/update.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:articles')


def data_throw(request):
    return render(request, 'articles/data-throw.html')


def data_catch(request):
    message = request.GET.get("message")
    context = {"message": message}
    return render(request, 'articles/data-catch.html', context)
