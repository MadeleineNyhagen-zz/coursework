a = [67,45,2,13,1,998]
print(a)
def listSort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
              if items[j] > items[j+1]:
                  items[j], items[j+1] = items[j+1], items[j]

listSort(a)

print(a)

              
        
        
