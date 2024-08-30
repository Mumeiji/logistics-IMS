from django.urls import path
from . import views

# URL CONFIGURATION
urlpatterns = [
    path('', views.admin_homepage),
    path('Add_Inv.html', views.add_inventory),
    path('Depreciated_Inv.html', views.depreciated_inventory),
    path('DepInv_Classroom.html', views.depinv_classroom),
    path('DepInv_Office.html', views.depinv_office),
    path('DepInv_Library.html', views.depinv_library),
    path('DepInv_Clinic.html', views.depinv_clinic),
    path('Purchase_Req.html', views.purchase_request),
    path('Eval_Req.html', views.evaluation_request),
    path('Add_Supplier.html', views.add_supplier),
    path('Supplier_List.html', views.supplier_list),
    path('Equip_Maintenance.html', views.equipment_maintenance),
    path('Archive.html', views.archive),
]
