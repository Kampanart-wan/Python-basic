type, gram = input().split()
teatype, sweetlevel, teacc = input().split()

gram = int(gram)
sweetlevel = int(sweetlevel)
teacc = int(teacc)

caloriepergram = {
    "H": 5,
    "O": 3,
    "J": 2,
}

teacalorie_table = {
    "R": {1: 12, 2: 18, 3: 25},
    "T": {1: 15, 2: 20, 3: 30},
    "M": {1: 10, 2: 15, 3: 20},
}

energy = caloriepergram[type] * gram
teaenergy = teacalorie_table[teatype][sweetlevel] * teacc

print(energy + teaenergy)
      