from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import URLForm,UserCreateForm
from .models import URL
from django.core.paginator import Paginator

# views for homepage
def homepage(request):
    return render(request,'homepage.html')

# views for Signup
def signup(request):
    if request.method =='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signinpage')
    else:
        form=UserCreateForm()
    return render(request,'signup.html',{'form':form})

# views for Signin
def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('homepage')
    else:
        form=AuthenticationForm()
    return render(request,'signin.html',{'form':form})

# views for Signout
@login_required(login_url='signinpage')
def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
    return render(request,'signout.html',{'user':request.user})

# views for AddURL
@login_required
def addurl(request):
    if request.method == "POST":
        form = URLForm(request.POST, user=request.user)
        # Count only the URLs added by the current user
        bookmark_count = URL.objects.filter(user=request.user).count()
        if bookmark_count >= 5:
            return render(request, 'count-url.html', {'message': 'I regret to inform you that the bookmark limit has been exceeded. You are only allowed to add a maximum of five URLs.'})  # Display an error page
        if form.is_valid():
            form.save()
            return redirect('addurlpage')
    else:
        form = URLForm()
    return render(request, 'add-url.html', {'form': form})
        
# views for ListURL        
@login_required(login_url='signinpage')
def listurl(request):
    lists = URL.objects.filter(user=request.user)
    # pagination
    paginator = Paginator(lists, 2)  # Set the number of items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list-url.html', {'page_obj': page_obj})

# views for editURL
@login_required(login_url='signinpage')
def editurl(request, id):
    geturl = URL.objects.get(pk=id)
    if request.method == 'POST':
        form = URLForm(request.POST, instance=geturl, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('listurlpage')
    else:
        form = URLForm(instance=geturl, user=request.user)
    return render(request, 'edit-url.html', {'form': form})

# views for DeleteURL
@login_required(login_url='signinpage')
def deleteurl(request, id):
    geturl = URL.objects.get(pk=id)
    if request.method == 'POST':
        geturl.delete()
        return redirect('listurlpage')
    context = {'geturl': geturl}
    return render(request, 'lists.html', context)




