import json
#inp = input() #

def findBiggestContraption(inp):
    containers = json.loads(inp)
    if len(containers) == 0: # Пустой массив
        return 0
    maxLength = 1 # Всегда существует матрешка как минимум из одного контейнера
    tree = []
    for c in containers:
        tree.append([c])

    while True:
        newTree = []
        for e in tree:
            parent = e[-1] # Последний элемент списка
            for n in containers:
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
    
# "[[5,4],[6,4],[6,7],[2,3]]"
if __name__ == '__main__':
    print(findBiggestContraption(input()))
