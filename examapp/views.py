from datetime import timezone
from django.shortcuts import render,redirect
from django.utils import timezone

from django.contrib.auth import logout
# from django.shortcuts import get_object_or_404, redirect
# from django.views.decorators.csrf import csrf_exempt

from examapp.models import Questions
from . models import Student
from . models import Result
from . models import AdminAccount

# Create your views here.

#questions
def getaddquespage(request):
    return render(request,'Questions/add_ques.html')

def getdeletequespage(request):
    return render(request,'Questions/delete_ques.html')

# def getshowallquespage(request):
#     return render(request,'Questions/showall_ques.html')
def getshowallquespage(request):
    all_questions = Questions.objects.all()
    print(f"DEBUG: Found {all_questions.count()} questions in database") # Check your terminal for this!
    return render(request, 'Questions/showall_ques.html', {'questions': all_questions})

def getupdatequespage(request):
    return render(request,'Questions/update_ques.html')

def getcurdquespage(request):
      return render(request,'Questions/que_curd.html')


def add_ques(request):
    
        qno = request.GET.get('qno')
        qname = request.GET.get('qname')
        op1 = request.GET.get('op1')
        op2 = request.GET.get('op2')
        op3 = request.GET.get('op3')
        op4 = request.GET.get('op4')
        correct_ans = request.GET.get('correct_ans')
        subject = request.GET.get('subject')
        

        Questions.objects.create(
            qno=qno,
            qname=qname,
            op1=op1,
            op2=op2,
            op3=op3,
            op4=op4,
            correct_ans=correct_ans,
            subject=subject,
          
            
        )
        return render(request,'Questions/add_ques.html',{'msg':'Question Addded Successfully !'})


# def delete_ques(request, id):
    
#         question = get_object_or_404(Questions, id=id)
#         question.delete()
#         return render(request,'Questions/delete_ques.html',{'msg':'Question Deleted Successfully !'})

# def delete_ques(request,id):
#     qno=request.GET.get('qno')
#     Questions.objects.filter(qno=qno).delete()
#     return render(request,'delete_ques.html',{'msg':'Que Deleted !'})

def showall_ques(request):
     questions = Questions.objects.all().order_by('qno')
  
     return render(request, 'Questions/showall_ques.html', {'questions': questions})

def show_updatepage(request):
    # try:
        qno=request.GET.get('qno')
        questions=Questions.objects.get(qno=qno)
        return render(request,'Questions/update_ques.html',{'questions':questions})


    # except Exception as e:
    #     e='question doesnt match !'
    #     return render(request,'Questions/update_ques.html',{'msg':'Can not show question'})


def update_updatepage(request):
     qno=request.GET.get('qno')
     questions=Questions.objects.filter(qno=qno)

     questions.update(
        qno = request.GET.get('qno'),
        qname = request.GET.get('qname'),
        op1 = request.GET.get('op1'),
        op2 = request.GET.get('op2'),
        op3 = request.GET.get('op3'),
        op4 = request.GET.get('op4'),
        correct_ans = request.GET.get('correct_ans'),
        subject = request.GET.get('subject'),
        
     )
     return render(request,'Questions/update_ques.html',{'questions':questions,'msg':'QUe details Updated !'})

def delete_deletepage(request):
      qno=request.GET.get('qno')
      Questions.objects.filter(qno=qno).delete()
      return render(request,'Questions/delete_ques.html',{'msg':'Question Deleted'})
     
def show_deletepage(request):
        qno=request.GET.get('qno')
        questions=Questions.objects.get(qno=qno)
        return render(request,'Questions/delete_ques.html',{'questions':questions})

def add_curd(request):
        qno = request.GET.get('qno')
        qname = request.GET.get('qname')
        op1 = request.GET.get('op1')
        op2 = request.GET.get('op2')
        op3 = request.GET.get('op3')
        op4 = request.GET.get('op4')
        correct_ans = request.GET.get('correct_ans')
        subject = request.GET.get('subject')
        

        Questions.objects.create(
            qno=qno,
            qname=qname,
            op1=op1,
            op2=op2,
            op3=op3,
            op4=op4,
            correct_ans=correct_ans,
            subject=subject,
           
            
        )
        return render(request,'Questions/que_curd.html',{'msg':'Question Addded Successfully !'})


