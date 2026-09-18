perangkat = {
    "router": {
        "nama": "Router",
        "ip": "192.168.1.1",
        "status": "Online"
    },
    "switch": {
        "nama": "Switch",
        "ip": "192.168.1.2",
        "status": "Online"
    },
    "server": {
        "nama": "Server",
        "ip": "192.168.1.10",
        "status": "Online"
    },
    "access_point": {
        "nama": "Access Point",
        "ip": "192.168.1.20",
        "status": "Offline"
    }
}

for key, data in perangkat.items():
    print(key, ":", data)