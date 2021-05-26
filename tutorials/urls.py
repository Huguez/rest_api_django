from django.urls import path
from . import views

urlpatterns = [
    path( 'api/prueba', views.hello_world ),

    path( 'api/create/tutorial', views.create_tutorial ),
    path( 'api/tutorials', views.tutorial_list ),
    path( 'api/delete/tutorial/<pk>', views.delete_tutorial ),
    path( 'api/update/tutorial/<pk>', views.update_tutorial ),
    path( 'api/tutorials/<pk>', views.tutorial_detail )
]
