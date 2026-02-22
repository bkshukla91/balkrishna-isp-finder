# 🛡️ Balkrishna ISP Finder v4.0
> **The Ultimate IP Intelligence & ISP Reconnaissance Tool for Professionals.**

![License](https://img.shields.io/github/license/bkshukla91/balkrishna-isp-finder?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge)

---

## 📸 Tool Preview
![Main Interface](assets/screenshot.png)

---

## 📊 Project Structure & Workflow
Below is the logical flow of how the tool processes a target IP:
```mermaid
graph TD
    A[Start Tool] --> B{Input IP Address}
    B -->|User Provides IP| C[Initialize Multi-API Connection]
    C --> D[Fetch Geo-Location & ISP Data]
    D --> E[Generate Google Maps Link]
    E --> F[Display Intelligence Report]
    F --> G[End Scan]

## Key Features
Full Intelligence: Fetches AS, Country, City, ISP, Org, and Zip.
Coordinate Precision: Provides exact Latitude and Longitude.
Visual Mapping: Generates a direct Google Maps link.
Optimized UI: Stylish ASCII Art and color-coded results for Termux/Linux.

📥 Installation & Usage
1. Clone the Repository
git clone [https://github.com/bkshukla91/balkrishna-isp-finder.git](https://github.com/bkshukla91/balkrishna-isp-finder.git)
cd balkrishna-isp-finder

2. Install Dependencies
pip install -r requirements.txt

3. Run the Tool
python balkrishna_isp.py

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
⚖️ Disclaimer
This tool is for Educational Purposes and Authorized Pentesting only. The author is not responsible for any misuse.
