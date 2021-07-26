# Django 템플릿

## 템플릿 변수

>{{ 변수명 }}

값을 표현하는 역할

* 변수의 속성에 점근할 경우 -> . 사용

## 템플릿 태그(로직)

>{% tag %}
>
>{% tag %} ... {% endtag %}

**[e.g.]**

* 위조 요청 방지

```python
{% csrf_token %}
```

* 정적파일 관리

```python
{% load static %}
```

* for 문 tag

```python
{% for num in nums %}
	# something to do
{% endfor %}
```

* if 문 tag

```python
{% if name == '게스트' %}
	# something to do
{% else %}
	# something else to do
{% endif %}
```

* ...etc
