from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import redirect

class IndexPageView(TemplateView):

    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 55}))