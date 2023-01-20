"""Company Info Views"""
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
		"""View to return contact us page"""
		# Help from Scottish Coder YouTube Tutorial - link in README
		if request.method == 'POST':
				# Send contact form to Gmail Account
				first_name = request.POST.get('first_name')
				last_name = request.POST.get('last_name')
				subject = request.POST.get('subject')
				email_address = request.POST.get('email_address')
				message = request.POST.get('message')

				message_data = {
					'first_name': first_name,
					'last_name': last_name,
					'email_address': email_address,
					'subject': subject,
					'message': message,
				}
				message = '''
				From: {}
				New message: {}
				'''.format(message_data['email_address'], message_data['message'])

				send_mail(
					message_data['subject'], message, '', ['testing@gmail.com'])

				messages.info(request, (
					f'Your message has been sent, we will contact you \
						via { email_address } as soon as possible.'))
				return render(request, 'home/index.html')

		return render(request, 'contact_us/contact_us.html')