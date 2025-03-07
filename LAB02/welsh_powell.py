import time

def welsh_powell(matrice_adj):
    """
    Algorithme de coloration Welsh et Powell.
    """
    temps_debut = time.time()
    n = len(matrice_adj) 
    degres = sorted(range(n), key=lambda v: sum(matrice_adj[v]), reverse=True) 
    couleurs = [-1] * n 
    nb_couleurs = 0  

    for sommet in degres:
        if couleurs[sommet] == -1:  # 
            couleurs[sommet] = nb_couleurs  

            for autre in degres:
                if couleurs[autre] == -1:  
                    if all(matrice_adj[autre][voisin] == 0 or couleurs[voisin] != nb_couleurs for voisin in range(n)):
                        couleurs[autre] = nb_couleurs
            
            nb_couleurs += 1  
    temps_execution = time.time() - temps_debut

    return couleurs, nb_couleurs, temps_execution