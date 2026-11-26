# Mega Man (USA) — integración ampliada

ROM: *Mega Man (USA)*, SHA-1 sin encabezado iNES `6047e52929dfe8ed4708d325766ccb8d3d583c7d` (la misma que usa la
integración oficial `MegaMan-Nes` de stable-retro).

La integración oficial solo trae `health`, `lives` y `score` y un estado. Esta versión **conserva esas tres variables
con las mismas direcciones** (compatible) y agrega las que usó Claudio para jugar el juego completo, más un estado de
inicio por cada Robot Master.

| Variable | Dirección | Significado |
|---|---|---|
| `health` | `$6A` | Vida de Mega Man (28 = llena) — *oficial* |
| `lives` | `$A6` | Vidas restantes — *oficial* |
| `score` | `$72` | Puntaje — *oficial* |
| `stage` | `$31` | Etapa: 0 Cut, 1 Ice, 2 Bomb, 3 Fire, 4 Elec, 5 Guts (6+ castillo de Wily) |
| `boss_health` | `$6C1` | Vida del jefe: se llena de 0 a 28 al entrar a su cuarto |
| `x` | `$480` | X en el mundo (byte bajo, sigue el scroll) |
| `section` | `$460` | Sección de la etapa (sube en tramos horizontales y verticales) |
| `screen` | `$1B` | Pantalla actual (sube también en tiros verticales donde `section` no cambia) |
| `y` | `$600` | Y (menor = más arriba) |
| `weapon` | `$5F` | Arma equipada: 0 Buster, 1 Cut, 2 Ice, 3 Bomb, 4 Fire, 5 Elec, 6 Guts, 7 Magnet Beam |
| `weapons_obtained` | `$5D` | Bits de armas obtenidas (jefes vencidos), p. ej. Fire = bit 6 |

## Estados

Tomados de la partida encadenada de Claudio (orden Fire → Bomb → Guts → Cut → Elec → Ice), así que cada etapa
empieza con las armas ganadas antes:

| Estado | Etapa | Armas ya obtenidas |
|---|---|---|
| `FireMan` (por omisión) | 3 | ninguna |
| `BombMan` | 2 | Fire |
| `GutsMan` | 5 | Fire, Bomb |
| `CutMan` | 0 | Fire, Bomb, Guts |
| `ElecMan` | 4 | + Cut |
| `IceMan` | 1 | + Elec |

Para proponerla a stable-retro conviene **agregar** estos estados y variables sin borrar el `Level1.state` oficial.

## Fuentes

- Data Crystal, *Mega Man (NES)/RAM map*: https://datacrystal.tcrf.net/wiki/Mega_Man_(NES)/RAM_map
- Verificación propia en emulador (stable-retro) durante la partida completa.
