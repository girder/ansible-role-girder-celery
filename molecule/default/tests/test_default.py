import pathlib

import packaging.version


def test_python(host):
    mongodb_package = host.package('python3')
    assert mongodb_package.is_installed
    assert mongodb_package.version.startswith('3.8')


def test_pip_version(host):
    python_packages = host.pip_package.get_packages(
        pip_path='/opt/celery/bin/pip')
    assert 'pip' in python_packages
    pip_version = packaging.version.parse(python_packages['pip']['version'])
    assert pip_version >= packaging.version.parse('20.3')


def test_pip_requirements(host):
    python_packages = host.pip_package.get_packages(
        pip_path='/opt/celery/bin/pip')
    # "requests" is only present in "requirements.txt", which should be found
    assert 'requests' in python_packages


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
    mongodb_group = host.user('celery')
    assert mongodb_group.exists


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
