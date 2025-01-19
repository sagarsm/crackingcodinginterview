#Ait is to find which element in the array is that appears most frequently
#and how many times it appears
# for e.g. input : [2,2,1,1,1] output : 1:3 times
# for e.g. input : [1,2,3,4,5] output : 1:1 times
# for e.g. input : [1,1,1,1,1] output : 1:5 times 
num = input("Enter a number array: ").split()
num = [int(i) for i in num]

# for i in num:
#     if num.count(i) > 1:
#         print(f"{i}:{num.count(i)} times")
#         break
#     else:
#         print(f"{i}:1 times")
#         break

counter = 0
freq = 0
highestfreq_item = None
for i in num:
   #if counter == 0:
   highestfreq_item = i
    #print(f"{highestfreq_item},{i}")
   if i == highestfreq_item:
        print("i matches highestfreq_item")
        counter += 1
        freq += 1
        print(f"{i}:{freq} times")
   else:
        counter -= 1
        freq = 1
   #print(f"{i}:{freq} times")

print(f"{highestfreq_item}:{freq}:{counter} times")
    