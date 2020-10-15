## CDH Cluster

### Master Hosts [Core:16, Mem:128G, Disk:(128G*1)]
--------------------------------------------------
#### Master Node 1
 - NameNode
 - JournalNode
 - FailoverController
 - Yarn ResourceManager
 - JobHistory Server
 - ZooKeeper
 - HiveServer2
 
#### Master Node 2
 - NameNode
 - JournalNode
 - FailoverController
 - Yarn ResourceManager
 - ZooKeeper
 - HiveServer2

#### Master Node 3
 - Spark History Server
 - JournalNode (requires dedicated disk)
 - Zookeeper
 - HiveServer2
 - MySQL(master)
--------------------------------------------------
### Worker Hosts [Core:16, Mem:128G, Disk:(128G*2)]
#### Worker Node [1-3]
 - DataNode
 - NodeManager
 
#### Worker Node [4]
 - DataNode
 - NodeManager
 - Presto Coordinator

#### Worker Node [5-8]
 - DataNode
 - NodeManager
 - Presto Worker
--------------------------------------------------
### Utility Host [Core:16, Mem:64G, Disk:(128G*1)]
 - Cloudera Manager
 - Cloudera Manager Management Service
 - MySQL(slave)
 - Hue

### CICD Host [Core:16, Mem:64G, Disk:(128G*1)]
 - Ansible server
 - Jenkins server
 - Nexus Server
--------------------------------------------------   
## Cheetah Cluster
### Cheetah Hosts [Core:16, Mem:64G, Disk:(128G*1)]
#### Cheetah Node 1
 - Airflow scheduler_failover_controller 
 - Airflow worker
 - Airflow webserver
 - Rabbitmq server

#### Cheetah Node 2
 - Airflow scheduler_failover_controller 
 - Airflow worker
 - RabbitMQ management
 - Rabbitmq server

#### Cheetah Node 3
 - Airflow scheduler_failover_controller 
 - Airflow worker
 - Rabbitmq server
--------------------------------------------------

Related source links:

https://docs.cloudera.com/documentation/enterprise/6/latest/topics/cm_ig_host_allocations.html#concept_f43_j4y_dw__section_dn3_ngj_ndb

https://docs.cloudera.com/documentation/enterprise/6/release-notes/topics/rg_cdh_62_release_notes.html#cdh62x_release_notes

