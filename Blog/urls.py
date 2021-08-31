from django.urls import include, path
from rest_framework import routers

from Blog.mysite import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'blogs', views.BlogSerializerViewSet)
router.register(r'sections', views.SectionSerializerViewSet)
router.register(r'subjects', views.SubjectSerializerViewSet)
router.register(r'subject_colors', views.SubjectColorSerializerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]