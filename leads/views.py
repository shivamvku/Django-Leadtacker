from django.http import Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from.models import Registers,Joinings,Course_names


def index11(request):
    register = Registers.objects.all()
    context = {'register': register}
    return render(request, 'leads/index11.html', context)

def detail(request,register_id):
	try:
		registers = Registers.objects.get(pk=register_id)
	except Registers.DoesNotExist:
		raise Http404("please Register .................")
	return render(request,'leads/detail.html',{'registers':registers})

def registers(request):
	template=loader.get_template('leads/registers.html')
	all_courses=Course_names.objects.all()
	return render(request,'leads/registers.html',{'all_courses':all_courses})


def joinings(request):
	template=loader.get_template('leads/joinings.html')
	all_courses=Course_names.objects.all()
	return render(request,'leads/joinings.html',{'all_courses':all_courses})

def walkins(request):
	all_registers=Registers.objects.all()
	template=loader.get_template('leads/walkins.html')
	context={
	'all_registers':all_registers,
	}
	return render(request,'leads/walkins.html',context)
def currents(request):
	all_joinings=Joinings.objects.all()
	template=loader.get_template('leads/current.html')
	context={
	'all_joinings':all_joinings,
	}
	return render(request,'leads/current.html',context)
def callings(request):
	template=loader.get_template('leads/callings.html')
	return render(request,'leads/callings.html')

def counselling(request):
	all_courses=Course_names.objects.all()
	template=loader.get_template('leads/counselling.html')
	context={
	'all_courses':all_courses,
	}
	return render(request,'leads/counselling.html',context)

def create(request):
    registers = Registers(st_name=request.POST['name'],st_mobile=request.POST['mobile'],st_email=request.POST['email'],st_course=request.POST['course'],st_sourse=request.POST['source'],st_lead_status=request.POST['demo_call'],st_demo_date=request.POST['demo_date'],st_counsler=request.POST['counsler'],st_remarks=request.POST['remarks'])
    registers.save()
    return redirect('/leads')

def create1(request):
    joinings = Joinings(course=request.POST['course'],name=request.POST['name'],complection_date=request.POST['date_of_complected'],date_join=request.POST['date_of_joining'],course_fee=request.POST['course_fee'],instructor=request.POST['instructor'],aadhar_number=request.POST['aadhar_number'],mobile=request.POST['mobile'],email= request.POST['email'],remarks=request.POST['remarks'])
    joinings.save()
    return redirect('/current/curr1')

def edit(request, id):
    joining = Joinings.objects.get(id=id)
    context = {'joining': joining}
    return render(request, 'leads/edit.html', context)

def update(request, id):
    joining = Joinings.objects.get(id=id)
    joining.name = request.POST['name']
    joining.complection_date = request.POST['complection_date']
    joining.status = "Inprocess"
    joining.save()
    return redirect('/current/curr1/')

def complete(request, id):
    joining = Joinings.objects.get(id=id)
    joining.status = "completed"
    joining.save()
    return redirect('/students/st1')

def delete(request, id):
    joining = Joinings.objects.get(id=id)
    joining.status = "Discontinue"
    joining.save()
    return redirect('/students/st1')
#------------------------------curd - registers ---------------
def callings1(request):
	all_registers=Registers.objects.all()
	demo_call = request.POST['demo_call']
	demo_date = request.POST['demo_date']
	print(demo_date)
	context={
	'demo_call':demo_call,
	'demo_date':demo_date,
	'all_registers':all_registers,
	}
	return render(request, 'leads/callings1.html', context)

def counselling1(request):
	all_registers=Registers.objects.all()
	demo_date = request.POST['demo_date']
	course = request.POST['course']
	print(demo_date)
	context={
	'course':course,
	'demo_date':demo_date,
	'all_registers':all_registers,
	}
	return render(request, 'leads/counselling1.html', context)

def edit1(request, id):
    register = Registers.objects.get(id=id)
    context = {'register': register}
    return render(request, 'leads/willin.html', context)

def update1(request, id):
    register = Registers.objects.get(id=id)
    register.st_name = request.POST['name']
    register.st_demo_date = request.POST['willing_date']
    register.save()
    return redirect('/walk/walk1/')

def delete1(request, id):
    register = Registers.objects.get(id=id)
    register.delete()
    return redirect('/leads/')


def students(request):
	joinings = Joinings.objects.all()
	context = {
	'joinings': joinings,

	}
	template=loader.get_template('leads/students.html')
	return render(request,'leads/students.html',context)

def editre(request, id):
    joining = Joinings.objects.get(id=id)
    context = {'joining': joining}
    return render(request, 'leads/rejoin.html', context)

def updatere(request, id):
    joining = Joinings.objects.get(id=id)
    joining.name = request.POST['name']
    joining.date_join = request.POST['date_join']
    joining.status = "Rejoined/Inprocess"
    joining.save()
    return redirect('/students/st1/')


#---------------------------------------------------------------
