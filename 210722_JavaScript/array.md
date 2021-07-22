# array

## 배열 생성

```javascript
var a = [1, 2, 3, 4, 5]
var a = new Array()
var a = new Array(10)
// 10개 element를 위한 방을 생성
```

## 활용

```javascript
var array_example1 = new Array("hello", "world")

var array_example2 = ["hello", "world"]
```

* push : 원소 넣기
* [index] : index를 통해 넣기
* pop : 마지막 원소 빼기

> cf) for each 를 활용할 경우
>
> ```javascript
> var a2 = [10, '가나다', true, , 3.5];
> for (var i in a2)
>     document.write("<h4>" + "index: " + i + typeof a2[i] + ":" + a2[i] + "</h4>")
> // javascript의 경우 undefined 원소의 index를 제외한 나머지 인덱스를 i에 보내줌(?)
> 
> // 실행결과
> index: 0 number:10
> index: 1 string:가나다
> index: 2 boolean:true
> index: 4 number:3.5
> ```

> 자바스크립트 참고 사이트
>
> [KoXo](http://koxo.com/lang/js/index.html)
> [w3schools](https://www.w3schools.com/js/default.asp)

### (window.)alert("")

경고창에 띄움!

> cf. document.write("") : document 영역에 표시!

