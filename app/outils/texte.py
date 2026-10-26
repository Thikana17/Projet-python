def est_palindrome(mot: str) -> bool:
    if not mot.isalpha():
        raise ValueError("Le texte doit contenir uniquement des lettres, sans espaces ni chiffres.")
    
    mot_minuscule = mot.lower()
    return mot_minuscule == mot_minuscule[::-1]
def compter_voyelles(texte: str) -> int:
    voyelles = "aeiouyAEIOUY"
    compteur = 0
    for lettre in texte:
        if lettre in voyelles:
            compteur += 1
    return compteur
def inverser(texte: str) -> str:
    return texte[::-1]