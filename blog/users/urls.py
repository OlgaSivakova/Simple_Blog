from django.urls import path, include
from users.views import Register
from .import views


urlpatterns = [path('', include('django.contrib.auth.urls')),
               path('register/', Register.as_view(), name='register'),
               path('',  views.PostView.as_view(), name='home'),
               path('add/',views.addpost, name='add'),
                path('<int:pk>/',views.PostElement.as_view()),
                path('del/<int:pk>/',views.DelElement.as_view(), name='del'),
                path('comments/<int:pk>',views.AddComments.as_view(), name='comment'),
                path('<int:pk>/add_likes/',views.AddLike.as_view(), name='add_likes'),
                path('<int:pk>/del_likes/',views.DelLike.as_view(), name='del_likes'),
                path('api/v1/postlist/<int:pk>',views.PostCRUD.as_view(), name='serializ'),
                path('api/v1/postlist/',views.PostAPIlist.as_view(), name='serializall'),
                
                     ]




