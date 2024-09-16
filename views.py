from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request,"index.html",{})
def doctor(request):
    return render(request,"doctor.html",{})
def department_single(request):
    return render(request,"department-single.html",{})
def departments(request):
    return render(request,"departments.html",{})
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {"msg":"Submitted Contact Form"})
        return render(request, "contact.html", {"msg":"Not Submitted Contact Form"})
    return render(request, "contact.html", {})
def blog_single(request):
    return render(request,"blog-single.html",{})
def blog(request):
    return render(request,"blog.html",{})
def about(request):
    return render(request,"about.html",{})