from django.shortcuts import render, redirect

LANGS = (
    'Python',
    'JAVA',
    'MERN',
)
LOCATIONS = (
    'Online',  
    'Chicago',
    'Seattle',
)

def index(request):
    return render(request, 'survey.html')

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['lang'] = request.POST['lang']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'result.html')