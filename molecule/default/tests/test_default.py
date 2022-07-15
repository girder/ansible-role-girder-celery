import pathlib

import packaging.version


def test_python(host):
    python_package = host.package('python3')
    assert python_package.is_installed
    assert python_package.version.startswith('3.8')


def test_pip_version(host):
    pip_package = host.pip('pip', pip_path='/opt/celery/bin/pip')
    assert pip_package.is_installed
    pip_version = packaging.version.parse(pip_package.version)
    assert pip_version >= packaging.version.parse('20.3')


def test_pip_requirements(host):
    # "requests" is only present in "requirements.txt", which should be found
    assert host.pip('requests', pip_path='/opt/celery/bin/pip').is_installed


def test_celery_user(host):
    celery_user = host.user('celery')
    assert celery_user.exists


def test_celery_user_home(host):
    celery_user = host.user('celery')
    assert celery_user.home == '/opt/celery'


def test_celery_user_shell(host):
    celery_user = host.user('celery')
    assert pathlib.PurePosixPath(celery_user.shell).name == 'nologin'


def test_celery_user_password(host):
    celery_user = host.user('celery')
    assert celery_user.password.startswith('!')


def test_celery_group(host):
    celery_group = host.user('celery')
    assert celery_group.exists


def test_celery_service(host):
    celery_service = host.service('celery')
    assert celery_service.is_enabled
    assert celery_service.is_running


def test_celery_environment_file(host):
    celery_environment_file = host.file('/etc/celery.conf')
    assert celery_environment_file.exists
    assert celery_environment_file.is_file


def test_celery_environment_file_ownership(host):
    celery_environment_file = host.file('/etc/celery.conf')
    assert celery_environment_file.user == 'root'
    assert celery_environment_file.group == 'root'


def test_celery_environment_file_permissions(host):
    celery_environment_file = host.file('/etc/celery.conf')
    assert celery_environment_file.mode == 0o600
