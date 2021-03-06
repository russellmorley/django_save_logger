from monitors import format_log_message, request_info, response_info, exception_info

logger = logging.getLogger( __name__ )

class ApiCallEventMiddleware(object):

  def __init__(self):
    pass

  def process_request(self, request):
    logger.info(
      format_log_message('request', request.user, request_info(request), '')
    )
    return None

  def process_response(self, request, response):
    logger.info(
      format_log_message(
        'response', 
        request.user, 
        request_info(request), 
        response_info(response)
    )
    return response

  def process_exception(self, request, exception):
    logger.info(
      format_log_message(
        'response_exception', 
        request.user, 
        request_info(request), 
        exception_info(exception)
    )
    return None


class ApiCallEventPersistMiddleware(ApiCallEventMiddleware):
  '''
  rely on process_response for practice's to track api calls
  def process_request(self, request):
    ret =  super(ApiCallEventPersistMiddleware, self).process_request(request)
    SystemEventModel.objects.create(
      type='request',
      user_pk = request.user.id,
      request_info=request_info(request),
    )
    return ret
  '''

  def process_response(self, request, response):
    ret =  super(ApiCallEventPersistMiddleware, self).process_response(request, response)
    SystemEventModel.objects.create(
      type='response',
      user_pk = request.user.id,
      request_info=request_info(request),
      other_info = response_info(response)
    )
    return ret

  '''
  def process_exception(self, request, exception):
    ret = super(ApiCallEventPersistMiddleware, self).process_exception(request, exception)
    SystemEventModel.objects.create(
      type='response_exception',
      user_pk = request.user.id,
      request_info=request_info(request),
      other_info = exception_info(exception)
    )
    return ret
  '''
