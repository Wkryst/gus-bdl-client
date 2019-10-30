# swagger_client.DataApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_by_unit_get**](DataApi.md#data_by_unit_get) | **GET** /data/by-unit/{unit-id} | Dane dla jednej jednostki terytorialnej / Data for single territorial unit
[**data_by_variable_get**](DataApi.md#data_by_variable_get) | **GET** /data/by-variable/{var-id} | Dane dla jednej zmiennej / Data for single variable
[**data_localities_by_unit_get**](DataApi.md#data_localities_by_unit_get) | **GET** /data/localities/by-unit/{unit-id} | Dane dla jednej miejscowości statystycznej / Data for single statistical locality
[**data_localities_by_variable_get**](DataApi.md#data_localities_by_variable_get) | **GET** /data/localities/by-variable/{var-id} | Dane dla miejscowości statystycznych dla jednej zmiennej / Data for statistical localities for single variable
[**data_metadata_get**](DataApi.md#data_metadata_get) | **GET** /data/metadata | Metadane / Metadata


# **data_by_unit_get**
> SingleUnitData data_by_unit_get(unit_id, var_id, year=year, aggregate_id=aggregate_id, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Dane dla jednej jednostki terytorialnej / Data for single territorial unit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
unit_id = 'unit_id_example' # str | Id jednostki terytorialnej / Territorial unit id
var_id = [56] # list[int] | Lista Id zmiennych / Variable Id list
year = [56] # list[int] | Lista lat / Years list (optional)
aggregate_id = 1 # int | Id poziomu agregacji / Aggregation level Id (optional) (default to 1)
page = 0 # int | Indeks strony / Page index (optional) (default to 0)
page_size = 10 # int | Rozmiar strony / Page size (optional) (default to 10)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Dane dla jednej jednostki terytorialnej / Data for single territorial unit
    api_response = api_instance.data_by_unit_get(unit_id, var_id, year=year, aggregate_id=aggregate_id, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_by_unit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **str**| Id jednostki terytorialnej / Territorial unit id | 
 **var_id** | [**list[int]**](int.md)| Lista Id zmiennych / Variable Id list | 
 **year** | [**list[int]**](int.md)| Lista lat / Years list | [optional] 
 **aggregate_id** | **int**| Id poziomu agregacji / Aggregation level Id | [optional] [default to 1]
 **page** | **int**| Indeks strony / Page index | [optional] [default to 0]
 **page_size** | **int**| Rozmiar strony / Page size | [optional] [default to 10]
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SingleUnitData**](SingleUnitData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_by_variable_get**
> SingleVariableData data_by_variable_get(var_id, year=year, unit_parent_id=unit_parent_id, unit_level=unit_level, aggregate_id=aggregate_id, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Dane dla jednej zmiennej / Data for single variable

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
var_id = 56 # int | Id zmiennej / Variable Id
year = [56] # list[int] | Lista lat / Years list (optional)
unit_parent_id = 'unit_parent_id_example' # str | Identyfikator nadrzędnej jednostki terytorialnej / Paren's territorial units Id (optional)
unit_level = 56 # int | Poziom jednostek terytorialnych / Territorial units level (optional)
aggregate_id = 1 # int | Id poziomu agregacji / Aggregation level Id (optional) (default to 1)
page = 0 # int | Indeks strony / Page index (optional) (default to 0)
page_size = 10 # int | Rozmiar strony / Page size (optional) (default to 10)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Dane dla jednej zmiennej / Data for single variable
    api_response = api_instance.data_by_variable_get(var_id, year=year, unit_parent_id=unit_parent_id, unit_level=unit_level, aggregate_id=aggregate_id, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_by_variable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_id** | **int**| Id zmiennej / Variable Id | 
 **year** | [**list[int]**](int.md)| Lista lat / Years list | [optional] 
 **unit_parent_id** | **str**| Identyfikator nadrzędnej jednostki terytorialnej / Paren&#39;s territorial units Id | [optional] 
 **unit_level** | **int**| Poziom jednostek terytorialnych / Territorial units level | [optional] 
 **aggregate_id** | **int**| Id poziomu agregacji / Aggregation level Id | [optional] [default to 1]
 **page** | **int**| Indeks strony / Page index | [optional] [default to 0]
 **page_size** | **int**| Rozmiar strony / Page size | [optional] [default to 10]
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SingleVariableData**](SingleVariableData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_localities_by_unit_get**
> SingleUnitData data_localities_by_unit_get(unit_id, var_id, year=year, aggregate_id=aggregate_id, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Dane dla jednej miejscowości statystycznej / Data for single statistical locality

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
unit_id = 'unit_id_example' # str | Id miejscowości statystycznej / Statistical locality id
var_id = [56] # list[int] | Lista Id zmiennych / Variable Id list
year = [56] # list[int] | Lista lat / Years list (optional)
aggregate_id = 1 # int | Id poziomu agregacji / Aggregation level Id (optional) (default to 1)
page = 0 # int | Indeks strony / Page index (optional) (default to 0)
page_size = 10 # int | Rozmiar strony / Page size (optional) (default to 10)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Dane dla jednej miejscowości statystycznej / Data for single statistical locality
    api_response = api_instance.data_localities_by_unit_get(unit_id, var_id, year=year, aggregate_id=aggregate_id, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_localities_by_unit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **str**| Id miejscowości statystycznej / Statistical locality id | 
 **var_id** | [**list[int]**](int.md)| Lista Id zmiennych / Variable Id list | 
 **year** | [**list[int]**](int.md)| Lista lat / Years list | [optional] 
 **aggregate_id** | **int**| Id poziomu agregacji / Aggregation level Id | [optional] [default to 1]
 **page** | **int**| Indeks strony / Page index | [optional] [default to 0]
 **page_size** | **int**| Rozmiar strony / Page size | [optional] [default to 10]
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SingleUnitData**](SingleUnitData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_localities_by_variable_get**
> SingleVariableData data_localities_by_variable_get(var_id, unit_parent_id, year=year, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Dane dla miejscowości statystycznych dla jednej zmiennej / Data for statistical localities for single variable

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
var_id = 56 # int | Id zmiennej / Variable Id
unit_parent_id = 'unit_parent_id_example' # str | Identyfikator nadrzędnej jednostki terytorialnej / Paren's territorial units Id
year = [56] # list[int] | Lista lat / Years list (optional)
page = 0 # int | Indeks strony / Page index (optional) (default to 0)
page_size = 10 # int | Rozmiar strony / Page size (optional) (default to 10)
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Dane dla miejscowości statystycznych dla jednej zmiennej / Data for statistical localities for single variable
    api_response = api_instance.data_localities_by_variable_get(var_id, unit_parent_id, year=year, page=page, page_size=page_size, lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_localities_by_variable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_id** | **int**| Id zmiennej / Variable Id | 
 **unit_parent_id** | **str**| Identyfikator nadrzędnej jednostki terytorialnej / Paren&#39;s territorial units Id | 
 **year** | [**list[int]**](int.md)| Lista lat / Years list | [optional] 
 **page** | **int**| Indeks strony / Page index | [optional] [default to 0]
 **page_size** | **int**| Rozmiar strony / Page size | [optional] [default to 10]
 **lang** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept-Language\&quot; jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \&quot;Accept-Language\&quot; is ignored) | [optional] 
 **format** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \&quot;Accept\&quot; jest ignorowany) / Expected response content type - optional (if parameter specified, request header \&quot;Accept\&quot; is ignored) | [optional] 
 **accept_language** | **str**| Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \&quot;lang\&quot;, nagłówek \&quot;Accept-Language\&quot; zostanie ignorowany) / Expected response conent language - optional (if \&quot;lang\&quot; parameter is specified, the \&quot;Accept-Language\&quot; header will be ignored) | [optional] 
 **accept** | **str**| Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \&quot;format\&quot;, nagłówek \&quot;Accept\&quot; zostanie zignorowany) / Expected response content type - optional (if the \&quot;format\&quot; parameter is specified, the \&quot;Accept\&quot; header will be ignored) | [optional] 
 **if_none_match** | **str**| Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) | [optional] 
 **if_modified_since** | **str**| Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since | [optional] 

### Return type

[**SingleVariableData**](SingleVariableData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.api+json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_metadata_get**
> Metadata data_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Metadane / Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lang = 'lang_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept-Language\" jest ignorowany) / Expected response conent language - optional (if parameter specified, request header \"Accept-Language\" is ignored) (optional)
format = 'format_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr, nagłówek \"Accept\" jest ignorowany) / Expected response content type - optional (if parameter specified, request header \"Accept\" is ignored) (optional)
accept_language = 'accept_language_example' # str | Oczekiwany język odpowiedzi - opcjonalny (jeśli podano parametr \"lang\", nagłówek \"Accept-Language\" zostanie ignorowany) / Expected response conent language - optional (if \"lang\" parameter is specified, the \"Accept-Language\" header will be ignored) (optional)
accept = 'accept_example' # str | Oczekiwany format odpowiedzi - opcjonalny (jeśli podano parametr \"format\", nagłówek \"Accept\" zostanie zignorowany) / Expected response content type - optional (if the \"format\" parameter is specified, the \"Accept\" header will be ignored) (optional)
if_none_match = 'if_none_match_example' # str | Nagłówek warunkowego żadania If-None-Match (entity tag)/Conditional Requests header If-None-Match (entity tag) (optional)
if_modified_since = 'if_modified_since_example' # str | Nagłówek warunkowego żadania If-Modified-Since/Conditional Requests header If-Modified-Since (optional)

try:
    # Metadane / Metadata
    api_response = api_instance.data_metadata_get(lang=lang, format=format, accept_language=accept_language, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->data_metadata_get: %s\n" % e)
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

