data = []
count = 0
sum = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了！總共有',len(data),'筆資料')

wc = {} #word_count
for d in data :
	words = d.split(' ')
	for word in words:
		if word not in wc:
			wc[word] = 1
		else:
			wc[word] += 1

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])
while True:
	key = input('請輸入你要找的字: ')
	if key == 'q':
		break
	if key in wc:
		print('你輸入的',key,'出現過',wc[key],'次！')
	elif key not in wc:
		print('這個字沒有出現過喔！')


# for i in data:
# 	sum += len(i)
# avg = sum / len(data)
# print('留言平均長度為', avg)

# new = []
# for d in data :
# 	if len(d) < 100:
# 		new.append(d)
# print('總共有', len(new), '留言小於100個字')

# good = []
# for d in data:
# 	if good in d:
# 		good.append(d)
# print('一共有', len(good), '個留言包含good')




#print(data)
