##given strings,find out the minimum changes to be done for changing them as anagram

w1=raw_input()
w2=raw_input()
import pdb;
#pdb.set_trace()
total=0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total+=abs(w1.count(letter)-w2.count(letter))
print total
