from django.shortcuts import render

# Create your views here.
from django.shortcuts import render  
from .forms import *  
  
def index(request):  
    fm = arcinfoForm()
    cm = arclocForm()
    fn = financialForm()
    wo = workforceinfoForm()
    re = repairinfoForm()
    eq = equipinfoForm()
    if request.method == 'POST':
        fm = arcinfoForm(request.POST,request.FILES)
        cm = arclocForm(request.POST)
        fn = financialForm(request.POST)
        wo = workforceinfoForm(request.POST)
        re = repairinfoForm(request.POST)
        eq = equipinfoForm(request.POST)
        if fm.is_valid() and cm.is_valid():
            # a = fm.cleaned_data['company']
            # b = fm.cleaned_data['owner']
            # c = fm.cleaned_data['contact']
            # d = fm.cleaned_data['manager']
            # e = fm.cleaned_data['managercont']
            # f = fm.cleaned_data['estimate']
            # reg = arcinfo(company=a,owner=b,contact=c,manager=d,managercont=e,estimate=f)
            fm.save()
            cm.save()
            fn.save()
            wo.save()
            re.save()
            eq.save()
            fm = arcinfoForm()
            cm = arclocForm()
            fn = financialForm()
            wo = workforceinfoForm()
            re = repairinfoForm()
            eq = equipinfoForm()
    return render(request,"index.html",{'form':fm,'corm':cm,'forn':fn,'worm':wo,'rorm':re,'qorm':eq})  

# def index(request):
#  if request.method == 'POST':
#   fm = OrderCreateForm(request.POST)
#   if fm.is_valid():
#             inv_1 = fm.cleaned_data['invoice_number']
#             inv_2 = fm.cleaned_data['terms']
#             inv_3 = fm.cleaned_data['sales_man']
#             inv_4 = fm.cleaned_data['customer_ref']
#             inv_5 = fm.cleaned_data['customer_id']
#             inv_6 = fm.cleaned_data['customer_name']
#             inv_7 = fm.cleaned_data['customer_address']
#             inv_8 = fm.cleaned_data['customer_city']
#             inv_9 = fm.cleaned_data['customer_contact_name']
#             inv_10 = fm.cleaned_data['customer_contact_tel']
#             inv_11 = fm.cleaned_data['customer_postal_code']
#             inv_12 = fm.cleaned_data['customer_vat_number']
#             inv_13 = fm.cleaned_data['seller_id']
#             inv_14 = fm.cleaned_data['seller_name']
#             inv_15 = fm.cleaned_data['seller_address']
#             inv_16 = fm.cleaned_data['seller_city']
#             inv_17 = fm.cleaned_data['seller_contact_name']
#             inv_18 = fm.cleaned_data['seller_contact_tel']
#             inv_19 = fm.cleaned_data['seller_postal_code']
#             inv_20 = fm.cleaned_data['seller_vat_number']
#             inv_21 = fm.cleaned_data['seller_IBAN']
#             inv_22 = fm.cleaned_data['vehicle_make']
#             inv_23 = fm.cleaned_data['vehicle_model']
#             inv_24 = fm.cleaned_data['vehicle_model_year']
#             inv_25 = fm.cleaned_data['vehicle_plate_info']
#             inv_26 = fm.cleaned_data['vehicle_vin']
#             inv_27 = fm.cleaned_data['claim_number']
#             inv_28 = fm.cleaned_data['insurance_name']
#             inv_29 = fm.cleaned_data['assessor_name']
#             reg = invoice_data(invoice_number=inv_1,terms=inv_2,sales_man=inv_3,customer_ref=inv_4,customer_id=inv_5,customer_name=inv_6,customer_address=inv_7,customer_city=inv_8,customer_contact_name=inv_9,customer_contact_tel=inv_10,customer_postal_code=inv_11,customer_vat_number=inv_12,seller_id=inv_13,seller_name=inv_14,seller_address=inv_15,seller_city=inv_16,seller_contact_name=inv_17,seller_contact_tel=inv_18,seller_postal_code=inv_19,seller_vat_number=inv_20,seller_IBAN=inv_21,vehicle_make=inv_22,vehicle_model=inv_23,vehicle_model_year=inv_24,vehicle_plate_info=inv_25,vehicle_vin=inv_26,claim_number=inv_27,insurance_name=inv_28,assessor_name=inv_29,user_id=user)
#             reg.save()
#             ag = invoice_data.objects.get(pk=reg.invoice_id)
#             # qr_data = f"Invoice_issue_date : {reg.date_time} \n invoice_number : {reg.invoice_number} \n insurance_info_name : {reg.insurance_info_name} \n insurance_info_claim_no : {reg.insurance_info_claim_no} \n insurance_info_assessor : {reg.insurance_info_assessor} \n make : {reg.make} \n model : {reg.model} \n vin : {reg.vin} \n plate_info : {reg.plate_info} \n bill_to_name : {reg.bill_to_name} \n bill_to_building_no : {reg.bill_to_building_no} \n bill_to_street_name : {reg.bill_to_street_name} \n bill_to_district : {reg.bill_to_disctrict} \n bill_to_city : {reg.bill_to_city} \n bill_to_country : {reg.bill_to_country} \n bill_to_postal_code : {reg.bill_to_postal_code} \n bill_to_additional_no : {reg.bill_to_additional_no} \n bill_to_vat_number : {reg.bill_to_vat_number} \n bill_to_other_seller_id : {reg.bill_to_other_seller_id} \n workshop_name : {reg.workshop_name} \n workshop_building_no : {reg.workshop_building_no} \n workshop_street_name : {reg.workshop_street_name} \n workshop_disctrict : {reg.workshop_disctrict} \n workshop_city : {reg.workshop_city} \n workshop_country : {reg.workshop_country} \n workshop_postal_code : {reg.workshop_postal_code} \n workshop_additional_no : {reg.workshop_additional_no} \n workshop_vat_number : {reg.workshop_vat_number} \n workshop_other_seller_id : {reg.workshop_other_seller_id}"  
#             # a = files.objects.create(url=qr_data,invoice=reg)
#             # print(a.qr_id)
#             # imgg = files.objects.get(pk=a.qr_id)
#             # return HttpResponseRedirect(f'/inv/{reg.invoice_id}',{'invoice_data':ag,'img':imgg})
#             return render(request, 'enroll/cong.html', {'invoice_data':ag})
#  else:
#   fm = invoice_data_form()
#  return render(request, 'enroll/addandshow.html', {'form':fm})
