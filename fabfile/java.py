from fabric.api import *
from fabric.decorators import task

@task
def install_java():
    sudo('yum install -y java')