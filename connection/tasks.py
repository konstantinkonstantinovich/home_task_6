from celery import shared_task

from django.core.mail import send_mail


@shared_task
def add():
    return 10 + 5


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_mail_task(subject, message, email):
    send_mail(subject, message, email, ['admin@example.com'])
