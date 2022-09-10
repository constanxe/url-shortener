CREATE SCHEMA IF NOT EXISTS `constancetan7`;
USE `constancetan7`;

DROP TABLE IF EXISTS `urls`;
CREATE TABLE `urls` (
  `url` varchar(255) NOT NULL,
  `converted_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`url`)
) ENGINE=InnoDB;
