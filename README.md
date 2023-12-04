# Ansible Collection - markuman.ansible


Documentation for the collection.

`ansible-galaxy collection install markuman.ansible`

# markuman.ansible

Just everything I need that's not shipped somehwere else...

## markuman.ansible.gitlab_merge_request_comment

* Task works only if `CI_OPEN_MERGE_REQUESTS` is defined
* `api_token` parameter can also be read from ENV `ANSIBLE_GITLAB_API_TOKEN`
* It's designed to act like a notification bot for merge requests
* Designed to run in a GitLab CI/CD Pipeline
  * On other environments you must possibly fake the requires ENV variables

```yml

    - name: post message
      markuman.ansible.gitlab_merge_request_comment:
        api_url: gitlab.com
        comment: |
          Summary

          | some | table |
          | --- | --- |
          | yes | 🐧 |
```

## markuman.ansible.gitea_pull_request_comment

* Tasks works only if `CI_REPO` and `CI_PULL_REQUST` is defined
* `api_token` parameter can also be read from ENV `ANSIBLE_GITEA_API_TOKEN`
* It's designed to act like a notification bot for merge requests
* Designed to run in a Woodpecker CI/CD Pipeline
  * On other environments you must possibly fake the requires ENV variables

```yml
    - name: post message
      markuman.ansible.gitea_pull_request_comment:
        api_url: git.osuv.de
        comment: |
          Summary

          | some | table |
          | --- | --- |
          | yes | 🐧 |
```

# Contribute

* Issues and Pull Requests: https://github.com/markuman/markuman.ansible
* Origin: https://git.osuv.de/ansible_collections/markuman.ansible