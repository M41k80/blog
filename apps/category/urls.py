from django.urls import path
from rest_framework.documentation import include_docs_urls
from .views import *


urlpatterns = [
    path('/list', ListCategoriesView.as_view()),
    path('/docs/', include_docs_urls(title='Category API')),
    
]