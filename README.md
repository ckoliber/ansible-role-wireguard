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
| `wireguard_cidr`     | WireGuard overlay network CIDR                     | 10.10.10.0/24     |
| `wireguard_port`     | WireGuard port number                              | 51820             |
| `wireguard_iface`    | WireGuard interface name                           | wg0               |
| `wireguard_graph`    | Graph of connections between wireguard peers       | {}                |
| `wireguard_packages` | Package list to install (overrides OS-family vars) | [wireguard-tools] |

Example graph definition:

```yaml
wireguard_graph:
    host1:
        locals: [192.168.1.0/24]
        targets: [host2, host3]
    host2:
        locals: [192.168.2.0/24]
        targets: [host1, host3]
    host3:
        locals: [192.168.3.0/24]
        targets: [host1, host2]
```
