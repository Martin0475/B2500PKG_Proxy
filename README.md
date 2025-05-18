# B2500PKG_Proxy – Home Assistant Add-on

Ein MQTT-Proxy für Geräte mit identischer Client-ID. Dieses Add-on erlaubt es, mehrere MQTT-Geräte über unterschiedliche Ports an Home Assistant weiterzuleiten.

## Funktionen

- Automatische Umbenennung der Client-ID (`mst_` → `mst_1901` bis `mst_1909`)
- 1:1 Topic-Durchleitung (senden + empfangen)
- Weboberfläche zur Eingabe von Benutzername und Passwort pro Gerät

## Installation

1. Repository zu Home Assistant hinzufügen:
   ```
   https://github.com/Martin0475/B2500PKG_Proxy
   ```
2. Add-on „B2500PKG_Proxy“ installieren
3. Konfiguration anpassen (Ports, Benutzer)
4. Add-on starten

## Beispielkonfiguration

```yaml
devices:
  - port: 1901
    username: "user1"
    password: "pass1"
  - port: 1902
    username: "user2"
    password: "pass2"
```

## Lizenz

MIT
