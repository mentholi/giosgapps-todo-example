from django.views import generic
from django.shortcuts import redirect

from giosgappsdk import GiosgAppSDK


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        secret = 'secret key loaded from some safe place'
        sdk = GiosgAppSDK(request, secret)
        if sdk.is_app_request:
            return redirect('todo-list')
        return self.render_to_response(context)


class AboutPage(generic.TemplateView):
    template_name = "about.html"
