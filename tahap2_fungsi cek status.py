perangkat = {
    "router": {
        "nama": "Router",
        "ip": "192.168.1.1",
        "status": "up"
    },
    "switch": {
        "nama": "Switch",
        "ip": "192.168.1.2",
        "status": "up"
    },
    "server": {
        "nama": "Server",
        "ip": "192.168.1.10",
        "status": "down"
    },
    "access_point": {
        "nama": "Access Point",
        "ip": "192.168.1.20",
        "status": "up"
    },
    "firewall": {
        "nama": "Firewall",
        "ip": "192.168.1.30",
        "status": "down"
    }
}

def cek_status(data):
    for key, perangkat in data.items():
        print(f"{perangkat['nama']} | IP: {perangkat['ip']} | Status: {perangkat['status']}")

cek_status(perangkat)