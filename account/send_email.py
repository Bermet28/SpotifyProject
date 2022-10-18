from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Для активации аккаунта перейдите по ссылке: {full_link}',
        'bemochka29@gmail.com',
        [user],
        fail_silently=False)
