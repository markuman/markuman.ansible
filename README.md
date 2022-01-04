# Ansible Collection - markuman.scm

![CI Status](https://woodpecker.aws.osuv.de/api/badges/m/markuman.scm/status.svg)

Documentation for the collection.


## markuman.scm.gitlab_merge_request_comment

* Task works only if `CI_OPEN_MERGE_REQUESTS` is defined
* `api_token` parameter can also be read from ENV `ANSIBLE_GITLAB_API_TOKEN`
* It's designed to act like a notification bot for merge requests
* Designed to run in a GitLab CI/CD Pipeline
  * Project ID and Merge Request ID are taken from ENV

```yml

    - name: post message
      markuman.scm.gitlab_merge_request_comment:
        api_url: gitlab.com
        comment: |
          Summary

          | some | table |
          | --- | --- |
          | yes | 🐧 |
```