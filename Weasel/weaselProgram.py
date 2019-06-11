import random

goal = list(input('ENTRE COM A PALAVARA A SER GERADA: ').upper())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
nChildren = 100
mutRate = 0.10
bestOffspring = []
parent = []
gen = 0

for i in range(len(goal)):
    parent.append(random.choice(alphabet))

while bestOffspring != goal:
    gen = gen + 1
    nGood = nBad = nNeutral = nMutation = 0.0
    nSame = nChildren
    kids = []

    for i in range(nChildren):
        kid = parent[:]
        kidChanged = False

        for pos in range(len(kid)):
            if random.random() < mutRate:
                kidChanged = True
                nMutation += 1

                oldSymbol = parent[pos]
                possNewSymb = set(alphabet) - set(oldSymbol)
                newSymbol = random.choice(list(possNewSymb))
                kid[pos] = newSymbol

                if oldSymbol == goal[pos]:
                    nBad += 1
                elif newSymbol == goal[pos]:
                    nGood += 1
                else:
                    nNeutral += 1

        if kidChanged:
            nSame -= 1
        kids.append(kid)

    smallestDiff = len(goal) + 1

    for kid in kids:
        dif = 0
        for pos in range(len(goal)):
            if kid[pos] != goal[pos]:
                dif = dif + 1
        if dif < smallestDiff:
            smallestDiff = dif
            bestOffspring = kid
    parent = bestOffspring

    fitness = (len(goal)-smallestDiff)/len(goal)
    goodFraction = nGood/nMutation
    badFraction = nBad/nMutation
    neutralFraction = nNeutral/nMutation
    exit = ""
    
    for pos in range(len(goal)):
        if bestOffspring[pos] == goal[pos]:
            exit += bestOffspring[pos]
        else:
            exit += bestOffspring[pos].lower()
    print("\n-------Geração: %4d   : %s -------\nTaxas de mutação dos filhos:\n Elementos Diferentes: %3d   Fit: %.4f   Boa: %.4f  Ruim: %.4f  Neutra: %.4f  Indiferente: %3d" %
          (gen, exit, smallestDiff, fitness, goodFraction, badFraction, neutralFraction, nSame)) # Imprime os dados coletados
