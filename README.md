# PRODIGY_PYDEV_Task05
Build a Network Packet Sniffer that:  Captures live packets  Extracts and displays:  Source IP  Destination IP  Protocol (TCP/UDP/ICMP/etc.)  Optional: Payload (hex or readable)

⚠️ Ethical Notice
This tool is developed strictly for educational purposes. Unauthorized packet sniffing is unethical and illegal. Always obtain proper permissions before analyzing any network traffic.

👨‍💻 Author
Rudra Narayan Swain
Cyber Security Enthusiast | Python Developer

# 🧪 Network Packet Analyzer

### 🚀 Task 05 - Prodigy InfoTech Internship (Comillas Negras)

This project is a **Network Packet Analyzer** built using Python and the `scapy` library. It captures live network packets and displays critical information such as **source/destination IP**, **protocols**, and **payload data**.

---

## 📦 Features

- Captures real-time network packets
- Displays:
  - 🔹 Source IP
  - 🔹 Destination IP
  - 🔹 Protocol (TCP, UDP, ICMP, etc.)
  - 🔹 Optional Payload (up to 50 bytes)
- Easily customizable and extendable
- Simple CLI-based packet sniffer

---

## 🛠️ Built With

- Python 3
- Scapy library (`pip install scapy`)

---

## 📄 How to Run

> ⚠️ Run with administrative/root privileges!


👨‍💻 Author
Rudra Narayan Swain
Cyber Security Enthusiast | Python Developer


```bash
# Install requirements
pip install scapy

# Run the sniffer
sudo python packet_sniffer.py
