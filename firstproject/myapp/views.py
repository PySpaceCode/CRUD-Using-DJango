from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Name,Customer_Detail,Blog
# Create your views here.
def hello(request):
    return HttpResponse("<h1>This is my first view</h1>")
def static(request):
    return render(request,"myapp/static.html")
"""Blog content """
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')

        # Create a new blog entry
        blog = Blog(title=title, content=content, image=image)
        blog.save()

        return HttpResponse("<h1>Blog have been created</h1>")  # Assuming you have a view named 'blog_list'

    return render(request, 'myapp/create_blog.html')


def index(request):
    d1={
        "name":"Adarsh tiwari",
        "age":21,
        "Address":"Lucknow"
    }
    resp=render(request,"myapp/index.html",context=d1)
    return resp
def test(request):
    if request.method=="get":
        return render(request,"myapp/test.html")
    elif request.method=="POST":
        name=request.POST.get("n","N/A")
        d1={"name":name}
        return render(request,"myapp/test.html",context=d1)
    return render(request,"myapp/test.html")

def add(request):
    if request.method=="GET":
        d1={"msg":"Get method have been used"}
        return render(request,"myapp/ad.html",context=d1)
    elif request.method=="POST":
        # a=request.POST.get("n1","N/A")
        # b=request.POST.get("n2","N/A")
        a=int(request.POST.get("n1",0))
        b=int(request.POST.get("n2",0))
        sum=a+b
        d2={'sum':sum}
        #d1={"msg":"This is post method"}
        return render(request,"myapp/ad.html",context=d2)
    # d2={"msg":"No method will be run"}
    return render(request,"myapp/ad.html")

def contact(request):
    resp=render(request,"myapp/contact.html")
    return resp
def about(request):
    resp=render(request,"myapp/about.html")
    return resp
def calc(request):
    if request.method=="GET":
        return render(request,"myapp/calc.html")
    elif request.method=="POST":
        if "btn_add" in request.POST:
            a=int(request.POST.get("n1",0))
            b=int(request.POST.get("n2",0))
            s=a+b
            d={'s':s}
            return render(request,"myapp/calc.html",context=d)
        elif "btn_sub" in request.POST:
            a=int(request.POST.get("n1",0))
            b=int(request.POST.get("n2",0))
            s=a-b
            d={'s':s}
            return render(request,"myapp/calc.html",context=d)
        elif "btn_mul" in request.POST:
            a=int(request.POST.get("n1",0))
            b=int(request.POST.get("n2",0))
            s=a*b
            d={'s':s}
            return render(request,"myapp/calc.html",context=d)
        elif "btn_div" in request.POST:
            a=int(request.POST.get("n1",0))
            b=int(request.POST.get("n2",0))
            s=a/b
            d={'s':s}
            return render(request,"myapp/calc.html",context=d)

        #return HttpResponse("<h1>Welcoe user</h1>")
    return render(request,"myapp/calc.html")

def form(request):
    if request.method=="GET":
        return render(request,"myapp/form.html")
    elif request.method=="POST":
      if "btn_insert" in request.POST:
        ob=Name()
        ob.name=request.POST.get("Name","N/A")
        ob.number=int(request.POST.get("Number","N/A"))
        ob.save()
        return render(request,"myapp/form.html")
      elif "btn_show" in request.POST:
          cus=Name.objects.all()
          d1={"cus":cus}
          return render(request,"myapp/form.html",context=d1)
    resp=render(request,"myapp/form.html")
    return resp
def customer_detail(request):
    if request.method=="GET":
        return render(request,"myapp/customer.html")
    elif request.method=="POST":
        if "btn_insert" in request.POST:
            c=Customer_Detail()
          #  c.cid
            c.cname=request.POST.get("cname","N/A")
            c.clname=request.POST.get("clname","N/A")
            c.cadd=request.POST.get("address","N/A")
            c.phone=int(request.POST.get("cphone",0))
            c.salary=float(request.POST.get("csalary",0))
            c.save()
            d1={'msg':"User have been created "}
            return render(request,"myapp/customer.html",context=d1)
        elif "btn_show" in request.POST:
            cus=Customer_Detail.objects.all()
            d1={'cus':cus}
            return render(request,"myapp/customer.html",context=d1)
        elif "btn_update" in request.POST:
            c=Customer_Detail()
            c.id=int(request.POST.get("txtid",0))
            if Customer_Detail.objects.filter(id=c.id).exists():
                  c.cname=request.POST.get("cname","N/A")
                  c.clname=request.POST.get("clname","N/A")
                  c.cadd=request.POST.get("address","N/A")
                  c.phone=int(request.POST.get("cphone",0))
                  c.salary=float(request.POST.get("csalary",0))
                  c.save()
                  return render(request,"myapp/customer.html")
        elif "btn_delete" in request.POST:
            c=Customer_Detail()
            c.id=int(request.POST.get("txtid",0))
            cd=Customer_Detail.objects.filter(id=c.id).delete()
            return render(request,"myapp/customer.html")

    return render(request,"myapp/customer.html")