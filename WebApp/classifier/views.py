from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .evaluation import ImageClass
from .models import Image

def predict(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form.title)
            # Get the current instance object to display in the template
            img_obj = form.instance
            pth = str(img_obj.image.url)
            pth = pth[1:]
            confidence_score, ac_class = ImageClass(pth)

            # writing into the model 

            img = Image.objects.get(title = img_obj.title)
            img.ans_class = ac_class
            img.score = confidence_score

            img.save()

            # return render(request, 'classifier\home.html', {'form': form})
            return render(request, 'classifier/predict.html', {'form': form, 'img_obj': img})
        else:
            # print('invalid')
            return HttpResponse('<h2> Form data not valid </h2> <br> Please check if you have uploaded any file before submission')
    else:
        form = ImageForm()
        return render(request, 'classifier/predict.html', {'form': form})
