from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .form import employeeForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})

def add_employee(request):
    form = employeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/form.html', {'form': form})

def edit_employee(request, id):
    employee= get_object_or_404(Employee, id=id)
    form = employeeForm(request.POST or None, instance=employee)
    if form.is_valid(): 
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/form.html', {'form': form, 'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/confirm_delete.html', {'employee': employee})