from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from physics.models import Homework, Question, Question_Part, Question_Hint, Answers, Summary
import logging
import sqlalchemy.pool as pool
import PySQLPool
import threading
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
homework_number=0;
question_number=0;
part_number=0;
hint_number=0;

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__ (self)

    def run(self):
        query = PySQLPool.getNewQuery(connection)
        sql = "INSERT INTO mayhar_users (user_name,user_email,user_password) VALUES ('Jay Shah','jayshah','jayyaj@1')"
        query.Query(sql)
        print "Inserted"
    
def index(request):
    return render_to_response("physics/index.html", {}, context_instance=RequestContext(request))

def index_student(request):
    return render_to_response("physics/index_student.html", {}, context_instance=RequestContext(request))

def get_homework(request):
    return render_to_response("physics/get_hw.html", {}, context_instance=RequestContext(request))

def verify(request):
    return render_to_response("physics/verify.html", {}, context_instance=RequestContext(request))

def submit_homework(request):
    if request.method == "POST":
        q_count = 0
        right_count = 0 
        results = ''
        hw_no = request.POST.get("Homework")
        q_no = request.POST.get("Question")
        student_id = request.POST.get("StudentID")
        print hw_no
        print q_no
        print student_id
        for x in request.POST:
            if "ANSWER" in x:
                q_count = q_count+1
                ans_que = x[6:]
                ans_explaination = request.POST.get('EXPLAIN'+ans_que)
                print ans_explaination
                print ans_que
                ans_details = ans_que.split(',')
                print "PartNo:"+ans_details[2]
                print "HintNo:"+ans_details[3]
                answer = request.POST.get(x)
                correctanswer = request.POST.get('CORRECT'+ans_que)
                print "Correct answer :"+correctanswer.encode('utf-8').strip()
                answer = answer.replace("%%%%"," ")
                correctanswer = correctanswer.replace("%%%%"," ")
                print answer
                if (answer==correctanswer):
                    right_count=right_count+1
                new_entry = Answers(Answers_Student_ID='3124',Answers_HW_Number=hw_no,Answers_Q_Number=q_no,Answers_QP_Number=ans_details[2],Answers_Hint_Number=ans_details[3],Answers_Explaination=ans_explaination,Answers_Correct_Answer=answer)
                new_entry.save()
        results = "You scored "+str(right_count)+" on "+str(q_count)
        return render_to_response("physics/hw_results.html", {'result':results}, context_instance=RequestContext(request))
    return render_to_response("physics/get_hw.html", {}, context_instance=RequestContext(request))

def retrieve_homework(request):
    table=[]
    hw_no = 0
    q_no = 0
    part_no = 0
    hint_no = 0
    question_content = None
    question_notation = None
    question_parts = []
    question_hints = []

    if request.method=="POST":
        hw_no = request.POST.get('homework')
        q_no = request.POST.get('question')
        print "Homework : "+str(hw_no)
        print "Question : "+str(q_no)
        questions = Question.objects.filter(Question_HW_Number=hw_no,Question_Number=q_no).values()
        for ques in questions:
            question_content = ques['Question_Content']
            question_notation  = ques['Question_Notation']
            hw_no = ques['Question_HW_Number']
            q_no = ques['Question_Number']
            parts_ques = Question_Part.objects.filter(Question_Part_HW_Number=hw_no,Question_Part_Q_Number=q_no).values()
            for part in parts_ques:
                part_no = part['Question_Part_Number']
                part_content = part['Question_Part_Content']
                hints_part = Question_Hint.objects.filter( Question_Hint_HW_Number = hw_no,Question_Hint_Q_Number=q_no,Question_Hint_QP_Number=part_no).values()
                for hint in hints_part:
                    hint_options=hint['Question_Hint_Options'].split('@@@')
                    hints = []
                    for a in hint_options:
                        hints.append([a,a.replace(" ","%%%%")])
                    correct = hint['Question_Hint_Correct_Answer']
                    correct = correct.replace(" ","%%%%")
                    question_hints.append((hint['Question_Hint_Number'],hint['Question_Hint_Content'],hints,correct))
                question_parts.append((part_no,part_content,question_hints))
                question_hints = []
            table.append((question_content,question_notation,question_parts))
        print table
    return render_to_response("physics/retrieve_hw.html", {'question':table,'Homework':hw_no,'Question':q_no}, context_instance=RequestContext(request))

