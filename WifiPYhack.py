import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()  # cria um objeto PyWiFi
iface = wifi.interfaces()[0]  # pega a primeira interface (normalmente a única)

# verifica se a interface está desligada e a ativa se estiver
if iface.status() == const.IFACE_DISCONNECTED:
    iface.disconnect()
iface.status()

# escaneia as redes WiFi disponíveis
iface.scan()
networks = iface.scan_results()

# exibe o nome e senha de cada rede encontrada
for network in networks:
    ssid = network.ssid
    bssid = network.bssid
    # verifica se a rede possui senha
    if network.akm:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN  # autenticação aberta (sem senha)
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # tipo de autenticação WPA2
        profile.cipher = const.CIPHER_TYPE_CCMP  # tipo de criptografia
        # cria uma nova conexão com a rede WiFi
        iface.remove_all_network_profiles()
        new_profile = iface.add_network_profile(profile)
        # configura a senha da rede
        pass_str = " "  # coloque aqui a senha desejada
        new_profile.auth = const.AUTH_ALG_OPEN
        new_profile.akm.append(const.AKM_TYPE_WPA2PSK)
        new_profile.cipher = const.CIPHER_TYPE_CCMP
        key = pass_str.encode('utf-8')
        new_profile.key = key
        # conecta à rede WiFi
        iface.connect(new_profile)
        iface.disconnect()
        iface.remove_network_profile(new_profile)
        print(f"Rede WiFi: {ssid}\nSenha: {pass_str}\n")
    else:
        print(f"Rede WiFi: {ssid}\nNão possui senha.\n")
