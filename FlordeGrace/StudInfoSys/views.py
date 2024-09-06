from django.shortcuts import render

def admin_homepage(request):
    return render(request, 'Admin_Home.html')

def add_inventory(request):
    return render(request, 'Add_Inv.html')

def depreciated_inventory(request):
    return render(request, 'Depreciated_Inv.html')

def depart_inv(request):
    return render(request, 'Depart_Inv.html')

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

def archived_inventory(request):
    return render(request, 'Archived_Inv.html')

def archived_suppliers(request):
    return render(request, 'Archived_Suppliers.html')