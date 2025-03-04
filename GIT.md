# Git Commands

## Git ignore

- A ``.gitignore file`` tells Git which files or folders to ignore (not track or commit). It’s often used to exclude temporary files, build outputs, and sensitive data (like passwords or API keys) from the repository.

## Remove file/folder in remote 

Remove directory from Git and local

```sh
$ git rm -r one-of-the-directories // This deletes from filesystem
$ git commit . -m "Remove duplicated directory"
$ git push origin <your-git-branch> (typically 'master', but not always)
```

Remove directory from Git but NOT local

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

## Git Tag

- When ever we release new functionality ex:- as package distribution (poetry build) to Nexus. We have to create a Git tag for it

```sh
# Create Git tag
git tag <tag> # ex:- v0.0.1

# Create Git tag with description
git tag <tag> -a

# Git tags
git tag

# Push git tag
git push origin <tag>
```

>**Note**: Create PR to to merge this new branch changes to main/develop branch