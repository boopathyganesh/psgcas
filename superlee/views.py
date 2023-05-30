from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import os
from django.views.decorators.csrf import csrf_exempt,csrf_protect,ensure_csrf_cookie
from django.middleware.csrf import get_token

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest,HttpResponseRedirect
from django.template import loader
import json,re
from django.core.serializers import serialize
import pandas as pd
from django.core.files.storage import FileSystemStorage
from .models import User_reg,intern_db,Intern_atn
from django.utils.datastructures import MultiValueDict
from django.template.loader import render_to_string
from .functions import handle_uploaded_file
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.writer.excel import save_workbook
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'superlee/media')
id=[]
'''data={
    'roll_no':'',
    'full_name':'',
    'current_pursuing':'',
    'current_department':'',
    'contact':'',
    'alternate_contact':'',
    'DOB':'',
    'gender':'',
    'marital_status':'',
    'fstrength':'',
    'famem':'',
    'mname':'',
    'mcontact':'',
    'moccupation':'',
    'fname':'',
    'fcontact':'',
    'foccupation':'',
    'sname':'',
    'scontact':'',
    'soccupation':'',
    'permanent_address':'',
    'current_address':'',
    'work_interest':'',
    'work_location':'',
    'sis':'',
    'why_placements':'',
    'about_yourself':'',
    'languages_known':'',
    'prog_languages':''
}'''


def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def dashboard(request):
    template=loader.get_template('dashboard.html')
    return HttpResponse(template.render())
def admin_dashboard(request):
    template=loader.get_template('admin/dashboard.html')
    return HttpResponse(template.render())

def vision(request):
    template=loader.get_template('vision.html')
    return HttpResponse(template.render())
def cdc_function(request):
    template=loader.get_template('function.html')
    return HttpResponse(template.render())
def cdc_function(request):
    template=loader.get_template('function.html')
    return HttpResponse(template.render())
def mission(request):
    template=loader.get_template('mission.html')
    return HttpResponse(template.render())

def p_process(request):
    template=loader.get_template('placementprocess.html')
    return HttpResponse(template.render())

