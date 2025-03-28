from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class PositionSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            degree = request.POST.get('degree')
            if not degree:
                return HttpResponseBadRequest("Необходимо указать диплом")

            if degree == "bachelor":
                request.position = "Библиотекарь"
                request.salary = 50000
            elif degree == "master":
                request.position = "Главный библиотекарь"
                request.salary = 70000
            elif degree == "docent":
                request.position = "Директор"
                request.salary = 90000
            else:
                request.position = "Стажер"
                request.salary = 30000