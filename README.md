# claudio-plays-retro

Integraciones de juegos de NES para [stable-retro](https://github.com/Farama-Foundation/stable-retro) y mapas de RAM
verificados, salidos del proyecto **Claudio Plays** (una IA que juega clásicos de NES con búsqueda Go-Explore).

> **No incluye ROMs.** Cada integración trae solo la huella de la ROM (`rom.sha`). Necesitas tu propia copia legal
> del juego e importarla con `python -m stable_retro.import <carpeta_con_tus_roms>`.

## Contenido

| Juego | Carpeta | Estado |
|---|---|---|
| Metroid (USA) | `integrations/Metroid-Nes/` | lista (probada con stable-retro 1.0.1) |
| Batman: The Video Game (USA) | `integrations/Batman-Nes/` | lista (probada con stable-retro 1.0.1) |
| Super Mario Bros. 2 (USA) | `integrations/SuperMarioBros2-Nes/` | lista (probada con stable-retro 1.0.1) |
| Mega Man (USA) — ampliada | `integrations/MegaMan-Nes/` | lista: mejora la oficial (8 variables y 6 estados más) |

Cada integración sigue el formato de stable-retro:

- `data.json`: variables de RAM (dirección y tipo).
- `scenario.json`: recompensa y condición de fin.
- `metadata.json`: estado por defecto.
- `*.state`: estados de inicio.
- `rom.sha`: SHA-1 de la ROM esperada.

## Uso

```bash
pip install stable-retro
python -m stable_retro.import /ruta/a/tus/roms
python tools/probar_integracion.py integrations/Metroid-Nes
```

## Fuentes

Las direcciones de RAM se verificaron en emulador y se contrastaron con desensambles y documentación pública
(se cita la fuente en `docs/` de cada juego).

## Licencia

MIT. Los juegos y sus marcas pertenecen a sus dueños; este repo no distribuye contenido de los juegos.
