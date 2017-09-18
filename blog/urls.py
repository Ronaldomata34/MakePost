from django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view() , name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='detail'),
    url(r'^post/new/$', views.NewPost.as_view(), name='new'),
    url(r'^post/update/(?P<pk>\d+)/$', views.UpdatePost.as_view(), name='update'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete'),
]

