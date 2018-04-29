from django.conf.urls import url
from django.urls import reverse
from . import views

app_name = "scrapers"
urlpatterns = [
    url(regex=r"^$", view=views.KeywordListView.as_view(), name="keyword_list"),
    url(regex=r"^~create/$", view=views.KeywordCreateView.as_view(), name="keyword_create"),
    url(regex=r"^~popularity_scrape/$", view=views.KeywordPopularyScrapeView.as_view(), name="keyword_popularity_scrape"),       
    # url(regex=r"^~redirect/$", view=views.UserRedirectView.as_view(), name="redirect"),
    # url(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    # url(
    #     regex=r"^(?P<username>[\w.@+-]+)/$",
    #     view=views.UserDetailView.as_view(),
    #     name="detail",
    # ),
    
]
