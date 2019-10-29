# swagger_client.AttributesApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributes_by_id_get**](AttributesApi.md#attributes_by_id_get) | **GET** /attributes/{id} | Atrybut o zadanym Id / Atrribute with selected Id
[**attributes_get**](AttributesApi.md#attributes_get) | **GET** /attributes | Lista atrybutów / Attributes list
[**attributes_metadata_get**](AttributesApi.md#attributes_metadata_get) | **GET** /attributes/metadata | Metadane / Metadata


# **attributes_by_id_get**
> Attribute attributes_by_id_get(id, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Atrybut o zadanym Id / Atrribute with selected Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
id = 56 # int | Id atrybutu / Attribute Id
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Atrybut o zadanym Id / Atrribute with selected Id
    api_response = api_instance.attributes_by_id_get(id, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->attributes_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id atrybutu / Attribute Id | 
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_get**
> AttributeList attributes_get(sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Lista atrybutów / Attributes list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
sort = 'sort_example' # str | Oczekiwana kolejność / Desired order (optional)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Lista atrybutów / Attributes list
    api_response = api_instance.attributes_get(sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Oczekiwana kolejność / Desired order | [optional] 
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**AttributeList**](AttributeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_metadata_get**
> Metadata attributes_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Metadane / Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Metadane / Metadata
    api_response = api_instance.attributes_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->attributes_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**Metadata**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

