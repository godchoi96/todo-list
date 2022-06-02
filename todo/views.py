from django.views.generic import TemplateView


class TDView(TemplateView):
    template_name = 'todo/todo.html'
