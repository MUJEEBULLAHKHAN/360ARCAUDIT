from django import forms
from django.forms import widgets
from .models import *

CHOICES=[('Yes/نعم','Yes/نعم'),
         ('No/لا','No/لا')]
class arcinfoForm(forms.ModelForm):
    company = forms.CharField(label='Company Name :/اسم الشركة')
    owner = forms.CharField(label='Owner Name/اسم المالك')
    contact = forms.CharField(label='Owner Contact :/رقم التواصل بالمالك')
    manager = forms.CharField(label='Manager Name :/اسم المدير')
    managercont = forms.CharField(label='Manager contacts /رقم التواصل بالمدير')
    estimate = forms.ChoiceField(choices=CHOICES,label='Computerized Estimating program :/هل يوجد برنامج تقدير محوسب', widget=forms.RadioSelect())
    # wi1 = forms.ImageField(label='Workshop Image1')
    # wi2 = forms.ImageField(label='Workshop Image2')
    # wi3 = forms.ImageField(label='Workshop Image3')
    # wi4 = forms.ImageField(label='Workshop Image4')
    # wi5 = forms.ImageField(label='Workshop Image5')
    # wi6 = forms.ImageField(label='Workshop Image6')
    class Meta:
        model = arcinfo
        fields = '__all__'

class arclocForm(forms.ModelForm):
    address = forms.CharField(label='address عنوان')
    class Meta:
        model = arcloc
        fields = '__all__'

class financialForm(forms.ModelForm):
    labor = forms.CharField(label='Labor Sales / Month /مبيعات اجور اليد / شهريا')
    part = forms.CharField(label='Parts Sales / Month /مبيعات قطع الغيار / شهريا')
    material = forms.CharField(label='Material Sales / Month /مبيعات المواد / شهريا')
    rent = forms.CharField(label='Rent /Month / الإيجار / شهريا')
    productive = forms.CharField(label='Staff Cost /Month Productive :/تكلفة العمالة / شهريا')
    support = forms.CharField(label='Staff Cost /Month Support:/ تكلفة الاداريين / شهريا')
    month = forms.CharField(label='Other Expenses / Month:/مصاريف أخرى / شهريا')
    class Meta:
        model = financial
        fields = '__all__'


class workforceinfoForm(forms.ModelForm):
    PPE = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Staff provided with PPE: /معدات الوقاية الشخصية ')
    denter = forms.CharField(label='Number of Denters :/عدد السمكرية :')
    painter = forms.CharField(label='Number of Painters :/عدد الدهانيين :')
    elec = forms.CharField(label='Number of Mechanic/Elec :/عدد الميكانيكية - الكهربائية ')
    staff = forms.CharField(label='Number of Support staff:/عدد موظفي الادارة')
    workbays = forms.CharField(label='Number of workbays :/عدد اماكن العمل داخل الورشة - الطاقة الاستيعابية للورشة:')
    body = forms.CharField(label='Number of Jobs / Month Bodyshop only :/انتاجية الورشة في ما يخص السمكرة و الدهان - شهريا')
    nonbody = forms.CharField(label='Number of Jobs / Month Non bodyshop only :/ انتاجية الورشة اعمال غير السمكرة و الدهان - شهريا:')
    sqm = forms.CharField(label='Workshop Size Sqm :/ مساحة الورشة - متر مربع:')
    insurance = forms.CharField(label='WP - Insurance % :/% نسبة العمل مع شركات التأمين')
    walkin = forms.CharField(label='WP - Walk-in % :/ % نسبة العمل مع العملاء الكاش - النقدي')
    fleet = forms.CharField(label='WP - Fleet % :/% شركات التي تمتلك اساطيل- شركات تاجير و وغيرها')
    park = forms.CharField(label='Number of Customer Parking :/ عدد مواقف السيارات للعملاء')
    recep = forms.CharField(label='Adequate Reception :/مكتب استقبال مناسب')
    wash = forms.CharField(label='Adequate Washroom - Customers:/ حمام مناسب - للعملاء')
    washstaff = forms.CharField(label='Adequate Washroom - Staff :/حمام مناسب - طاقم عمل')
    scrap = forms.CharField(label='Scrap storage :/منطقة تخزين الاسكراب')
    newpart = forms.CharField(label='New parts Storage :/منطقة تخزين قطع غيار جديدة')
    oilstorage = forms.CharField(label='Used Oil Storage :/منطقة تخزين الزيوت المستعملة')
    class Meta:
        model = workforceinfo
        fields = '__all__'


