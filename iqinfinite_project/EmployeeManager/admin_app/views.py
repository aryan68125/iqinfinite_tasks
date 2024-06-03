from django.shortcuts import render,redirect

# Create your views here.
def manage_users_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_app/manage_users_page.html')
        else:
            return redirect('LoginPage')
    else:
        return redirect('LoginPage')
    
def assign_users_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_app/admin_assign_user.html')
        else:
            return redirect('LoginPage')
    else:
        return redirect('LoginPage')
    
def manage_tasks_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_app/manage_tasks_page.html')
        else:
            return redirect('LoginPage')
    else:
        return redirect('LoginPage')
    
def admin_settings_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_app/admin_settings_page.html')
        else:
            return redirect('LoginPage')
    else:
        return redirect('LoginPage')