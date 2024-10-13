from django.shortcuts import render, redirect, get_object_or_404
from menfess_app import forms
from menfess_app.models import Menfess, Reply
import random
# Create your views here.

def index(request):
    menfess_data = Menfess.objects.all().order_by('-date')
    
    random_caption = ["Have a confession or secret to share? Say it anonymously and let your story be heard without revealing your identity. Speak your truth safely here!", 
                      "Want to vent or confess without anyone knowing it's you? Here, your thoughts are safe and anonymous. Let it all out—completely free of judgment!", 
                      "Need a space to share what's on your mind without the spotlight? Drop your thoughts here—anonymously and effortlessly. Your voice, your way!", 
                      "Got something on your chest? Share your feelings, stories, or secrets anonymously. It's your moment, without the world knowing it's you!", 
                      "Looking for a safe place to confess or speak your mind? Share your thoughts here without revealing who you are. Your story, your secret!", 
                      "Keep your identity hidden while sharing your confessions or thoughts. It's your voice, your truth—no names attached!", 
                      "Feeling the need to speak up but want to remain unseen? Share your thoughts, secrets, and confessions anonymously. We've got your back!", 
                      "Say what you need to say, no strings attached. Confess, vent, or share your story in total anonymity. Your voice, your space!", 
                      "Got a secret or thought that you can't keep in? Share it here without revealing your identity. Speak freely, we keep it anonymous!", 
                      "Sometimes, you just need to get something off your chest. Share your thoughts and feelings with the world anonymously. Your secret is safe with us!",
                      "Got something to say but want to stay anonymous? Share your thoughts, confessions, or secrets freely with the world here. Your voice, your story—completely anonymous!"]
    caption = random.choice(random_caption)
    
    return render(request, "menfess_app/index.html", context={'menfess_data':menfess_data,
                                                              'caption': caption})

def create(request):
    form = forms.CreateMenfess()
    if request.method == 'POST':
        form = forms.CreateMenfess(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request, "menfess_app/create_menfess.html", context={'form': form,})

# def reply(request, slug):
#     form = forms.Reply()
#     get_reply = get_object_or_404(Menfess, slug=slug)
#     if request.method == 'POST':
#         form = forms.Reply(request.POST)
#         if form.is_valid():
#             reply = form.save()
            
#             form.save()
#             return redirect('reply')
#     return render(request, "menfess_app/reply.html", context={'form': form, 'reply':get_reply})


def reply(request, slug):
    post = get_object_or_404(Menfess, slug=slug)  # Mengambil berdasarkan slug

    form = forms.ReplyMenfess()
    all_reply = Reply.objects.filter(menfess=post.pk).order_by('-reply_date')
    if request.method == 'POST':
        form = forms.ReplyMenfess(request.POST)
        
        if form.is_valid():
            reply = form.save(commit=False)
            reply.menfess = post  # Hubungkan reply dengan post terkait
            reply.save()
            form = forms.ReplyMenfess()
            return redirect(f'{request.path}#{reply.pk}')# Arahkan ke halaman index setelah reply
    
    return render(request, "menfess_app/reply.html", context={'form': form, 'post': post, 'all_reply': all_reply})

