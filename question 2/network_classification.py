devices = ["Switch", "Router", "Bridge", "Access Point"]

media = ["Ethernet Cable", "Fiber Optic Cable", "Wireless"]

device_info = {
    "Switch": (
        "Data Link Layer (Layer 2)",
        "Connects devices in a LAN and forwards frames using MAC addresses."
    ),
    "Router": (
        "Network Layer (Layer 3)",
        "Connects different networks and forwards packets using IP addresses."
    ),
    "Bridge": (
        "Data Link Layer (Layer 2)",
        "Connects two LAN segments and filters traffic using MAC addresses."
    ),
    "Access Point": (
        "Data Link Layer (Layer 2)",
        "Provides wireless access and connects wireless devices to a LAN."
    )
}

media_info = {
    "Ethernet Cable": "Wired medium used for LAN communication.",
    "Fiber Optic Cable": "High-speed medium that transmits data using light.",
    "Wireless": "Uses radio waves for wireless communication."
}

print("NETWORK DEVICE CLASSIFICATION REPORT")
print("=" * 50)

for device in devices:
    layer, function = device_info[device]
    print("\nDevice:", device)
    print("Layer:", layer)
    print("Primary Function:", function)

print("\nTRANSMISSION MEDIA")
print("=" * 50)

for medium in media:
    print("\nMedium:", medium)
    print("Function:", media_info[medium])