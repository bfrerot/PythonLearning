########## API- HTTP ##########


### "requests" module

import requests


## .get()
reply = requests.get('http://localhost:3000')


## .status_code
print(reply.status_code)
# 200

print(requests.codes.__dict__)
# {'name': 'status_codes', 'continue': 100, 'CONTINUE': 100, 'switching_protocols': 101, 'SWITCHING_PROTOCOLS': 101, 'processing': 102, 'PROCESSING': 102, 'early-hints': 102, 'EARLY-HINTS': 102, 'checkpoint': 103, 'CHECKPOINT': 103, 
#  'uri_too_long': 414, 'URI_TOO_LONG': 414, 'request_uri_too_long': 122, 'REQUEST_URI_TOO_LONG': 122, 'ok': 200, 'OK': 200, 'okay': 200, 'OKAY': 200, 'all_ok': 200, 'ALL_OK': 200, 'all_okay': 200, 'ALL_OKAY': 200, 'all_good': 200, 
#  'ALL_GOOD': 200, '\\o/': 200, '✓': 200, 'created': 201, 'CREATED': 201, 'accepted': 202, 'ACCEPTED': 202, 'non_authoritative_info': 203, 'NON_AUTHORITATIVE_INFO': 203, 'non_authoritative_information': 203, 
#  'NON_AUTHORITATIVE_INFORMATION': 203, 'no_content': 204, 'NO_CONTENT': 204, 'reset_content': 205, 'RESET_CONTENT': 205, 'reset': 205, 'RESET': 205, 'partial_content': 206, 'PARTIAL_CONTENT': 206, 'partial': 206,
#  'PARTIAL': 206, 'multi_status': 207, 'MULTI_STATUS': 207, 'multiple_status': 207, 'MULTIPLE_STATUS': 207, 'multi_stati': 207, 'MULTI_STATI': 207, 'multiple_stati': 207, 'MULTIPLE_STATI': 207, 
#  'already_reported': 208, 'ALREADY_REPORTED': 208, 'im_used': 226, 'IM_USED': 226, 'multiple_choices': 300, 'MULTIPLE_CHOICES': 300, 'moved_permanently': 301, 'MOVED_PERMANENTLY': 301, 'moved': 301, 'MOVED': 301,
#  '\\o-': 301, 'found': 302, 'FOUND': 302, 'see_other': 303, 'SEE_OTHER': 303, 'other': 303, 'OTHER': 303, 'not_modified': 304, 'NOT_MODIFIED': 304, 'use_proxy': 305, 'USE_PROXY': 305, 'switch_proxy': 306, 'SWITCH_PROXY': 306,
#  'temporary_redirect': 307, 'TEMPORARY_REDIRECT': 307, 'temporary_moved': 307, 'TEMPORARY_MOVED': 307, 'temporary': 307, 'TEMPORARY': 307, 'permanent_redirect': 308, 'PERMANENT_REDIRECT': 308, 'resume_incomplete': 308, 'RESUME_INCOMPLETE': 308,
#  'resume': 308, 'RESUME': 308, 'bad_request': 400, 'BAD_REQUEST': 400, 'bad': 400, 'BAD': 400, 'unauthorized': 401, 'UNAUTHORIZED': 401, 'payment_required': 402, 'PAYMENT_REQUIRED': 402, 'payment': 402, 'PAYMENT': 402, 'forbidden': 403, 
#  'FORBIDDEN': 403, 'not_found': 404, 'NOT_FOUND': 404, '-o-': 404, '-O-': 404, 'method_not_allowed': 405, 'METHOD_NOT_ALLOWED': 405, 'not_allowed': 405, 'NOT_ALLOWED': 405, 'not_acceptable': 406, 'NOT_ACCEPTABLE': 406, 'proxy_authentication_required': 407,
#  'PROXY_AUTHENTICATION_REQUIRED': 407, 'proxy_auth': 407, 'PROXY_AUTH': 407, 'proxy_authentication': 407, 'PROXY_AUTHENTICATION': 407, 'request_timeout': 408, 'REQUEST_TIMEOUT': 408, 'timeout': 408, 'TIMEOUT': 408, 'conflict': 409, 'CONFLICT': 409,
#  'gone': 410, 'GONE': 410, 'length_required': 411, 'LENGTH_REQUIRED': 411, 'precondition_failed': 412, 'PRECONDITION_FAILED': 412, 'precondition': 428, 'PRECONDITION': 428, 'request_entity_too_large': 413, 'REQUEST_ENTITY_TOO_LARGE': 413, 
#  'content_too_large': 413, 'CONTENT_TOO_LARGE': 413, 'request_uri_too_large': 414, 'REQUEST_URI_TOO_LARGE': 414, 'unsupported_media_type': 415, 'UNSUPPORTED_MEDIA_TYPE': 415, 'unsupported_media': 415, 'UNSUPPORTED_MEDIA': 415, 'media_type': 415, 
#  'MEDIA_TYPE': 415, 'requested_range_not_satisfiable': 416, 'REQUESTED_RANGE_NOT_SATISFIABLE': 416, 'requested_range': 416, 'REQUESTED_RANGE': 416, 'range_not_satisfiable': 416, 'RANGE_NOT_SATISFIABLE': 416, 'expectation_failed': 417, 
#  'EXPECTATION_FAILED': 417, 'im_a_teapot': 418, 'IM_A_TEAPOT': 418, 'teapot': 418, 'TEAPOT': 418, 'i_am_a_teapot': 418, 'I_AM_A_TEAPOT': 418, 'misdirected_request': 421, 'MISDIRECTED_REQUEST': 421, 'unprocessable_entity': 422, 
#  'UNPROCESSABLE_ENTITY': 422, 'unprocessable': 422, 'UNPROCESSABLE': 422, 'unprocessable_content': 422, 'UNPROCESSABLE_CONTENT': 422, 'locked': 423, 'LOCKED': 423, 'failed_dependency': 424, 'FAILED_DEPENDENCY': 424, 'dependency': 424,
#  'DEPENDENCY': 424, 'unordered_collection': 425, 'UNORDERED_COLLECTION': 425, 'unordered': 425, 'UNORDERED': 425, 'too_early': 425, 'TOO_EARLY': 425, 'upgrade_required': 426, 'UPGRADE_REQUIRED': 426, 'upgrade': 426, 'UPGRADE': 426, 
#  'precondition_required': 428, 'PRECONDITION_REQUIRED': 428, 'too_many_requests': 429, 'TOO_MANY_REQUESTS': 429, 'too_many': 429, 'TOO_MANY': 429, 'header_fields_too_large': 431, 'HEADER_FIELDS_TOO_LARGE': 431, 'fields_too_large': 431, 
#  'FIELDS_TOO_LARGE': 431, 'no_response': 444, 'NO_RESPONSE': 444, 'none': 444, 'NONE': 444, 'retry_with': 449, 'RETRY_WITH': 449, 'retry': 449, 'RETRY': 449, 'blocked_by_windows_parental_controls': 450, 'BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS': 450,
#  'parental_controls': 450, 'PARENTAL_CONTROLS': 450, 'unavailable_for_legal_reasons': 451, 'UNAVAILABLE_FOR_LEGAL_REASONS': 451, 'legal_reasons': 451, 'LEGAL_REASONS': 451, 'client_closed_request': 499, 'CLIENT_CLOSED_REQUEST': 499, 
#  'internal_server_error': 500, 'INTERNAL_SERVER_ERROR': 500, 'server_error': 500, 'SERVER_ERROR': 500, '/o\\': 500, '✗': 500, 'not_implemented': 501, 'NOT_IMPLEMENTED': 501, 'bad_gateway': 502, 'BAD_GATEWAY': 502, 'service_unavailable': 503, 
#  'SERVICE_UNAVAILABLE': 503, 'unavailable': 503, 'UNAVAILABLE': 503, 'gateway_timeout': 504, 'GATEWAY_TIMEOUT': 504, 'http_version_not_supported': 505, 'HTTP_VERSION_NOT_SUPPORTED': 505, 'http_version': 505, 'HTTP_VERSION': 505, 
#  'variant_also_negotiates': 506, 'VARIANT_ALSO_NEGOTIATES': 506, 'insufficient_storage': 507, 'INSUFFICIENT_STORAGE': 507, 'bandwidth_limit_exceeded': 509, 'BANDWIDTH_LIMIT_EXCEEDED': 509, 'bandwidth': 509, 'BANDWIDTH': 509, 
#  'not_extended': 510, 'NOT_EXTENDED': 510, 'network_authentication_required': 511, 'NETWORK_AUTHENTICATION_REQUIRED': 511, 'network_auth': 511, 'NETWORK_AUTH': 511, 'network_authentication': 511, 'NETWORK_AUTHENTICATION': 511}


