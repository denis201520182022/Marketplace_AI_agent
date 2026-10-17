#!/bin/bash
# ==============================================================================
# Script to configure Squid Forward Proxy on Ubuntu/Debian VPS (JustHost)
# Usage: sudo bash setup_proxy.sh <PROXY_USER> <PROXY_PASSWORD>
# ==============================================================================

set -e

PROXY_USER=${1:-"proxyuser"}
PROXY_PASS=${2:-"StrongPassword123!"}

echo ">>> Updating packages..."
apt-get update -y
apt-get install -y squid apache2-utils ufw

echo ">>> Setting up basic auth..."
htpasswd -cb /etc/squid/passwords "$PROXY_USER" "$PROXY_PASS"
chmod 640 /etc/squid/passwords
chown root:proxy /etc/squid/passwords

echo ">>> Copying squid.conf..."
cp squid.conf /etc/squid/squid.conf

echo ">>> Enabling UFW port 3128..."
ufw allow 3128/tcp || true

echo ">>> Restarting Squid service..."
systemctl restart squid
systemctl enable squid

echo "====================================================================="
echo " Squid Proxy successfully installed and running!"
echo " Proxy URL: http://${PROXY_USER}:${PROXY_PASS}@<VPS_IP>:3128"
echo "====================================================================="
