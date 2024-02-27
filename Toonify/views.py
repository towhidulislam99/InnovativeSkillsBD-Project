from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sliderpage,WorkProcedureHeading,WorkProcedureTopic,ToonificationHeading,ToonificationImage,HyperparametersHeading,HyperparametersImage
import os


def Toonify(request):

    sliderdata = Sliderpage.objects.all()
    workprocedureheading = WorkProcedureHeading.objects.all()
    workproceduretopic = WorkProcedureTopic.objects.all()
    toonificationHeadingdata = ToonificationHeading.objects.all()
    toonificationimagedata = ToonificationImage.objects.all()
    hyperparametersHeadingdata = HyperparametersHeading.objects.all()
    hyperparametersimagedata = HyperparametersImage.objects.all()
    

    data = {
        'sliderdata': sliderdata,
        'workprocedureheading': workprocedureheading,
        'workproceduretopic': workproceduretopic,
        'toonificationHeadingdata': toonificationHeadingdata,
        'toonificationimagedata': toonificationimagedata,
        'hyperparametersHeadingdata': hyperparametersHeadingdata,
        'hyperparametersimagedata': hyperparametersimagedata,
    }
    return render(request, 'index.html', data)

def indexpage(request):
    sliderdata = Sliderpage.objects.all()
    workprocedureheading = WorkProcedureHeading.objects.all()
    workproceduretopic = WorkProcedureTopic.objects.all()
    toonificationHeadingdata = ToonificationHeading.objects.all()
    toonificationimagedata = ToonificationImage.objects.all()
    hyperparametersHeadingdata = HyperparametersHeading.objects.all()
    hyperparametersimagedata = HyperparametersImage.objects.all()
    

    data = {
        'sliderdata': sliderdata,
        'workprocedureheading': workprocedureheading,
        'workproceduretopic': workproceduretopic,
        'toonificationHeadingdata': toonificationHeadingdata,
        'toonificationimagedata': toonificationimagedata,
        'hyperparametersHeadingdata': hyperparametersHeadingdata,
        'hyperparametersimagedata': hyperparametersimagedata,
    }
    return render(request, 'adminhome.html', data)

#<-------Slider Page  Section Work -----------------> 
#====================================================================================

def sliderpage(request):
    return render(request, 'sliderinput.html')

def sliderpageinsert(request):
    if request.method == 'POST':
        slider_heading = request.POST.get('slider_heading')
        slider_paragraph = request.POST.get('slider_paragraph')
        slider_photo = request.FILES.get('slider_photo')
        
        # Create a new instance of the Sliderpage model and assign values
        sliderpage_obj = Sliderpage()
        sliderpage_obj.slider_heading = slider_heading
        sliderpage_obj.slider_paragraph = slider_paragraph
        sliderpage_obj.slider_photo = slider_photo
        sliderpage_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('sliderpage')  
    
    return render(request, 'sliderinput.html')  

def sliderdatatable(request):
    sliderdata = Sliderpage.objects.all()
    data = {"sliderdata": sliderdata}
    return render(request,'sliderdatatable.html',data)

def sliderpageedit(request, id):
    sliderdata = Sliderpage.objects.get(id=id)
    data = {"sliderdata": sliderdata}
    return render(request,'sliderpageUpdate.html',data)

def sliderpageupdate(request):
    id = request.POST.get('id')
    slider_heading = request.POST.get('slider_heading')
    slider_paragraph = request.POST.get('slider_paragraph')
   
    # Get the user object by ID
    sliderpage_obj = get_object_or_404(Sliderpage, id=id)
    
    # Check if new image and video files are provided
    if 'slider_photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if sliderpage_obj.slider_photo:
            os.remove(sliderpage_obj.slider_photo.path)
        sliderpage_obj.slider_photo = request.FILES['slider_photo']
    
    sliderpage_obj.slider_heading = slider_heading
    sliderpage_obj.slider_paragraph = slider_paragraph
    sliderpage_obj.save()
    return redirect('sliderdatatable')

def deleteslider(request, id):
    sliderpage_obj = get_object_or_404(Sliderpage, id=id)
    sliderpage_obj.delete()
    return redirect('sliderdatatable')
    
#     <-------Work Procedure Heading  Section Work -----------------> 
#====================================================================================
def workprocedurepage(request):
    return render(request, 'workprocedureheadinginput.html')

def workprocedureheadinginsert(request):
    if request.method == 'POST':
        work_pro_heading = request.POST.get('work_pro_heading')
        
        workprocedureheading_obj = WorkProcedureHeading()
        workprocedureheading_obj.work_pro_heading = work_pro_heading
        workprocedureheading_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('workprocedurepage')  
    
    return render(request, 'workprocedureheadinginput.html') 

def workproceduredatatable(request):
    workprocedureheadingdata = WorkProcedureHeading.objects.all()
    data = {"workprocedureheadingdata": workprocedureheadingdata}
    return render(request,'workproceduredatatable.html', data)

