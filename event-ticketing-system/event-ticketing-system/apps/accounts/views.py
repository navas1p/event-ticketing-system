from django.shortcuts import render

# Create your views here.
def login(request):
	# Minimal login view that renders the login template
	if request.method == 'POST':
		# Placeholder: authentication should be implemented
		return render(request, 'accounts/login.html', {'message': 'Login submitted (not implemented).'})
	return render(request, 'accounts/login.html')
