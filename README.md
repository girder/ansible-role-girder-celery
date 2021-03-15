# girder.celery
[![Apache 2.0](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/girder/ansible-role-girder-celery/master/LICENSE)

An Ansible role to install a Celery worker.

## Requirements

Ubuntu 20.04+.

The Celery-using project itself has several requirements:
* It must be installable from a Git repository.
  * To support projects installed solely from PyPI,
    please [file an issue](https://github.com/girder/ansible-role-girder-celery/issues/new).
* It must be pip-installable.
* If it includes a `requirements.txt` file, that must list the
  requirement `.`, to also install the project itself.
* It must include `celery` as a requirement.
* It must have
  [a Celery app instance](https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#about-the-app-argument)
  in an importable location.

## Role Variables

| parameter               | required | default | comments                                                                   |
| ----------------------- | -------- | ------- | -------------------------------------------------------------------------- |
| `celery_app`            | yes      |         | The import path of the Celery project's app, as passed to `-A` or `--app`. |
| `celery_repository_url` | yes      |         | The HTTP URL of the Git repository with the Celery project.                |
| `celery_repository_ref` | no       | `HEAD`  | The Git ref to checkout when cloning the repository.                       |
| `celery_environment`    | no       | `{}`    | A mapping with environment variables for the Celery worker at runtime.     |

## Example Playbook

A typical playbook using this role may look like:

```yaml
- name: Deploy Celery worker
  hosts: all
  vars:
    ansible_python_interpreter: auto
  roles:
    - role: girder.celery
      vars:
        celery_app: test_project.celery
        celery_repository_url: https://github.com/girder/ansible-role-girder-celery.git
        celery_environment:
          DJANGO_STORAGE_BUCKET_NAME: "my-bucket"
```

A typical
[Ansible Galaxy `requirements.yml` file](https://galaxy.ansible.com/docs/using/installing.html#installing-multiple-roles-from-a-file)
should look like:

```yaml
- src: girder.celery
  version: master
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)
