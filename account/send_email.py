from django.core.mail import send_mail, EmailMessage


# def send_confirmation_email(user, code):
#     full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
#     send_mail(
#         'Здравствуйте активируйте ваш аккаунт!',
#         f'Для активации аккаунта перейдите по ссылке: {full_link}',
#         'bemochka29@gmail.com',
#         [user],
#         fail_silently=False)

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
