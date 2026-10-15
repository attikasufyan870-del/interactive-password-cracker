"""
==================================================
Project: Interactive Password Cracker Automation
Author: Attika Sufyan
Description: A security utility script demonstrating 
             runtime user input, dictionary iteration, 
             and conditional matching logic for 
             cybersecurity learning.
==================================================
"""

import time

# User input for target password
target_password = input("Enter target password to crack: ")

# Pre-defined wordlist
wordlist = ["admin", "123", "786", "password", "sufyan007", "Sufyan007$AM$"]

print("[*] Cracking password for target...\n")

# Iterating and matching logic
for pwd in wordlist:
    print(f"[-] Trying: {pwd}")
    time.sleep(0.5)
    
    if pwd == target_password:
        print(f"\n[+] SUCCESS! Password found: {pwd}")
        break
