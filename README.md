# Web Application Directory Brute-Forcer

An automated web application auditing tool designed to perform dictionary attacks against web servers. It automates HTTP requests to discover hidden directories and sensitive files that might not be linked on the main user interface.

---

## Key Features
* Automated HTTP Requests: Seamlessly handles web connections using standard GET methods.
* Status Code Filtering: Distinctly filters and prints responses based on HTTP status codes (e.g., 200 OK for success and 403 Forbidden for restricted paths).
* Robust Exception Handling: Gracefully handles sudden connection failures and user interruptions (Ctrl+C).

---

## Setup & Usage

1. Install Dependencies: This script requires the external requests library. Install it using pip:
   `bash
   pip install requests
