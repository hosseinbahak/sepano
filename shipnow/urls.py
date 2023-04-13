from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls', namespace='account'),),
    path('api/v1/store/', include('store.urls', namespace='store'),),
    path('', include_docs_urls(
                                title='Store APIs Document',
                                description='description of all APIs will add here',
                                    
                            )
    )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