def workprocedurepageedit(request, id):
    workprocedureheadingdata = WorkProcedureHeading.objects.get(id=id)
    data = {"workprocedureheadingdata": workprocedureheadingdata}
    return render(request,'workprocedurepageUpdate.html',data)

def workprocedureupdate(request):
    id = request.POST.get('id')
    work_pro_heading = request.POST.get('work_pro_heading')
   
    # Get the user object by ID
    workprocedureheading_obj = get_object_or_404(WorkProcedureHeading, id=id)
    
    workprocedureheading_obj.work_pro_heading = work_pro_heading
    workprocedureheading_obj.save()
    return redirect('workproceduredatatable')

def deleteworkprocedure(request, id):
    workprocedureheading_obj = get_object_or_404(WorkProcedureHeading, id=id)
    workprocedureheading_obj.delete()
    return redirect('workproceduredatatable')

#      <-------Work Procedure Topic/ Paragraph Section Work -----------------> 
#====================================================================================

def workproceduretopicpage(request):
    return render(request, 'workproceduretopicinput.html')

def workproceduretopicinsert(request):
    if request.method == 'POST':
        work_pro_paragraph = request.POST.get('work_pro_paragraph')
        
        workproceduretopic_obj = WorkProcedureTopic()
        workproceduretopic_obj.work_pro_paragraph = work_pro_paragraph
        workproceduretopic_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('workproceduretopicpage')  
    
    return render(request, 'workproceduretopicinput.html')  

def workproceduretopicdatatable(request):
    workprocedureparagraphdata = WorkProcedureTopic.objects.all()
    data = {"workprocedureparagraphdata": workprocedureparagraphdata}
    return render(request,'workprocedureTopicdatatable.html', data)

def workproceduretopicepageedit(request, id):
    workprocedureparagraphdata = WorkProcedureTopic.objects.get(id=id)
    data = {"workprocedureparagraphdata": workprocedureparagraphdata}
    return render(request,'workprocedurepageTopicUpdate.html', data)

def workproceduretopicupdate(request):
    id = request.POST.get('id')
    work_pro_paragraph = request.POST.get('work_pro_paragraph')
        
    workproceduretopic_obj = get_object_or_404(WorkProcedureTopic, id=id)
    workproceduretopic_obj.work_pro_paragraph = work_pro_paragraph
    workproceduretopic_obj.save()
    return redirect('workproceduretopicdatatable')

def deleteworkproceduretopic(request, id):
    workproceduretopic_obj = get_object_or_404(WorkProcedureTopic, id=id)
    workproceduretopic_obj.delete()
    return redirect('workproceduretopicdatatable')


#     <-------Toonification Heading  Section Work -----------------> 
#====================================================================================

def toonificationheadingpage(request):
    return render(request, 'toonificationheadingpage.html')

def toonificationheadinginsert(request):
    if request.method == 'POST':
        toonification_heading = request.POST.get('toonification_heading')
        
        toonificationHeading_obj = ToonificationHeading()
        toonificationHeading_obj.toonification_heading = toonification_heading
        toonificationHeading_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('toonificationheadingpage') 
    
    return render(request, 'toonificationheadingpage.html')  

def Toonificationdatatable(request):
    toonificationheadingdata = ToonificationHeading.objects.all()
    data = {"toonificationheadingdata": toonificationheadingdata}
    return render(request,'toonificationdatatable.html', data)

def ToonificationHeadingpageedit(request, id):
    toonificationheadingdata = ToonificationHeading.objects.get(id=id)
    data = {"toonificationheadingdata": toonificationheadingdata}
    return render(request,'toonificationheadingpageUpdate.html',data)

def ToonificationHeadingupdate(request):
    id = request.POST.get('id')
    toonification_heading = request.POST.get('toonification_heading')
   
    # Get the user object by ID
    toonificationHeading_obj = get_object_or_404(ToonificationHeading, id=id)
    
    toonificationHeading_obj.toonification_heading = toonification_heading
    toonificationHeading_obj.save()
    return redirect('Toonificationdatatable')

def deleteToonificationHeading(request, id):
    toonificationHeading_obj = get_object_or_404(ToonificationHeading, id=id)
    toonificationHeading_obj.delete()
    return redirect('Toonificationdatatable')

#     <-------Toonification Imgae/Photo Section Work -----------------> 
#====================================================================================

def toonificationimagepage(request):
    return render(request, 'toonificationimagepage.html')

def toonificationimageinsert(request):
    if request.method == 'POST':
        toonification_photo = request.FILES.get('toonification_photo')
        
        toonificationImage_obj = ToonificationImage()
        toonificationImage_obj.toonification_photo = toonification_photo
        toonificationImage_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('toonificationimagepage')  
    
    return render(request, 'toonificationimagepage.html')  

