"""Company Info Views"""
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def about_us(request):
    """View to return shipping and returns info page"""
    return render(request, 'company/about_us.html')


def privacy_policy(request):
    """View to return shipping and returns info page"""
    return render(request, 'company/privacy_policy.html')


def faq_page(request):
    """View to return FAQ's page"""
    return render(request, 'help/faqs.html')


def shipping_returns(request):
    """View to return shipping and returns info page"""
    return render(request, 'help/shipping_returns.html')


def contact(request):
	
	if request.method == 'POST':
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
			message_data['subject'], message, '', ['ganiyatbadara@gmail.com'])

	    messages.info(request, (
			f'Your message has been sent, we will contact you \
				via { email_address } as soon as possible.'))
	return render(request, 'home/index.html')

	return render(request, 'contact_us/contact_us.html')
