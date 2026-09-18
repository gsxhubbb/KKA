def cek_status(nama, status):
    return f"Perangkat {nama} berstatus {status}"

print(cek_status("Router", "Online"))
print(cek_status("Switch", "Online"))
print(cek_status("Server", "Offline"))