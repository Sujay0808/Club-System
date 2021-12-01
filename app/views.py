from django.shortcuts import render
from django.contrib.admin import site
from django.forms.models import model_to_dict

# Create your views here.
def View(request, modelName="", primeKey=-1):
    context={
        'models_name': [],
        'modelName': modelName,
        'objects': None,
        'object': None,
        'objects_view': False,
        'object_view': False,
        'object_data': None,
    }
    for model, model_admin in site._registry.items():
        if model._meta.app_label == 'app':
            context['models_name'].append(model._meta.model_name)
    
    if modelName != '':
        context['objects_view'] = True
        context['object_view'] = False
        for model, model_admin in site._registry.items():
            if modelName == model._meta.model_name:
                if primeKey == -1:
                    context['objects'] = model.objects.all()
                else:
                    context['objects_view'] = False
                    context['object_view'] = True
                    context['object'] = model.objects.get(pk=primeKey)
                    context['object_data'] = model_to_dict(context['object']).items()
    return render(request, template_name='system_view.html', context=context)