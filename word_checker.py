#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. Then you
#can use the in operator as a fast way to check whether a string is in the
#dictionary.


check = open ('words.txt')
c_list = []

for checker in check:
    clear = checker.split()
    for clears in clear:

         c_list.append(clears)
    


c_dic = dict()


for obs in c_list:

  if obs not in c_dic:
     c_dic[obs]= 1
  else:
      c_dic[obs] +=1

print (c_dic)    
