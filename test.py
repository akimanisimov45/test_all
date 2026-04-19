animals = ["кот","слон","пёс","тигр","лиса"]

for i in range(1, 11):
    print(i**2)

for i in range(1,20):
    if i % 2 == 0:
        print(i)

for word in animals:
    if len(word)>4:
        print(word)

test1 = [i**2 for i in range(1,11)]
print(test1)

testik= [i for i in range(1,21) if i%2 == 0]
print(testik)

testovik=[word for word in animals if len(word)>4]
print(testovik)