from django.contrib import admin

from .models import Sliderpage, WorkProcedureHeading,WorkProcedureTopic,ToonificationHeading,ToonificationImage,HyperparametersHeading,HyperparametersImage

admin.site.register(Sliderpage)
admin.site.register(WorkProcedureHeading)
admin.site.register(WorkProcedureTopic)
admin.site.register(ToonificationHeading)
admin.site.register(ToonificationImage)
admin.site.register(HyperparametersHeading)
admin.site.register(HyperparametersImage)