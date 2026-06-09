import requests
import sys
import os


target_url = input("Enter Target URL: ")

wordlist_file = "Worldlist.txt"

if target_url.startswith("http://") or target_url.startswith("https://"):
 if not os.path.exists(wordlist_file):
    print(f"[!] Error: The file '{wordlist_file}' was not found.")
    sys.exit()

 print("-" * 50)
 print(f"[*] Starting Directory Brute-Force on: {target_url}")
 print(f"[*] Using wordlist: {wordlist_file}")
 print("-" * 50)

 try:
    with open(wordlist_file, "r", encoding="utf-8") as file:
        for line in file:
            directory = line.strip()

            if not directory:
                continue

            full_url = f"{target_url}/{directory}"


            response = requests.get(full_url, timeout=5.0)

            if response.status_code == 200:
                print(f"    └── [SUCCESS] Found: {full_url} (200 OK)")


 except KeyboardInterrupt:
    print("\n [!] Process interrupted by the user.")
    sys.exit()

 except requests.exceptions.ConnectionError:
    print("\n [!] Connection failed. Please check the URL or your internet connection.")
    sys.exit()

 print("-" * 50)
 print("[*] Wordlist scanning completed.")

else:
    print("\n [!] URL is NOT valid.")
