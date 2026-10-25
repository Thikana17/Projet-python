def est_palindrome(mot: str) -> bool:
    if not mot.isalpha():
        raise ValueError("Le texte doit contenir uniquement des lettres, sans espaces ni chiffres.")
    
    mot_minuscule = mot.lower()
    return mot_minuscule == mot_minuscule[::-1]