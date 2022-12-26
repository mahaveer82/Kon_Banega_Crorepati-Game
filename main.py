# Kaun Banega CrorePati Game
import time
import random

print("Welcome To The Game")
print("KON BANEGA CROREPATI")
count_money = 0
Life = 1

def flip_question():
      global count_money
      global Life
      n = int(input("\nWhich question did you come from Question's No. "))
      print("\nYour 'Filleped Question' is\n")
      p = []
      Q = ["This Is The Zero Index",
    "Who is The Chieft Minister of Madhya Pradesh? ==> a) Mr. Narendra Modi b) Mr. Shivraj Singh chouhan c) Mr. Amit Shah d) Mr. Udhav Thakre",
       "Who is The Chieft Minister Of Tamil Nadu? ==> a) Mr. M. K. Stalin b) Mr. Shivraj Singh chouhan c) Mr. Amit Shah d) Mr. Udhav Thakre",
       "Who is The Chieft Minister Of Maharashtra? ==> a) Mr. M. K. Stalin b) Mr. Eknath Shinde c) Mr. Amit Shah d) Mr. Udhav Thakre",
       "Who is the current president of india 2022? ==> a) Mr. Ram Nath Kovind b) Mr. ShivRaj Singh Chouhan c) Shri M. Venkaiah Naidu d) Smt. Droupadi Murmu",
        "The International Literacy Day is observed on ==> a) Sep 8 b) Nov 28 c) May 2 d) Sep 22",
         "The language of Lakshadweep. a Union Territory of India, is ==> a) Tamil b) Telugu c) Malayalam d) Hindi",
        ]
      A = ["0","b","a","b","d","a","c"]
      prize = ["0","1000","2000","3000","5000","10000","40000","100000","500000","1000000","5000000","10000000"]
      for element in prize:
        p.append(int(element))
      Question = random.randint(1, len(Q)-1)
      print(Q[Question])
      ans = str(input("\nType Your Option a, b, c or d->"))
      b = A.index(A[Question])
  
      if (Question == b or ans == A[Question]):
        print("Yo, You are right! You Won The", p[n],"Rupees")
        count_money += p[n]
        print("\nYour Total Money Is:", count_money)
        del Q[Question]
        print("\nYou have",Life-1,"Life Left")
        # Life -= 1
        Life = 0
        if n == 1:
          question2()
        if n == 2: 
          question3()
        if n == 3:
          question4()
        if n == 4: 
          question5()
        if n == 5:
          question6()
        if n == 6:
          question7() 
      else:
        print("You Choose Wrong Option")
        print("\nYour Total Money Is:", count_money)
        print("Better Luck Next Time")
        Life = 1
        exit()
      print("You Have",Life,"Life, You Cannot Access More Life")
   
def rules():
  print("\nGAME RULES(Read CareFully)\n1)You Have 1 LifeLine\n2)Your age is Above 18\n3)You Have Indian Nationality and Documents\n")

