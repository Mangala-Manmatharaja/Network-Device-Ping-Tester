🔍 Network Device Ping Tester
This is a basic Python-based ping tester that checks the status of network devices (e.g., routers, servers) by pinging their IP addresses and logs the results to a text file. Perfect for educational purposes or ethical network monitoring.

📌 Features

Ping multiple network devices from a list of IPs
Detects if devices are UP, DOWN, or return an ERROR
Outputs results to both console and a file (ping_results.txt)
Simple and lightweight for learning network monitoring


⚠️ Disclaimer

🚨 This tool is intended for educational purposes only.Do not ping devices or networks you do not own or have permission to test.


💪 Requirements

Python 3.x

This script uses Python's built-in modules:

subprocess
No external libraries required.


🚀 Usage

Clone the repository:
git clone https://github.com/Mangala-Manmatharaja/Network-Device-Ping-Tester.git
cd ping-tester


Create a device list:

Create a file named devices.txt in the project folder.
Add IP addresses to ping, one per line (e.g., 127.0.0.1, 8.8.8.8).


Run the script:
python ping_tester.py


Results:

Console will show the status of each device (UP/DOWN/ERROR)
A file named ping_results.txt will be created with the full results




🧪 Example Output
127.0.0.1: UP
8.8.8.8: UP
Results saved to ping_results.txt

Sample ping_results.txt:
127.0.0.1: UP
8.8.8.8: UP


📄 License
MIT License — feel free to use, modify, and share with credit.

✍️ Author

Mangala Manmatharaja
