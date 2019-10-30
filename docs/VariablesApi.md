# swagger_client.VariablesApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variables_by_id_get**](VariablesApi.md#variables_by_id_get) | **GET** /variables/{id} | Zmienna o zadanym Id / Variable with selected Id
[**variables_get**](VariablesApi.md#variables_get) | **GET** /variables | Lista zmiennych / Variables list
[**variables_metadata_get**](VariablesApi.md#variables_metadata_get) | **GET** /variables/metadata | Metadane / Metadata
[**variables_search_get**](VariablesApi.md#variables_search_get) | **GET** /variables/search | Wyszukiwanie zmiennych wg warunków/ Search variables with condition


# **variables_by_id_get**
> VariableDetails variables_by_id_get(id, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Zmienna o zadanym Id / Variable with selected Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
id = 56 # int | Id zmiennej / Variable Id
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Zmienna o zadanym Id / Variable with selected Id
    api_response = api_instance.variables_by_id_get(id, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->variables_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id zmiennej / Variable Id | 
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**VariableDetails**](VariableDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_get**
> VariableList variables_get(subject_id=subject_id, level=level, year=year, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Lista zmiennych / Variables list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
subject_id = 'subject_id_example' # str | Id tematu / Subject Id (optional)
level = 56 # int | Poziom / Level (optional)
year = [56] # list[int] | Lista lat / Years list (optional)
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
    # Lista zmiennych / Variables list
    api_response = api_instance.variables_get(subject_id=subject_id, level=level, year=year, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Id tematu / Subject Id | [optional] 
 **level** | **int**| Poziom / Level | [optional] 
 **year** | [**list[int]**](int.md)| Lista lat / Years list | [optional] 
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

[**VariableList**](VariableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_metadata_get**
> Metadata variables_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Metadane / Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Metadane / Metadata
    api_response = api_instance.variables_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->variables_metadata_get: %s\n" % e)
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

# **variables_search_get**
> VariableList variables_search_get(subject_id=subject_id, name=name, level=level, year=year, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Wyszukiwanie zmiennych wg warunków/ Search variables with condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
subject_id = 'subject_id_example' # str | Id tematu nadrzędnego / Parent's subject Id (optional)
name = 'name_example' # str | Tekst w polach N1...N5 / Text in N1... N5 fields (optional)
level = 56 # int | Poziom / Level (optional)
year = [56] # list[int] | Lista lat / Years list (optional)
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
    # Wyszukiwanie zmiennych wg warunków/ Search variables with condition
    api_response = api_instance.variables_search_get(subject_id=subject_id, name=name, level=level, year=year, page=page, page_size=page_size, sort=sort, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->variables_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Id tematu nadrzędnego / Parent&#39;s subject Id | [optional] 
 **name** | **str**| Tekst w polach N1...N5 / Text in N1... N5 fields | [optional] 
 **level** | **int**| Poziom / Level | [optional] 
 **year** | [**list[int]**](int.md)| Lista lat / Years list | [optional] 
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

[**VariableList**](VariableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

