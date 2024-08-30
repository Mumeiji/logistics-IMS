from django.shortcuts import render

def admin_homepage(request):
    return render(request, 'Admin_Home.html')

def add_inventory(request):
    return render(request, 'Add_Inv.html')

def depreciated_inventory(request):
    return render(request, 'Depreciated_Inv.html')

def depinv_classroom(request):
    return render(request, 'DepInv_Classroom.html')

def depinv_office(request):
    return render(request, 'DepInv_Office.html')

def depinv_library(request):
    return render(request, 'DepInv_Library.html')

def depinv_clinic(request):
    return render(request, 'DepInv_Clinic.html')

def purchase_request(request):
    return render(request, 'Purchase_Req.html')

def evaluation_request(request):
    return render(request, 'Eval_Req.html')

def add_supplier(request):
    return render(request, 'Add_Supplier.html')

def supplier_list(request):
    return render(request, 'Supplier_List.html')

def equipment_maintenance(request):
    return render(request, 'Equip_Maintenance.html')

def archive(request):
    return render(request, 'Archive.html')