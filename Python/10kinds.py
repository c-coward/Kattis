from sys import stdin

def find(parents,a):
    if a == parents[a]: return a

    parents[a] = find(parents,parents[a])
    return parents[a]

def union(parents,size,a,b):
    fa = find(parents,a)
    fb = find(parents,b)
    
    if size[fa] < size[fb]:
        fa,fb = fb,fa
    
    size[fa] += size[fb]
    parents[fb] = fa

def main():
    r,c = [int(i) for i in input().split()]
    board = [stdin.readline() for i in range(r)]

    parents = [i for i in range(r*c)]
    size = [1] * (r*c)

    for i in range(r):
        for j in range(c):
            if (i + 1 < r and board[i][j] == board[i+1][j]):
                union(parents,size,i*c + j,(i+1)*c+j)

            if (j + 1 < c and board[i][j] == board[i][j+1]):
                union(parents,size,i*c + j,i*c+j+1)


    tests = int(stdin.readline())
    outs = []

    user = ['binary','decimal']

    for t in range(tests):
        y1,x1,y2,x2 = [int(i)-1 for i in stdin.readline().split()]
        start = c*y1 + x1
        end = c*y2 + x2

        if find(parents,start) == find(parents,end):
            outs.append(user[int(board[y1][x1])])
        else:
            outs.append('neither')

    print('\n'.join(outs))

main()
