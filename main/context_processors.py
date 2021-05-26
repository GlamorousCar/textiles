from main.models import Category
from django.http import JsonResponse

def category(request):
    return {"categories": Category.objects.all()}
