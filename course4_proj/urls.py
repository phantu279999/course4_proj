from django.contrib import admin
from django.urls import path

import gh.views
import movies.views

urlpatterns = [
    path("", gh.views.index, name='index'),
    path("search/", movies.views.search, name="search"),
    path(
        "search-wait/<uuid:result_uuid>/", movies.views.search_wait, name="search_wait"
    ),
    path("search-results/", movies.views.search_results, name="search_results"),
    path('admin/', admin.site.urls),
]
