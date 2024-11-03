#!/bin/bash

# This script installs all dependencies for the Vora tool on EndeavourOS.

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1
}

echo "Starting the installation of dependencies for Vora..."

# Update the package list
echo "Updating package database..."
sudo pacman -Syu --noconfirm

# Install Python and pip if not installed
if ! command_exists python; then
    echo "Installing Python 3..."
    sudo pacman -S --noconfirm python python-pip
fi

# Install required Python packages
echo "Installing required Python packages..."
pip install colorama

# Install system utilities
declare -a tools=(
    "nmap"
    "bind-tools"     # for 'dig'
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
        sudo pacman -S --noconfirm "$tool"
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
    sudo pacman -S --noconfirm ruby ruby-dev
    gem install wpscan
else
    echo "WPScan is already installed."
fi

# Clean up
echo "Cleaning up..."
sudo pacman -Rns $(pacman -Qdtq) --noconfirm  # Remove unused packages

echo "All dependencies for Vora have been installed successfully!"

# Provide instructions on how to run Vora
echo "You can now run Vora using the following command:"
echo "python /path/to/vora.py"
