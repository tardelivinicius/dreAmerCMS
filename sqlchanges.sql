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