def verify_homework(request):
    table=[]
    hw_no = 0
    q_no = 0
    part_no = 0
    hint_no = 0
    question_content = None
    question_notation = None
    question_parts = []
    question_hints = []

    if request.method=="POST":
        hw_no = request.POST.get('homework')
        q_no = request.POST.get('question')
        print "Homework : "+str(hw_no)
        print "Question : "+str(q_no)
        questions = Question.objects.filter(Question_HW_Number=hw_no,Question_Number=q_no).values()
        for ques in questions:
            question_content = ques['Question_Content']
            question_notation  = ques['Question_Notation']
            hw_no = ques['Question_HW_Number']
            q_no = ques['Question_Number']
            parts_ques = Question_Part.objects.filter(Question_Part_HW_Number=hw_no,Question_Part_Q_Number=q_no).values()
            for part in parts_ques:
                part_no = part['Question_Part_Number']
                part_content = part['Question_Part_Content']
                hints_part = Question_Hint.objects.filter( Question_Hint_HW_Number = hw_no,Question_Hint_Q_Number=q_no,Question_Hint_QP_Number=part_no).values()
                for hint in hints_part:
                    hint_options=hint['Question_Hint_Options'].split('@@@')
                    hints = []
                    for a in hint_options:
                        hints.append([a,a.replace(" ","%%%%")])
                    correct = hint['Question_Hint_Correct_Answer']
                    correct = correct.replace(" ","%%%%")
                    question_hints.append((hint['Question_Hint_Number'],hint['Question_Hint_Content'],hints,correct))
                question_parts.append((part_no,part_content,question_hints))
                question_hints = []
            table.append((question_content,question_notation,question_parts))
        print table
    return render_to_response("physics/verify_question.html", {'question':table,'Homework':hw_no,'Question':q_no}, context_instance=RequestContext(request))


def retrieve_summary(request):
    table=[]
    hw_no = 0
    summary=''
    question_content = None
    question_notation = None
    question_parts = []
    question_hints = []

    if request.method=="POST":
        hw_no = request.POST.get('homework')
        summary = Summary.objects.filter(Summary_HW_Number=hw_no).values()
        for sum_value in summary:
            summary = sum_value['Summary_Content']
    return render_to_response("physics/retrieve_summary.html", {'summary':summary,'Homework':hw_no}, context_instance=RequestContext(request))


def enter_homework(request):
    if request.method == "POST":
        homework_number = request.POST.get('homework')
        i = datetime.now()
        valid_datetime = datetime.strptime(i.strftime('%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S')
        new_entry = Homework(HW_Number = homework_number,HW_Submission_Date = valid_datetime, HW_Timestamp = valid_datetime)
        result = new_entry.save()
        print result
        return render_to_response("physics/question.html", {'hw':homework_number}, context_instance=RequestContext(request))
    return render_to_response("physics/enter_hw.html", {}, context_instance=RequestContext(request))

def enter_summary(request):
    if request.method == "POST":
        homework_number = request.POST.get('homework')
        content = request.POST.get('content')
        print content
        i = datetime.now()
        valid_datetime = datetime.strptime(i.strftime('%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S')
        new_entry = Summary(Summary_HW_Number = homework_number,Summary_Content = content, Summary_Timestamp = valid_datetime)
        result = new_entry.save()
        print result
        return render_to_response("physics/question.html", {'hw':homework_number}, context_instance=RequestContext(request))
    return render_to_response("physics/summary.html", {}, context_instance=RequestContext(request))

def enter_question(request):
    if request.method == "POST":
        homework_number = request.POST.get('homework')
        question_number = request.POST.get('question')
        question_content = request.POST.get('content').encode('utf-8')
        print question_content
        question_notation = request.POST.get('notation')
        i = datetime.now()
        valid_datetime = datetime.strptime(i.strftime('%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S')
        new_entry = Question(Question_HW_Number = homework_number,Question_Number=question_number,Question_Content = question_content, Question_Notation=question_notation,  Question_Image=None, Question_Timestamp = valid_datetime)
        result = new_entry.save()
        print result
        return render_to_response("physics/question_part.html", {'hw':homework_number,'q_no':question_number}, context_instance=RequestContext(request))
    return render_to_response("physics/question.html", {}, context_instance=RequestContext(request))

def enter_question_part(request):
    if request.method == "POST":
        homework_number = request.POST.get('homework')
        question_number = request.POST.get('question')
        part_number = request.POST.get('part')
        question_content = request.POST.get('content')
        i = datetime.now()
        valid_datetime = datetime.strptime(i.strftime('%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S')
        new_entry = Question_Part(Question_Part_HW_Number = homework_number,Question_Part_Q_Number=question_number,Question_Part_Number=part_number,Question_Part_Content = question_content, Question_Part_Image=None,Question_Part_Points=0,  Question_Part_Timestamp = valid_datetime)
        result = new_entry.save()
        print result
        return render_to_response("physics/question_hint.html", {'hw':homework_number,'q_no':question_number,'p_no':part_number}, context_instance=RequestContext(request))
    return render_to_response("physics/question_part.html", {}, context_instance=RequestContext(request))

def enter_question_hint(request):
    if request.method == "POST":
        homework_number = request.POST.get('homework')
        question_number = request.POST.get('question')
        part_number = request.POST.get('part')
        hint_number = request.POST.get('hint')
        question_content = request.POST.get('content')
        options = ''
        if(request.POST.get('option1')):
            options +=request.POST.get('option1') + '@@@'
        if(request.POST.get('option2')):
            options +=request.POST.get('option2') + '@@@'
        if(request.POST.get('option3')):
            options +=request.POST.get('option3') + '@@@'
        if(request.POST.get('option4')):
            options +=request.POST.get('option4') + '@@@'
        if(request.POST.get('option5')):
            options +=request.POST.get('option5') + '@@@'
        if(request.POST.get('option6')):
            options +=request.POST.get('option6') + '@@@'
        if(request.POST.get('option7')):
            options +=request.POST.get('option7') + '@@@'
        if(request.POST.get('option8')):
            options +=request.POST.get('option8') + '@@@'
        if(request.POST.get('option9')):
            options +=request.POST.get('option9') + '@@@'
        options = options[:-3]
        print options
        correct_answer = request.POST.get('answer')
        i = datetime.now()
        valid_datetime = datetime.strptime(i.strftime('%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S')
        new_entry = Question_Hint(Question_Hint_HW_Number = homework_number,Question_Hint_Q_Number=question_number,Question_Hint_QP_Number=part_number,Question_Hint_Number=hint_number,Question_Hint_Content = question_content, Question_Hint_Options=options,Question_Hint_Correct_Answer=correct_answer, Question_Hint_Timestamp = valid_datetime)
        result = new_entry.save()
        print result
        return render_to_response("physics/question_hint.html", {'hw':homework_number,'q_no':question_number,'p_no':part_number}, context_instance=RequestContext(request))
    return render_to_response("physics/question_hint.html", {}, context_instance=RequestContext(request))


def question_part(request):
    return render_to_response("physics/question_part.html", {}, context_instance=RequestContext(request))

def question_hint(request):
    return render_to_response("physics/question_hint.html", {}, context_instance=RequestContext(request))

def question_hint_insert(request):
    print request.POST.get('option')
    return render_to_response("physics/question_hint.html", {}, context_instance=RequestContext(request))
