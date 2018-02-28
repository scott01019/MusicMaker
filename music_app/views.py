from django.shortcuts import render

# Create your views here.
def music_maker(req):
    return render(req, "music_app/music_maker.html")