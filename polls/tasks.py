from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Author, Quote


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
def reminder_task(email, reminder_text):
    send_mail('Notification:', reminder_text, email, ['admin@example.com'])


@shared_task
def parse_quotes():
    r = requests.get('https://quotes.toscrape.com')
    it = 0
    while it < 5:
        soup = BeautifulSoup(r.content, features='html.parser')
        articles = soup.findAll('div', {'class': 'quote'})
        for i in articles:
            author = i.find('small').text
            quote = i.find('span', {'class': 'text'}).text
            if not Author.objects.filter(name=author):
                a = Author(name=author)
                a.save()
                q = Quote(quote=quote, author=a)
                q.save()
                it += 1
            else:
                if not Quote.objects.filter(quote=quote):
                    a = Author.objects.get(name=author)
                    q = Quote(quote=quote, author=a)
                    q.save()
                    it += 1
            if it == 5 or it > 5:
                break
        page = soup.find('li', {'class': 'next'})
        if page is None:
            if quote is None:
                send_mail('Notification:',
                          'Goood job', 'Vova@gmail.com', ['admin@example.com'])
                return
            break
        page_next = page.a.get('href')
        r = requests.get('https://quotes.toscrape.com' + page_next)