def question2():
    global Life
    chance = input("\nDo You Continue Your Journey... Press Yes Or No->")
    if chance in ("yes","Yes","y","Y"):
      # 2 Question
      print("\nYour Next Questions is:")
      Q2 = ["What is the National Sports of India? ==> a) Cricket b) Football c) Hockey d) Table Tennis"]
      print(Q2[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans2():
          while True:
            if ans == "c":
              global count_money
              second_prize = 2000
              print("Yo, You are right! You Won The 2000 Rupees")
              count_money += second_prize
              print("\nYour Total Money Is:", count_money)
              question3()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans2()
      elif anss in ("no", "No", "n", "N") and  Life == 1:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          flip_question()
        else:
          print("Press The Right Option Again!")
      else:
        print("\nYou haven't Sufficient Life Play Another Time")
        print("\nTotal Money You Win:", count_money)
        exit()
    else:
      print("\nYour Total Money Is:", count_money)
      print("Better Luck Next Time")
      exit()

def question3():
    global Life
    chance = input("\nDo You Continue Your Journey... Press Yes Or No->")
    if chance in ("yes","Yes","y","Y"):
      # 3 Question
      print("\nYour Next Questions is:")
      Q3 = ["Who is The First Prime Minister Of India? ==> a) Pt. Jawahar Lal Nehru b) Mr. Narendra Modi c) Dr. Manmohan Singh d) Lal Bahadur shastri"]
      print(Q3[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans3():
          while True:
            if ans == "a":
              global count_money
              third_prize = 3000
              print("Yo, You are right! You Won The 3000 Rupees")
              count_money += third_prize
              print("\nYour Total Money Is:", count_money)
              question4()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans3()
      elif anss in ("no", "No", "n", "N") and  Life == 1:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          flip_question()
        else:
          print("Press The Right Option Again!")
      else:
        print("\nYou haven't Sufficient Life Play Another Time")
        print("\nTotal Money You Win:", count_money)
        exit()
    else:
      print("\nYour Total Money Is:", count_money)
      print("Better Luck Next Time")
      exit()


def question4():
    global Life
    chance = input("\nDo You Continue Your Journey... Press Yes Or No->")
    if chance in ("yes","Yes","y","Y"):
      # 4 Question
      print("\nYour Next Questions is:")
      Q4 = ["Who is the first Indian origin astronaut? ==> a) Rakesh Sharma b) Dr. A P J Abdul c) Kalpana Chawla d) Raja Chari"]
      print(Q4[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans4():
          while True:
            if ans == "a":
              global count_money
              fourth_prize = 5000
              print("Yo, You are right! You Won The 5000 Rupees")
              count_money += fourth_prize
              print("\nYour Total Money Is:", count_money)
              question5()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans4()
      elif anss in ("no", "No", "n", "N") and  Life == 1:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          flip_question()
        else:
          print("Press The Right Option Again!")
      else:
        print("\nYou haven't Sufficient Life Play Another Time")
        print("\nTotal Money You Win:", count_money)
        exit()
    else:
      print("\nYour Total Money Is:", count_money)
      print("Better Luck Next Time")
      exit()

def question5():
    global Life
    chance = input("\nDo You Continue Your Journey... Press Yes Or No->")
    if chance in ("yes","Yes","y","Y"):
      # 5 Question
      print("\nYour Next Questions is:")
      Q5 = ["Who is the First Female Astronaut Going To Moon? ==> a) Rakesh Sharma b) Dr. A P J Abdul c) Kalpana Chawla d) Raja Chari"]
      print(Q5[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans5():
          while True:
            if ans == "c":
              global count_money
              fifth_prize = 10000
              print("Yo, You are right! You Won The 10000 Rupees")
              count_money += fifth_prize
              print("\nYour Total Money Is:", count_money)
              question6()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans5()
      elif anss in ("no", "No", "n", "N") and  Life == 1:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          flip_question()
        else:
          print("Press The Right Option Again!")
      else:
        print("\nYou haven't Sufficient Life Play Another Time")
        print("\nTotal Money You Win:", count_money)
        exit()
    else:
      print("\nYour Total Money Is:", count_money)
      print("Better Luck Next Time")
      exit()

def question6():
    global Life
    chance = input("\nDo You Continue Your Journey... Press Yes Or No->")
    if chance in ("yes","Yes","y","Y"):
      # 6 Question
      print("\nYour Next Questions is:")
      Q6 = ["Bahubali festival is related to? ==> a) Hinduism  b) Islam c) Buddhism d) Jainism"]
      print(Q6[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans6():
          while True:
            if ans == "d":
              global count_money
              sixth_prize = 40000
              print("Yo, You are right! You Won The 40000 Rupees")
              count_money += sixth_prize
              print("\nYour Total Money Is:", count_money)
              # question7()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans6()
      elif anss in ("no", "No", "n", "N") and  Life == 1:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          flip_question()
        else:
          print("Press The Right Option Again!")
      else:
        print("\nYou haven't Sufficient Life Play Another Time")
        print("\nTotal Money You Win:", count_money)
        exit()
    else:
      print("\nYour Total Money Is:", count_money)
      print("Better Luck Next Time")
      exit()

def question7():
    global Life
    chance = input("\nDo You Continue Your Journey... Press Yes Or No->")
    if chance in ("yes","Yes","y","Y"):
      # 7 Question
      print("\nYour Next Questions is:")
      Q7 = ["Which day is observed as the World Standards Day? ==> a) june 26  b) oct 14 c) Nov 15 d) Dec 2"]
      print(Q7[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans7():
          while True:
            if ans == "b":
              global count_money
              seventh_prize = 100000
              print("Yo, You are right! You Won The 100000 Rupees")
              count_money += seventh_prize
              print("\nYour Total Money Is:", count_money)
              # question7()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans7()
      elif anss in ("no", "No", "n", "N") and  Life == 1:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          flip_question()
        else:
          print("Press The Right Option Again!")
      else:
        print("\nYou haven't Sufficient Life Play Another Time")
        print("\nTotal Money You Win:", count_money)
        exit()
    else:
      print("\nYour Total Money Is:", count_money)
      print("Better Luck Next Time")
      exit()

def start():
  global Life
  command = input("Type Yes For Playing And No for Not Playing->")
  if command in ("yes", "Yes", "Y", "y"):
    rules()
    rule = input("Press Okay To Understand The Rules\nPress Not For Don't Understand->")
    if rule in ("Okay","ok","Ok","Yes","yes","okay"):
      # 1 Question
      print("\nLet's Begin...\nYour First Questions is:")
      Q1 = ["What is the National Bird of India? ==> a) Lion b) Peacock c) Pigeon d) Crow"]
      print(Q1[0:])
      print("\nThink Your Option a, b, c or d\n")
      time.sleep(0)
      anss = input("Do You Have The Answer?\nPress Yes For Answer:\nPress No For Not have the Answer:")
      if anss in ("yes", "Yes", "Y", "y"):
        ans = input("\n Type Your Option Here:")
        def ans1():
          while True:
            if ans == "b":
              global count_money
              first_prize = 1000
              print("\nYo, You are right! You Won The 1000 Rupees")
              count_money += first_prize
              print("\nYour Total Money Is:", count_money)
              question2()
            else:
              print("You Choose Wrong Option")
              print("\nYour Total Money Is:", count_money)
              print("Better Luck Next Time")
              exit()
            break
        ans1()
        
      else:
        lifline = input("\nLifeLine You Have\n Press 1 For 'Flip The Question'->")
        if lifline == "1":
          print("\nYou Have Only 1 Life!")
          flip_question()
        else:
          print("Press The Right Option Again!")
    else:
      print("\nPlease Read The Rules Carefully")
      # rules()
      exit()
  else:
    print("\nBye Bye! See You Next Time")
    exit()
if __name__ == "__main__":
  start()