data = []
count = 0
sum = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
for i in data:
	sum += len(i)
avg = sum / len(data)
print('留言平均長度為', avg)
new = []
for d in data :
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '留言小於100個字')



#print(data)
