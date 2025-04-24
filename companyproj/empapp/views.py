from django.shortcuts import render
from .utils import add_once
from .models import Employee
from django.http import HttpResponseRedirect
# Create your views here.
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect("/show_employees/")
    
def edit_employee(request, id):
    try:
        x = Employee.objects.get(id=id)
    except Exception:
        x = None
    data={
        "record": x,
    }
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("Name")
        extension = request.POST.get("Extension")
        email = request.POST.get("Email")
        title = request.POST.get("Title")
        salary = request.POST.get("Salary")
        dob = request.POST.get("DOB")
        hire_date = request.POST.get("hire_date")

        Employee.objects.filter(id=id).update(
                name=name,
                extension=extension,
                email=email,
                title=title,
                salary=salary,
                DOB=dob,
                hire_date=hire_date
            )
        return render(request, "edit_employee.html", context={"msg": "Employee updated successfully"})
    return render(request, "edit_employee.html", context=data)
def add_employee(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("Name")
        extension = request.POST.get("Extension")
        email = request.POST.get("Email")
        title = request.POST.get("Title")
        salary = request.POST.get("Salary")
        dob = request.POST.get("DOB")
        hire_date = request.POST.get("hire_date")

        Employee.objects.create(
                id=id,
                name=name,
                extension=extension,
                email=email,
                title=title,
                salary=salary,
                DOB=dob,
                hire_date=hire_date
            )
        return render(request, "add_employee.html", context={"msg": "Employee added successfully"})
    return render(request, "add_employee.html")
def index_view(request):
    data={}

    return render(request, "index_view.html", context=data)

def show_employees(request):
    employees = Employee.objects.all()
    return render(request, "show_employees.html", context={'employees': employees})

def employee_record(request, id):
    try:
        x = Employee.objects.get(id=id)
    except Exception:
        x = None
    data={
        "record": x,
    }
    return render(request, "employee_record.html", context=data)

def employee_stat(request):
    employees = Employee.objects.all()
    data = {}
    salaries = []
    for x in employees:
        salaries.append(x.salary)
    

    data["no_employees"] = len(salaries)
    data["avg_salary"] = sum(salaries)/len(salaries)
    data["min_salary"] = min(salaries)
    data["max_salary"] = max(salaries)
    
    return render(request, "employee_stat.html", context=data)