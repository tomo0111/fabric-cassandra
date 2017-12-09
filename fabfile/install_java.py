# coding:utf8

from fabric.api import *
from fabric.decorators import task

@task
def install_java():
    """
    Install Java
    """
    sudo('yum install -y java')