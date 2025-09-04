# [2.0.0](https://github.com/ckoliber/ansible-role-wireguard/compare/1.5.0...2.0.0) (2025-09-04)


### Features

* change endpoint to be conditional ([348f061](https://github.com/ckoliber/ansible-role-wireguard/commit/348f06189bfdf062ca8282d0d2f6a7b36268e39a))


### BREAKING CHANGES

* host variable must be used

# [1.5.0](https://github.com/ckoliber/ansible-role-wireguard/compare/1.4.0...1.5.0) (2025-09-04)


### Features

* add conditional peer endpoint variable ([16b2bd0](https://github.com/ckoliber/ansible-role-wireguard/commit/16b2bd0e0ec7bc305db958bd14389ce425b57e5d))

# [1.4.0](https://github.com/ckoliber/ansible-role-wireguard/compare/1.3.0...1.4.0) (2025-09-04)


### Features

* remove unnecessary hooks ([9769dc3](https://github.com/ckoliber/ansible-role-wireguard/commit/9769dc3468744789b333ac224b52f4c21d608356))

# [1.3.0](https://github.com/ckoliber/ansible-role-wireguard/compare/1.2.0...1.3.0) (2025-08-30)


### Bug Fixes

* add default value if empty for postups, predowns ([09a5737](https://github.com/ckoliber/ansible-role-wireguard/commit/09a573742cac05190a10adc7559dc2c79c482aae))
* change CIDR range ([45e43d1](https://github.com/ckoliber/ansible-role-wireguard/commit/45e43d1b07a0cc941877dc2c89f702480d0d5921))
* remove bash requirement in shell module ([f8a2f0c](https://github.com/ckoliber/ansible-role-wireguard/commit/f8a2f0c04a12e38e95926af2139c0d2d366f6065))


### Features

* add wg wireguard overlay IPs to AllowedIPs ([f4732ea](https://github.com/ckoliber/ansible-role-wireguard/commit/f4732ea594825f0f65fbfa6a625760926069d8d2))
* add wireguard postup, predown hooks ([7b38056](https://github.com/ckoliber/ansible-role-wireguard/commit/7b38056036b59546601f3cefeb6d5fd4b9b1d2b9))

# [1.2.0](https://github.com/ckoliber/ansible-role-wireguard/compare/1.1.0...1.2.0) (2025-08-29)


### Features

* enable wireguard iface MASQUERADE ([939bb23](https://github.com/ckoliber/ansible-role-wireguard/commit/939bb233610f39149c4b21a5f8456a9f2af305b8))

# [1.1.0](https://github.com/ckoliber/ansible-role-wireguard/compare/1.0.0...1.1.0) (2025-08-28)


### Bug Fixes

* ansible shell pipefail lint ([3f983a7](https://github.com/ckoliber/ansible-role-wireguard/commit/3f983a7742325044654bb794a74515fc47000497))
* change handlers listener ([94f5d6e](https://github.com/ckoliber/ansible-role-wireguard/commit/94f5d6e6dc7c895ae0cdb0ad0bb96b5fdcce3c2e))
* change metadata arch linux name ([ecc24c2](https://github.com/ckoliber/ansible-role-wireguard/commit/ecc24c26b6294b02c1005874fae3a77239fa544d))
* change wg reload to restart ([1dd286e](https://github.com/ckoliber/ansible-role-wireguard/commit/1dd286ee9fd2e5be6f98572d5d23923e9dfa9230))
* include os family vars ([beb6d0a](https://github.com/ckoliber/ansible-role-wireguard/commit/beb6d0af9bb1afd28129fa8578c4065df32a69c9))
* lint module name ([bbdc5f0](https://github.com/ckoliber/ansible-role-wireguard/commit/bbdc5f084b3629d79cedbafd4cb4663cc7edeb11))


### Features

* add preshared key ([de90a05](https://github.com/ckoliber/ansible-role-wireguard/commit/de90a05a81cafac4d8634446756a2074b928c479))
* split logic into tasks, handlers ([4ef03b1](https://github.com/ckoliber/ansible-role-wireguard/commit/4ef03b12de768b682af4c367260baf3326a8734e))
* support all linux OS families ([ad039a7](https://github.com/ckoliber/ansible-role-wireguard/commit/ad039a73c888faf183d65581177b38e3381b758d))

# 1.0.0 (2025-08-28)


### Bug Fixes

* lint problems ([a6cee88](https://github.com/ckoliber/ansible-role-wireguard/commit/a6cee88906ca93c5e5d4a7c1685f272902d79c40))


### Features

* add base config, keys ([18d3816](https://github.com/ckoliber/ansible-role-wireguard/commit/18d3816ccdf4f5fb42820c2301901698cda2b8dc))
* add metadata ([a0b5a37](https://github.com/ckoliber/ansible-role-wireguard/commit/a0b5a372cd8c716f0f3eb611331c1f6628ef8f98))
* add wg0 template ([ed716e4](https://github.com/ckoliber/ansible-role-wireguard/commit/ed716e4bb28ddd667c919a645d7ea2174e18a457))
* add wireguard routes ([08bd91e](https://github.com/ckoliber/ansible-role-wireguard/commit/08bd91e4518832d82caeee452a94c26f9f57f625))
* init project ([a673c43](https://github.com/ckoliber/ansible-role-wireguard/commit/a673c43131c7340328e1b5bc532816d2147766d1))
