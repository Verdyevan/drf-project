from django.urls import path, include
from .views import ArticleAPIView, article_detail, article_list, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    #Versi paling simple List&CRUD
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    #Versi paling ribet List
    #path('article/', article_list),

    #Versi tingkat 2 List
    path('article/', ArticleAPIView.as_view()),

    #Versi paling ribet CRUD
    #path('detail/<int:id>/', article_detail),

    #Versi tingkat 2 CRUD
    path('detail/<int:id>/', ArticleDetails.as_view()),

    #Versi tingkat 3 List&CRUD
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]