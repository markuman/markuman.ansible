#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: gitea_pull_request_comment
short_description: write messages to gitea pull requests
description:
  - write messages to gitea pull requests.
  - works only if `CI_PULL_REQUEST` is defined
  - it's designed to run inside woodpecker ci/cd pipeline
version_added: "1.0.0"
author:
  - "Markus Bergholz (@markuman)"
options:
  comment:
    description:
      - Comment message.
    required: true
    type: str
  api_token:
    description:
      - API Token.
      - If not provided, it's read from ENV ANSIBLE_GITEA_API_TOKEN
    required: false
    type: str
  api_url:
    description:
      - URL of your gitea instance
    required: true
    type: str
requirements:
    - requests
'''

EXAMPLES = '''
    - name: post message
      markuman.scm.gitea_pull_request_comment:
        api_url: gitea.io
        comment: |
          Summary

          | some | table |
          | --- | --- |
          | yes | 🐧 |
'''

from ansible.module_utils.basic import AnsibleModule
import requests
import os


def main():
    module = AnsibleModule(
        argument_spec=dict(
            comment=dict(required=True, type='str'),
            api_token=dict(required=False, type='str', no_log=True),
            api_url=dict(required=True, type='str')
        )
    )

    comment = module.params.get("comment")
    api_token = module.params.get("api_token") or os.environ.get('ANSIBLE_GITEA_API_TOKEN')
    api_url = module.params.get("api_url")

    issue_id = os.environ.get('CI_PULL_REQUEST')

    if issue_id and api_token:

        repo = os.environ.get('CI_REPO')

        gitea_url = f'https://{api_url}/api/v1/repos/{repo}/issues/{issue_id}/comments'

        headers = {
            'Authorization': f'token {api_token}',
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }

        data = {
            'body': comment
        }

        x = requests.post(gitea_url, json=data, headers=headers)

        change = False
        if x.status_code == 201:
            change = True

        module.exit_json(changed=change, status=x.status_code)

    else:
        module.exit_json(changed=False, status=None)


if __name__ == '__main__':
    main()
