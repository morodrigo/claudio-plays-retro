# Batman: The Video Game (USA) — RAM verificada

ROM: *Batman: The Video Game (USA)*, SHA-1 sin encabezado iNES `a6c56ac787ff11a67921867ffc9f79a57a382657`.
Integración: `integrations/Batman-Nes/`.

Direcciones comprobadas en emulador (stable-retro) jugando los 18 tramos del juego completo, a partir del mapa de
Data Crystal.

| Variable | Dirección | Significado |
|---|---|---|
| `level` | `$88` | Tramo: 0 = 1-1 y sube de 2 en 2 (1-2 = 2, 1-3 = 4, 2-1 = 6 … 5-3 = `$22`) |
| `health` | `$B7` | Vida (8 = llena). No se rellena entre tramos |
| `lives` | `$BE` | Vidas restantes (2 = tres vidas; negativo = game over) |
| `ammo` | `$B8` | Munición del arma actual |
| `weapon` | `$A6` | Arma (nibble alto): `$00` golpe, `$50` batarang, `$60` estrellas, `$C0` pistola |
| `y_screen`, `y` | `$D0`, `$D1` | Posición vertical: pantalla y píxel |
| `x_screen`, `x` | `$D3`, `$D4` | Posición horizontal: pantalla y píxel |

`scenario.json`: termina cuando se acaban las vidas; recompensa por pasar de tramo (`level`) y una pequeña por
avanzar en `x`.

`Level1-1.state`: inicio de la etapa 1 (las calles de Gotham) con control.

## Fuentes

- Data Crystal, *Batman: The Video Game (NES)/RAM map*: https://datacrystal.tcrf.net/wiki/Batman:_The_Video_Game_(NES)/RAM_map
- Códigos Action Replay del tramo (`0088`), de almarsguides.com
