import datetime

from polls.models import LogModel


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.find('admin') != -1:
            return response
        path = request.path
        method = request.method
        timestamps = datetime.datetime.now()

        LogModel.objects.create(path=path, method=method,
                                timestamps=timestamps)
        return response
