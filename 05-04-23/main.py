import json
inp = input() #"[[5,4],[6,4],[6,7],[2,3]]"
crates = json.loads(inp)

maxLength = 1 # Всегда существует матрешка из как минимум одного контейнера
tree = []
for c in crates:
    tree.append([c])

while True:
    newTree = []
    for e in tree:
        parent = e[-1] # Последний элемент списка
        for n in crates:
            if n[0] < parent[0] and n[1] < parent[1]:
                path = e.copy()
                path.append(n)
                
                newTree.append(path)

    if len(newTree) != 0:
        maxLength += 1
        tree = newTree
    else:
        #print(tree) # Выводит самые длинные цепочки
        break

print(maxLength)
# или print(len(tree[0])), тогда можно избавиться от maxLength
