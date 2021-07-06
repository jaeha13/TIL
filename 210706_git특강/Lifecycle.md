# Lifecycle

> 파일이 가질 수 있는 상태

* Untracked
* Tracked
  * Unmodifed -> status에 나오지 않음
  * Modified
  * Staged

```bash
$ git status
On branch master
# 변경된 사항들 in Staging Area(두번째 통)
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
# 수정/삭제/생성
        new file:   git_1.md
        new file:   markdown.md
        new file:   python project
        new file:   "\354\213\244\354\212\265.md"
# 변경된 사항들 in Working Directory(첫번째 통)
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  (commit or discard the untracked or modified content in submodules)
        deleted:    git_1.md
        deleted:    markdown.md
        modified:   python project (new commits, untracked content)
        deleted:    "\354\213\244\354\212\265.md"

# 변경된 사항들 in Working Directory(첫번째 통)
# 한번도 git에 들어가지 않은 것
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        d.txt
```

![image-20210706105252878](C:/Users/hajae/OneDrive/%EB%B0%94%ED%83%95%20%ED%99%94%EB%A9%B4/image-20210706105252878.png)

