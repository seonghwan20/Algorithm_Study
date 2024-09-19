import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000000)

def bfs(x,y):
    graph[x][y]=0
    q=deque()
    q.append((x,y))

    while q:
        x,y =q.popleft()

        dx=[1,-1,0,0]
        dy=[0,0,1,-1]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<= nx < n and 0 <= ny < m and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))


t=int(input())

for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    cnt=0

    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1

    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)