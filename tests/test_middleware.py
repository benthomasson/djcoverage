from djcoverage import coverage_middleware


def get_response(request):
    return dict()


def test_middleware():

    middleware = coverage_middleware(get_response)
    middleware(dict())
