# branch 명령어

독립된 작업 흐름을 만들기 위하여 `branch`를 사용

작업이 완료가 되면 `merge`를 통해 병합한다.

## 브랜치

### 브랜치 생성

```bash
$ git branch <브랜치 이름>
```

### 브랜치 이동

```bash
hajae@Stevia MINGW64 ~/OneDrive/바탕 화면/TIL/210706_git특강/웹프로젝트 (master)
$ git checkout test
Switched to branch 'test'
(test) $
```

### 브랜치 생성 및 이동

```bash
$ git checkout -b test-1
Switched to a new branch 'test-1'
(test-1) $
```

### 브랜치 목록

```bash
$ git branch
* master
  test
```

### 브랜치 병합

```bash
(master) $ git merge test
```

* **메인이 되는 브랜치로 이동한 이후 특정 작업 브랜치를 병합!**

### 브랜치 삭제

```bash
$ git branch -d test
Deleted branch test (was fc034c1)
```

* 생성과 삭제 모두 어디서든 가능하나 자기 자신이 삭제는 불가