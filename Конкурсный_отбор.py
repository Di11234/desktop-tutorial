n=int(input())
l=[]
for i in range(n):
    l.append(input())
l=tuple(l)
def delete():
    l_changed=list()
    for i in range(len(l)):
        print(l[i])
        if '2' in l[i] or '3' in l[i]:
            continue
        else:
            l_changed.append(l[i])
    print()
    for i in range(len(l_changed)):
        print(l_changed[i])
delete()