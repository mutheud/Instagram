from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewProfileForm,CommentForm
from tinymce.models import HTMLField
from .models import Profile, Image, Comment
from django.views.generic import RedirectView

@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    comments = Comment()

    return render(request, 'welcome.html',{'images':images})

def profile(request,profile_id):
    try:
        profile =  Profile.objects.get(id =  profile_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"profile.html", {" profile": profile})


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('welcome')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def logout(request):
    
    return redirect('welcome')

def search_results(request):
    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        searched_users = User.objects.filter(username=search_term)
        profile = Profile.search_user(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'users':searched_users, 'profilesa':profile})
    else:
        message = 'Enter term to search'
        return render(request, 'main_pages/search.html', {'message':message})

def one_image(request,image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
    return redirect('welcome')

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("image_id")
        print(slug)
        obj = get_object_or_404(Image, slug=image_id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_
