##Emrullah Arseven
#emrullaharseven@yandex.com

##enine arama
graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']

}

graph1 = {
    '1':['2','3','4'],
    '2':['1','3','5'],
    '3':['1','2','6'],
    '4':['1'],
    '5':['2'],
    '6':['3']
    }

def bfs(graph, start):
    ziydug = []
    kuyruk = [start]
    while kuyruk:
        simdikidug = kuyruk.pop(0)
        if simdikidug not in ziydug:
            ziydug.append(simdikidug)
            kuyruk.extend(graph[simdikidug])#burda stack listemize graph listesindeki node ekledik
    return ziydug


print("Ziyaret edilen dugumler")
print (bfs(graph1, '1'))

###################################################

##derine arama
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
ziydug = []
graph2={
    '1':['2','3','4'],
    '2':['1','3','5'],
    '3':['1','2','6'],
    '4':['1'],
    '5':['2'],
    '6':['3']


}

def dfs(graph,node):
    if node not in ziydug:
        ziydug.append(node)
        for n in graph[node]:
            dfs(graph,n)

dfs(graph2,'5')
print(ziydug)