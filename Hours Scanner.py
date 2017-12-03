name = input("Enter file:")
if len(name) < 1 : name = "messege.txt"
handle = open(name)
time=[]
hours=[]
dic={}
i=0
temp=[]
for line in handle:
    line.rstrip()
    if not line.startswith('From') or line.startswith('From:'):continue
    time.append(line.split()[-2])
    hours.append(time[i].split(":")[0])
    i = i+1
for hour in hours:
    dic[hour] = dic.get(hour , 0) + 1
for k,v in dic.items():
    newtuple = (k,v)
    temp.append(newtuple)
temp = sorted(temp)
for k ,v in temp:
    print (k, v)
