# Metroid (USA) — RAM verificada

ROM: *Metroid (USA)*, SHA-1 sin encabezado iNES `fdbfc7871962f72a1ef57e5a7e456164fb93430b`.
Integración: `integrations/Metroid-Nes/`.

Todas las direcciones se comprobaron en emulador (stable-retro) jugando y repitiendo partidas, y se contrastaron con
las fuentes de abajo. Las de `$6xxx` son RAM del cartucho (stable-retro las expone en su dirección absoluta).

| Variable | Dirección | Significado |
|---|---|---|
| `routine` | `$1E` | Rutina principal: 3 jugando, 4 game over, 5 pausa |
| `area` | `$74` | Zona (nibble bajo): 0 Brinstar, 1 Norfair, 2 Kraid, 3 Tourian, 4 Ridley |
| `room_x`, `room_y` | `$50`, `$4F` | Cuarto en el mapa de 32×32 |
| `samus_half` | `$30C` | Mitad de la sala (0/1) |
| `samus_x`, `samus_y` | `$30E`, `$30D` | Posición dentro de la sala |
| `samus_state` | `$300` | 0 de pie, 1 corre, 2 salta, 3 bolita, 7/8 derrotada |
| `energy_lo`, `energy_hi` | `$106`, `$107` | Energía en BCD: unidades en el nibble alto de `$106`, decenas en el nibble bajo de `$107` |
| `energy_tanks` | `$6877` | Tanques de energía |
| `items` | `$6878` | Bits: 01 Bombas, 02 High Jump, 04 Long Beam, 08 Screw Attack, 10 Morph Ball, 20 Varia, 40 Wave Beam, 80 Ice Beam |
| `missiles`, `missiles_max` | `$6879`, `$687A` | Misiles actuales / máximo |
| `kraid_status`, `ridley_status` | `$687B`, `$687C` | Bits 0-1: jefe vencido; bit 7: estatua levantada |

`scenario.json`: termina con game over (`routine == 4`); recompensa por tanques de energía y por aumentar el máximo
de misiles.

## Fuentes

- Data Crystal, *Metroid/RAM map*: https://datacrystal.tcrf.net/wiki/Metroid/RAM_map
- Desensamblado de Nick Mikstas (`Metroid_Defines.asm`): https://github.com/nmikstas/metroid-disassembly
- TASVideos, *Game Resources: Metroid (NES)*: https://tasvideos.org/GameResources/NES/Metroid
