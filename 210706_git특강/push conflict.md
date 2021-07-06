# push conflict

## 문제

원격에서 README.md를 직접 만들었을 경우

```bash
$ git push origin master
To github.com:jaeha13/TIL.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'github.com:jaeha13/TIL.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

## 원인

로컬(PC)과 원격(Github) 저장소의 (commit에 의한) 현재 버전관리가 다르다.

## 해결

버전을 맞춰주자!!

### 1. 원격저장소 내용 가져옴(pull)

```bash
$ git pull origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 666 bytes | 22.00 KiB/s, done.
From github.com:jaeha13/TIL
 * branch            master     -> FETCH_HEAD
   dfa34c8..e42e974  master     -> origin/master
Merge made by the 'recursive' strategy.
 README.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

### 2. 머지(merge) 커밋

> vim - CLI 환경 텍스트에디터
>
> 저장하기 위해서는 `esc` `:` `w` `q` 를 누르고 엔터`esc` `:` 
>
> `w` - write / `q` - quit

## 3. 다시 push

```bash
$ git push origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 499 bytes | 249.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To github.com:jaeha13/TIL.git
   e42e974..fbe65d0  master -> master
```