## .headers[]

print(reply.headers)
# {'X-Powered-By': 'tinyhttp', 'Content-Length': '13', 'Content-Type': 'text/html;charset=utf-8', 'Last-Modified': 'Mon, 29 Sep 2025 08:15:15 GMT', 'Cache-Control': 'no-store', 'Date': 'Mon, 29 Sep 2025 08:22:14 GMT',
#  'Connection': 'keep-alive', 'Keep-Alive': 'timeout=5'}

print(reply.headers['Content-Type'])
# text/html;charset=utf-8


## .text

print(reply.text)
# CARS DATABASE

reply2 = requests.get('http://localhost:3000/cars/2')
print(reply2.text)
# {
#   "id": "2",
#   "brand": "Chevrolet",
#   "model": "Camaro",
#   "production_year": 1988,
#   "convertible": true
# }



### retrieve a specific parameter

# sometimes, API is not fully open
reply2 = requests.get('http://localhost:3000/cars/2/model')
print(reply2.text)
# Not Found

# thru a "manual" python code
url = "http://localhost:3000/cars/2"

r = requests.get(url)
if r.ok:
    data = r.json()
    model = data.get("model")
    prod_year = data.get("production_year")
    print("Model :", model)
    print("Production year :", prod_year)
else:
    print("Erreur", r.status_code, r.text)
# Model : Camaro
# Production year : 1988


### timeout - requests.exceptions.Timeout
import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')
finally:
    print(reply.text)
# Here is your data, my Master!
# CARS DATABASE


try:
    reply = requests.get('http://localhost:3000', timeout=0.00000000000000000001)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')
    print(reply.text)
# Sorry, Mr. Impatient, you didn't get your data


### wrong listening port - requests.exceptions.ConnectionError

import requests

try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
else:
    print('Everything fine!')
# Nobody's home, sorry!



### invalid url - requests.exceptions.InvalidURL

import requests

try:
    reply = requests.get('http:////////////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')
# Recipient unknown!



### request module Exception tree

'''
RequestException
|___HTTPError
|___ConnectionError
|   |___ProxyError	
|   |___SSLError	
|___Timeout
|   |___ConnectTimeout
|   |___ReadTimeout
|___URLRequired
|___TooManyRedirects
|___MissingSchema
|___InvalidSchema
|___InvalidURL
|   |___InvalidProxyURL
|___InvalidHeader
|___ChunkedEncodingError
|___ContentDecodingError
|___StreamConsumedError
|___RetryError
|___UnrewindableBodyError
'''