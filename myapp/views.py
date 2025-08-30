from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from . form import userinfoform

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Hello world!')

def success(request):
    return render(request, 'success.html')

def login(request):
    if request.method =='POST':
        form = userinfoform(request.POST)
        print("Form submited!")

        if form.is_valid():
            print("form is valid!")
            # print("cleaned data:", form.cleaned_data)
            
            try: 
                user_data = form.save()
                print(f"Data saved! ID: {user_data.id}")
                return redirect('success')
            except Exception as e:
                print(f"Database Error:{e}")

        else:
            print("Form error:", form.errors)

    else: 
        form=userinfoform()

    return render(request, 'login.html',{'form':form})




