# Getting Started
 * Environment Apache Cassandra on CentOS7

# Commands
```
$ fab -l
Available commands:

    cassandra.daemon_reload
    cassandra.enable_cassandra
    cassandra.install_cassandra
    cassandra.setup_cassandra_rackdc
    cassandra.setup_cassandra_yaml
    cassandra.setup_repo
    cassandra.start_cassandra
    cassandra.stop_cassandra
    java.install_java
```

# Single node environment
Setup repo
```
$ fab cassandra.setup_repo
```

Install Java
```
$ fab cassandra.install_java
```

Install Cassandra
```
$ fab cassandra.install_cassandra
```

Setup cassandra.yaml
```
$ fab cassandra.setup_cassandra_yaml
```

Setup cassandra-rackdc.properties
```
$ fab cassandra.setup_cassandra_rackdc
```

Start Cassandra 
```
$ fab cassandra.start_cassandra
```

Enable Cassandra 
```
$ fab cassandra.enable_cassandra
```
