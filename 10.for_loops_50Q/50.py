highest_score=0
score_word=""
highest_v=0
vowel_word=0
highest_d=0
digit_word=0
total_text=0
total_v=0
total_c=0
total_d=0
total_s=0
for i in range(1,11):
    string=input("Enter string : ")
    count_u=0
    count_l=0
    count_d=0
    count_s=0
    vowel=0
    consonents=0
    count_space=0
    score=0
    for j in string:
        if j>='A' and j<'Z':
            total_text+=1
            count_u+=1
        elif j>='a' and j<='z':
            total_text+=1
            count_l+=1
        elif j>='0' and j<='9':
            total_d+=1
            count_d+=1
            score+=3
        elif j==" ":
            count_space+=1
            score+=0
        else:
            total_s+=1
            count_s+=1
            score+=4

        if j in "AEIOUaeiou":
            total_v+=1
            vowel+=1
            score+=2
        elif j>='A' and j<='Z' or j>'a' and j<='z':
            total_c+=1
            consonents+=1
            score+=1
        if score>highest_score:
            highest_score=score
            score_word=string
        if vowel>highest_v:
            highest_v=vowel
            vowel_word=string
        if count_d>highest_d:
                highest_d=count_d
                digit_word=string

    print(f" {i} {string}: uppercase {count_u} , lowercase {count_l} , digita {count_d} , space {count_space} , special ch {count_s} ,vowel {vowel} , consonats {consonents} ,")
    print(f"score of word {i}: {score}")



print(f"\nTotal: \nvowel {total_v} \n consonents {total_c}\ndigits {total_d}\nspeical case {total_s}")
print(f"highest score {highest_score} of {score_word}")
print(f"highest vowel {highest_v} of {vowel_word}")
print(f"highest digit {highest_d} of {digit_word}")



if total_text>total_s and total_text>total_d and total_text>total_c and total_text>total_v:
    print("text heavy")
elif total_d>total_text and total_d>total_v and total_d>total_c and total_d>total_s:
    print("Number heavy")
elif total_c>total_s and total_c>total_d and total_c>total_v and total_c>total_text:
    print("special character heavy")
else:
    print("balance")


