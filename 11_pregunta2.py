import time
import asyncio
import random

PRECIO_MINIMO = 20000 #El precio base al que se inicia la subasta
PRECIO_MAXIMO = 20000 * 1.2 #El precio maximo que cualquiera de los participantes está dispuesto a pagar(úselo como tope en random.randint()

async def ofertas(oferta_actual, min, max):
    if oferta_actual > min:
        min = int(oferta_actual + 500)
        max = int(oferta_actual * 1.2)
    oferta = random.randint(min, max)
    return oferta, min, max

async def subasta():
    global final_a, final_b, final_c, final_d, final_e
    global ofertador_actual
    min = PRECIO_MINIMO
    max = PRECIO_MAXIMO
    oferta_actual = 2000
    ofertadores = ["a", "b", "c", "d", "e"]
    final_a=0; final_b=0; final_c=0; final_d=0; final_e=0
    ofertador_actual = 'z'

    while True:
        id = random.randint(0,4)
        ofertador = ofertadores[id]
        if ofertador == ofertador_actual:
            ofertador = ofertadores[id-1]
        oferta_actual, min, max = await ofertas(oferta_actual, min, max)
        ofertador_actual = ofertador
        if (id == 0):
            final_a = oferta_actual
        if (id == 1):
            final_b = oferta_actual
        if (id == 2):
            final_c = oferta_actual
        if (id == 3):
            final_d = oferta_actual
        if (id == 4):
            final_e = oferta_actual
        print(f"Participante {ofertador} hizo reoferta: {oferta_actual}")
        await asyncio.sleep(random.randint(0, 10))

async def main():

    try:
        await asyncio.wait_for(asyncio.gather(subasta()), timeout = 60)
    except asyncio.TimeoutError:
        print("Se cumplió el tiempo de 60 segundos")
    finally:
        print(f"Ofertas finales: ['a': {final_a}, 'b': {final_b}, 'c': {final_c}, 'd': {final_d}, 'e': {final_e}]")
        pass

if __name__ == "__main__":
    asyncio.run(main())
    print(f"El ganador es: {ofertador_actual}")