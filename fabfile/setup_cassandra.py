# coding:utf8

from fabric.api import *
from fabric.decorators import task
from cuisine import *

@task
def daemon_reload():
    """
    Daemon reload cassandra
    """
    sudo('systemctl daemon-reload')

@task
def setup_cassandra_yaml():
    """
    Setup cassandra yaml
    """

@task
def setup_cassandra_rackdc():
    """
    Setup cassandra rackdc
    """

@task
def start_cassandra():
    """
    Start cassandra
    """
    sudo('systemctl start cassandra')

@task
def enable_cassandra():
    """
    Enable cassandra
    """
    sudo('systemctl enable cassandra')

@task
def stop_cassandra():
    """
    Stop cassandra
    """
    sudo('systemctl stop cassandra')
