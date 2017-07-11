sentence=input().strip().split(' ')		#Get the input in an array seperated by space
for i in range(len(sentence)):
	if i%2:
		sentence[i]=sentence[i][::-1] 		#To reverse the alternate string
print(*sentence)