def delete_curd(request):
      qno=request.GET.get('qno')
      Questions.objects.filter(qno=qno).delete()
      return render(request,'Questions/que_curd.html',{'msg':"Question Deleted !"})

def update_curd(request):
     qno=request.GET.get('qno')
     questions=Questions.objects.filter(qno=qno)

     questions.update(
        qno = request.GET.get('qno'),
        qname = request.GET.get('qname'),
        op1 = request.GET.get('op1'),
        op2 = request.GET.get('op2'),
        op3 = request.GET.get('op3'),
        op4 = request.GET.get('op4'),
        correct_ans = request.GET.get('correct_ans'),
        subject = request.GET.get('subject'),
        
     )
     return render(request,'Questions/que_curd.html',{'questions':questions,'msg':'Question details Updated !'})

def show_curd(request):
        qno=request.GET.get('qno')
        questions=Questions.objects.get(qno=qno)
        return render(request,'Questions/que_curd.html',{'questions':questions })




#Student
def getaddstudpage(request):
    return render(request,'Student/add_stud.html')

def getdeletestudpage(request):
    return render(request,'Student/delete_stud.html')

def getupdatestudpage(request):
    return render(request,'Student/update_stud.html')

def getcurdstudpage(request):
    return render(request,'Student/stud_curd.html')

def getshowallstudpage(request):
    # Fetch all students from the database
    all_stud = Student.objects.all()
    
    # Debug print to your terminal to verify data exists
    print(f"DEBUG: Found {all_stud.count()} students in database") 
    
    # We pass 'all_stud' into the template using the name 'student'
    return render(request, 'Student/show_stud.html', {'student': all_stud})
def add_stud(request):
    msg = ""

    if request.method == "GET" and request.GET:
        sid = request.GET.get('sid')
        sname = request.GET.get('sname')
        semail = request.GET.get('semail')
        smob_no = request.GET.get('smob_no')
        password = request.GET.get('password')

        if sid and sname and semail and smob_no and password:
            Student.objects.create(
                sid=sid,
                sname=sname,
                semail=semail,
                smob_no=smob_no,
                password=password
            )
            msg = "Student Added Successfully"
        else:
            msg = "All fields are required"

    return render(request, "Student/add_stud.html", {"msg": msg})

def delete_stud(request):
      sid=request.GET.get('sid')
      Student.objects.filter(sid=sid).delete()
      return render(request,'Student/delete_stud.html',{'msg':"Student Deleted !"})

def show_delete_stud(request):
      sid=request.GET.get('sid')
      student=Student.objects.filter(sid=sid).first()
      return render(request,'Student/delete_stud.html',{"student" : student})


def showall_stud(request):
      student=Student.objects.all()
      return render(request, 'Student/show_stud.html', {'s':student})


# def showall_ques(request):
#      questions = Questions.objects.all().order_by('qno')
  
#      return render(request, 'Questions/showall_ques.html', {'questions': questions})


def update_stud(request):
     sid=request.GET.get('sid')
     student=Student.objects.filter(sid=sid)

     student.update(
          sid=request.GET.get('sid'),
          sname=request.GET.get('sname'),
          semail=request.GET.get('semail'),
          smob_no=request.GET.get('smob_no'),
          password=request.GET.get('password'),

     )
     return render(request, 'Student/update_stud.html', {'student':student , 'msg':'Employee details Updated !'})


def show_update_stud(request):
      sid=request.GET.get('sid')
      student=Student.objects.filter(sid=sid).first()
      return render(request,'Student/update_stud.html',{"student" : student})


