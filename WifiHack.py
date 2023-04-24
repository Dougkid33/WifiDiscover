# first let print de header here
import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors="backslashreplace")

# separando dados linhas por linhas
data = data.split('\n')

# criando uma lista de profiles
profiles = []

# passar os dados

for i in data:
    if "All User Profile" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        profiles.append(i)

print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
print("------------------------------------------------")

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])

        results = results.decode('utf-8', errors="backslashreplace")
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(i, ""))

        except IndexError:
            print("{:<30}| {:<}".format(i, ""))

    except subprocess.CalledProcessError:
        print("Encoding Error Occurred")
