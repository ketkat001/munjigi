from django.urls import path
from . import views
from .views import HeritageListAPI, HeritageDetailAPI, HeritageLikeAPI, HeritageBookmarkAPI, HeritageVisitAPI, HeritageRatingAPI, HeritageListAPI2

urlpatterns = [
    path('', HeritageListAPI.as_view()),
    path('<int:pk>/', HeritageDetailAPI.as_view()),
    path('<int:pk>/like/', HeritageLikeAPI.as_view()),
    path('<int:pk>/dib/', HeritageBookmarkAPI.as_view()),
    path('<int:pk>/visit/', HeritageVisitAPI.as_view()),
    path('<int:pk>/score/', HeritageRatingAPI.as_view()),
    path('search/', HeritageListAPI2.as_view())
]
