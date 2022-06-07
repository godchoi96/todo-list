from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.generic import ListView, DeleteView

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
        print(todoList)
        return JsonResponse(data=todoList, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteAPIView(DeleteView):
    # DeleteAPIView 클래스의 의도
    """
    클라이언트 단에서는 삭제하였으나 서버 단에서는 삭제되어있지 않는다.
    따라서 똑같이 DB에서 삭제될 수 있도록 DeleteView의 delete 메소드를 오버라이딩한다.
    """

    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)