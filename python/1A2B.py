# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:58:08 2021

@author: water
"""
#>>>comment>>>
#架構：
#1.起始階段
#在按下開始後，從0~9中選四個不重複的數字
#為了可以一直玩到不想完，在每次出答案時都要初始化答案覆蓋到ans裡。
#2.輸入階段
#利用int型別存入數字，如果輸入符合格式的話就可以用除法把每個十進位數分離開。
#同時檢查一些不符合格式的輸入，如果錯了就重跑新的一輪迴圈。
#3.配對階段
#將分離成陣列的數組與答案進行配對，得到AB分別的個數
#如果是4A，代表猜中了，跳出判斷迴圈；若不是4A，就把結果輸出。
#同時為了讓玩家知道紀錄，要把猜的數字也顯示出來。
#如果是第八次配對也沒猜中，代表玩家輸了。



#>>>code>>>>

import random
number=[0,1,2,3,4,5,6,7,8,9]
number1=[]
def ans():
    number1=[]
    for n in number:
        number1.append(n)
    random.shuffle(number1)
    number1=number1[0:4]
    return number1

def re(x1):
    a=x1//1000
    b=x1%1000
    c=b%100
    d=c%10
    b=b//100
    c=c//10
    x=[a,b,c,d]
    return x


def D(x,sol):
    A=0
    B=0
    for i in range(0,4,1):
        if x[i]==sol[i]:
            A=A+1
        elif x[i]in sol:
            B=B+1
    return A,B


def judge(x):
    t=0
    if x[0]>=10:
        return 1
    for i in range(0,2):
        for j in range(i+1,4):
            if x[i]==x[j]:
                t=1
    return t                            
            
def main():
    print("猜數字遊戲\n開始後會生成一個隨機數字不重複的四位數(首位數可能為0)")
    print("A:數字正確且位數也正確\nB:數字正確但位數不正確")
    print("ex.答案為0123 猜0456→1A0B(0)、猜1234→0A3B(123)")
    print("八次內沒猜中就輸了")
    c=1
    sol=ans()
    go=int(input("\n\n1.開始遊戲 其他按鍵:離開"))
    while(go==1): 
        print("第",c,"次:")
        x1=int(input())
        x=re(x1)
        t=judge(x)
        if t==1:
            print("格式錯誤!")
            continue
        A,B=D(x,sol)
        if A!=4:
            print("第",c,"次猜",x,A,"A",B,"B")
        c+=1
        if A==4:
            print("正確答案是",sol)
            print("你贏了!")
            go=int(input("是否繼續?\n1.是2.否"))
            sol=ans()
            c=1
        if c>8:
            print("正確答案是",sol)
            print("你輸了!")
            go=int(input("是否繼續?\n1.是2.否"))
            sol=ans()
            c=1
        
main()

print(88888)
            
            
        
