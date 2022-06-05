from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView

from todo.models import Todo


class ListAPIView(ListView):
    #  ListAPIView 클래스의 의도
    """
    모델에서부터 name과 todo를 가져온다.
    가져오고 클라이언트 단에서 todoList라는 변수로 참조하기 때문에 todoList로 매핑해서 JsonResponse를 한다.
    """

    model = Todo

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)