class repairinfoForm(forms.ModelForm):
    measure = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Estimates with 3D Measurement :/ نظام قياس ثلاثي الابعاد :')
    nonstruct = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Body repair - Non Structural Repairs :/ إصلاح الجسم - الإصلاحات غير الهيكلية ')
    struct = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Body repair - Structural Repairs :/ إصلاح الجسم - الإصلاحات الهيكلية :')
    paint = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Refinishing - Paint - Full :/ خدمات الدهان كاملة:')
    ac = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='General Electric Service / AC :/: خدمات الكهرباء و التكيف')
    body = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Aluminum Body Repair :/ إصلاح الألومنيوم :')
    qc = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='QC Report with 3D measurement :/: تقرير مراقبة الجودة مع قياسات ثلاثية الابعاد')
    brakes = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='General Repairs - Brakes/Suspension :/ الإصلاحات العامة - الفرامل / نظام التعليق :')
    tyre = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Tire Service :/خدمة الإطارات ')
    wheel = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Wheel Alignment :/وزن الاذرعة :')
    computer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Computer Diagnostic / Calibration/Repairs:/التشخيص / المعايرة الحاسوبية :')
    adas = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='ADAS (Advance Driver Assistance System) :/ اصلاح نظام الامان و مساعدة السائق :')
    engine = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Engine / Drive train Overhaul :/إصلاح المحرك / لرفع المحرك و نقله :')
    plastic = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Plastic Parts Repair :/إصلاح الأجزاء البلاستيكية :')
    welder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Plastic Repair Tools- Hot Stapler, Hot Air Welder, Plastic Brazing:/أدوات إصلاح البلاستيك - دباسة ساخنة ، آلة لحام بالهواء الساخن ، لحام بلاستيك :')
    class Meta:
        model = repairinfo
        fields = '__all__'

class equipinfoForm(forms.ModelForm):
    it = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="IT system for Managing Workshop :/نظام حاسوبي لإدارة الورشة ")
    comp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Computerized Estimation system :/نظام تقدير حاسوبي")
    access = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to vehicle measurement DATA sheet :/هل يوجد صلاحية للدخول لمعلومات قياسات السيارات من الشركات العالمية (شاصيه)")
    oem = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to OEM Repair Manuals (OEM) :/ الوصول إلى كتيبات إصلاح OEM")
    guide = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to OEM Labor time Guide (OEM) :/الوصول إلى دليل وقت عمل OEM")
    lift = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Two Post Lifts :/ رافعة بعامودين")
    frame = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Frame / Unibody structure alignment system :/ نظام اصلاح الشاصي")
    four = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="FOUR point anchoring system - Unibody :/ نظام إرساء ذو أربع نقاط- قطعة واحدة")
    anchor = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="FOUR point anchoring system - Frame :/نظام إرساء ذو أربع نقاط / إطار")
    ton = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="10 ton Pulling system :/ نظام سحب 10 طن")
    oxy = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Oxy/Acetylene Welding Equipment :/معدات لحام الأكسجين / الأسيتيلين")
    resistance = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Resistance / Spot Welding Equipment :/معدات لحام بتقنيةمقاومة المغنطه")
    heater = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Induction Heater :/ سخان الحث")
    plasma = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Plasma cutter :/ قاطعه بتقنية البلازما")
    mig = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="MIG welder Steel :/ لحام مخصص للفولاذ")
    dent = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Dent Puller - Steel :/ دنت بولير - فولاذ")
    air = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Air compressor :/ ضاغط الهواء")
    chain = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Chain Block / Port-A-Power:/سلسلة السحب")
    charging = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="AC Charging / Recovery Equipment :/ معدات شحن الفريون/ استعادة التيار المتردد")
    kit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Denter Tools KIT :/ مجموعة أدوات السمكرة")
    dry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Dry Sanding Equipment :/ معدات الصنفرة الجافة")
    hvlp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="HVLP Spray Guns :/مسدسات الرش HVLP")
    vet = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wet/Dry Vacuum Machines :/ ماكينات تنظيف جاف / رطب")
    booth = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Paint Booth :/ فرن لرش السيارات")
    prep = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Prep Station :/محطة تجهييز المركبة")
    mixing = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Paint Mixing Room fully equipped :/ غرفة خلط الدهان مجهزة بالكامل")
    tools = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Painter Tools Kit :/ طقم أدوات الرش")
    toolkit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Electrician Tool Kit :/ طقم أدوات كهربائية")
    lifts = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Four Post Lifts - for Wheel Alignment :/ رافعات عامودية - لوزن الاذرعة")
    align = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wheel Aligning Equipment :/ جهاز وزن الاذرعه")
    rise = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Low Rise Lift :/ رافعة منخفضة الارتفاع")
    changer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Tire Changer :/ مغير الاطارات")
    balancer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wheel Balancer :/ ترصيص الكفرات")
    lathe = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Brake Lathe :/ مخرطة الفرامل")
    notes = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Notes : Recommendation for Betterment in tools/service etc. /.ملاحظات : توصية لتحسين الأدوات/ الخدمات وما إلى ذلك")
    class Meta:
        model = equipinfo
        fields = '__all__'

