import copy

laberinto = [
    ['F',  1,  1,  1,  0,  1,  1,  1,  1],
    [ -2,  0,  0, -1,  0,  1,  0,  1,  0],
    [  1,  1,  0,  1,  1,  1,  0,  1,  0],
    [  0,  1,  0, -1,  0,  0,  0, -1,  0],
    [  1,  1,  1,  1,  1,  1,  1,  1,  0],
    [ -1,  0,  0,  0,  0,  0,  0,  1,  1],
    [  1,  1,  1,  1, -1,  1,  1,  1,  0],
    [  1,  0,  0,  1,  0,  1,  0,  1,  0],
    ['I',  1, -1,  1,  1,  1,  0,  1,  1],
]
FILAS=9; COLS=9; INICIO=(8,0); FIN=(0,0)
MOVIMIENTOS=[(1,0),(0,1),(-1,0),(0,-1)]
NOMBRES=["abajo","derecha","arriba","izquierda"]

def valor(r,c):
    v=laberinto[r][c]
    return 1 if v in ('I','F') else v

def mostrar(path=None):
    p=set(path) if path else set()
    for r in range(FILAS):
        print("  ".join("*" if (r,c) in p else str(laberinto[r][c]) for c in range(COLS)))
    print()

def backtrack(r,c,vidas,vis,camino,sol):
    if (r,c)==FIN:
        sol.append(copy.deepcopy(camino))
        print(f"META en {FIN}, vidas={vidas}")
        return True
    for (dr,dc),nom in zip(MOVIMIENTOS,NOMBRES):
        nr,nc=r+dr,c+dc
        if not(0<=nr<FILAS and 0<=nc<COLS): continue
        if valor(nr,nc)==0: continue
        if (nr,nc) in vis: continue
        nv=vidas+valor(nr,nc)
        if nv<=0:
            print(f"INVIABLE [{nr},{nc}] vidas={nv}")
            continue
        camino.append((nr,nc)); vis.add((nr,nc))
        print(f"Avanzo [{nr},{nc}] ({nom}) vidas={nv}")
        if backtrack(nr,nc,nv,vis,camino,sol): return True
        print(f"Retrocedo de [{nr},{nc}]")
        camino.pop(); vis.remove((nr,nc))
    return False

print("LABERINTO ORIGINAL:"); mostrar()
camino=[INICIO]; vis={INICIO}; sol=[]
encontrado=backtrack(INICIO[0],INICIO[1],3,vis,camino,sol)
print("="*40)
if encontrado:
    print("El raton LOGRO salir!")
    print(f"Camino: {sol[0]}")
    print("\nRUTA SOLUCION:"); mostrar(sol[0])
else:
    print("El raton NO pudo salir.")
print("="*40)
