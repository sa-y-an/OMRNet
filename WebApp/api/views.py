from rest_framework import generics, permissions, mixins, serializers, status
from classifier.models import Image
from .serializers import ImageSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from classifier.evaluation import ImageClass

class ImageCreate(generics.ListCreateAPIView):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self,serializer):
        serializer.save()
        pth = str(serializer.instance.image.url)
        pth = pth[1:]
        confidence_score, ac_class = ImageClass(pth)

        # writing into the model 

        # img = Image.objects.get(title = img_obj.title)
        serializer.instance.ans_class = ac_class
        serializer.instance.score = confidence_score

        serializer.save()

        # img.save()
        
