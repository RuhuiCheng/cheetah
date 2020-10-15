-------------------------------------
create database cheetah default charset utf8 collate utf8_general_ci;
create user cheetah identified by 'cheetah';
grant all on cheetah.* to 'cheetah'@'%' identified by 'cheetah';
flush privileges;
-------------------------------------

-------------------------------------
truncate table cheetah.dag;
truncate table cheetah.node;
truncate table cheetah.relation;

select * from cheetah.dag;
select * from cheetah.node;
select * from cheetah.relation;

-- data init
-- dag
INSERT INTO cheetah.dag (name) VALUES('daily_increment');

-- node
-- ods
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'ods', 'flow_tag1');
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'ods', 'flow_tag2');
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'ods', 'flow_tag3');
-- dwd
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dwd', 'flow_tag1');
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dwd', 'flow_tag1');
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dwd', 'flow_tag1');
-- dws
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dws', 'mdm');
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dws', 'mlp');
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dws', 'sap');
-- dm
INSERT INTO cheetah.node (dag_id, layer, flow_tag) VALUES(1, 'dm', 'demo1');

-- relation
-- ods>dwd
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(1, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(2, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(3, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(4, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(5, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(6, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(7, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(8, 50);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(9, 50);

INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(10, 51);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(11, 51);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(12, 51);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(13, 51);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(14, 51);

INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(15, 52);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(16, 52);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(17, 52);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(18, 52);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(19, 52);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(20, 52);


-- dwd>dws
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(50, 53);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(51, 53);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(51, 54);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(52, 54);

-- dws>dm
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(53, 55);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(54, 55);
INSERT INTO cheetah.relation (node_from_id, node_to_id) VALUES(49, 55);
