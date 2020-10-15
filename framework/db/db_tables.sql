CREATE TABLE `dag` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The dag id',
	`name` varchar(200) NOT NULL COMMENT 'dag name',
	`is_enabled` tinyint NOT NULL DEFAULT 1 COMMENT '0:disable 1:enable',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when dag is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when dag is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='dag list';

CREATE TABLE `node` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'node id',
    `dag_id` int NOT NULL  COMMENT 'The dag id',
	`layer` varchar(200) NOT NULL COMMENT 'dwd > dws > dm',
    `flow_tag` varchar(200) NOT NULL COMMENT 'the tag name of dm',
	`is_enabled` tinyint NOT NULL DEFAULT 1 COMMENT '0:disable 1:enable',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when dm is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when dm is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='nodes of dw layer list';

CREATE TABLE `relation` (
    `id` int NOT NULL AUTO_INCREMENT COMMENT 'dm_dws id',
    `node_from_id` int NOT NULL COMMENT 'from node id',
    `node_to_id` int NOT NULL COMMENT 'to node id',
	`is_enabled` tinyint NOT NULL DEFAULT 1 COMMENT '0:disable 1:enable',
    `insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when dm_dws is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when dm_dws is updated',
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='the relation of node';
