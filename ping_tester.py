import subprocess

def ping_device(ip):
    try:
        output = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)
        return "UP" if output.returncode == 0 else "DOWN"
    except Exception:
        return "ERROR"

# ------ Read devices from file -------
with open('devices.txt', 'r') as f:
    devices = [line.strip() for line in f]

# ----- Ping and save results
with open('ping_results.txt', 'w') as f:
    for ip in devices:
        status = ping_device(ip)
        print(f"{ip}: {status}")
        f.write(f"{ip}: {status}\n")
print("Results saved to ping_results.txt")