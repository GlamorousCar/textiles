from .forms import ContactModelForm
from django.http import JsonResponse

def contact(request):

    form = ContactModelForm()

    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():

            form.save()
            return JsonResponse({
                'message': 'success'
            })

    return {'form': form}