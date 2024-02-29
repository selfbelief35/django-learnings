from django.shortcuts import render

def index(request):
    context_dict = {'text':'Hello World', 'number':100}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_path.html')


# Create your views here.
