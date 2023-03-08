"""
P1. Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea
într-un text care conține mai multe cuvinte separate prin ” ” (spațiu).
De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".
"""
# determina si returneaza cel mai mare cuvant lexicografic dintr-un text dat
# statement: str - textul dat
# returns str
def get_last_word_lexicographically(statement: str):
    #se imparte textul in cuvinte
    words = statement.split()
    last_word = words.pop()
    # se itereaza prin toate cuvintele si se alege cel mai mare lexicografic
    for word in words:
        if last_word < word:
            last_word = word
    return last_word


"""
P2. Să se determine distanța 
Euclideană între două locații identificate prin perechi de numere. 
De ex. distanța între (1,5) și (4,1) este 5.0
"""
# calculam si returnam distanta dintre doua puncte in plan
# Ax, Ay - int, coordonatele primului punct
# Bx, By - int, coordonatele celui de-al doilea punct
#returns double
def compute_euclidian_distance(Ax, Ay, Bx, By):
    return ((Bx - Ax) ** 2 + (By - Ay) ** 2) ** (1 / 2)


"""
P3. Să se determine produsul scalar a doi vectori rari care conțin numere reale.
Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni. 
De ex. produsul scalar a 2 vectori unidimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.
"""
# calculeaza si returneaza produsul scalar a doi vectori
# v1: list of int, vector de numere
# v2: list of int, vector de numere
# returns int
def scalar_multiplication(v1: list, v2: list):
    # in cazul in care vectorii sunt inegali luam lungimea cea mai mica
    minlen = min(len(v1), len(v2))
    p = 0
    # parcurgem vectorii in paralel
    for i in range(0, minlen):
        # adaugam in produsul scalar produsele elementelor de pe aceeasi pozitie in cei doi vectori
        p = p + (v1[i] * v2[i])
    return p


"""
P4. Să se determine cuvintele unui text 
care apar exact o singură dată în acel text. 
De ex. cuvintele care apar o singură dată în 
”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
"""
# determina cuvintele care apar o singura data intr-un text dat
# text - str, textul dat
# returns list of str
def get_unique_words(text: str):
    # se imparte textul in cuvinte
    words = text.split()
    # pregatim un dictionar pentru contorizarea aparitiilor cuvintelor
    word_counter = {}
    # iteram prin toate cuvintele
    for w in words:
        #verificam daca exista cuvantul in dictionar
        if w in word_counter:
            # incrementam numarul de aparitii
            word_counter[w] += 1
        else:
            # adaugam cuvantul in dictionar
            word_counter[w] = 1
    unique_words = []
    # se populeaza 'unique_words' cu acele cuvinte care au numarul de aparitii egal cu 1
    for k in word_counter:
        if word_counter[k] == 1:
            unique_words.append(k)
    return unique_words


"""
P5. Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} 
astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
"""

# determina un numar care apare de doua ori intr-un sir
# sir - list of int, un sir in care o singura valoare apare de doua ori
# returns int
def get_twin_number(sir: list):
    # pregatim un dictionar pentru contorizarea aparitiilor numerelor
    aparition_counter = {}
    # iteram prin toate numerele din sirul dat
    for n in sir:
        # verificam daca exista numarul in dictionar
        if n in aparition_counter:
            # incrementam numarul de aparitii
            aparition_counter[n] += 1
        else:
            # adaugam numarul in dictionar
            aparition_counter[n] = 1
    for n in aparition_counter:
        # returneaza valoarea care apare de doua ori
        if aparition_counter[n] == 2:
            return n


"""
P6. Pentru un șir cu n numere întregi care conține și duplicate,
să se determine elementul majoritar (care apare de mai mult de n / 2 ori). 
De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
"""
# determina elementul majoritar dintr-un sir dat = elementul cu nr de aparitii cel mai mare si peste n/2
def get_number_in_majority(sir: list):
    # dictionar pentru contorizarea aparitiilor
    apparence_counter = {}
    # numarul maxim de aparitii
    maxap = 0
    # valoarea din sir cu numar maxim de aparitii
    maxn = 0

    lgt = len(sir)
    for n in sir:
        if n in apparence_counter:
            # incrementam numarul de aparitii
            apparence_counter[n] += 1
        else:
            # adaugam numarul in dictionar
            apparence_counter[n] = 1
        # se calculeaza numarul maxim de aparitii
        if apparence_counter[n] > maxap:
            maxap = apparence_counter[n]
            # se retine valoarea cu nr maxim de aparitii
            maxn = n
    # se returneaza numarul maxim de aparitii daca este mai mare decat jumatate din lungimea sirului initial
    if maxap > lgt / 2:
        return maxn
    return "Nu exista nr majoritar"


"""
P7. Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.
"""
# determina si returneaza al k-lea cel mare element al unui sir dat
def get_kth_biggest_number(sir: list, k: int):
    # se foloseste mergesort pentru aa se sorta sirul
    def mergesort(arr):
        if(len(arr) > 1):
            # se determina mijlocul sirului
            mid = len(arr)//2
            # se imparte sirul in doua parti de la mijloc
            sub_st = arr[:mid]
            sub_dr = arr[mid:]
            # se autoapeleaza recursiv pana se ajunge la valori atomice
            mergesort(sub_st)
            mergesort(sub_dr)

            # se face interclasarea subsirurilor stang si drept
            i = j = k = 0
            while i < len(sub_st) and j < len(sub_dr):
                # ordine descrescatoare
                if sub_st[i] >= sub_dr[j]:
                    arr[k] = sub_st[i]
                    i += 1
                else:
                    arr[k] = sub_dr[j]
                    j += 1
                k += 1
            while i < len(sub_st):
                arr[k] = sub_st[i]
                i += 1
                k += 1
            while j < len(sub_dr):
                arr[k] = sub_dr[j]
                j += 1
                k += 1
    # se sorteaza sirul descrescator cu mergesort
    mergesort(sir)
    return sir[k-1]


"""
P8. Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. 
De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.
"""