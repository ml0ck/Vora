#!/bin/bash

# This script installs all dependencies for the Vora tool.

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1
}

echo "Starting the installation of dependencies for Vora..."

# Update the package list
echo "Updating package list..."
sudo apt update

# Install Python and pip if not installed
if ! command_exists python3; then
    echo "Installing Python 3..."
    sudo apt install -y python3 python3-pip
fi

# Install required Python packages
echo "Installing required Python packages..."
pip3 install colorama

# Install system utilities
declare -a tools=(
    "nmap"
    "dnsutils"      # for 'dig'
    "curl"
    "whois"
    "fping"
    "tcpdump"
    "nikto"
    "openssl"
    "wget"
    "inotify-tools"
    "pwgen"
    "iperf"
)

for tool in "${tools[@]}"; do
    if ! command_exists "$tool"; then
        echo "Installing $tool..."
        sudo apt install -y "$tool"
    else
        echo "$tool is already installed."
    fi
done

# Clone Sublist3r from GitHub if not already present
if [ ! -d "Sublist3r" ]; then
    echo "Cloning Sublist3r repository..."
    git clone https://github.com/aboul3la/Sublist3r.git
else
    echo "Sublist3r is already cloned."
fi

# Install WPScan
if ! command_exists wpscan; then
    echo "Installing WPScan..."
    sudo apt install -y ruby ruby-dev libcurl4-openssl-dev make
    sudo gem install wpscan
else
    echo "WPScan is already installed."
fi

# Clean up
echo "Cleaning up..."
sudo apt autoremove -y

echo "All dependencies for Vora have been installed successfully!"

# Provide instructions on how to run Vora
echo "You can now run Vora using the following command:"
echo "python3 /path/to/vora.py"
