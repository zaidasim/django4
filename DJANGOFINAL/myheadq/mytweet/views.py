from django.shortcuts import render
from django.urls import path
from .models import Tweet
from .forms import Tweetforms
from django.shortcuts import  get_object_or_404,redirect
# Create your views here
def index(request):
    return render(request, 'index.html')
def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at') 
    return render(request,'treat_list.html',{'tweets':tweets})
def tweet_create(request):
    if request.method == 'POST':
        form=Tweetforms(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=Tweetforms()
    return render(request,'Tweetforms.html',{'form':form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = Tweetforms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Tweetforms(instance=tweet)

    return render(request, 'Tweetforms.html', {'form': form})
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})