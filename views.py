from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hi Good Evening to All.....")


def htmltag(req):
	return HttpResponse("<h2>welcome to  new internship in html</h2>")


def usernameprint(request,uname):
	return HttpResponse("<h2>Hi welcome to <span style= 'color:green'>{}</span</h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:centre'> hi user<span style='color:yellow'>{}</span> and your age is: <span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('hi welcome {}')</script><h3>hi welcome {} and your age is: {} and your id is: {}</h3>".format(ename,ename,eage,eid))


def html(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def employ(request,id,name):
	k={'i':id, 'n':name}
	return render(request,'html/employ.html',k)

def employ01(request,id,name):
	k={'i':id, 'n':name}
	return render(request,'html/employ01.html',k)

def studentdetails(request):
	return render(request,'html/std.html')	


def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname=req.POST['uname']
		rollno=req.POST['rollno']
		email=req.POST.get('email')
		#print(uname,rollno,email)
		data={'username':uname,'rno':rollno,'emailid':email}
		return render(req,'html/display.html',data)
	return render(req,'html/myform.html')

def registration(req):
	if req.method=="POST":
		#print(req.POST)
		fname=req.POST['firstname']
		lname=req.POST['lastname']
		gender=req.POST.get('gender')
		phno=req.POST['phonenumber']
		address=req.POST['address']
		lang=req.POST.get('languageknown')
		email=req.POST.get('email')
		#print(firstname,lastname,gender,phonenumber,address,languagesknown,email)
		data={'firstname':fname,'lastname':lname,'gender':gender,'phonenumber':phno,'address':address,'languagesknown':lang,'email':email}
		return render(req,'html/registration display.html',data)
	return render(req,'html/registration.html')


def loginpage(req):
	if req.method=="POST":
		#print(req.POST)
		email=req.POST.get('email')
		password=req.POST.get('password')
		#print(uname,rollno,email)
		data={'email':email,'password':password,}
		return render(req,'html/login display.html',data)
	return render(req,'html/loginpage.html')

def bootstarpfun(request):
	return render(request,'html/sampleboot.html')

def newreg(req):
	if req.method=="POST":
		#print(req.POST)
		fname=req.POST['firstname']
		lname=req.POST['lastname']
		gender=req.POST.get('gender')
		phno=req.POST['phonenumber']
		address=req.POST['address']
		lang=req.POST.get('languageknown')
		email=req.POST.get('email')
		#print(firstname,lastname,gender,phonenumber,address,languagesknown,email)
		data={'firstname':fname,'lastname':lname,'gender':gender,'phonenumber':phno,'address':address,'languagesknown':lang,'email':email}
		return render(req,'html/registration display.html',data)
	return render(req,'html/newreg.html')


def newlog(req):
	if req.method=="POST":
		#print(req.POST)
		email=req.POST.get('email')
		password=req.POST.get('password')
		#print(uname,rollno,email)
		data={'email':email,'password':password,}
		return render(req,'html/login display.html',data)
	return render(req,'html/newlog.html')


def btregst(request):
	return render(request,'html/btregst.html')

def sandeep(request):
	return render(request,'html/sandeep.html')

def register1(req):
	# name="sandep"
	# email="sandeep@gmail.com"
	reg=Register(name="sandeeep",email="sandeep@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully!")

def register2(req):
	if req.method=="POST":
		name= req.POST['name']
		email=req.POST['email']
		reg=Register(name= name, email= email)
		reg.save()
		return HttpResponse("Record inserted sucessfully......")
	return render(req,"html/register2.html")


def display(req):
	data= Register.objects.all()
	return render(req,'html/display2.html',{'data':data})

def sview(request,y):
	w=Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	# return HttpResponse("Your name is: {} and your email id is: {}".format(w.name,w.email))


def supt(request,q):
	t=Register.objects.get(id=q)
	if request.method=="POST":
		na=request.POST['n']
		em=request.POST['e']
		t.name=na
		t.email=em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b=Register.objects.get(id=p)
	if request.method=="POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'z':b})


