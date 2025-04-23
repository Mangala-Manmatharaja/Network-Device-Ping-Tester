import subprocess

def ping_device(ip):
    try:
        output = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)
        return "UP" if output.returncode == 0 else "DOWN"
    except Exception:
        return "ERROR"
