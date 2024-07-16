
import coverage
cov = coverage.Coverage()


def coverage_middleware(get_response):

    def middleware(request):
        cov.start()
        response = get_response(request)
        cov.stop()
        cov.save()
        return response

    return middleware