def toonificationimagedatatable(request):
    toonificationimagedata = ToonificationImage.objects.all()
    data = {"toonificationimagedata": toonificationimagedata}
    return render(request,'toonificationimagedatatable.html', data)

def toonificationimagepageedit(request, id):
    toonificationimagedata = ToonificationImage.objects.get(id=id)
    data = {"toonificationimagedata": toonificationimagedata}
    return render(request,'tonificationimagepageUpdate.html',data)

def toonificationimageupdate(request):
    id = request.POST.get('id')

    # Get the user object by ID
    toonificationImage_obj = get_object_or_404(ToonificationImage, id=id)
    
     # Check if new image and video files are provided
    if 'toonification_photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if toonificationImage_obj.toonification_photo:
            os.remove(toonificationImage_obj.toonification_photo.path)
        toonificationImage_obj.toonification_photo = request.FILES['toonification_photo']
   
    toonificationImage_obj.save()
    return redirect('toonificationimagedatatable')

def deletetoonificationimage(request, id):
    toonificationImage_obj = get_object_or_404(ToonificationImage, id=id)
    toonificationImage_obj.delete()
    return redirect('Toonificationdatatable')



#     <------- Hyperparameters Heading Section Work -----------------> 
#====================================================================================

def hyperparametersheadingpage(request):
    return render(request, 'hyperparametersheadingpage.html')

def hyperparametersheadinginsert(request):
    if request.method == 'POST':
        hyperparameters_heading = request.POST.get('hyperparameters_heading')
        
        hyperparameters_obj = HyperparametersHeading()
        hyperparameters_obj.hyperparameters_heading = hyperparameters_heading
        hyperparameters_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('hyperparametersheadingpage') 
    
    return render(request, 'hyperparametersheadingpage.html')  

def hyperparametersdatatable(request):
    hyperparametersheadingdata = HyperparametersHeading.objects.all()
    data = {"hyperparametersheadingdata": hyperparametersheadingdata}
    return render(request,'hyperparametersdatatable.html', data)

def hyperparametersHeadingpageedit(request, id):
    hyperparametersheadingdata = HyperparametersHeading.objects.get(id=id)
    data = {"hyperparametersheadingdata": hyperparametersheadingdata}
    return render(request,'hyperparametersheadingpageUpdate.html',data)

def hyperparametersHeadingupdate(request):
    id = request.POST.get('id')
    hyperparameters_heading = request.POST.get('hyperparameters_heading')
   
    # Get the user object by ID
    hyperparameters_obj = get_object_or_404(HyperparametersHeading, id=id)
    
    hyperparameters_obj.hyperparameters_heading = hyperparameters_heading
    hyperparameters_obj.save()
    return redirect('hyperparametersdatatable')

def deletehyperparametersHeading(request, id):
    hyperparameters_obj = get_object_or_404(HyperparametersHeading, id=id)
    hyperparameters_obj.delete()
    return redirect('hyperparametersdatatable')


#     <------- Hyperparameters Imgae/Photo Section Work -----------------> 
#====================================================================================

def hyperparametersimagepage(request):
    return render(request, 'hyperparametersimagepage.html')

def hyperparametersimageinsert(request):
    if request.method == 'POST':
        hyperparameters_photo = request.FILES.get('hyperparameters_photo')
        
        hyperparametersImage_obj = HyperparametersImage()
        hyperparametersImage_obj.hyperparameters_photo = hyperparameters_photo
        hyperparametersImage_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('hyperparametersimagepage')  
    
    return render(request, 'index.html')  

def hyperparametersimagedatatable(request):
    hyperparametersimagedata = HyperparametersImage.objects.all()
    data = {"hyperparametersimagedata": hyperparametersimagedata}
    return render(request,'hyperparametersimagedatatable.html', data)

def hyperparametersimagepageedit(request, id):
    hyperparametersimagedata = HyperparametersImage.objects.get(id=id)
    data = {"hyperparametersimagedata": hyperparametersimagedata}
    return render(request,'hyperparametersimagepageUpdate.html',data)

def hyperparametersimageupdate(request):
    id = request.POST.get('id')

    # Get the user object by ID
    hyperparametersImage_obj = get_object_or_404(HyperparametersImage, id=id)
    
     # Check if new image and video files are provided
    if 'hyperparameters_photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if hyperparametersImage_obj.hyperparameters_photo:
            os.remove(hyperparametersImage_obj.hyperparameters_photo.path)
        hyperparametersImage_obj.hyperparameters_photo = request.FILES['hyperparameters_photo']
   
    hyperparametersImage_obj.save()
    return redirect('hyperparametersimagedatatable')

def deletehyperparametersimage(request, id):
    hyperparametersImage_obj = get_object_or_404(HyperparametersImage, id=id)
    hyperparametersImage_obj.delete()
    return redirect('hyperparametersimagedatatable')



    
    
    

