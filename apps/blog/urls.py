from django.urls import path
from rest_framework.documentation import include_docs_urls
from .views import *





urlpatterns = [
    path('/list', BlogListView.as_view()),
    path('/by_category', ListPostByCategoryView.as_view()),
    path('/detail/<slug>', PostDetailView.as_view()),
    path('/search', SearchBlogView.as_view()),
    path('/docs/', include_docs_urls(title='Blog API')),
]