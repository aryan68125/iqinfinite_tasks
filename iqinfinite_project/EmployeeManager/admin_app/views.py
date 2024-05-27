from django.shortcuts import render,redirect

# Create your views here.
def admin_dashboard_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_app/admin_dashboard_page.html')
        else:
            return redirect('LoginPage')
    else:
        return redirect('LoginPage')