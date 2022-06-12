from django.shortcuts import render,redirect
from . models import User,Home

# Create your views here.
def singup(request):
    if request.method == 'POST':
        v_frist_name = request.POST.get('frist_name')
        v_last_name = request.POST.get('last_name')
        v_email = request.POST.get('email')
        v_password = request.POST.get('password')
        if v_frist_name != '' and v_last_name != ''and v_email!= '' and v_password != '':
            try:
                User.objects.create(m_frist_name=v_frist_name, m_last_name=v_last_name, m_email=v_email, m_password=v_password)
                return redirect('/login')
            except :
                error = ('Sorry to SING UP.!! You already had an account. Please login.')    
                return render(request,'blog_app/singup.html',{'error':error})

    return render(request,'blog_app/singup.html')


def login(request):
    if request.method == 'POST':
        lv_email = request.POST.get('email')
        lv_password = request.POST.get('password')
        context = {'login':User.objects.all()} 
        for i in context['login']:
            if lv_email == i.m_email and lv_password == i.m_password:
                return redirect('/home')

    return render(request,'blog_app/login.html')



def home(request):
    context = {'blog':Home.objects.all()}   

    if request.method == 'POST':
        v_title = request.POST.get('title')
        v_summary = request.POST.get('summary')
        v_categories = request.POST.get('categories')
        if v_title != ' ' and v_summary != ' ' and v_categories != ' ':
            Home.objects.create(m_title = v_title, m_summary = v_summary,m_categories = v_categories)
            return redirect('/home')

    return render(request,'blog_app/home.html',context)    


def web_development(request):
    context = {'web_development':Home.objects.filter(m_categories= 'web_development')}            
    return render(request,'blog_app/home.html',context)  


def blockchain_technology(request):
    context = {'blockchain_technology':Home.objects.filter(m_categories= 'blockchain_technology')}
    return render(request,'blog_app/home.html',context) 


def cryptocurrency(request):
    context = {'cryptocurrency':Home.objects.filter(m_categories= 'cryptocurrency')}
    return render(request,'blog_app/home.html',context)


