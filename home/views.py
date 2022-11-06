from django.http import HttpResponseRedirect
from django.urls import reverse, set_script_prefix     
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Genre, Serie, Episode


User = get_user_model()

def Home(request):
    genres = Genre.objects.all()
    series = Serie.objects.all().order_by('-date')[:6]
    template_name = 'home/index.html'
    context = {
        'genres': genres,
        'series': series, 
        }
    return render(request, template_name, context)

def Single(request, slug):
    serie = get_object_or_404(Serie, slug=slug)
    episodes = Episode.objects.filter(serie=serie)
    genres = Genre.objects.all()
    template_name = 'home/detail_serie.html'
    context = {
        'serie': serie, 
        'episodes': episodes, 
        'genres': genres,
        }
    return render(request, template_name, context)

def Play(request, slug):
    episode = get_object_or_404(Episode, slug=slug)
    other_episodes = Episode.objects.filter(serie=episode.serie).exclude(pk=episode.pk)
    # episode = get_object_or_404(Episode, slug=slug)
    template_name = 'home/play.html'
    context = {
        'episode': episode, 
        'other_episodes': other_episodes,
        }
    return render(request, template_name, context)


# @login_required
# def DetailPost(request, slug):
#     template_name = 'post/detail_post.html'
#     # Commentaires
#     comments = Comment.objects.filter(post=post).order_by('date')
#     user = request.user
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.user = user
#             comment.save()
#             return HttpResponseRedirect(reverse('detail_post', args=[slug]))
#     else:
#         form = CommentForm()
#     return render(request, template_name, {
#         'post': post, 
#         'form': form, 
#         'comments': comments, 
#         'genres': genres, 
#         'aside': aside
#         })


# def Suggestions(request):
#     posts = Post.objects.all()
#     aside = Post.objects.all().order_by('?')[:9]
#     genres = Genre.objects.all()
#     template_name = 'post/suggestions.html'
#     context = {
#         'posts': posts, 
#         'aside': aside,
#         'genres': genres,
#         }
#     return render(request, template_name, context)




# def Search(request):
#     search = request.GET.get('search')
#     posts = Post.objects.filter(title__icontains=search)
#     aside = Post.objects.all().order_by('?')[:5]
#     genres = Genre.objects.all()
#     context = {
#         'search': search,
#         'posts': posts,
#         'aside': aside,
#         'genres': genres,
#         }
#     return render(request, 'post/search.html', context)
  