import string
import sys
import IPython.display as display
input = open('c:/Users/Denis.kozarenko/VS_code/VS_code/Skillfactory/Algoritms/dots.txt', 'r') #расскомментировать решая задачу локально

# input = sys.stdin //расскомментировать при сдаче задачи в системе
s = []
n = int(input.readline())
for i in range(1,n+1):
    x,y = map(int, input.readline().split())
    s.append([x,y])



def getKey(item):
    return item[1]
s.sort(key = getKey) 



        
def output(lst):
    dots_lst = []

    
    def dots(lst):
        right_dot = lst[0][1]
        dots_lst.append(right_dot)
        for cut in reversed(lst):
            if cut[0] <= right_dot <= cut[1]:
                lst.remove(cut)
                
        if lst:
            dots(lst)
        return None
                
    dots(lst)   
    rez = dots_lst
    print(len(rez))
    print(*rez)

output(s)



