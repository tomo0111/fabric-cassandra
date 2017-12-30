from fabric.api import *
from fabric.contrib.files import sed
from fabric.decorators import task
from cuisine import *

host = ''

@task
def setup_repo():
    file_upload('/etc/yum.repos.d/cassandra.repo', 'files/cassandra.repo', sudo=True)

@task
def install_cassandra():
    sudo('yum install -y cassandra')

@task
def daemon_reload():
    sudo('systemctl daemon-reload')

@task
def setup_cassandra_yaml():
    sed('/etc/cassandra/default.conf/cassandra.yaml', 'listen_address: localhost', 'listen_address: ' + host, use_sudo=True)
    sed('/etc/cassandra/default.conf/cassandra.yaml', 'rpc_address: localhost', 'rpc_address: ' + host, use_sudo=True)
    sed('/etc/cassandra/default.conf/cassandra.yaml', 'endpoint_snitch: SimpleSnitch', 'endpoint_snitch: GossipingPropertyFileSnitch', use_sudo=True)
    sed('/etc/cassandra/default.conf/cassandra.yaml', '127.0.0.1', host, use_sudo=True)

@task
def setup_cassandra_rackdc():
    file_upload('/etc/cassandra/default.conf/cassandra-rackdc.properties', 'files/cassandra-rackdc.properties', sudo=True)

@task
def start_cassandra():
    sudo('systemctl start cassandra')

@task
def enable_cassandra():
    sudo('systemctl enable cassandra')

@task
def stop_cassandra():
    sudo('systemctl stop cassandra')
