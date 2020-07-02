from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


from posts import views
from django.conf import settings
from django.conf.urls.static import static


API_TITLE = 'Blog API' # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.' # new
#schema_view = get_schema_view(title=API_TITLE) # new
schema_view = get_swagger_view(title=API_TITLE)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), # new
    #path('schema/', schema_view),
    path('swagger-docs/', schema_view),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('djrichtextfield/', include('djrichtextfield.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