# class invoice_data_form(forms.ModelForm):
#     class Meta:
#         model = arcinfo
#         fields = '__all__'
#         widgets = {
#                     "estimate" : forms.RadioSelect(attrs={'class' : 'form-control'}),
#                     "terms" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "sales_man" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_ref" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_id" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_address" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_city" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_contact_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_contact_tel" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_postal_code" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "customer_vat_number" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_id" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_address" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_city" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_contact_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_contact_tel" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_postal_code" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_vat_number" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "seller_IBAN" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "vehicle_make" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "vehicle_model" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "vehicle_model_year" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "vehicle_plate_info" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "vehicle_vin" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "claim_number" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "insurance_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "assessor_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                   }

# class line_items_form(forms.ModelForm):
#     class Meta:
#         model = line_items
#         fields = ["item_code","item_name","pack","quantity","unit_price","taxable_amount","discount","tax_rate","tax_amount","item_sub_total_including_vat"]
#         widgets = {
#                     "item_code" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "item_name" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "pack" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "quantity" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "unit_price" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "taxable_amount" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "discount" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "tax_rate" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "tax_amount" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "item_sub_total_including_vat" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     }

# class item_cal_form(forms.ModelForm):
#     class Meta:
#         model = item_cal
#         fields = ["cal_id","total_excluding_vat","total_discount","total_taxable_amount_excluding_vat","net_excluding_VAT","total_vat_15perc","net_amount","excess_amount_plus_VAT","deprecation_amount_plus_VAT","total_amount_due","remarks"]
#         widgets = {
#                     "total_excluding_vat" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "total_discount" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "total_taxable_amount_excluding_vat" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "net_excluding_VAT" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "total_vat_15perc" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "net_amount" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "excess_amount_plus_VAT" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "deprecation_amount_plus_VAT" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "total_amount_due" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     "remarks" : forms.TextInput(attrs={'class' : 'form-control'}),
#                     }

# class contacts_form(forms.ModelForm):
#     class Meta:
#         model = contacts
#         fields = ['c_name','c_phone','c_mail','c_category','c_description']
#         widgets = {
#             'c_name' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'c_phone' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'c_mail' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'c_category' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'c_description' : forms.Textarea(attrs={'class' : 'form-control'}),
#         }


# class L2_form(forms.ModelForm):
#     class Meta:
#         model = L2
#         fields = ["license_id","license_key"]
#         widgets = {
#             'license_key' : forms.TextInput(attrs={'class' : 'form-control'})    
#         }
