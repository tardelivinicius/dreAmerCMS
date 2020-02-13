ALTER TABLE `users`
	ALTER `seckey` DROP DEFAULT,
	ALTER `facebook_id` DROP DEFAULT,
	ALTER `facebook` DROP DEFAULT,
	ALTER `cblueits` DROP DEFAULT;
ALTER TABLE `users`
	CHANGE COLUMN `seckey` `seckey` VARCHAR(999) NULL AFTER `active_players`,
	CHANGE COLUMN `facebook_id` `facebook_id` VARCHAR(50) NULL AFTER `seckey`,
	CHANGE COLUMN `facebook` `facebook` VARCHAR(200) NULL AFTER `facebook_id`,
	CHANGE COLUMN `cblueits` `cblueits` VARCHAR(50) NULL AFTER `staff_profileimage_url`;
	CHANGE COLUMN `rank` `rank_class` INT(1) UNSIGNED NULL DEFAULT '1' AFTER `auth_ticket`;


ALTER TABLE `cms_settings`
	ALTER `variable` DROP DEFAULT;
ALTER TABLE `cms_settings`
	ADD COLUMN `id` INT(100) NOT NULL AUTO_INCREMENT FIRST,
	CHANGE COLUMN `variable` `type` VARCHAR(80) NOT NULL AFTER `id`,
	DROP COLUMN `example`,
	DROP PRIMARY KEY,
	ADD PRIMARY KEY (`id`);

INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (1, 'cms_name', 'http://localhost\r\n', 'A url para o diretório de raiz de websites');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (2, 'cms_url', '192.99.242.13', 'O endereço IP para seu emulador hotel');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (3, 'cms_clientlimit', '90\r\n', 'The port that your emulator is running on');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (4, 'cms_maintenance', '30001', 'The port that your emulators MUS is running on');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (5, 'client_ip', '', 'The url to your external variables');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (6, 'client_mus', '', 'The url to your external texts');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (7, 'client_texts', 'Habbed', 'The username you signed up to RetroTopsites.com with');
INSERT INTO `cms_settings` (`id`, `type`, `value`, `description`) VALUES (8, 'client_variables', 'Habbed', 'Nome de Seu Hotel');


ALTER TABLE `users`
	ALTER `real_name` DROP DEFAULT;
ALTER TABLE `users`
	CHANGE COLUMN `real_name` `real_name` VARCHAR(40) NULL COLLATE 'latin1_swedish_ci' AFTER `username`;
ALTER TABLE `users`
	ALTER `working` DROP DEFAULT,
	ALTER `mymusik` DROP DEFAULT,
	ALTER `secretcode` DROP DEFAULT,
	ALTER `cms_currency` DROP DEFAULT,
	ALTER `age` DROP DEFAULT,
	ALTER `role` DROP DEFAULT,
	ALTER `photo_perfil` DROP DEFAULT,
	ALTER `homework` DROP DEFAULT,
	ALTER `color` DROP DEFAULT,
	ALTER `cms_birthday` DROP DEFAULT,
	ALTER `cms_twitter` DROP DEFAULT,
	ALTER `cms_video` DROP DEFAULT,
	ALTER `cms_pin` DROP DEFAULT,
	ALTER `cms_role` DROP DEFAULT;
ALTER TABLE `users`
	CHANGE COLUMN `working` `working` VARCHAR(60) NULL COLLATE 'latin1_swedish_ci' AFTER `auth_ticket`,
	CHANGE COLUMN `mymusik` `mymusik` VARCHAR(60) NULL COLLATE 'latin1_swedish_ci' AFTER `working`,
	CHANGE COLUMN `secretcode` `secretcode` VARCHAR(60) NULL COLLATE 'latin1_swedish_ci' AFTER `mymusik`,
	CHANGE COLUMN `cms_currency` `cms_currency` VARCHAR(255) NULL AFTER `allow_pull`,
	CHANGE COLUMN `age` `age` VARCHAR(255) NULL AFTER `trusted`,
	CHANGE COLUMN `role` `role` VARCHAR(255) NULL AFTER `age`,
	CHANGE COLUMN `photo_perfil` `photo_perfil` VARCHAR(255) NULL AFTER `pin`,
	CHANGE COLUMN `homework` `homework` VARCHAR(400) NULL COLLATE 'latin1_swedish_ci' AFTER `facebook_vin`,
	CHANGE COLUMN `color` `color` VARCHAR(10) NULL COLLATE 'latin1_swedish_ci' AFTER `birthday`,
	CHANGE COLUMN `cms_birthday` `cms_birthday` VARCHAR(100) NULL AFTER `change_name`,
	CHANGE COLUMN `cms_twitter` `cms_twitter` VARCHAR(100) NULL AFTER `cms_pprofile`,
	CHANGE COLUMN `cms_video` `cms_video` VARCHAR(50) NULL AFTER `cms_style`,
	CHANGE COLUMN `cms_pin` `cms_pin` VARCHAR(10) NULL AFTER `cms_video`,
	CHANGE COLUMN `cms_role` `cms_role` VARCHAR(50) NULL AFTER `cms_pin`;


CREATE TABLE `cms_settings` (
	`id` INT(100) NOT NULL AUTO_INCREMENT,
	`hotel_name` VARCHAR(80) NOT NULL,
	`hotel_url` VARCHAR(80) NULL DEFAULT '',
	`hotel_maintenance` INT(1) NULL DEFAULT '0',
	`hotel_register_enable` INT(1) NULL DEFAULT '1',
	`client.allow.cross.domai` INT(1) NULL DEFAULT '0',
	`client.notify.cross.domain` INT(1) NULL DEFAULT '1',
	`connection.info.host` VARCHAR(50) NULL DEFAULT NULL,
	`connection.info.port` VARCHAR(50) NULL DEFAULT NULL,
	`external.variables.txt` VARCHAR(50) NULL DEFAULT NULL,
	`external.texts.txt` VARCHAR(50) NULL DEFAULT NULL,
	`external.figurepartlist.txt` VARCHAR(50) NULL DEFAULT NULL,
	`flash.dynamic.avatar.download.configuration` VARCHAR(50) NULL DEFAULT NULL,
	`productdata.load.url` VARCHAR(50) NULL DEFAULT NULL,
	`furnidata.load.url` VARCHAR(50) NULL DEFAULT NULL,
	`use.sso.ticket` INT(1) NULL DEFAULT '1',
	`processlog.enabled` INT(1) NULL DEFAULT '1',
	`client.starting` VARCHAR(50) NOT NULL,
	`flash.client.url` VARCHAR(50) NOT NULL,
	`flash.client.origin` VARCHAR(50) NOT NULL,
	`ads.domain` VARCHAR(50) NOT NULL,
	`diamonds.enabled` INT(1) NOT NULL DEFAULT 1,
	PRIMARY KEY (`id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=MyISAM
AUTO_INCREMENT=14
;
