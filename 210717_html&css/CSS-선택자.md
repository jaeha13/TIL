# CSS

## selector(선택자)

스타일을 적용하기 위해 대상을 선택하는 방법

```css
selector {
    속성명: 속성값;
    속성명: 속성값;
    속성명: 속성값;
    속성명: 속성값;
    속성명: 속성값;
    ..
}
```

* 태그 선택자 : 태그명으로 선택

  ```css
  p {font-size: 12px; font-family: "돋음";}
  ```

* id 선택자 : 태그가 가진 id 속성으로 선택 -> unique 한 값

  ```css
  #idname {clear: both; float: left;}
  ```

* class 선택자 : 태그가 갖는 class 속성으로 선택 -> unique 할 필요 없음

  ```css
  .classname {color: red;}
  ```

* 속성 선택자 : 태그가 가진 속성을 통해 선택

  ```css
  [속성] : 지정한 속성을 가지고 있는 요소를 찾아 스타일을 적용
  [속성 ~= 값] : 속성 값이 여러 개의 값 중 하나만 일치해도 적용
  [속성 ^= 값] : 속성 값이 지정한 문자로 시작하는 속성에 적용
  [속성 $= 값] : 속성 값이 지정한 문자로 끝나는 속성에 적용
  [속성 *= 값] : 속성 값 중 '값'의 일부가 포함되어 있는 속성에 적용
  ```

* 자식 선택자 : 어떤 태그의 자식에 해당되는 태그 선택

  > 자식 : 어떤 태그의 content에 포함된 태그

  ```html
  <body>
      <h1></h1>
      <hr>
      <form></form>
  </body>
  <!--body 부모; h1/hr/form 자식-->
  ```

  ```css
  section > p {color: blue;}
  ```

* 자손 선택자 : 자식을 포함하여 모든 자손을 선택

  ```html
  <body>
      <h1></h1>
      <hr>
      <form>
      	<input>
      </form>
  </body>
  <!--body 조상; h1/hr/form/input 자손-->
  ```

  ```css
  section p {color: blue;}
  ```

* 형제 선택자 : 모든 형제 관계를 선택

  ```html
  <body>
      <h1></h1>
      <hr>
      <form>
      	<input>
      </form>
  </body>
  <!--h1/hr/form 형제-->
  ```

  * 인접 형제 선택자

  ```css
  h1 + p {text-decoration: underline;}
  ```

  * 형제 선택자

  ```css
  h1 ~ p {text-decoration: underline;}
  ```

* 전체 선택자 : * 를 통해 모두 선택

  ```css
  * {margin: 0; padding: 0;}
  ```



빌트인 선택자의 경우 성격이 조금 다름!!

* 빌트인 선택자 : 웹 문서의 소스에는 실제로 존재하지 않지만 필요에 의해 임의로 가상의 서택자를 지정하여 사용하는 것!

