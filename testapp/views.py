from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        fullname = firstname + ' ' + lastname
        return render(request,'home.html',{'fname':fullname})
    return render(request, 'home.html', )
