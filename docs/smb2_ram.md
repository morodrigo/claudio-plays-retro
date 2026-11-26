# Super Mario Bros. 2 (USA) — RAM verificada

ROM: *Super Mario Bros. 2 (USA) (PRG0)*, SHA-1 sin encabezado iNES `43ac7c7aaf1846ead7b544302bb9131e4964fd32`.
Integración: `integrations/SuperMarioBros2-Nes/` (la que ya trae stable-retro, `SuperMarioBros2Japan-Nes`, es otro
juego: el *Lost Levels* japonés).

Direcciones tomadas del desensamble de Xkeeper0 (`ram.asm`, `defs.asm`) y comprobadas en emulador jugando los
niveles 1-1 a 3-2 (en la versión europea, PAL) y en esta ROM USA (inicio de 1-1, daño, caída, avance).

| Variable | Dirección | Significado |
|---|---|---|
| `world` | `$635` | Mundo (0 = Mundo 1) |
| `level` | `$531` | Nivel absoluto: 0 = 1-1, 1 = 1-2 … `$13` = 7-2 |
| `area` | `$532` | Área dentro del nivel (puertas, jarrones, subespacio cambian de área) |
| `area_pages` | `$53F` | Páginas del área − 1 (0 = cuarto de una pantalla) |
| `mode` | `$4EC` | 0 jugando, 1 tarjeta de nivel, 2 game over, 3 Bonus Chance |
| `player_state` | `$50` | 0 normal, 1 trepando, 2 levantando, 3 transición al trepar, 4/5 jarrón, 6 boca del halcón, 7 perdiendo vida, 8 cambio de tamaño |
| `x_page`, `x` | `$14`, `$28` | Posición horizontal: página y píxel |
| `y_page`, `y` | `$1E`, `$32` | Posición vertical: página y píxel (página `$FF` = arriba de la pantalla) |
| `horizontal` | `$EC` | 1 = área horizontal, 0 = vertical |
| `character` | `$8F` | 0 Mario, 1 Princesa, 2 Toad, 3 Luigi |
| `health` | `$4C2` | Vida: nibble alto + 1 = corazones llenos (`$1F` = 2, `$0F` = 1) |
| `lives` | `$4ED` | Vidas restantes |
| `holding` | `$9C` | ≠ 0 = carga un objeto |
| `subspace` | `$628` | ≠ 0 = dentro de un jarrón o en el subespacio |
| `crystal` | `$4B5` | ≠ 0 = ya tiene el cristal (abre la boca del halcón). Vuelve a 0 al entrar al cuarto del jefe |

Notas útiles para agentes:

- Al cambiar de área, durante algunos cuadros `x`/`y` todavía son los del área anterior aunque el jugador ya tenga
  control: conviene esperar a que la posición se asiente antes de usarla.
- En la selección de personaje la RAM parece "en juego" (`mode` 0, reloj corriendo) antes de que aparezca la pantalla.

`scenario.json`: termina en game over (`mode == 2`); recompensa por pasar de nivel.

`Level1-1.state`: inicio de 1-1 con Mario (cayendo por la puerta, con control).

## Fuentes

- Desensamble de Xkeeper0, *smb2*: https://github.com/Xkeeper0/smb2
- Data Crystal, *Super Mario Bros. 2 (NES)/RAM map*: https://datacrystal.tcrf.net/wiki/Super_Mario_Bros._2_(NES)/RAM_map
