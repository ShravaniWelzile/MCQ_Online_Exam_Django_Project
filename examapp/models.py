from django.db import models

# Create your models here.
class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    qno=models.IntegerField()
    qname=models.CharField(max_length=20)
    op1=models.CharField(max_length=20)
    op2=models.CharField(max_length=20)
    op3=models.CharField(max_length=20)
    op4=models.CharField(max_length=20)
    correct_ans=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    

class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=20)
    semail=models.EmailField()
    password=models.CharField(max_length=20)
    smob_no=models.BigIntegerField()


# class Result(models.Model):
#     rid = models.AutoField(primary_key=True)
#     marks = models.IntegerField()
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     total_questions = models.IntegerField(default=0)
#     percentage = models.FloatField(default=0)
#     correct_answers = models.IntegerField(default=0)
#     status = models.CharField(max_length=10, default="FAIL")

class Result(models.Model):
    sname = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    marks = models.IntegerField()

    class Meta:
        db_table = 'result'


# class Result(models.Model):
#     rid = models.AutoField(primary_key=True)

#     student = models.ForeignKey(
#         Student,
#         on_delete=models.CASCADE
#     )

#     subject = models.CharField(max_length=50)

#     total_questions = models.IntegerField(default=0)
#     correct_answers = models.IntegerField()
#     marks = models.IntegerField()

#     percentage = models.FloatField()

#     status = models.CharField(
#         max_length=10,
#         choices=[
#             ('PASS', 'PASS'),
#             ('FAIL', 'FAIL')
#         ]
#     )

#     exam_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student} - {self.subject} - {self.marks}"


class AdminAccount(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username