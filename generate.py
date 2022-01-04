from typing import List
import random

class vertex:
    def __init__(self, id: int, size: int):
        self.found = False
        self.id = id
        self.nei = []
        if self.id % size != 0:
            self.nei.append(self.id - 1)
        if self.id % size != size - 1:
            self.nei.append(self.id + 1)
        if self.id - size >= 0:
            self.nei.append(self.id - size)
        if self.id + size < size ** 2:
            self.nei.append(self.id + size)

        self.select_nei = []
        self.isSoln = False


# dfs takes a graph G and perform dfs then return the processed graph G'
def dfs(verList: List[vertex]):
    stack = []
    parentMap = {}
    size = len(verList)
    hasSoln = False
    # Choose the initial ver, mark it as found and push it to the stack
    stack.append(verList[0])
    verList[0].found = True
    # While the stack is not empty
    while len(stack) != 0:        
        # Pop a ver from the stack and make it a current ver
        curr_ver = stack.pop()
        unfound_nei = []
        # get all un-found vertices
        for n in curr_ver.nei:
            if verList[n].found == False:
                unfound_nei.append(n)

        # if current vertex has unfound neighbour, we randomly choice a selected vertice and
        # append this selected vertex to the stack
        if len(unfound_nei) > 0:
            select_ver = verList[random.choice(unfound_nei)]
            curr_ver.select_nei.append(select_ver)
            select_ver.select_nei.append(curr_ver)
            select_ver.found = True
            stack.append(select_ver)
            if not hasSoln:
                parentMap[select_ver] = curr_ver
            if select_ver.id == size - 1:
                hasSoln = True

        # if current vertex has more than one unfound neighbour,
        # append current vertex to the stack
        if len(unfound_nei) > 1:
            stack.append(curr_ver)

    curr = verList[size - 1]
    while curr.id != 0:
        verList[curr.id].isSoln = True
        curr = parentMap[curr]

# generates a maze
def make_map(size: int) -> List[List[int]]:

    numVerti = size ** 2
    verList = []

    for id in range(numVerti):
        verList.append(vertex(id, size))

    dfs(verList)
    return verList