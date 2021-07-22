# JavaScript

브라우저에서 처리되는 프로그래밍 언어

> 목적: 클라이언트 단에서의 동적처리 하기

* HTML 만으로는 구현할 수 없는 `동적인 웹 페이지` 구성을  하고자할 때 HTML 소스 안에 구현하는 프로그래밍 언어

  ```
  동적 웹 페이지
  서버에 있는 데이터들을 스크립트에 의해 가공처리한 후 생성되어 전달괴는 웹 페이지
  ```

HTML(내용) + CSS(디자인) + JavaScript(동적 내용)

## JavaScript 정의 방법

```html
<head>
	<script>...</script>
</head>
<body>
    <script>...</script>
</body>
```

* html 문서 어디에 작성해도 상관 없지만 가급적 **\</body> 태그의 바로 위**에 삽입하는 것을 권장

## 구문

### 변수 생성 방법

> var 변수명 = 값

### 오류 확인 방법

javascript는 에러를 페이지에 표시하지 않을 뿐 에러 경고나 정보를 직접적으로 알려주지 않고 다른 작업들을 수행

> 개발자 도구 -> console 을 통해 확인

### 주석처리

* 단일행 : // ~~~~
* 다중행 : /* ~~~~ */

### 데이터 타입

| type         | 예시                               |   이름    |
| ------------ | ---------------------------------- | :-------: |
| 숫자타입     | 10, 20, 3.14                       |  number   |
| 문자(열)타입 | 'a', "a", "100"                    |  string   |
| 부울타입     | true, false                        |  boolean  |
| 객체타입     | {key = value, ...}<br />new Data() |  object   |
| undefined    | undefined                          | undefined |
| null         |                                    |   null    |

**boolean**

```
Python	: True, False
JS		: true, false
R		: TRUE(T), FALSE(F)
```

### 연산자

* 수치 연산자

  * 사칙 연산자: +, -, *, /, %

  * 증감 연산자 -> 단항 연산자: ++, --

    > 변수++ : 다른 일 한 후에 1 증가시킴
    > ++변수 : 먼저 1 증가시키고 다른 일 수행
    >
    > 변수--   : 다른 일 한 후에 1 감소시킴
    > --변수   : 먼저 1 감소시키고 다른 일 수행

  * 문자열 연산자: + : 문자열을 합하여 하나의 문자열 생성

* 비교 연산자

  * <, >, <=, >=, ==, ===, !=, !==

    > ==  	: 타입과 관계없이 내용만 확인
    >
    > ===	: 타입과 내용 모두 확인

* 조건 연산자

  * and : &&, or : ||, not : !, 삼항연산자 : ?

    > && 과 || 를 이용한 조건식 처리
    >
    > ```javascript
    > if (num % 2 == 0)
    >     document.writeln(num + "는 짝수");
    > else
    >     document.writeln(num + "는 홀수")
    > 
    > // 같은 의미의 논리 연산자 이용한 조건식
    > num % 2 == 0 && document.writeln(num + "는 짝수")
    > num % 2 == 0 || document.writeln(num + "는 홀수")
    > ```

    * boolean 식 && boolean 식 => 앞이 참이면 뒤에도 실행
      앞이 참이면 뒤에 실행시켜서 참인지 확인해야 하므로 뒤 실행 O
    * boolean 식 || boolean 식 => 앞이 거짓이면 뒤에 실행
      앞이 참이면 뒤에 실행시켜서 확인할 필요 없으므로 뒤 실행 X

* 대입 연산자

  * =, +=, -=, *=, /=, %=

* 비트 연산자

  * and : &, or : |, xor : ^, 좌우이동: <<, >>

* 타입 점검 연산자

  * typeof, instanceof

* 삭제 연산자

  * delete

### 제어문(조건문, 반복문, 분기문)

* 조건문 : if-else 또는 논리 연산자(&&, ||)

* 다중 분기문 : switch

* 반복문 : for, while, do-while

  * for 문

    1. Tranditional For

       ```javascript
       for (초기식; 조건식; 증감식)
           /* do something */
       ```

       > 반복횟수를 정해놓고 반복할 때
       > 변수값을 정해진 룰대로 변화시키면서 반복할 때

    2. For Each

       ```javascript
       for (변수 선언 in 배열 or 객체)
           /* do something */ // index가 전달됨
       ```

* 분기 제어문 : break, continue

* 예외처리 구문 : try-catch-finally

### 함수생성과 활용

#### 함수 정의 방법1

```javascript
function myFunction(인자, ..){
	/* do something */	
}
```

#### 함수 정의 방법2

```javascript
var myFunction = function(인자, ..){
    /* do something */
}
```

### 배열

> 파이썬의 리스트와 비슷

### 객체생성 방법

#### 방법1

* { k = v, k = v, ...}

#### 방법 2

* new 생성자함수

## DOM 프로그래밍

이벤트 처리 구현
특정 이벤트가 발생했을 때 처리

## AJAX 프로그래밍

> 비동기적인 웹 애플리케이션의 제작을 위한 웹 개발 기법

< django와 함께 공부할 예정 >

## MAP 프로그래밍

지도출려하는 프로그래밍