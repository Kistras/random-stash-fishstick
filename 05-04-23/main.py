import json

def findBiggestContraption(inp):
    containers = [(x[0], x[1]) for x in json.loads(inp)]
    if len(containers) == 0: # Пустой массив
        return 0
    maxLength = 1 # Всегда существует матрешка как минимум из одного контейнера
    tree = []
    paths = {}
    for c1 in containers:
        pos = []
        for c2 in containers:
            if c1[0] > c2[0] and c1[1] > c2[1]:
                pos.append(c2)
        paths[c1] = pos

    for c in containers:
        tree.append([c])

    while True:
        newTree = []
        for e in tree:
            parent = e[-1] # Последний элемент списка
            for n in paths[parent]:
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

    return maxLength
    # или return len(tree[0]), тогда можно избавиться от maxLength

if __name__ == '__main__':
    print(findBiggestContraption(input()))
