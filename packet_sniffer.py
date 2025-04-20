

# ⚠️ Task K-05: Network Packet Analyzer (Educational Use Only)
# Internship: Prodigy InfoTech - Comillas Negras

from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        # Identify protocol
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = f"Other (Proto ID: {proto})"

        print(f"\n🔍 Packet Captured:")
        print(f"  ➤ Source IP: {src_ip}")
        print(f"  ➤ Destination IP: {dst_ip}")
        print(f"  ➤ Protocol: {protocol}")

        # Optional payload display
        if packet.payload:
            print(f"  ➤ Payload: {bytes(packet.payload)[:50]}")

print("🛡️ Starting Packet Sniffer (Press Ctrl+C to stop)...")
sniff(prn=analyze_packet, store=False)
