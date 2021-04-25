from datetime import datetime
from celery.task import task
from celery import shared_task
from django.http.response import HttpResponse 
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
from django.apps import apps
app = Celery('task',broker="redis://localhost:6379/0")

def mail(mail_list,asset,expire,name):
    subject = 'welcome to GFG world'
    message = f'Hi {name}, You have got {asset}. for {expire}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = mail_list
    send_mail( subject, message, email_from, recipient_list )



@task
def send_notifiction():
    from .models import AssignAsset
    # model = apps.get_model('dashboard', 'AssignAsset')
    queryset=AssignAsset.objects.filter(expire_on__lte=datetime.now().date(),release=True)
    mail_list=[]
    for employee in queryset:
        email=employee.employee.email
        name=employee.employee.name
        asset =employee.asset
        expire=employee.expire_on
        mail_list.append(email)
        mail(mail_list,asset,expire,name)
        print("hello")


app.conf.beat_schedule = {
"run-me-every-ten-seconds": {
"task": "task.send_notifiction",
"schedule": 5.0
 }
} 
        
        




    


    