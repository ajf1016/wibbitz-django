import json

from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse
from web.models import Subscribe,Customer,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog,Contact
from web.forms import ContactForm


def index(request):
    customers = Customer.objects.all()
    latest_customers = Customer.objects.all()[:4]
    features = Feature.objects.all()
    video_blog = VideoBlog.objects.all()
    testimonial = Testimonial.objects.all()
    making_feature = MarketingFeature.objects.all()
    product = Product.objects.all()
    blog = Blog.objects.all()
    
    form = ContactForm()
    
    context = {
        "customers": customers,
        "features": features,
        "video_blog" : video_blog,
        "testimonial": testimonial,
        "making_feature": making_feature,
        "products": product,
        "blog" : blog,
        "form" : form,
        "latest_customers" : latest_customers
    }
    
    return render(request,"index.html",context=context)

def subscribe(request):
    data = request.POST.get("email")
    
    if not Subscribe.objects.filter(email=data).exists():
        Subscribe.objects.create(
            email=data
        )
        
        response_data = {
            "status" : "success",
            "title" : "Succesfully Subscribed",
            "message" : "You are subscribed our newsletter Successfully"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You already Subscribed",
            "message" : "You are a Member"
        }
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")

def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        
        response_data = {
            "status" : "success",
            "title" : "Succesfully Subscribed",
            "message" : "You are subscribed our newsletter Successfully"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You already Subscribed",
            "message" : "You are a Member"
        }
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")


def product(request,pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    customers = Customer.objects.filter(product=product)
    context = {
        "product" : product
    }
    return render(request,"product.html",context=context)