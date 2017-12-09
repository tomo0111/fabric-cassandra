# coding:utf8

from fabric.api import *
from fabric.decorators import task
from cuisine import *

@task
def setup_repo():
    """
    Setup cassandra repo
    """
    file_upload('/etc/yum.repos.d/cassandra.repo', 'files/cassandra.repo', sudo=True)

@task
def install_cassandra():
    """
    Install cassandra
    """
    sudo('yum install -y cassandra')