# Django

## request

### [ query 문자열 ]

> 웹 클라이언트인 브라우저에서 웹 서버에게 URL 문자열을 가지고 요청할 때 추가로 전달되는 name 과 value 로 구성되는 문자열



#### < W3C 에서 정한 표준 규격 >

* name = value&name=value&... 구성

* 영문자와 숫자는 그대로 구성되지만 이외의 문자들은 '%16진수코드값'으로 변환되어 구성됨
* 공백은 + 문자 또는 %20 또는 %2C 로 변환되어 구성됨



#### < query 문자열이 웹서버로 전달되는 방식 >

* GET 방식
  요청시 URL 문자열 뒤에 ? 기호와 함께 추가되어 전달

  > Query 문자열이 외부로 보여지고 길이 제한이 있음

  * `default`
  * `Query 문자열 없이 요청`할 때도 자동으로 GET
  * 브라우저에서 `직접 URL 문자열을 입력`해서 요청하는 것 - GET
  * `<a>` 텍스트나 이미지를 클릭해서 요청하는 것 - GET
  * `location.href` 속성으로 요청하는 것 - GET
  * `<form>` 로 요청하는 경우 - GET 가능

  ```python
  request.GET		# dict
  ```

* POST 방식
  요청 바디 안에 담겨서 전달

  > Query 문자열이 외부로 보여지지 않고 길이 제한 없음

  * `<form>` 로 요청하는 경우 - POST
  * `{% csrf_token %}` 반드시 필요!
    - 외부에서 들어오는 정당하지 않은 요청 위조를 방지

  ```python
  request.POST	# dict
  ```
