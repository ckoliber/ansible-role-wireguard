# Ansible Role WireGuard

This Ansible role installs and configures [WireGuard](https://www.wireguard.com/) VPN on Linux hosts. It allows you to easily set up secure, fast, and modern VPN tunnels for your infrastructure.

## Features

-   Installs WireGuard from official repositories
-   Configures server and client peers
-   Generates keys if not provided
-   Supports multiple peers/networks
-   Manages firewall rules for WireGuard
-   Idempotent and safe to run multiple times

## Requirements

-   Ansible 2.9+
-   Linux (Debian/Ubuntu/RHEL/Alma/Rocky/Fedora/Arch/Alpine/SUSE)

## Role Variables

Variables can be set in your playbook or inventory. See `defaults/main.yml` for all options.
OS-family specific packages are defined in `vars/<Family>.yml` and loaded automatically.

| Variable             | Description                                        | Default           |
| -------------------- | -------------------------------------------------- | ----------------- |
| `wireguard_cidr`     | WireGuard overlay network CIDR                     | 10.10.0.0/16      |
| `wireguard_port`     | WireGuard port number                              | 51820             |
| `wireguard_iface`    | WireGuard interface name                           | wg0               |
| `wireguard_network`  | WireGuard network topology                         | `{}`              |
| `wireguard_packages` | Package list to install (overrides OS-family vars) | [wireguard-tools] |

Example network definition:

```yaml
wireguard_network:
    host1:
        host: default or <PUBLIC_IP_OR_DNS>
        locals: [192.168.1.0/24]
        targets: [host2, host3]
        postups:
            - echo PostUp
        predowns:
            - echo PreDown
    host2:
        host: default or <PUBLIC_IP_OR_DNS>
        locals: [192.168.2.0/24]
        targets: [host1, host3]
    host3:
        host: default or <PUBLIC_IP_OR_DNS>
        locals: [192.168.3.0/24]
        targets: [host1, host2]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT](LICENSE.md).  
Copyright (c) KoLiBer (koliberr136a1@gmail.com)
