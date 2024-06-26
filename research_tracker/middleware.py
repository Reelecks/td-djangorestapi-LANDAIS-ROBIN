from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [reverse('login_view'), reverse('register_view'), '/admin/']
        
        if not request.user.is_authenticated and request.path not in allowed_paths and not request.path.startswith('/admin/'):
            return redirect('login_view')
        
        response = self.get_response(request)
        return response
