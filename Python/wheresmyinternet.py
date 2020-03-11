from sys import stdin

def main():
    n,m = map(int,stdin.readline().split())
    parents = list(range(n+1))
    size = [1 for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,stdin.readline().split())
        union(parents,size,a,b)

    discon = [str(i) for i in range(n+1) if find(parents,parents[i]) != find(parents,1)]
    if discon[1:]:
        print('\n'.join(discon[1:]))
    else:
        print('Connected')

def find(parents,x):
    if x == parents[x]: return x

    parents[x] = find(parents,parents[x])
    return parents[x]

def union(parents,size,x,y):
    fx,fy = find(parents,x),find(parents,y)

    if fx == fy: return
    if size[fx] < size[fy]: fx,fy = fy,fx

    parents[fy] = fx
    size[fx] += size[fy]

main()