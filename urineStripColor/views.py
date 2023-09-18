from django.shortcuts import render, redirect
from .forms import StripImageForm
from rest_framework import viewsets, permissions
from .models import StripImage
from .serializers import StripImageSerializer

from .colors_values import values


def reading(my_dict):
    values = list(my_dict.values())
    print(values)

    colors = {
        'URO': list(values[0]),
        'BIL': list(values[1]),
        'KET': list(values[2]),
        'BLD': list(values[3]),
        'PRO': list(values[4]),
        'NIT': list(values[5]),
        'LEU': list(values[6]),
        'GLU': list(values[7]),
        'SG': list(values[8]),
        'PH': list(values[9]),
    }
    return (colors)


def analyze_strip(request):
    if request.method == 'POST':
        form = StripImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            form.save()

            # Read the uploaded image using OpenCV
            image_path = form.instance.url.path
            colors = values(image_path=image_path)

            content = reading(colors)

            # Return the color results as JSON
            return render(request, 'urineStripColor/index.html', {'data': content})
    else:
        form = StripImageForm()
    return render(request, 'urineStripColor/index.html', {'form': form})


class StripImageViewSet(viewsets.ModelViewSet):
    queryset = StripImage.objects.all()
    serializer_class = StripImageSerializer
    permission_classes = [permissions.AllowAny]
