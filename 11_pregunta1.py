import time
import asyncio
import random

PRECIO_MINIMO = 20000   #El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  #El precio maximo que cualquiera de los participantes está dispuesto a pagar(úselo como tope en random.randint()

async def participante():
    subasta = random.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
    await asyncio.sleep(random.randint(0, 10))
    return subasta
async def reconocer_elemento(idx):
    if idx == 0:
        return "a"
    elif idx == 1:
        return "b"
    elif idx == 2:
        return "c"
    elif idx == 3:
        return "d"
    elif idx == 3:
        return "e"
async def main():
    ofertas = await asyncio.gather(participante(), participante(), participante(), participante(), participante())
    ganador = max(ofertas)
    indice = ofertas.index(ganador)
    p_ganador = await asyncio.gather(reconocer_elemento(indice))
    msg = "El ganador es: " + p_ganador[0]
    ofertas_msg = f"Ofertas finales: ['a': {ofertas[0]}, 'b': {ofertas[1]}, 'c': {ofertas[2]}, 'd': {ofertas[3]}, 'e': {ofertas[4]}]"
    return ofertas_msg, msg
if __name__ == "__main__":
    ofertas, msg = asyncio.run(main())
    print(ofertas)
    print(msg)