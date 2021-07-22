# JavaScript의 API

### review(js 구문)

**document** - write, writeln

**window** - alert, confirm, prompt

**new Array()** -> 객체를 변수에 담아서

**new Date()** -> 객체를 변수에 담아서

**console** - log

**Math** - random, floor



## 활용

DOM

```javascript
document.getElementsByTagName("태그명")
// return 배열
document.getElementById("id속성값")
// return 태그객체
document.getElementsByClassName("class 속성명")
// return 배열
document.querySelector("CSS선택자")
// return 태그객체
document.querySelecotrAll("CSS선택자")
// return 배열
```

### 이벤트 모델

> JavaScript는 이벤트 드리븐 모델에 기반하여 동작함
> 웹 페이지 안에서 발생한 여러가지 사건(이벤트)에 따라 대응하는 처리(이벤트 핸들러)를 호출하여 실행하는 모델

#### 용어

* event: 어떤 사건 - '사용자가 클릭했을 때'
* event target: 이벤트가 일어날 객체 - '클릭한 버튼'
* event type: 이벤트의 종류 - '클릭'
* event handler: 이벤트가 발생했을 때 동작하는 코드 - '클릭 발생 시 일어나는 일'

#### 종류

* 인라인 이벤트 모델

  `태그 내 직접` JavaScript 명령어를 작성하는 방법

  ```javascript
  <태그 on이벤트="함수로가자()">이렇게저렇게<\태그>	// ? 왜 /는 빨간색이 뜨지??
  <script>
  	function 함수로가자() {
      	// something to do
  }    
  <\script>
  ```

* 전역적 이벤트 모델 (고전 이벤트 모델)

  `스크립트 내`에서 `태그id 찾아서` 이벤트 function 만들기

  ```javascript
  <script>
  	태그id.event = function(){};
  <\script>
  ```

* 표준 이벤트 모델

  `스크립트 내`에서 `태그 변수 불러와` 이벤트를 직접 지정

  ```javascript
  <script>
  태그변수.addEvent******('이벤트명', function(){})
  <\script>
  ```

  - 이벤트 핸들러 등록시

    ```javascript
    addEventListener(eventName, handler, useCapture)
    ```
  
  - 이벤트 핸들러 해제시
  
    ```javascript
    removeEventListener(eventName, handler)
    ```
    
    

