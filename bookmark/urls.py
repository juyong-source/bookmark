from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/???
    # 내부적으로 함수형 뷰로 처리
    # list는 URL 패턴의 이름
    # detail/<int:pk/> 기본 형식은 문자열임
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BoomarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BoomarkDeleteView.as_view(), name='delete'),
]