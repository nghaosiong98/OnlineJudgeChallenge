import sys
import time

map = {}

def main():
    for line in sys.stdin:
        start = time.time()
        print(f(int(line)))
        print(time.time()-start)

def f(n):
    if n==0:
        return 0
    elif n in map:
        return map[n]
    else:
        aux = f(int(n/2))+f(int(n/3))+f(int(n/4))
        if aux>n:
            map[n]=aux
        else:
            map[n]=n
        return map[n]

if __name__=='__main__':
    main()