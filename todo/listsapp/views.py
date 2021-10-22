# from django.shortcuts import render
# import json
# from django.http import HttpResponse
# from .models import List

# def index(request):
#     return HttpResponse("Hello World")

# def displayAllLists(request):
#     data = List.objects.values()
#     # print(data)
#     # Users.objects.values_list('firstnames', flat=True)

#     return HttpResponse(json.dumps(list(data)), content_type="application/json")

from rest_framework import viewsets
from .serializers import ListSerializer
from .models import List

# ViewSets define the view behavior.
class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer