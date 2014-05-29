#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript
#
# to restore it, run
# manage.py runscript module_name.this_script_name 
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    #initial imports

    def locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        #You may change this function to do specific lookup for specific objects
        #
        #original_class class of the django orm's object that needs to be located
        #original_pk_name the primary key of original_class
        #the_class      parent class of original_class which contains obj_content
        #pk_name        the primary key of original_class
        #pk_value       value of the primary_key
        #obj_content    content of the object which was not exported.
        #
        #you should use obj_content to locate the object on the target db    
        #
        #and example where original_class and the_class are different is
        #when original_class is Farmer and
        #the_class is Person. The table may refer to a Farmer but you will actually
        #need to locate Person in order to instantiate that Farmer
        #
        #example:
        #if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:        
        #    pk_name="name"
        #    pk_value=obj_content[pk_name]
        #if the_class == StaffGroup:
        #    pk_value=8
            
        search_data = { pk_name: pk_value }
        the_obj =the_class.objects.get(**search_data)
        #print the_obj
        return the_obj    

    #Processing model: University
    from syllabus.academia.models import University

    university = University()
    university.name = "Stevenson School"
    university.save()
    
    #Processing model: College
    from syllabus.academia.models import College
    
    college_1 = College()
    college_1.name = "College of Letters and Sciences"
    college_1.university = university
    college_1.save()
    
    #Processing model: MajorRequirement
    from syllabus.academia.models import MajorRequirement
    
    major_requirement_1 = MajorRequirement()
    major_requirement_1.number = 1
    major_requirement_1.minGrade = 70
    major_requirement_1.save()
    
    
    major_requirement_2 = MajorRequirement()
    major_requirement_2.number = 1
    major_requirement_2.name = "English Reading and Composition"
    major_requirement_2.abbrv = "A"
    major_requirement_2.minGrade = 70
    major_requirement_2.save()

    #Processing model: Major
    from syllabus.academia.models import Major
    
    major_1 = Major()
    major_1.name = "Undeclared"
    major_1.type="BS"
    major_1.save()
    
    college_1.majors.add(major_1)
    college_1.requirements.add(major_requirement_2)
    
    major_1.major.add(major_requirement_1)


    from django.contrib.auth.models import Group

    auth_group_1 = Group()
    auth_group_1.name = u'admin'
    auth_group_1.save()
    
    auth_group_2 = Group()
    auth_group_2.name = u'faculty'
    auth_group_2.save()
    
    auth_group_3 = Group()
    auth_group_3.name = u'staff'
    auth_group_3.save()
    
    auth_group_4 = Group()
    auth_group_4.name = u'student'
    auth_group_4.save()

    #Processing model: User

    from syllabus.core.models import SyllUser

    auth_user_1 = SyllUser()
    auth_user_1.username = u'admin'
    auth_user_1.first_name = u'Alec'
    auth_user_1.last_name = u'Aivazis'
    auth_user_1.email = u'a@a.com'
    auth_user_1.password = u'pbkdf2_sha256$10000$zBHsErUgPidy$+yJFG3G/Zz0mRhCrOH8FBlukrz5IByHsmkEHaceAosE='
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2012, 8, 3, 9, 27, 43, 283933)
    auth_user_1.date_joined = datetime.datetime(2012, 6, 15, 15, 37, 43)
    auth_user_1.save()

    auth_user_1.major.add(major_1)
    auth_user_1.groups.add(auth_group_1)

    from syllabus.socialservice.models import Tutor

    tutor1 = Tutor()
    tutor1.user = auth_user_1
    tutor1.save()




    #Processing model: MetaData

    from syllabus.core.models import MetaData

    Syllabus_metadata_1 = MetaData()
    Syllabus_metadata_1.key = u'possiblePoints'
    Syllabus_metadata_1.value = u'50'
    Syllabus_metadata_1.save()

    Syllabus_metadata_2 = MetaData()
    Syllabus_metadata_2.key = u'associatedReading'
    Syllabus_metadata_2.value = u'KK Ch 34,23'
    Syllabus_metadata_2.save()

    Syllabus_metadata_3 = MetaData()
    Syllabus_metadata_3.key = u'associatedReading'
    Syllabus_metadata_3.value = u'KK Ch 34,23'
    Syllabus_metadata_3.save()

    Syllabus_metadata_4 = MetaData()
    Syllabus_metadata_4.key = u'associatedReading'
    Syllabus_metadata_4.value = u''
    Syllabus_metadata_4.save()

    Syllabus_metadata_5 = MetaData()
    Syllabus_metadata_5.key = u'possiblePoints'
    Syllabus_metadata_5.value = u'50'
    Syllabus_metadata_5.save()

    Syllabus_metadata_6 = MetaData()
    Syllabus_metadata_6.key = u'possiblePoints'
    Syllabus_metadata_6.value = u'100'
    Syllabus_metadata_6.save()

    #Processing model: File

    from syllabus.core.models import File

    Syllabus_file_1 = File()
    Syllabus_file_1.fileName = u'/Users/alec/dv/syllabus/resources/uploads/GEN PHYSICS-assignments/IMG_0068.jpg'
    Syllabus_file_1.save()

    Syllabus_file_2 = File()
    Syllabus_file_2.fileName = u'/Users/alec/dv/syllabus/resources/uploads/GEN PHYSICS-lectures/attachment.jpg'
    Syllabus_file_2.save()

    Syllabus_file_3 = File()
    Syllabus_file_3.fileName = u'/Users/alec/dv/syllabus/resources/uploads/GEN PHYSICS-lectures/on.png'
    Syllabus_file_3.save()

    Syllabus_file_4 = File()
    Syllabus_file_4.fileName = u'/Users/alec/dv/syllabus/resources/uploads/GEN PHYSICS-assignments/Screen Shot 2012-07-22 at 10.15.10 AM.png'
    Syllabus_file_4.save()

    Syllabus_file_5 = File()
    Syllabus_file_5.fileName = u'/Users/alec/dv/syllabus/resources/uploads/PHYS22-messageboard/68822f32.jpg'
    Syllabus_file_5.save()

    Syllabus_file_6 = File()
    Syllabus_file_6.fileName = u'/Users/alec/dv/syllabus/resources/uploads/PHYS22-messageboard/bg.png'
    Syllabus_file_6.save()

    #Processing model: Event

    from syllabus.classroom.models import Event

    Syllabus_event_1 = Event()
    Syllabus_event_1.title = u'Problem Set 16'
    Syllabus_event_1.description = u'see attached file'
    Syllabus_event_1.date = datetime.date(2012, 7, 16)
    Syllabus_event_1.time = datetime.time(13, 0)
    Syllabus_event_1.category = u'assignment'
    Syllabus_event_1.save()

    Syllabus_event_1.files.add(Syllabus_file_1)
    Syllabus_event_1.metaData.add(Syllabus_metadata_1)

    Syllabus_event_2 = Event()
    Syllabus_event_2.title = u'An Introduction to E/M'
    Syllabus_event_2.description = u"An introduction to electromagnetism: Gauss's Law, Bio-Savart Law, Induction, etc."
    Syllabus_event_2.date = datetime.date(2012, 7, 9)
    Syllabus_event_2.time = datetime.time(13, 0)
    Syllabus_event_2.category = u'lecture'
    Syllabus_event_2.save()

    Syllabus_event_2.files.add(Syllabus_file_2)
    Syllabus_event_2.metaData.add(Syllabus_metadata_2)

    Syllabus_event_3 = Event()
    Syllabus_event_3.title = u'More E/M'
    Syllabus_event_3.description = u'More on the applications of important laws of E/M'
    Syllabus_event_3.date = datetime.date(2012, 7, 11)
    Syllabus_event_3.time = datetime.time(13, 0)
    Syllabus_event_3.category = u'lecture'
    Syllabus_event_3.save()

    Syllabus_event_3.files.add(Syllabus_file_3)
    Syllabus_event_3.metaData.add(Syllabus_metadata_3)

    Syllabus_event_4 = Event()
    Syllabus_event_4.title = u'Advanced Concepts in E/M'
    Syllabus_event_4.description = u'And introduction to advanced concepts in E/M that will be studied in the upper division'
    Syllabus_event_4.date = datetime.date(2012, 7, 13)
    Syllabus_event_4.time = datetime.time(13, 0)
    Syllabus_event_4.category = u'lecture'
    Syllabus_event_4.save()

    Syllabus_event_4.metaData.add(Syllabus_metadata_4)

    Syllabus_event_5 = Event()
    Syllabus_event_5.title = u'Problem Set 15'
    Syllabus_event_5.description = u'Problem set covering fluid mechanics'
    Syllabus_event_5.date = datetime.date(2012, 7, 9)
    Syllabus_event_5.time = datetime.time(13, 0)
    Syllabus_event_5.category = u'assignment'
    Syllabus_event_5.save()

    Syllabus_event_5.files.add(Syllabus_file_4)
    Syllabus_event_5.metaData.add(Syllabus_metadata_5)

    Syllabus_event_6 = Event()
    Syllabus_event_6.title = u'Exam on E/M'
    Syllabus_event_6.description = u'Includes all matierial covered in lecture as well as relevant sections in KK'
    Syllabus_event_6.date = datetime.date(2012, 7, 18)
    Syllabus_event_6.time = datetime.time(13, 0)
    Syllabus_event_6.category = u'test'
    Syllabus_event_6.save()

    Syllabus_event_6.metaData.add(Syllabus_metadata_6)


    #Processing model: Term

    from syllabus.academia.models import Term

    Syllabus_term_1 = Term()
    Syllabus_term_1.name = u'Winter'
    Syllabus_term_1.start = datetime.date(2012, 3, 18)
    Syllabus_term_1.end = datetime.date(2015, 7, 28)
    Syllabus_term_1.save()

    Syllabus_term_2 = Term()
    Syllabus_term_2.name = u'Spring'
    Syllabus_term_2.start = datetime.date(2012, 9, 25)
    Syllabus_term_2.end = datetime.date(2012, 12, 25)
    Syllabus_term_2.save()

    #Processing model: Timeslot

    from syllabus.core.models import Timeslot

    Syllabus_timeslot_1 = Timeslot()
    Syllabus_timeslot_1.day = u'1'
    Syllabus_timeslot_1.start = datetime.time(10, 55)
    Syllabus_timeslot_1.end = datetime.time(12, 15)
    Syllabus_timeslot_1.save()

    Syllabus_timeslot_2 = Timeslot()
    Syllabus_timeslot_2.day = u'1'
    Syllabus_timeslot_2.start = datetime.time(12, 30)
    Syllabus_timeslot_2.end = datetime.time(15, 45)
    Syllabus_timeslot_2.save()

    Syllabus_timeslot_3 = Timeslot()
    Syllabus_timeslot_3.day = u'1'
    Syllabus_timeslot_3.start = datetime.time(15, 30)
    Syllabus_timeslot_3.end = datetime.time(16, 45)
    Syllabus_timeslot_3.save()

    Syllabus_timeslot_4 = Timeslot()
    Syllabus_timeslot_4.day = u'1'
    Syllabus_timeslot_4.start = datetime.time(16, 30)
    Syllabus_timeslot_4.end = datetime.time(17, 35)
    Syllabus_timeslot_4.save()

    Syllabus_timeslot_5 = Timeslot()
    Syllabus_timeslot_5.day = u'1'
    Syllabus_timeslot_5.start = datetime.time(17, 35)
    Syllabus_timeslot_5.end = datetime.time(18, 34)
    Syllabus_timeslot_5.save()

    Syllabus_timeslot_6 = Timeslot()
    Syllabus_timeslot_6.day = u'1'
    Syllabus_timeslot_6.start = datetime.time(4, 30)
    Syllabus_timeslot_6.end = datetime.time(5, 35)
    Syllabus_timeslot_6.save()

    Syllabus_timeslot_7 = Timeslot()
    Syllabus_timeslot_7.day = u'2'
    Syllabus_timeslot_7.start = datetime.time(15, 30)
    Syllabus_timeslot_7.end = datetime.time(16, 45)
    Syllabus_timeslot_7.save()

    tutor1.available.add(Syllabus_timeslot_1)
    tutor1.available.add(Syllabus_timeslot_5)
    tutor1.available.add(Syllabus_timeslot_7)

    #Processing model: GradingCategory

    from syllabus.classroom.models import GradingCategory

    Syllabus_gradingcategory_1 = GradingCategory()
    Syllabus_gradingcategory_1.lower = 0.0
    Syllabus_gradingcategory_1.value = u'F'
    Syllabus_gradingcategory_1.save()

    Syllabus_gradingcategory_2 = GradingCategory()
    Syllabus_gradingcategory_2.lower = 10.0
    Syllabus_gradingcategory_2.value = u'F'
    Syllabus_gradingcategory_2.save()

    Syllabus_gradingcategory_3 = GradingCategory()
    Syllabus_gradingcategory_3.lower = 20.0
    Syllabus_gradingcategory_3.value = u'F'
    Syllabus_gradingcategory_3.save()

    Syllabus_gradingcategory_4 = GradingCategory()
    Syllabus_gradingcategory_4.lower = 30.0
    Syllabus_gradingcategory_4.value = u'F'
    Syllabus_gradingcategory_4.save()

    Syllabus_gradingcategory_5 = GradingCategory()
    Syllabus_gradingcategory_5.lower = 40.0
    Syllabus_gradingcategory_5.value = u'F'
    Syllabus_gradingcategory_5.save()

    Syllabus_gradingcategory_6 = GradingCategory()
    Syllabus_gradingcategory_6.lower = 50.0
    Syllabus_gradingcategory_6.value = u'F'
    Syllabus_gradingcategory_6.save()

    Syllabus_gradingcategory_7 = GradingCategory()
    Syllabus_gradingcategory_7.lower = 60.0
    Syllabus_gradingcategory_7.value = u'D'
    Syllabus_gradingcategory_7.save()

    Syllabus_gradingcategory_8 = GradingCategory()
    Syllabus_gradingcategory_8.lower = 70.0
    Syllabus_gradingcategory_8.value = u'C'
    Syllabus_gradingcategory_8.save()

    Syllabus_gradingcategory_9 = GradingCategory()
    Syllabus_gradingcategory_9.lower = 80.0
    Syllabus_gradingcategory_9.value = u'B'
    Syllabus_gradingcategory_9.save()

    Syllabus_gradingcategory_10 = GradingCategory()
    Syllabus_gradingcategory_10.lower = 90.0
    Syllabus_gradingcategory_10.value = u'A'
    Syllabus_gradingcategory_10.save()

    Syllabus_gradingcategory_11 = GradingCategory()
    Syllabus_gradingcategory_11.lower = 99.0
    Syllabus_gradingcategory_11.value = u'A'
    Syllabus_gradingcategory_11.save()

    #Processing model: GradingScale

    from syllabus.classroom.models import GradingScale

    Syllabus_gradingscale_1 = GradingScale()
    Syllabus_gradingscale_1.name = u'tens'
    Syllabus_gradingscale_1.save()

    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_1)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_2)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_3)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_4)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_5)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_6)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_7)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_8)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_9)
    Syllabus_gradingscale_1.categories.add(Syllabus_gradingcategory_10)

    Syllabus_gradingscale_2 = GradingScale()
    Syllabus_gradingscale_2.name = u'default'
    Syllabus_gradingscale_2.save()

    Syllabus_gradingscale_2.categories.add(Syllabus_gradingcategory_1)
    Syllabus_gradingscale_2.categories.add(Syllabus_gradingcategory_7)
    Syllabus_gradingscale_2.categories.add(Syllabus_gradingcategory_8)
    Syllabus_gradingscale_2.categories.add(Syllabus_gradingcategory_9)
    Syllabus_gradingscale_2.categories.add(Syllabus_gradingcategory_10)

    Syllabus_gradingscale_3 = GradingScale()
    Syllabus_gradingscale_3.name = u''
    Syllabus_gradingscale_3.save()

    Syllabus_gradingscale_3.categories.add(Syllabus_gradingcategory_1)
    Syllabus_gradingscale_3.categories.add(Syllabus_gradingcategory_7)
    Syllabus_gradingscale_3.categories.add(Syllabus_gradingcategory_8)
    Syllabus_gradingscale_3.categories.add(Syllabus_gradingcategory_9)
    Syllabus_gradingscale_3.categories.add(Syllabus_gradingcategory_11)

    #Processing model: WeightCategory

    from syllabus.classroom.models import WeightCategory

    Syllabus_weightcategory_1 = WeightCategory()
    Syllabus_weightcategory_1.category = u'assignment'
    Syllabus_weightcategory_1.percentage = 30
    Syllabus_weightcategory_1.save()

    Syllabus_weightcategory_2 = WeightCategory()
    Syllabus_weightcategory_2.category = u'test'
    Syllabus_weightcategory_2.percentage = 70
    Syllabus_weightcategory_2.save()

    #Processing model: Weight

    from syllabus.classroom.models import Weight

    Syllabus_weight_1 = Weight()
    Syllabus_weight_1.name = u''
    Syllabus_weight_1.save()

    Syllabus_weight_1.categories.add(Syllabus_weightcategory_1)
    Syllabus_weight_1.categories.add(Syllabus_weightcategory_2)

    #Processing model: Post

    from syllabus.messages.models import Post

    Syllabus_post_1 = Post()
    Syllabus_post_1.author = auth_user_1
    Syllabus_post_1.body = u"Damn.. that's pretty cool"
    Syllabus_post_1.datePosted = datetime.datetime(2012, 8, 3, 9, 27, 31, 290568)
    Syllabus_post_1.kind = u'image'
    Syllabus_post_1.save()

    Syllabus_post_1.files.add(Syllabus_file_5)

    #Processing model: Topic

    from syllabus.messages.models import Topic

    Syllabus_topic_1 = Topic()
    Syllabus_topic_1.title = u'Does this work?'
    Syllabus_topic_1.body = u'It sure does! And you can upload things too! Check it out...'
    Syllabus_topic_1.datePosted = datetime.datetime(2012, 8, 3, 9, 27, 31, 298009)
    Syllabus_topic_1.author = auth_user_1
    Syllabus_topic_1.save()

    Syllabus_topic_1.replies.add(Syllabus_post_1)
    Syllabus_topic_1.read.add(auth_user_1)

    #Processing model: Grade

    from syllabus.classroom.models import Grade

    Syllabus_grade_1 = Grade()
    Syllabus_grade_1.student = auth_user_1
    Syllabus_grade_1.event = Syllabus_event_1
    Syllabus_grade_1.score = 40.0
    Syllabus_grade_1.save()

    Syllabus_grade_2 = Grade()
    Syllabus_grade_2.student = auth_user_1
    Syllabus_grade_2.event = Syllabus_event_5
    Syllabus_grade_2.score = 45.0
    Syllabus_grade_2.save()

    Syllabus_grade_3 = Grade()
    Syllabus_grade_3.student = auth_user_1
    Syllabus_grade_3.event = Syllabus_event_6
    Syllabus_grade_3.score = 87.0
    Syllabus_grade_3.save()

    #Processing model: Interest

    from syllabus.academia.models import Interest
    
    interest1 = Interest()
    interest1.name = 'Physics'
    interest1.abbrv = 'PHYS'
    interest1.save()

    interest2 = Interest()
    interest2.name = 'English'
    interest2.abbrv = 'ENG'
    interest2.save()
    
    #Processing model: ClassProfile

    from syllabus.academia.models import ClassProfile

    Syllabus_classprofile_1 = ClassProfile()
    Syllabus_classprofile_1.name = u'GEN PHYSICS'
    Syllabus_classprofile_1.fullName = u''
    Syllabus_classprofile_1.units = 4
    Syllabus_classprofile_1.description = u'a hard physics course'
    Syllabus_classprofile_1.interest = interest1
    Syllabus_classprofile_1.number = 22
    Syllabus_classprofile_1.save()

    Syllabus_classprofile_2 = ClassProfile()
    Syllabus_classprofile_2.name = u'Who gives a shit'
    Syllabus_classprofile_2.fullName = u'Who gives a shit'
    Syllabus_classprofile_2.units = 3
    Syllabus_classprofile_2.description = u"It's some fucking english class"
    Syllabus_classprofile_2.interest = interest2
    Syllabus_classprofile_2.number = 20
    Syllabus_classprofile_2.save()


    major_requirement_1.courses.add(Syllabus_classprofile_1)
    tutor1.courses.add(Syllabus_classprofile_1)

    #Processing model: Class

    from syllabus.classroom.models import Class

    Syllabus_class_1 = Class()
    Syllabus_class_1.location = u'Broida 1640'
    Syllabus_class_1.syllabus = u'<div><p><span>Welcome to the third quarter of the core sequence in General Physics! &nbsp;This quarter extends your understanding of Mechanics from laws that govern how one or two rigid objects move to laws that govern how flexible, and even fluid, objects move; and how motion of and within a simple fluid object, an ideal gas, can ultimately be explained in terms of the motion of rigid objects that comprise it! &nbsp;It\'s a complex, but deeply rewarding, narrative that will give you a glimpse of why it seems possible, by firmly grounding our thinking in quantitative observation, to come up with a Theory of Everything :) <br></span></p><p><br></p><p>My name is Alec Aivazis and I am your lecturer for this course. Our graduate student assistant is Jessica Clayton. She will run the problem sessions.  I welcome you to contact me with questions about Physics any time.  I will do my best to respond e-mail within 24 hours, but can offer no guarantees and am never offended by reminders.  I can offer you immediate attention during my office hours*, Mondays between 5 and 7 pm in 2419 Broida (x2449), or by appointment. Jessica Clayton will also be available to field your physics questions in person in the Physics Study Room on Mondays from 2 to 5 pm. Problem sets will be assigned Mondays (except for the first, which is assigned below) and will be due the following Monday at 9 pm. <br></p><p><span><br></span></p><p>There are two required texts for the course:<br><a href="http://www.amazon.com/dp/0070350485/">An Introduction to Mechanics</a>, by Kleppner and Kolenkow&nbsp;(ISBN 0-07-035048-5)<br><a href="http://www.amazon.com/dp/0471804584/">Physics, vol. 1, 4th Edition</a>, by Halliday, Resnick&nbsp;and Krane&nbsp;(ISBN <span>0-471-80458-4</span>)&nbsp;<br>and a couple of others which I recommend highly and will draw from in lecture:<br><a href="http://www.amazon.com/dp/0393099369/">Vibrations and Waves</a>, by A.P. French (ISBN 0-393-09936-9)<br><a href="http://www.amazon.com/dp/0199572194/">The Laws of Thermodynamics: A very short introduction</a>, by P. Atkins (ISBN 0-19-957219-9)</p><p><span>Lectures are Tuesdays and Thursdays from 11:00-12:15 am in Broida 1640. <br></span></p><p><span><br></span></p><p><span>Problem sessions are Fridays from 3:00 - 3:50 pm or&nbsp;4:00 - 4:50 pm in Phelps 1508. &nbsp;Both lectures and one problem session are mandatory.</span></p><p><br>I encourage you to start on homeworks on Wednesday or Thursday evenings in the PSR after hours (6 to 8 pm), when it is manned by the PSR Fellows - senior physics students dedicated to helping you, their junior colleagues, succeed in and enjoy the major.&nbsp;</p><p><span>Homework turned in up to&nbsp;<span>three days</span>&nbsp;late will have 50% of the score removed. Homework turned in more than three days late will be noted, but no points for credit will be given. &nbsp;You may work with others on the problems, but you must write up solutions independently of one another.<br><br>Neatness and clarity in the presentation of your homework are <span>essential</span>. &nbsp;If it is not possible to understand your logic from your write-up in the short amount of time (a minute or two) available to grade it, it will not be graded and you will receive no credit for that problem. &nbsp;The first time this happens, you will be given the opportunity to clarify your logic and resubmit, but a resubmission, like a late submission, will only be awarded 50% credit.&nbsp;</span></p><p><span>The plan for grading is: Problem sets, 30%; Midterms (Tuesday, May 1 and&nbsp;<span>Tuesday, May. 29</span>), 20%; Final (Wednesday, June 13 @ 12-3 pm), 50%.<br><br>*If you are a student with disabilities and would like to discuss special academic accommodations, please contact me during my office hours. &nbsp; <br></span></p></div>'
    Syllabus_class_1.gradingScale = Syllabus_gradingscale_1
    Syllabus_class_1.weights = Syllabus_weight_1
    Syllabus_class_1.profile = Syllabus_classprofile_1
    Syllabus_class_1.term = Syllabus_term_1
    Syllabus_class_1.maxOccupancy = 80
    Syllabus_class_1.save()




    Syllabus_class_1.professor.add(auth_user_1)
    Syllabus_class_1.messageBoard.add(Syllabus_topic_1)
    Syllabus_class_1.events.add(Syllabus_event_1)
    Syllabus_class_1.events.add(Syllabus_event_2)
    Syllabus_class_1.events.add(Syllabus_event_3)
    Syllabus_class_1.events.add(Syllabus_event_4)
    Syllabus_class_1.events.add(Syllabus_event_5)
    Syllabus_class_1.events.add(Syllabus_event_6)
    Syllabus_class_1.times.add(Syllabus_timeslot_2)
    Syllabus_class_1.times.add(Syllabus_timeslot_3)
    Syllabus_class_1.times.add(Syllabus_timeslot_7)

    Syllabus_class_2 = Class()
    Syllabus_class_2.location = u'Broida 234'
    Syllabus_class_2.syllabus = u''
    Syllabus_class_2.gradingScale = Syllabus_gradingscale_2
    Syllabus_class_2.weights = None
    Syllabus_class_2.maxOccupancy = 80
    Syllabus_class_2.profile = Syllabus_classprofile_1
    Syllabus_class_2.term = Syllabus_term_1
    Syllabus_class_2.save()

    Syllabus_class_2.professor.add(auth_user_1)
    Syllabus_class_2.times.add(Syllabus_timeslot_1)

    #Processing model: Section

    from syllabus.classroom.models import Section

    Syllabus_section_1 = Section()
    Syllabus_section_1.name = u'234'
    Syllabus_section_1.qlass = Syllabus_class_1
    Syllabus_section_1.location = u'Broida 1640'
    Syllabus_section_1.maxOccupancy = 15
    Syllabus_section_1.save()

    Syllabus_section_1.times.add(Syllabus_timeslot_1)
    Syllabus_section_1.times.add(Syllabus_timeslot_2)

    Syllabus_section_2 = Section()
    Syllabus_section_2.name = u'12345'
    Syllabus_section_2.qlass = Syllabus_class_2
    Syllabus_section_2.location = u'fdg'
    Syllabus_section_2.maxOccupancy = 15
    Syllabus_section_2.save()

    Syllabus_section_2.times.add(Syllabus_timeslot_3)
    Syllabus_section_2.tas.add(auth_user_1)

    Syllabus_section_3 = Section()
    Syllabus_section_3.name = u'5678'
    Syllabus_section_3.qlass = Syllabus_class_2
    Syllabus_section_3.location = u'broida 2034'
    Syllabus_section_3.maxOccupancy = 18
    Syllabus_section_3.save()

    Syllabus_section_3.times.add(Syllabus_timeslot_3)
    Syllabus_section_3.tas.add(auth_user_1)

    #Processing model: Enrollment

    from syllabus.academia.models import Enrollment

    Syllabus_enrollment_1 = Enrollment()
    Syllabus_enrollment_1.student = auth_user_1
    Syllabus_enrollment_1.section = Syllabus_section_1
    Syllabus_enrollment_1.grade = u''
    Syllabus_enrollment_1.save()



    #Processing model: Department

    from syllabus.academia.models import Department

    Syllabus_department_1 = Department()
    Syllabus_department_1.name = u'Phsyics'
    Syllabus_department_1.save()

    Syllabus_department_1.interests.add(interest1)
    Syllabus_department_1.interests.add(interest2)
    
    college_1.departments.add(Syllabus_department_1)

    #Re-processing model: Class

    
