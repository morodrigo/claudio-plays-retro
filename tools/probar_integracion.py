"""Prueba una integracion de este repo con stable-retro: carga el juego, imprime las variables de data.json al inicio
y cada N cuadros mientras se oprimen botones al azar, y verifica que el estado por defecto cargue.

uso: python tools/probar_integracion.py integrations/<Juego>-Nes <ruta_a_tu_rom.nes> [cuadros] [estado]
La ROM se copia temporalmente como rom.nes dentro de la carpeta (esta en .gitignore: nunca se sube).
"""
import os
import random
import shutil
import sys

import stable_retro as retro

carpeta = os.path.abspath(sys.argv[1])
rom = sys.argv[2]
cuadros = int(sys.argv[3]) if len(sys.argv) > 3 else 600
estado = sys.argv[4] if len(sys.argv) > 4 else retro.State.DEFAULT
juego = os.path.basename(carpeta)
raiz = os.path.dirname(carpeta)

shutil.copy(rom, os.path.join(carpeta, "rom.nes"))
try:
    retro.data.Integrations.add_custom_path(raiz)
    env = retro.make(game=juego, state=estado, inttype=retro.data.Integrations.CUSTOM_ONLY, use_restricted_actions=retro.Actions.ALL,
                     render_mode=None)
    env.reset()
    rnd = random.Random(0)
    info = None
    for f in range(cuadros):
        accion = [rnd.random() < 0.15 for _ in range(env.action_space.shape[0])]
        _, recompensa, terminado, truncado, info = env.step(accion)
        if f % 100 == 0:
            print(f, {k: int(v) for k, v in info.items()}, "recompensa", recompensa)
        if terminado or truncado:
            print("fin del episodio en el cuadro", f)
            break
    print("OK", juego, "variables:", sorted(info))
    env.close()
finally:
    os.remove(os.path.join(carpeta, "rom.nes"))
