

def coverage_middleware(get_response):

    def middleware(request):

        response = get_response(request)

        print('woo')

        return response


    return middleware
