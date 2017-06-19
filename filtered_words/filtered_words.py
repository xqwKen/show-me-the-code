# coding=utf-8
user_input=input("Leave your comments:  ")
for filter_word in open("filtered_words.txt"):
    fw=filter_word.rstrip()
    if fw in user_input:
        fw_len=len(fw)
        user_input=user_input.replace(fw,'*'*fw_len)  #将user_input在原处进行修改，进行下一次循环查找。

else:
           print(user_input)