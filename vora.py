#!/usr/bin/env python3

import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII Art
ascii_art = r"""
 ▌ ▐·      ▄▄▄   ▄▄▄· 
▪█·█▌▪     ▀▄ █·▐█ ▀█ 
▐█▐█• ▄█▀▄ ▐▀▀▄ ▄█▀▀█ 
 ███ ▐█▌.▐▌▐█•█▌▐█ ▪▐▌
. ▀   ▀█▄▀▪.▀  ▀ ▀  ▀ 
"""

# Define gradient colors: Red and White
def gradient(text):
    gradient_text = ''
    for i, char in enumerate(text):
        if i % 2 == 0:
            gradient_text += Fore.RED + char
        else:
            gradient_text += Fore.WHITE + char
    return gradient_text

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_menu(menu_options):
    clear_screen()

    # Center the ASCII art with gradient
    for line in ascii_art.splitlines():
        print(gradient(line.center(os.get_terminal_size().columns)))

    print(Fore.GREEN + "Welcome to the Vora Tool!".center(os.get_terminal_size().columns))
    print(Fore.YELLOW + "Please choose an option:".center(os.get_terminal_size().columns))

    # Centering the menu with gradient
    for i, option in enumerate(menu_options, start=1):
        centered_option = f"{i}. {option['name']}".center(os.get_terminal_size().columns)
        print(gradient(centered_option))

    # Footer
    footer = "Made by @ml0ck & ChatGPT"
    print(Fore.WHITE + footer.center(os.get_terminal_size().columns))

def execute_tool(command):
    print(Fore.WHITE + f"Executing: {command}")
    subprocess.run(command, shell=True)

def get_input(prompt):
    return input(Fore.YELLOW + prompt)

def main():
    menu_options = [
        {
            "name": "Network Scan",
            "command": "nmap -sn {ip_range}",
            "input_prompt": "Enter IP range (e.g., 192.168.1.0/24): "
        },
        {
            "name": "Port Monitoring",
            "command": "netstat -tuln",
            "input_prompt": None  # No input needed
        },
        {
            "name": "Service Check",
            "command": "nmap -sV {ip}",
            "input_prompt": "Enter IP address to check service version: "
        },
        {
            "name": "Vulnerability Scan (Nessus)",
            "command": "echo 'Nessus is a paid tool and requires setup.'",
            "input_prompt": None  # No input needed
        },
        {
            "name": "DNS Analysis",
            "command": "dig {domain}",
            "input_prompt": "Enter domain name (e.g., example.com): "
        },
        {
            "name": "HTTP Analysis",
            "command": "curl -I {url}",
            "input_prompt": "Enter URL (e.g., http://example.com): "
        },
        {
            "name": "IP Check",
            "command": "whois {ip}",
            "input_prompt": "Enter IP address to check: "
        },
        {
            "name": "Ping Sweep",
            "command": "fping -a -g {ip_range}",
            "input_prompt": "Enter IP range (e.g., 192.168.1.0/24): "
        },
        {
            "name": "Traffic Analysis",
            "command": "tcpdump -i any",
            "input_prompt": None  # No input needed
        },
        {
            "name": "Web Scanner (Nikto)",
            "command": "nikto -h {url}",
            "input_prompt": "Enter URL to scan (e.g., http://example.com): "
        },
        {
            "name": "SSL Analysis",
            "command": "openssl s_client -connect {url}:443",
            "input_prompt": "Enter domain name for SSL analysis (e.g., example.com): "
        },
        {
            "name": "Subdomain Search (Sublist3r)",
            "command": "sublist3r -d {domain}",
            "input_prompt": "Enter domain name to search subdomains (e.g., example.com): "
        },
        {
            "name": "CMS Scanner (WPScan)",
            "command": "wpscan --url {url}",
            "input_prompt": "Enter WordPress site URL (e.g., http://example.com): "
        },
        {
            "name": "Data Download",
            "command": "wget {url}",
            "input_prompt": "Enter URL to download (e.g., http://example.com/file): "
        },
        {
            "name": "File Monitoring",
            "command": "inotifywait -m {directory}",
            "input_prompt": "Enter directory to monitor: "
        },
        {
            "name": "Disk Usage Analysis",
            "command": "du -h {directory}",
            "input_prompt": "Enter directory to analyze disk usage: "
        },
        {
            "name": "Bandwidth Test",
            "command": "iperf -s",
            "input_prompt": None  # No input needed
        },
        {
            "name": "Log Monitoring",
            "command": "tail -f {logfile}",
            "input_prompt": "Enter log file to monitor (e.g., /var/log/syslog): "
        },
        {
            "name": "Password Generator",
            "command": "pwgen 12 1",
            "input_prompt": None  # No input needed
        },
        {
            "name": "API Vulnerability Scanner",
            "command": "echo 'Postman requires a GUI interface.'",
            "input_prompt": None  # No input needed
        },
        {
            "name": "Quit",
            "command": None,
            "input_prompt": None  # No input needed
        },
    ]

    while True:
        display_menu(menu_options)
        choice = get_input("Enter your choice: ")

        try:
            choice_index = int(choice) - 1
            if choice_index < 0 or choice_index >= len(menu_options):
                raise ValueError("Invalid choice")
            
            selected_tool = menu_options[choice_index]
            if selected_tool["command"] is not None:
                if selected_tool["input_prompt"]:
                    user_input = get_input(selected_tool["input_prompt"])
                    command = selected_tool["command"].format(**{key: user_input for key in ['ip', 'ip_range', 'domain', 'url', 'directory', 'logfile']})
                else:
                    command = selected_tool["command"]
                execute_tool(command)
            else:
                print(Fore.RED + "Exiting Vora. See you soon!")
                break

        except ValueError as e:
            print(Fore.RED + str(e))

        input(Fore.YELLOW + "Press Enter to continue...")

if __name__ == "__main__":
    main()
