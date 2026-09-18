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
    print("=== STATUS PERANGKAT ===")
    for key, perangkat in data.items():
        print(f"{perangkat['nama']} | IP: {perangkat['ip']} | Status: {perangkat['status']}")

def hitung_ringkasan(data):
    aktif = 0
    tidak_aktif = 0

    for perangkat in data.values():
        if perangkat["status"] == "up":
            aktif += 1
        else:
            tidak_aktif += 1

    return aktif, tidak_aktif

cek_status(perangkat)

aktif, tidak_aktif = hitung_ringkasan(perangkat)

print("\n=== RINGKASAN ===")
print(f"Jumlah perangkat aktif: {aktif}")
print(f"Jumlah perangkat tidak aktif: {tidak_aktif}")