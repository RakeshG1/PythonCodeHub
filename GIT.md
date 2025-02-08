# Git Commands

## Git ignore

- A ``.gitignore file`` tells Git which files or folders to ignore (not track or commit). It’s often used to exclude temporary files, build outputs, and sensitive data (like passwords or API keys) from the repository.

## Remove file/folder in remote Repo

```sh
$ git rm -r --cached dist
```

- Removes the dist folder from Git tracking (staging/index). After committing and pushing, it also removes dist from the remote repo.

## Holding the changes

```sh
$ git stash
```

- git stash temporarily saves your uncommitted changes (like putting them “on hold”), so you can switch branches or revert to a clean working state without losing your current edits. You can later reapply those stashed changes with git stash pop or git stash apply.

## Show existing branches

```sh
git branch 
```

## Create new branch

```sh
git branch new-branch
```

## Checkout to new branch

```sh
git checkout new-branch
```

## Commit to new branch

```sh
git add *
git commit -m "new changes"
git push origin new-branch
```

## Revert a commit 

- Which already pushed to remote Repo

```sh
$ git revert commit-id
# $ git push --force
# $ git push
$ git push --set-upstream origin dev
```

>**Note**: Create PR to to merge this new branch changes to main/develop branch