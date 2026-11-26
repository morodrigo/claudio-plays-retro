# Mega Man 2 (USA) — integración ampliada

ROM: *Mega Man 2 (USA)*, SHA-1 sin encabezado iNES `2ec08f9341003ded125458df8697ca5ef09d2209` (la misma que usa la
integración oficial `MegaMan2-Nes` de stable-retro).

La integración oficial trae `health`, `lives`, `progress` y un estado (Flash Man). Esta versión **conserva esas tres
variables con las mismas direcciones** y la misma condición de fin, y agrega las que usó Claudio para jugar el juego
completo (en la versión europea, con las mismas direcciones; aquí comprobadas otra vez en la ROM USA), más un estado
de inicio por cada Robot Master.

| Variable | Dirección | Significado |
|---|---|---|
| `health` | `$6C0` | Vida de Mega Man (28 = llena) — *oficial* |
| `lives` | `$A8` | Vidas restantes — *oficial* |
| `progress` | `$45F` (2 bytes) | Avance horizontal — *oficial* |
| `stage` | `$2A` | Etapa: 0 Heat, 1 Air, 2 Wood, 3 Bubble, 4 Quick, 5 Flash, 6 Metal, 7 Crash, 8+ castillo de Wily |
| `boss_health` | `$6C1` | Vida del jefe (se llena al entrar a su cuarto) |
| `etanks` | `$A7` | E-tanks |
| `x_screen`, `x` | `$440`, `$460` | Posición horizontal: pantalla y píxel |
| `y` | `$4A0` | Posición vertical |
| `weapon` | `$A9` | Arma equipada: 0 Buster, 1 Heat, 2 Air, 3 Wood, 4 Bubble, 5 Quick, 6 Flash, 7 Metal, 8 Crash, 9-11 ítems 1-3 |
| `weapons_obtained` | `$9A` | Bits: 01 Atomic Fire, 02 Air Shooter, 04 Leaf Shield, 08 Bubble Lead, 10 Quick Boomerang, 20 Time Stopper, 40 Metal Blade, 80 Crash Bomb |
| `items` | `$9B` | Ítems 1/2/3 obtenidos |
| `difficulty` | `$CB` | 0 Normal, 1 Difficult |

## Estados

`Normal.<Jefe>.Level1`: dificultad Normal, partida nueva (sin armas, 3 vidas), Mega Man ya aterrizado en el inicio de
cada etapa: Heatman, Airman, Woodman, Bubbleman, Quickman, Flashman (por omisión, como la oficial), Metalman,
Crashman.

Para proponerla a stable-retro conviene **agregar** los siete estados nuevos y las variables sin reemplazar el
`Normal.Flashman.Level1.state` oficial.

Nota: en la ROM USA el "READY" dura más que en la europea; para tomar los estados se espera a que Mega Man baje
(cambia la posición) y quede quieto 8 cuadros.

## Fuentes

- Data Crystal, *Mega Man 2 (NES)/RAM map*: https://datacrystal.tcrf.net/wiki/Mega_Man_2_(NES)/RAM_map
- Verificación propia en emulador (stable-retro).
