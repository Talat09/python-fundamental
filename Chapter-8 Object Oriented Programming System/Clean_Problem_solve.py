def process_queue(n,x,queue):
    ice_cream_count=x
    distressed_kids=0
    for operation, d in queue:
        if operation=="+":
            ice_cream_count+=d
        else:
            if ice_cream_count<d:
                distressed_kids+=1
            else:
                ice_cream_count-=d
    return ice_cream_count,distressed_kids

n,x=map(int,input().split())
queue=[]
for _ in range(n):
        operation,d=input().split()
        queue.append((operation,int(d)))
ice_cream_count,distressed_kids=process_queue(n,x,queue)

print(ice_cream_count,distressed_kids)