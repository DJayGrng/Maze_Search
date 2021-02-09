import time
import os
from collections import deque

R=0
C=0
stx=0
sty=0
ed=0
dr=[-1,+1,0,0]
dc=[0,0,+1,-1]
end=False


def ret_path(graph,way):
    global R
    global C
    global stx
    global sty
    global ed

    edx, edy = zip(ed)
    edx = list(edx)
    edy = list(edy)
    path=[]
    while graph[edx[0]][edy[0]]!="s":
        edx,edy=zip(way[edx[0]][edy[0]])
        path.append([edx[0],edy[0]])


    return path


def path(graph):
    global R, C, stx, sty,end
    og_path=[]
    qx = deque([])
    qy = deque([])
    qx.append(stx)
    qy.append(sty)
    visited = [[0 for y in range(C)] for x in range(R)]
    way = [[None for y in range(C)] for x in range(R)]
    visited[stx][sty] = 1
    while len(qx)>0 :
        x=qx.popleft()
        y=qy.popleft()
        if graph[x][y]=='e':
            end = True
            break
        i = 0
        while i < 4:
            rr = x + dr[i]
            cc = y + dc[i]
            i += 1
            if rr < 0 or cc < 0:
                continue
            elif rr >= R or cc >= C:
                continue
            elif (graph[rr][cc]=='.' or graph[rr][cc]=='e') and visited[rr][cc]==0:
                qx.append(rr)
                qy.append(cc)
                visited[rr][cc]=1
                way[rr][cc]=[x,y]
            else:
                continue
    if end==True:
        og_path=ret_path(graph,way)
        og_path.reverse()
        print("Path is :", end="")
        print(og_path)
        print("Length of path is :", end="")
        print(len(og_path))
    else:
        print("No Path")




def read_maze(filename):
    global R, C, stx, sty, ed
    file = open(filename,"r")
    data = file.readlines()
    R=len(data)
    C=len(data[0])-1
    graph=[["" for y in range(C)] for x in range(R)]
    for r in range(len(data)):
        ch = data[r]
        ch = ch[:-1]
        for c in range(len(ch)):
            graph[r][c] = ch[c]

    for x in range(R):
        for y in range(C):
            if "s" == graph[x][y]:
                stx, sty = x, y
            if "e" == graph[x][y]:
                ed = [x, y]
    start = time.time()
    path(graph)
    end = time.time()
    print("Time Taken:",end="")
    print(end - start)
    file.close()



if __name__ == "__main__":

    items = os.listdir(".")
    newlist = []
    for names in items:
        if names.endswith(".txt"):
            newlist.append(names)
    while True:
        R = 0
        C = 0
        stx = 0
        sty = 0
        ed = 0
        end = False
        print("Which file do you want to choose?")
        i=0
        while i<len(newlist):
            i+=1
            print(newlist[i-1])
        ans=input("Enter Answer Here:")
        if ans not in newlist:
            print("Wrong Choice .. Exiting !!")
            break
        read_maze(ans)