def add_curd(request):
    msg = ""

    if request.method == "GET" and request.GET:
        sid = request.GET.get('sid')
        sname = request.GET.get('sname')
        semail = request.GET.get('semail')
        smob_no = request.GET.get('smob_no')
        password = request.GET.get('password')

        if sid and sname and semail and smob_no and password:
            Student.objects.create(
                sid=sid,
                sname=sname,
                semail=semail,
                smob_no=smob_no,
                password=password
            )
            msg = "Student Added Successfully"
        else:
            msg = "All fields are required"

    return render(request, "Student/stud_curd.html", {"msg": msg})  

def delete_curd(request):
      sid=request.GET.get('sid')
      Student.objects.filter(sid=sid).delete()
      return render(request,'Student/stud_curd.html',{'msg':"Student Deleted !"})

def update_curd(request):
     sid=request.GET.get('sid')
     student=Student.objects.filter(sid=sid)

     student.update(
          sid=request.GET.get('sid'),
          sname=request.GET.get('sname'),
          semail=request.GET.get('semail'),
          smob_no=request.GET.get('smob_no'),
          password=request.GET.get('password'),

     )
     return render(request, 'Student/stud_curd.html', {'student':student , 'msg':'Student details Updated !'})

def show_curd(request):
      sid=request.GET.get('sid')
      student=Student.objects.filter(sid=sid).first()
      return render(request,'Student/stud_curd.html',{"student" : student})



def GiveMeRegisterPage(request):
    return render(request,'Student/register.html')

def Register(request):
    sid=request.GET.get('sid')
    sname = request.GET.get('sname')
    password = request.GET.get('password')
    semail=request.GET.get('email')
    smob_no = request.GET.get('smob_no')

    Student.objects.create(sid=sid,sname = sname, password = password, smob_no = smob_no)
    return render(request,'Student/Login.html',{'msg': 'Student Register Successfully'})

def GiveMeLoginPage(request):
    return render(request,'Student/login.html')

def Login(request):
    sname = request.GET.get('sname')
    password = request.GET.get('password')

    request.session['sname'] = sname

    student = Student.objects.get(sname = sname)



    if (student.password == password):
        request.session['answer'] = {}
        request.session['score'] = 0
        request.session['qno'] = 0
        return render(request,'Questions/subject.html')
    else :
        return render(request,'Student/login.html',{'message':'invalid password'})
    

#
def GetHomePage(request):
     return render(request,'home.html')


#result


def StartTest(request):
    subject = request.GET.get('subject')
    request.session['subject'] = subject
    request.session['qno'] = 0
    request.session['answer'] = {} # Clear previous answers

    queryset = Questions.objects.filter(subject=subject).values()
    listallquestions = list(queryset)

    request.session['listallquestions'] = listallquestions
    
    # Pass qno 0 to the template
    return render(request, 'starttest.html', {
        "question": listallquestions[0],
        "qno": 0
    })

def NextQuestion(request):
    allquestions = request.session.get('listallquestions', [])
    qno = request.session.get('qno', 0)
    answers = request.session.get('answer', {})

    # SAVE current selection before moving
    if 'op' in request.GET:
        answers[str(qno)] = request.GET.get('op') # Force key to String
        request.session['answer'] = answers

    # MOVE Forward
    if qno < len(allquestions) - 1:
        qno += 1
        request.session['qno'] = qno

    question = allquestions[qno]
    selected = answers.get(str(qno)) # Retrieve answer for the NEW question

    return render(request, 'starttest.html', {
        'question': question,
        'qno': qno,
        'selected': selected
    })

def PreviousQuestion(request):
    allquestions = request.session.get('listallquestions', [])
    qno = request.session.get('qno', 0)
    answers = request.session.get('answer', {})

    # SAVE current selection before moving
    if 'op' in request.GET:
        answers[str(qno)] = request.GET.get('op') 
        request.session['answer'] = answers

    # MOVE Backward
    if qno > 0:
        qno -= 1
        request.session['qno'] = qno

    question = allquestions[qno]
    selected = answers.get(str(qno))

    return render(request, 'starttest.html', {
        'question': question,
        'qno': qno,
        'selected': selected
    })

