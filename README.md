# PORTXY - Port Scanner
```
:::::::::   ::::::::  ::::::::: ::::::::::: :::   ::: 
:+:    :+: :+:    :+: :+:    :+:    :+:     :+:   :+: 
+:+    +:+ +:+    +:+ +:+    +:+    +:+      +:+ +:+  
+#++:++#+  +#+    +:+ +#++:++#:     +#+       +#++:   
+#+        +#+    +#+ +#+    +#+    +#+        +#+    
#+#        #+#    #+# #+#    #+#    #+#        #+#    
###         ########  ###    ###    ###        ###    
```

Ein einfacher, schneller Port-Scanner geschrieben in Python, der die ersten 1024 Ports einer Ziel-IP-Adresse scannt.

## Features

- 🔍 Scannt Ports 1-1024
- ⚡ Schnelle Scan-Geschwindigkeit mit Socket-Timeouts
- 🎨 Animierte Scan-Anzeige
- 💻 Cross-Platform (Windows, Linux, macOS)
- 🎯 Einfache Bedienung

## Voraussetzungen

- Python 3.x
- Keine externen Bibliotheken erforderlich (nutzt nur Python Standard-Library)

## Installation

1. Repository klonen:
```bash
git clone https://github.com/analyzeCS/portxy.git
cd portxy
```

2. Script ausführen:
```bash
python portxy.py
```

## Usage

1. Starte das Script:
```bash
python portxy.py
```

2. Gib die zu scannende IP-Adresse ein:
```
Enter the IP adress you want to scan: 192.168.1.1
```

3. Warte auf die Scan-Ergebnisse:
```
/ Scanning ports... 

Port 22 is open
Port 80 is open
Port 443 is open

Scan complete.
```

## Beispiele

**Lokales Netzwerk scannen:**
```bash
# Beispiel: Router scannen
Enter the IP adress you want to scan: 192.168.1.1
```

**Localhost scannen:**
```bash
Enter the IP adress you want to scan: localhost
```

**Externe IP scannen:**
```bash
Enter the IP adress you want to scan: 8.8.8.8
```

## Funktionsweise

Der Scanner nutzt TCP-Socket-Verbindungen, um zu überprüfen, ob Ports offen sind:
- **Timeout:** 0.5 Sekunden pro Port
- **Scan-Bereich:** Ports 1-1024 (Well-known Ports)
- **Methode:** TCP Connect Scan

## Häufig offene Ports

| Port | Service |
|------|---------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 80   | HTTP    |
| 443  | HTTPS   |
| 3306 | MySQL   |
| 3389 | RDP     |

## Rechtliche Hinweise

⚠️ **WICHTIG:** Dieses Tool darf nur für legale Zwecke verwendet werden!

- Scanne nur Systeme, für die du eine ausdrückliche Genehmigung hast
- Das Scannen fremder Systeme ohne Erlaubnis ist in vielen Ländern illegal
- Nutze dieses Tool nur zu Bildungszwecken oder für eigene Systeme
- Der Autor übernimmt keine Haftung für missbräuchliche Verwendung

## Limitierungen

- Scannt nur die ersten 1024 Ports
- Kein UDP-Support
- Keine Service-Erkennung
- Einfacher TCP Connect Scan (kann von Firewalls/IDS erkannt werden)

## Geplante Features

- [ ] Erweiterter Port-Bereich (custom range)
- [ ] Multi-Threading für schnellere Scans
- [ ] Service-Erkennung
- [ ] Export der Ergebnisse (JSON/CSV)
- [ ] UDP-Port-Scanning
- [ ] Banner-Grabbing

## Troubleshooting

**Problem:** "You must enter an IP address to scan."
- **Lösung:** Gib eine gültige IP-Adresse oder "localhost" ein

**Problem:** Keine offenen Ports gefunden
- **Lösung:** 
  - Überprüfe die IP-Adresse
  - Firewall könnte Scans blockieren
  - Ziel-Host könnte offline sein

**Problem:** Script hängt beim Scannen
- **Lösung:** Timeout-Wert in `s.settimeout(0.5)` anpassen

## Kontakt

**Made by Attack**

- Telegram: [t.me/mumbus200](https://t.me/mumbus200)
- GitHub: [github.com/analyzeCS](https://github.com/analyzeCS)

## Lizenz

Dieses Projekt ist für Bildungszwecke gedacht. Bitte nutze es verantwortungsvoll.

---

⭐ Wenn dir dieses Projekt gefällt, gib ihm einen Star auf GitHub!
