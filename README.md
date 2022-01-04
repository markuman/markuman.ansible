# Ansible Collection - markuman.devops

![CI Status](https://woodpecker.aws.osuv.de/api/badges/ansible_collections/markuman.devops/status.svg)

Documentation for the collection.

`ansible-galaxy collection install markuman.devops`

# markuman.devops

Covers/plan gitlab (_just one_), gitea and woodpecker modules and sentry (_glitchtip_) callback plugin (_so far_).

## markuman.devops.gitlab_merge_request_comment

* Task works only if `CI_OPEN_MERGE_REQUESTS` is defined
* `api_token` parameter can also be read from ENV `ANSIBLE_GITLAB_API_TOKEN`
* It's designed to act like a notification bot for merge requests
* Designed to run in a GitLab CI/CD Pipeline
  * On other environments you must possibly fake the requires ENV variables

```yml

    - name: post message
      markuman.devops.gitlab_merge_request_comment:
        api_url: gitlab.com
        comment: |
          Summary

          | some | table |
          | --- | --- |
          | yes | 🐧 |
```

## markuman.devops.gitea_pull_request_comment

* Tasks works only if `CI_REPO` and `CI_PULL_REQUST` is defined
* `api_token` parameter can also be read from ENV `ANSIBLE_GITEA_API_TOKEN`
* It's designed to act like a notification bot for merge requests
* Designed to run in a Woodpecker CI/CD Pipeline
  * On other environments you must possibly fake the requires ENV variables

```yml
    - name: post message
      markuman.devops.gitea_pull_request_comment:
        api_url: git.osuv.de
        comment: |
          Summary

          | some | table |
          | --- | --- |
          | yes | 🐧 |
```

# Contribute

* Issues and Pull Requests: https://github.com/markuman/markuman.devops
* Origin: https://git.osuv.de/ansible_collections/markuman.devops