def End_Test(request):
    answers = request.session.get('answer', {})
    qno = request.session.get('qno', 0)
    
    if 'op' in request.GET:
        answers[str(qno)] = request.GET.get('op')
        request.session['answer'] = answers

    allquestions = request.session.get('listallquestions', [])
    score = 0
    response = []

    for i, question in enumerate(allquestions):
        selected_letter = answers.get(str(i)) # This is 'A', 'B', etc.
        correct_letter = str(question['correct_ans']).strip() # This is 'A', 'B', etc.

        # Logic to get the FULL TEXT of the correct answer
        correct_text = ""
        if correct_letter == 'A': correct_text = question['op1']
        elif correct_letter == 'B': correct_text = question['op2']
        elif correct_letter == 'C': correct_text = question['op3']
        elif correct_letter == 'D': correct_text = question['op4']

        # Logic to get the FULL TEXT of what the user selected
        selected_text = "Not Attempted"
        if selected_letter == 'A': selected_text = question['op1']
        elif selected_letter == 'B': selected_text = question['op2']
        elif selected_letter == 'C': selected_text = question['op3']
        elif selected_letter == 'D': selected_text = question['op4']

        # Check if correct
        is_correct = False
        if selected_letter == correct_letter:
            score += 1
            is_correct = True

        response.append({
            'qno': i + 1,
            'question': question['qname'],
            'selected': selected_text, # Now shows the full text!
            'correct': correct_text,   # Now shows the full text!
            'is_correct': is_correct
        })

    # ... (Keep your Result.objects.create code here) ...

    return render(request, 'Result/score.html', {
        'response': response,
        'finalscore': score
    })



def GetAllResultPage(request):
    rdb= Result.objects.all()
    return render (request, 'Result/allresult.html',{'rdb':rdb})

def LogoutUser(request):
    logout(request)
    return render (request,'home.html')

#admin

def GetAdminRegister(request):
    return render(request, 'Admin/Admin_Register.html')

def admin_registration(request):
    u = request.GET.get('username')
    e = request.GET.get('email')
    p = request.GET.get('pwd')

    # This will print in your VS Code / Terminal window
    print(f"DEBUG: username={u}, email={e}, password={p}")

    if u and e and p:
        AdminAccount.objects.create(username=u, email=e, password=p)
        # We render the Login page with a success message
        return render(request, 'Admin/Admin_Login.html', {'msg': 'Registration Successful!'})
    
    return render(request, 'Admin/Admin_Register.html')

def GetAdminLogin(request):
    return render(request, 'Admin/Admin_Login.html')

# def admin_login(request):
#     u = request.GET.get('user')
#     p = request.GET.get('pass')
    
#     if u and p:
#         admin = AdminAccount.objects.filter(username=u, password=p).first()
#         if admin:
#             request.session['admin_user'] = admin.username
#             # Instead of redirect, we render the home page directly
#             return render(request, 'Admin/Admin_Home.html')
#         else:
#             return render(request, 'Admin/Admin_Login.html', {'error': 'Invalid Credentials'})
            
#     return render(request, 'Admin/Admin_Login.html')

# examapp/views.py

def admin_login(request):
    user_val = request.GET.get('user')
    pass_val = request.GET.get('pass')

    # Use filter instead of get to avoid the exception
    admin = AdminAccount.objects.filter(username=user_val, password=pass_val).first()

    if admin:
        # Success: Log the user in or redirect
        return render(request, 'Admin/Admin_Home.html')
    else:
        # Failure: Show an error message
        return render(request, 'Admin/Admin_Login.html', {'error': 'Invalid Username or Password'})
          




def admin_home(request):
    # Simple session check
    if 'admin_user' in request.session:
        return render(request, 'Admin/Admin_Home.html')
    # If session fails, stay on login page
    return render(request, 'Admin/Admin_Login.html', {'error': 'Please login first'})

def GetAdminHome(request):
    return render(request,'Admin/Admin_Home.html')

def admin_logout(request):
    if 'admin_user' in request.session:
        del request.session['admin_user']
    return redirect('/admin_login/')
