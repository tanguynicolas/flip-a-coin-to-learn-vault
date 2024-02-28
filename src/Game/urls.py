from django.urls import path

from .views import homepage, tails, heads, reset

urlpatterns = [
    path('', homepage, name="game-homepage"),
    path('tails/', tails, name="game-tails"),
    path('heads/', heads, name="game-heads"),
    path('reset/', reset, name="game-reset")
]
