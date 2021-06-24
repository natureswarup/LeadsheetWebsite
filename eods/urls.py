from django.urls import path
from . import views
# For uploading in development
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'eods'
urlpatterns = [
    path('', views.index, name='index'),
    path('csv', views.csv_download, name='csv_download'),
    path('<int:office_id>/', views.option, name='option'),
    path('<int:office_id>/create_lead', views.create_lead, name='create_lead'),
    path('<int:office_id>/view_lead', views.view_lead, name='view_lead'),
    path('<int:office_id>/review_lead',
         views.review_lead, name='review_lead'),
    path('<int:office_id>/<int:leadsheet_id>',
         views.edit_lead, name='edit_lead'),

    path('<int:office_id>/<int:leadsheet_id>/email_lead',
         views.email_lead, name='email_lead'),
    path('<int:office_id>/view_lead/<int:leadsheet_id>',
         views.delete_lead, name='delete_lead'),


]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
