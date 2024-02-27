"""
URL configuration for Toonify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.urls import path,include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    
    path('indexpage/', views.indexpage, name='indexpage'),
    
    
    path('sliderpage/', views.sliderpage, name='sliderpage'),
    path('sliderpageinsert/', views.sliderpageinsert, name='sliderpageinsert'),
    path('sliderdatatable/', views.sliderdatatable, name='sliderdatatable'),
    path('sliderpageedit/<int:id>', views.sliderpageedit, name='sliderpageedit'),
    path('sliderpageupdate/', views.sliderpageupdate, name='sliderpageupdate'),
    path('deleteslider/<int:id>', views.deleteslider, name='deleteslider'),
    
    
    path('workprocedurepage/', views.workprocedurepage, name='workprocedurepage'),
    path('workprocedureheadinginsert/', views.workprocedureheadinginsert, name='workprocedureheadinginsert'),
    path('workproceduredatatable/', views.workproceduredatatable, name='workproceduredatatable'),
    path('workprocedurepageedit/<int:id>', views.workprocedurepageedit, name='workprocedurepageedit'),
    path('workprocedureupdate/', views.workprocedureupdate, name='workprocedureupdate'),
    path('deleteworkprocedure/<int:id>', views.deleteworkprocedure, name='deleteworkprocedure'),
    
    
    path('workproceduretopicpage/', views.workproceduretopicpage, name='workproceduretopicpage'),
    path('workproceduretopicinsert/', views.workproceduretopicinsert, name='workproceduretopicinsert'),
    path('workproceduretopicdatatable/', views.workproceduretopicdatatable, name='workproceduretopicdatatable'),
    path('workproceduretopicepageedit/<int:id>', views.workproceduretopicepageedit, name='workproceduretopicepageedit'),
    path('workproceduretopicupdate/', views.workproceduretopicupdate, name='workproceduretopicupdate'),
    path('deleteworkproceduretopic/<int:id>', views.deleteworkproceduretopic, name='deleteworkproceduretopic'),
    
    
    path('toonificationheadingpage/', views.toonificationheadingpage, name='toonificationheadingpage'),
    path('toonificationheadinginsert/', views.toonificationheadinginsert, name='toonificationheadinginsert'),
    path('Toonificationdatatable/', views.Toonificationdatatable, name='Toonificationdatatable'),
    path('ToonificationHeadingpageedit/<int:id>', views.ToonificationHeadingpageedit, name='ToonificationHeadingpageedit'),
    path('ToonificationHeadingupdate/', views.ToonificationHeadingupdate, name='ToonificationHeadingupdate'),
    path('deleteToonificationHeading/<int:id>', views.deleteToonificationHeading, name='deleteToonificationHeading'),
    
    
    path('toonificationimagepage/', views.toonificationimagepage, name='toonificationimagepage'),
    path('toonificationimageinsert/', views.toonificationimageinsert, name='toonificationimageinsert'),
    path('toonificationimagedatatable/', views.toonificationimagedatatable, name='toonificationimagedatatable'),
    path('toonificationimagepageedit/<int:id>', views.toonificationimagepageedit, name='toonificationimagepageedit'),
    path('toonificationimageupdate/', views.toonificationimageupdate, name='toonificationimageupdate'),
    path('deletetoonificationimage/<int:id>', views.deletetoonificationimage, name='deletetoonificationimage'),
    
    
    path('hyperparametersheadingpage/', views.hyperparametersheadingpage, name='hyperparametersheadingpage'),
    path('hyperparametersheadinginsert/', views.hyperparametersheadinginsert, name='hyperparametersheadinginsert'),
    path('hyperparametersdatatable/', views.hyperparametersdatatable, name='hyperparametersdatatable'),
    path('hyperparametersHeadingpageedit/<int:id>', views.hyperparametersHeadingpageedit, name='hyperparametersHeadingpageedit'),
    path('hyperparametersHeadingupdate/', views.hyperparametersHeadingupdate, name='hyperparametersHeadingupdate'),
    path('deletehyperparametersHeading/<int:id>', views.deletehyperparametersHeading, name='deletehyperparametersHeading'),
    
    
    path('hyperparametersimagepage/', views.hyperparametersimagepage, name='hyperparametersimagepage'),
    path('hyperparametersimageinsert/', views.hyperparametersimageinsert, name='hyperparametersimageinsert'),
    path('hyperparametersimagedatatable/', views.hyperparametersimagedatatable, name='hyperparametersimagedatatable'),
    path('hyperparametersimagepageedit/<int:id>', views.hyperparametersimagepageedit, name='hyperparametersimagepageedit'),
    path('hyperparametersimageupdate/', views.hyperparametersimageupdate, name='hyperparametersimageupdate'),
    path('deletehyperparametersimage/<int:id>', views.deletehyperparametersimage, name='deletehyperparametersimage'),
    
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
