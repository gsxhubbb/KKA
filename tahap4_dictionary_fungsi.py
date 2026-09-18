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
        "status": "up"
    },
    "access_point": {
        "nama": "Access Point",
        "ip": "192.168.1.20",
        "status": "down"
    }
}

def cek_semua(data):
    for key, perangkat in data.items():
        print(perangkat["nama"], ":", perangkat["status"])

def hitung_aktif(data):
    jumlah = 0
    for perangkat in data.values():
        if perangkat["status"] == "up":
            jumlah += 1
    return jumlah

cek_semua(perangkat)
print("Jumlah perangkat aktif:", hitung_aktif(perangkat))