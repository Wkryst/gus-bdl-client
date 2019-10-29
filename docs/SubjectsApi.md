# swagger_client.SubjectsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subjects_by_id_get**](SubjectsApi.md#subjects_by_id_get) | **GET** /subjects/{id} | Temat o zadanym / Subject with selected Id
[**subjects_get**](SubjectsApi.md#subjects_get) | **GET** /subjects | Lista tematów / Subjects list
[**subjects_metadata_get**](SubjectsApi.md#subjects_metadata_get) | **GET** /subjects/metadata | Metadane / Metadata
[**subjects_search_get**](SubjectsApi.md#subjects_search_get) | **GET** /subjects/search | Wyszukiwanie tematów wg nazwy / Searching subjects by name


# **subjects_by_id_get**
> SubjectDetails subjects_by_id_get(id, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Temat o zadanym / Subject with selected Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubjectsApi()
id = 'id_example' # str | Id tematu / Subject Id
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Temat o zadanym / Subject with selected Id
    api_response = api_instance.subjects_by_id_get(id, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubjectsApi->subjects_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id tematu / Subject Id | 
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SubjectDetails**](SubjectDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subjects_get**
> SubjectList subjects_get(parent_id=parent_id, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Lista tematów / Subjects list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubjectsApi()
parent_id = 'parent_id_example' # str | Identyfikator tematu nadrzędnego / Parent subject's Id (optional)
page = 0 # int | Indeks strony / Page index (optional) (default to 0)
page_size = 10 # int | Rozmiar strony / Page size (optional) (default to 10)
sort = 'sort_example' # str | Oczekiwana kolejność / Desired order (optional)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Lista tematów / Subjects list
    api_response = api_instance.subjects_get(parent_id=parent_id, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubjectsApi->subjects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| Identyfikator tematu nadrzędnego / Parent subject&#39;s Id | [optional] 
 **page** | **int**| Indeks strony / Page index | [optional] [default to 0]
 **page_size** | **int**| Rozmiar strony / Page size | [optional] [default to 10]
 **sort** | **str**| Oczekiwana kolejność / Desired order | [optional] 
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SubjectList**](SubjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subjects_metadata_get**
> Metadata subjects_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Metadane / Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubjectsApi()
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Metadane / Metadata
    api_response = api_instance.subjects_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubjectsApi->subjects_metadata_get: %s\n" % e)
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

# **subjects_search_get**
> SubjectList subjects_search_get(name, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Wyszukiwanie tematów wg nazwy / Searching subjects by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubjectsApi()
name = 'name_example' # str | Fragment nazwy tematu / Subject's name fragment
page = 0 # int | Indeks strony / Page index (optional) (default to 0)
page_size = 10 # int | Rozmiar strony / Page size (optional) (default to 10)
sort = 'sort_example' # str | Oczekiwana kolejność / Desired order (optional)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Wyszukiwanie tematów wg nazwy / Searching subjects by name
    api_response = api_instance.subjects_search_get(name, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubjectsApi->subjects_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Fragment nazwy tematu / Subject&#39;s name fragment | 
 **page** | **int**| Indeks strony / Page index | [optional] [default to 0]
 **page_size** | **int**| Rozmiar strony / Page size | [optional] [default to 10]
 **sort** | **str**| Oczekiwana kolejność / Desired order | [optional] 
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SubjectList**](SubjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