def infrastructure(request):
    template=loader.get_template('infrastructure.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())

def companies(request):
    template=loader.get_template('companies.html')
    return HttpResponse(template.render())

"""def attendance(request):
    df = pd.read_excel('./superlee/static/data.xlsx')
    data = df.to_dict('records')
    #filtered_data = df.loc[df[drive] == 'Google']
    #data = filtered_data.to_dict('records')
    return render(request, 'attendance.html', {'data': data})
    #template=loader.get_template('attendance.html')
    #return HttpResponse(template.render())"""

def attendance(request):
    df = pd.read_excel('./superlee/static/data.xlsx')
    data = df.to_dict('records')

    if request.method == 'POST':
        ajax_data = json.loads(request.body)
        drive = ajax_data['drive']
        year = ajax_data['year']
        filtered_data = df.loc[df['drive_name'] == drive]
        #data = data.copy()  # make a copy of the original data dictionary
        #data.extend(filtered_data.to_dict('records'))  # update with filtered data
        data = filtered_data.to_dict('records')
        render(request, 'attendance.html', {'title': drive + year})
        return JsonResponse({'data': data})  # send back the updated data as a JSON response
    else:
        return render(request, 'attendance.html', {'data': data})

def input1(request):
    df = pd.read_excel('./superlee/static/eligible_list.xlsx')
    data = df.to_dict('records')
    '''if request.method == 'POST':
        ajax_data = json.loads(request.body)
        search = ajax_data['search']
        print(search)
        filtered_data = df.loc[df['Roll_Number'] == search]
        data = filtered_data.to_dict('records')
        return JsonResponse({'data': data})  # send back the updated data as a JSON response'''
    if request.method == 'POST':
        search_value = request.POST.get('search')
        search_value=search_value.upper()
        filtered_data = df.loc[df['Roll_Number'] == search_value]
        data = filtered_data.to_dict('records')
        tsg = '''
                                                <div class="form-check form-check-success m-1">
                                                  <label class="form-check-label">
                                                    <input type="checkbox" class="form-check-input">
                                                    Present
                                                  </label>
                                                </div>
                                                <div class="form-check form-check-danger m-1">
                                                  <label class="form-check-label">
                                                    <input type="checkbox" class="form-check-input">
                                                    Absent
                                                  </label>
                                                </div>
        '''
        return JsonResponse({'data': data,'tsg':tsg})  # send back the updated data as a JSON response
    else:
        tsg = '''
                                                <div class="form-check form-check-success m-1">
                                                  <label class="form-check-label">
                                                    <input type="checkbox" class="form-check-input">
                                                    Present
                                                  </label>
                                                </div>
                                                <div class="form-check form-check-danger m-1">
                                                  <label class="form-check-label">
                                                    <input type="checkbox" class="form-check-input">
                                                    Absent
                                                  </label>
                                                </div>

                '''
        return render(request, 'atn-input.html', {'data': data,'tsg':tsg})

def input(request):
    tsg = '''
                                                    <div class="form-group d-flex justify-content-center align-items-center mb-0">
                            <div class="form-check form-check-success">
                              <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="membershipRadios" id="membershipRadios1" value="" checked>
                                Present
                              </label>
                            </div>
                            <div class="form-check form-check-danger ml-5">
                              <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="membershipRadios" id="membershipRadios2" value="option2">
                                Absent
                              </label>
                            </div>
                        </div>
            '''
    df = pd.read_excel('./superlee/static/eligible_list.xlsx')
    data = df.to_dict('records')
    '''if request.method == 'POST':
        ajax_data = json.loads(request.body)
        search = ajax_data['search']
        print(search)
        filtered_data = df.loc[df['Roll_Number'] == search]
        data = filtered_data.to_dict('records')
        return JsonResponse({'data': data})  # send back the updated data as a JSON response'''
    if request.method == 'POST':
        search_value = request.POST.get('search')
        if search_value != '':
            search_value = search_value.upper()
            filtered_data = df.loc[df['Roll_Number'] == search_value]
            data = filtered_data.to_dict('records')
            return JsonResponse({'data': data, 'tsg': tsg})
        else:
            return JsonResponse({'data': data,'tsg':tsg})  # send back the updated data as a JSON response
    else:
        return render(request, 'atn-input.html', {'data': data,'tsg':tsg})
@ensure_csrf_cookie
def registration(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        if form_data.values != '':
            print(form_data)
            request.session['rollno']=form_data['rollno']
            request.session['full_name'] = form_data['full_name']
            request.session['current_pursuing'] = form_data['current_pursuing']
            request.session['department'] = form_data['department']
            request.session['con'] = form_data['con']
            request.session['email'] = form_data['email']
            request.session['altcon'] = form_data['altcon']
            request.session['aemail'] = form_data['aemail']
            request.session['gender'] = form_data['gender']
            request.session['marital-sts'] = form_data['marital-sts']
            # Return a JSON response indicating success
            return JsonResponse({'success': True}, content_type='application/json')
        else:
            print('error')
            return JsonResponse({'error': "Form Can't be Empty"}, status=401)
    else:
        template = loader.get_template('registration.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))

@ensure_csrf_cookie
def family_details(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        roll_number=request.session['rollno']
        print(roll_number)
        request.session['mname']  = form_data['mname'],
        request.session['mcontact'] = form_data['mcontact'],
        request.session['moccupation'] = form_data['moccupation'],
        request.session['fname'] = form_data['fname'],
        request.session['fcon'] = form_data['fcon'],
        request.session['foccupation'] = form_data['foccupation'],
        request.session['scount'] = form_data['scount'],
        request.session['permanent_address'] = form_data['permanent_address'],
        request.session['p_pincode'] = form_data['p_pincode'],
        request.session['current_address'] = form_data['current_address'],
        request.session['c_pincode']= form_data['c_pincode']
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')

    else:
        template = loader.get_template('family_details.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))

@ensure_csrf_cookie
def schoolings(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        roll_number = request.session['rollno']
        request.session['sslc_school'] = form_data['sslc_school'],
        request.session['sslc_school_address'] = form_data['sslc_school_address'],
        request.session['sslc_percentage'] = form_data['sslc_percentage'],
        request.session['sslc_year'] = form_data['sslc_year'],
        request.session['hsc_or_diploma'] = form_data['hsc_or_diploma'],
        request.session['hsc_school'] = form_data['hsc_school'],
        request.session['hsc_school_address'] = form_data['hsc_school_address'],
        request.session['hsc_percentage'] = form_data['hsc_percentage'],
        request.session['hsc_year'] = form_data['hsc_year'],
        request.session['diploma_clg'] = form_data['diploma_clg'],
        request.session['diploma_clg_address'] = form_data['diploma_clg_address'],
        request.session['diploma_percentage'] = form_data['diploma_percentage'],
        request.session['diploma_year'] = form_data['diploma_year'],
        fs = FileSystemStorage(location=MEDIA_ROOT + '/' + roll_number)
        if request.session['hsc_or_diploma'][0] == '12th':
            print('12th')
            uploaded_file = request.FILES['sslc_certi']
            print(uploaded_file)
            fs.save(name=roll_number + '_sslc certificate.pdf', content=uploaded_file)
            uploaded_file = request.FILES['hsc_certi']
            fs.save(name=roll_number + '_hsc certificate.pdf', content=uploaded_file)
        elif request.session['hsc_or_diploma'][0] == 'Diploma':
            print('diploma')
            uploaded_file = request.FILES['sslc_certi']
            print(uploaded_file)
            fs.save(name=roll_number + '_sslc certificate.pdf', content=uploaded_file)
            uploaded_file = request.FILES['diploma_certi']
            fs.save(name=roll_number + '_diploma certificate.pdf', content=uploaded_file)
        else:
            print(request.session['hsc_or_diploma'])
        current_pursuing = request.session['current_pursuing']
        # Return a JSON response indicating success
        return JsonResponse({'success': True,'pursuing':current_pursuing}, content_type='application/json')
    else:
        template=loader.get_template('schoolings.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))
@ensure_csrf_cookie
def ug_details(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        print(request.session)
        roll_number = request.session['rollno']

        #request.session['ug_department'] = form_data['ug_department'],
        request.session['ug_hod'] = form_data['ug_hod'],
        request.session['ug_hod_no'] = form_data['ug_hod_no'],
        request.session['ug_hod_mail'] = form_data['ug_hod_mail'],
        request.session['ug_seed'] = form_data['ug_seed'],
        request.session['ug_seed_no'] = form_data['ug_seed_no'],
        request.session['ug_seed_mail'] = form_data['ug_seed_mail'],
        request.session['ug_percentage'] = form_data['ug_percentage'],
        request.session['active_ug_arrears_count'] = form_data['active_ug_arrears_count'],
        request.session['ug_arrears_count'] = form_data['ug_arrears_count'],
        request.session['ug_intern_period'] = form_data['ug_intern_period']

        fs = FileSystemStorage(location=MEDIA_ROOT + '/' + roll_number)
        uploaded_file = request.FILES['ug_marksheet']
        fs.save(name=roll_number + '_ug_marksheet.pdf', content=uploaded_file)
        print(roll_number)
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        template=loader.get_template('ug_details.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))
@ensure_csrf_cookie
def pg_details(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        roll_number = request.session['rollno']
        request.session['pg_hod'] = form_data['pg_hod'],
        request.session['pg_hod_no'] = form_data['pg_hod_no'],
        request.session['pg_seed'] = form_data['pg_seed'],
        request.session['pg_seed_no'] = form_data['pg_seed_no'],
        request.session['pg_seed_mail'] = form_data['pg_seed_mail'],
        request.session['pg_percentage'] = form_data['pg_percentage'],
        request.session['active_pg_arrears_count'] = form_data['active_pg_arrears_count'],
        request.session['pg_arrears_count'] = form_data['pg_arrears_count'],
        request.session['pg_intern_period'] = form_data['pg_intern_period'],
        request.session['ex_ug_university'] = form_data['ex_ug_university'],
        request.session['ex_ug_college'] = form_data['ex_ug_college'],
        request.session['ex_ug_college_address'] = form_data['ex_ug_college_address'],
        request.session['ex_ug_department'] = form_data['ex_ug_department'],
        request.session['ex_ug_percentage'] = form_data['ex_ug_percentage'],
        request.session['ex_ug_internship_companyplace'] = form_data['ex_ug_internship_companyplace'],
        request.session['ex_ug_internship_companyname'] = form_data['ex_ug_internship_companyname'],
        request.session['ex_ug_internship_companyaddress'] = form_data['ex_ug_internship_companyaddress'],
        request.session['ex_ug_internship_period'] = form_data['ex_ug_internship_period'],
        request.session['ex_ug_work_company'] = form_data['ex_ug_work_company'],
        request.session['ex_ug_work_period']  = form_data['ex_ug_work_period'],
        request.session['ex_ug_work_uan'] = form_data['ex_ug_work_uan']

        fs = FileSystemStorage(location=MEDIA_ROOT + '/' + roll_number)
        uploaded_file = request.FILES['ex_ug_marksheets']
        fs.save(name=roll_number + '_ug_marksheet.pdf', content=uploaded_file)
        uploaded_file = request.FILES['ex_ug_provisional']
        fs.save(name=roll_number + '_ug_provisional.pdf', content=uploaded_file)
        uploaded_file = request.FILES['pg_marksheet']
        fs.save(name=roll_number + '_pg_marksheet.pdf', content=uploaded_file)
        print(roll_number)
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        template=loader.get_template('pg_details.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))
@ensure_csrf_cookie
def other_details(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        roll_number = request.session['rollno']
        request.session['why_placements'] = form_data['why_placements'],
        request.session['about_yourself'] = form_data['about_yourself'],
        request.session['languages_known'] = form_data['languages_known'],
        request.session['prog_languages'] = form_data['prog_languages']

        print(roll_number)
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        template=loader.get_template('others.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))
@ensure_csrf_cookie
def workloc_agreement(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        roll_number = request.session['rollno']
        request.session['work_interest'] = form_data['work_interest'],
        request.session['work_location'] = form_data['pan_inpyd'],
        request.session['sis'] = form_data['bond']
        print(roll_number)
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')

    else:
        template=loader.get_template('workloc_agreement.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))
@ensure_csrf_cookie
def mand_docs(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        roll_number = request.session['rollno']
        request.session['aadhar_no'] = form_data['aadhar_no'],
        request.session['pan_number'] = form_data['pan_number'],
        request.session['linkedin_profile'] = form_data['linkedin_profile'],
        request.session['linkedin_link'] = form_data['linkedin_link'],
        request.session['pursuing'] = form_data['pursuing']

        fs = FileSystemStorage(location=MEDIA_ROOT + '/' + roll_number)
        uploaded_file = request.FILES['aadhar']
        fs.save(name=roll_number+'_aadhar card.pdf', content=uploaded_file)
        uploaded_file = request.FILES['pan_card']
        fs.save(name=roll_number+'_pan card.pdf', content=uploaded_file)
        uploaded_file = request.FILES['pp']
        fs.save(name=roll_number+'_PP photo.jpg', content=uploaded_file)
        uploaded_file = request.FILES['clg_id']
        fs.save(name=roll_number+'_college id.pdf', content=uploaded_file)
        uploaded_file = request.FILES['passport']
        fs.save(name=roll_number+'_passport.pdf', content=uploaded_file)
        #
        print(roll_number)
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')

    else:
        template=loader.get_template('mand_docs.html')
        context = {}
        # Add CSRF token to the context
        context['csrf_token'] = get_token(request)
        return HttpResponse(template.render(context, request))
@ensure_csrf_cookie
def ack(request):
        roll_number = request.session['rollno']
        user_data = User_reg.objects.filter(Roll_Number=roll_number).values()
        user_data=dict(user_data[0])
        return render(request,'ack_page.html',{'data':user_data})

@ensure_csrf_cookie
def application_sts(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        form_data = request.POST
        print(form_data)
        '''roll_number = request.session['Roll_Number']
        user_data=User_reg.objects.filter(Roll_Number=roll_number).values()
        print(user_data)'''
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        '''roll_number = request.session['Roll_Number']
        user_data = User_reg.objects.filter(Roll_Number=roll_number).values()
        user_data=dict(user_data[0])'''
        return render(request,'application_sts.html',{'data':'user_data'})
@ensure_csrf_cookie
def test(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        data = request.POST
        print(data)
        # Return a JSON response indicating success
        return JsonResponse({'success': True}, content_type='application/json')

    else:
        template = loader.get_template('testing.html')
        return HttpResponse(template.render())


@csrf_exempt
def intern_attendance_login(request):
    if request.method == 'POST':
        form_data=request.POST
        print(form_data)
        db_data=intern_db.objects.filter(reg_no=form_data['intern_uname']).values()
        try:
            if form_data['intern_uname'] == db_data[0]['reg_no'] and form_data['intern_pass'] == db_data[0]['password']:
                print('Authentication Success')
                request.session['intern_id'] = db_data[0]['reg_no']
                request.session['intern_name'] = db_data[0]['name']
                print(request.session['intern_id'])
                return JsonResponse({'success': True}, content_type='application/json')
            else:
                return JsonResponse({'error': 'Authentication Failed'}, status=401)
        except IndexError:
                print('Index Error')
                #return JsonResponse({'error': True}, content_type='application/json')
                return JsonResponse({'error': 'All fields Must be filled'}, status=401)
        except KeyError:
                print('Key Error')
                #return JsonResponse({'error': True}, content_type='application/json')
                return JsonResponse({'error': 'All fields Must be filled'}, status=401)

    else:
        template = loader.get_template('intern_atn_login.html')
        return HttpResponse(template.render())

@csrf_exempt
def intern_attendance(request):
    if request.method == 'POST':
        form_data = request.POST
        print(form_data)
        print(request.session['intern_id'])
        request.session['date'] = form_data['inDate']
        #request.session['date'] = '4/23/2023'
        #intern = intern_db.objects.filter(reg_no=(request.session['intern_id'])).get()
        internStu=Intern_atn(
            reg_no=request.session['intern_id'],
            #name=intern.name,
            Date=form_data['inDate'],
            #Date='4/23/2023',
            Intime=form_data['inTime'],
            locationIn=form_data['latitude']+','+form_data['longitude']
        )
        internStu.save()
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        intern_id = request.session['intern_id']
        data = Intern_atn.objects.filter(reg_no=intern_id).values()
        stu_data = intern_db.objects.filter(reg_no=intern_id).values()
        studata = dict(stu_data[0])
        return render(request,'intern_atn.html',{'data':data,'intern':studata})


@csrf_exempt
def intern_attendance_out(request):
    if request.method == 'POST':
        form_data = request.POST
        print(form_data)
        id=request.session['intern_id']
        date=request.session['date']
        Intern_atn.objects.filter(reg_no=id,Date=date).update(
            Outtime=form_data['outTime'],
            locationOut=form_data['outLatitude']+','+form_data['outLongitude']
        )
        request.session.clear()
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        template = loader.get_template('intern_atn.html')
        return HttpResponse(template.render())

'''@csrf_exempt
def mark_extract(request):
    if request.method == 'POST':
        form_data = request.POST
        print(form_data)
        cropper('./superlee/test2.jpg')
        scan('./superlee/static/output/board.jpg')
        sts = txtchecker('tamilnadu')
        if sts == 'tamilnadu':
            sslc = ['secondary', 'school', 'leaving', 'certificate']
            for key in sslc:
                sts = txtchecker(key)
                print("Certificate Verifying . . . . . ")
                if sts in key:
                    scan('./superlee/static/output/marks.jpg')
                    marks = numcheck2()
                    print(marks)
                    if len(marks) != 0:
                        total = sum(marks)
                        # sts=txtchecker()
                        percentage = total / 5
                        print(f"\nTotal Marks:{total}\nPercentage:{percentage}%")
                        break
                    else:
                        print('mark not found')
                        break
                else:
                    print("Certificate is Unrecognizable")
        else:
            print("ERROR 404")
        return JsonResponse({'success': True}, content_type='application/json')
    else:
        template = loader.get_template('mark_ext.html')
        return HttpResponse(template.render())'''

def student_data(request):
    template = loader.get_template('admin/student-data.html')
    return HttpResponse(template.render())
def admin_attendance(request):
    template = loader.get_template('admin/student-data.html')
    return HttpResponse(template.render())
def msg_center(request):
    template = loader.get_template('admin/student-data.html')
    return HttpResponse(template.render())
def acc_settings(request):
    template = loader.get_template('admin/student-data.html')
    return HttpResponse(template.render())
def logout(request):
    template = loader.get_template('admin/student-data.html')
    return HttpResponse(template.render())
