from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    Responsible for HTTP interaction
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        #product_code = body["product_code"]
        print(body)

        #Business rule
        print('Im on View')
        #HTTP response
        return HttpResponse(status_code=200, body={"Python": "here"})
    