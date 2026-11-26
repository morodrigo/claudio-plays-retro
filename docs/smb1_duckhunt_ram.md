# Super Mario Bros. / Duck Hunt (USA) — integración

ROM: cartucho combinado *Super Mario Bros. / Duck Hunt (USA)*, SHA-1 sin encabezado iNES
`36e695ba6cacc8a5098fb67d9c1f8e6828d6c2c6`. Integración: `integrations/SuperMarioBrosDuckHunt-Nes/`.

La integración oficial `SuperMarioBros-Nes` de stable-retro usa el cartucho de *Super Mario Bros.* solo (otra ROM).
El código de Mario dentro del combo es el mismo, así que **las direcciones de RAM son las mismas**: esta integración
conserva las 9 variables oficiales y agrega las que usó Claudio para jugar los 32 niveles.

| Variable | Dirección | Significado |
|---|---|---|
| `coins`, `levelHi`, `levelLo`, `lives`, `score`, `scrolling`, `time`, `xscrollHi`, `xscrollLo` | (las oficiales) | Igual que `SuperMarioBros-Nes` |
| `player_state` | `$0E` | Estado: 8 normal, 0B cayendo/perdiendo vida, 6 perdió |
| `x_page`, `x` | `$6D`, `$86` | Posición horizontal: página y píxel |
| `y_page`, `y` | `$B5`, `$CE` | Posición vertical (`y_page` ≥ 2: cayó a un hoyo) |
| `power` | `$756` | 0 chico, 1 grande, 2 fuego |
| `mode` | `$770` | 1 jugando, 2 final |
| `area` | `$750` | Área (tubos y zonas de bonus cambian de área) |

`levelHi` = mundo − 1 y `levelLo` = nivel − 1 (4-2 → 3 y 1).

## Estados

`Level1-1` … `Level8-4`: los 32 niveles, tomados de la partida encadenada de Claudio (sin warps), así que cada nivel
empieza con las vidas, monedas, puntaje y tamaño que traía de antes.

## Fuentes

- Data Crystal, *Super Mario Bros. (NES)/RAM map*: https://datacrystal.tcrf.net/wiki/Super_Mario_Bros./RAM_map
- Integración oficial `SuperMarioBros-Nes` de stable-retro (variables originales).
- Verificación propia en emulador (stable-retro) durante la partida completa.
