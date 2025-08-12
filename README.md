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
-   Linux (Debian/Ubuntu/CentOS/RedHat/Fedora/Arch)

## Role Variables

Variables can be set in your playbook or inventory. See `defaults/main.yml` for all options.

| Variable                | Description                                 | Default       |
| ----------------------- | ------------------------------------------- | ------------- |
| `wireguard_port`        | UDP port for WireGuard                      | 51820         |
| `wireguard_interface`   | Name of the WireGuard interface             | wg0           |
| `wireguard_address`     | Address/subnet for the interface            | 10.10.10.1/24 |
| `wireguard_private_key` | Private key for the server (auto-generated) | ''            |
| `wireguard_peers`       | List of peer configurations                 | []            |

Example peer definition:

```yaml
wireguard_peers:
    - name: client1
        public_key: "<client1_public_key>"
        allowed_ips: "10.10.10.2/32"
```

## Example Playbook

```yaml
- hosts: vpnservers
    become: true
    roles:
        - role: wireguard
            vars:
                wireguard_address: "10.10.10.1/24"
                wireguard_peers:
                    - name: client1
                        public_key: "<client1_public_key>"
                        allowed_ips: "10.10.10.2/32"
```
