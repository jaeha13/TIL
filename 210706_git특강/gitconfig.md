# gitconfig

>Git 설정 파일

# Global

> ~/.gitconfig 파일에 기록된 설정들

```bash
# 현재 설정 알아보기
$ git config --global -l
```

### 필수

#### user 정보

commit시 Author로 기록되기 위해서 초기에 설정할 필요가 있다.

```bash
# 초기 설정
$ git config --global user.email "use_email"
$ git config --global user.name "user_name"

# user 정보 확인
$ git config --global user.email
hajaeyeon13@gmail.com
$ git config --global user.name
jaeha13

```

## 선택

### credential(Github 인증 등)

```bash
$ git config --global credential.provider generic
```

* 현재 git bash 2.32에 발생된 버그를 해결하기 위함

### 커밋 에디터 설정

> 기존 vim에서 vs code로 변경

```bash
$ git config --global core.editor "code --wait"
```

