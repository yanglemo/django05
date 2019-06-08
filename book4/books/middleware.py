from django.http import HttpResponse


def simple_middleware(get_response):
    def middleware(request):
        # username=request.COOKIES.get('username')
        # if username is None:
        #     print('username is None')
        #     return HttpResponse('哥们,你没有登陆哎')
        print('before request 1-1')
        response = get_response(request)
        print('after request/response 1-2')
        return response

    return middleware


def simple_middleware2(get_response):
    def middleware(request):
        # username = request.COOKIES.get('username')
        # if username is None:
        #     print('username is None')
        #     return HttpResponse('哥们,你没有登陆哎')
        print('before request 2-1')
        response = get_response(request)
        print('after request/response 2-2')
        return response

    return middleware
