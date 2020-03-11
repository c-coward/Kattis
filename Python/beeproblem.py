from collections import deque
from sys import stdin

def main():
    h,r,c = map(int,stdin.readline().split())
    
    visited = [0]*(r*c)
    sizes = [] # size of each honey cluster
    
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    diags = [[(1,-1),(-1,-1)],[(1,1),(-1,1)]]
    
    graph = [line.strip().split() for line in stdin]
    
    for l in range(r):
        for m in range(c):
            if graph[l][m] == '#': continue
            if visited[l*c+m]: continue
    
            q = deque()
            q.append((l,m))
            visited[l*c+m] = 1
            honeyhere = 0
    
            while q:
                y,x = q.popleft()
                honeyhere += 1
                if honeyhere == h: break
    
                for i,j in dirs:
                    if not (0 <= y+i < r and 0 <= x+j < c): continue
                    if graph[y+i][x+j] == '.' and not visited[(y+i)*c+(x+j)]:
                        visited[(y+i)*c+(x+j)] = 1
                        q.append((y+i,x+j))
    
                for i,j in diags[y%2]:
                    if not (0 <= y+i < r and 0 <= x+j < c): continue
                    if graph[y+i][x+j] == '.' and not visited[(y+i)*c+(x+j)]:
                        visited[(y+i)*c+(x+j)] = 1
                        q.append((y+i,x+j))
    
            sizes.append(honeyhere)
    
    sizes = sorted(sizes,reverse=True)
    adds = 0
    for s in sizes:
        if h <= 0: break
        h -= s
        adds += 1
    
    print(adds)

main()