from django.views.generic import TemplateView

class IndexPageView(TemplateView):

    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
