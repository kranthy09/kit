from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from essentails.models import Form
from essentails.serializers import FormSerializer

# from django.http.response import HtpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello world')

@csrf_exempt
def form_list(request):

    print(request)
    if request.method == "GET":
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def form_detail(request, pk):

    try:
        form = Form.objects.get(pk=pk)
    except Form.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = FormSerializer(form)
        return JsonResponse(serializer.data, status=201)

    elif request.method == "PUT":
        data = JSONParser().parse(form)
        serializer = FormSerializer(form, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        form.delete()
        return HttpResponse(status=204)

