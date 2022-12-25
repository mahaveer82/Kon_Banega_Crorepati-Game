# Kaun Banega CrorePati Game
import time

print("Welcome To The Game")
print("KON BANEGA CROREPATI")
count_money = 0


def start():
  command = input("Type Yes For Playing And No for Not Playing->")
  if command in ("yes", "Yes", "Y", "y"):
    print("\nYour First Questions is:")
    Q1 = [
      "What is the National Bird of India? ==> a) Lion b) Peacock c) Pigeon d) Crow"
    ]
    print(Q1[0:])
    ans = input("\nType Your Option a, b, c or d->")

    def ans1():
      while True:
        if ans == "b":
          global count_money
          first_prize = 1000
          print("Yo, You are right! You Won The 1000 Rupees")
          count_money += first_prize
          print("\nYour Total Money Is:", count_money)
        else:
          print("You Choose Wrong Option")
          print("\nYour Total Money Is:", count_money)
          print("Better Luck Next Time")
          print("\n You Have Only Two Option Left")
        break

    ans1()
    chance = input("Can You Continue This.. Press Yes or No->")
    if chance in ("yes", "Yes", "Y", "y"):
      print("\nYour Next Questions is:")
      print("3...")
      time.sleep(1)
      print("2..")
      time.sleep(0.5)
      print("1.")
      time.sleep(0.3)
      Q2 = [
        "What is the National Sports of India? ==> a) Cricket b) Badminton c) Chess d) Hockey"
      ]
      print(Q2[0:])
      ans = input("\nType Your Option a, b, c or d->")

      def ans2():
        while True:
          if ans == "d":
            global count_money
            second_prize = 10000
            print("Yo, You are right! You Won The 10000 Rupees")
            count_money += second_prize
            print("\nYour Total Money Is:", count_money)
          else:
            print("You Choose Wrong Option")
            print("\nYour Total Money Is:", count_money)
            print("Better Luck Next Time")
            print("\n You Have Only One Option Left")
          break

      ans2()
    else:
      print("\nBye Bye! See You Next Time")
      print("Your Total Money is:", count_money)
      exit()

    chance = input("Can You Continue This.. Press Yes or No->")
    if chance in ("yes", "Yes", "Y", "y"):
      print("\nYour Next Questions is:")
      print("3...")
      time.sleep(1)
      print("2..")
      time.sleep(0.5)
      print("1.")
      time.sleep(0.3)
      Q3 = ["What is the Total State in India? ==> a) 26 b) 27 c) 29 d) 28"]
      print(Q3[0:])
      ans = input("\nType Your Option a, b, c or d->")

      def ans3():
        while True:
          if ans == "d":
            global count_money
            third_prize = 50000
            print("Yo, You are right! You Won The 50000 Rupees")
            count_money += third_prize
            print("\nYour Total Money Is:", count_money)
          else:
            print("You Choose Wrong Option")
            print("\nYour Total Money Is:", count_money)
            print("Better Luck Next Time")
            exit()
          break

      ans3()
    else:
      print("\nBye Bye! See You Next Time")
      print("Your Total Money is:", count_money)
      exit()

    chance = input("Can You Continue This.. Press Yes or No->")
    if chance in ("yes", "Yes", "Y", "y"):
      print("\nYour Next Questions is:")
      print("3...")
      time.sleep(1)
      print("2..")
      time.sleep(0.5)
      print("1.")
      time.sleep(0.3)
      Q4 = [
        "What is the Total Union Territories in India? ==> a) 6 b) 8 c) 2 d) 11"
      ]
      print(Q4[0:])
      ans = input("\nType Your Option a, b, c or d->")

      def ans4():
        while True:
          if ans == "b":
            global count_money
            fourth_prize = 100000
            print("Yo, You are right! You Won The 100000 Rupees")
            count_money += fourth_prize
            print("\nYour Total Money Is:", count_money)
          else:
            print("You Choose Wrong Option")
            print("\nYour Total Money Is:", count_money)
            print("Better Luck Next Time")
            exit()
          break

      ans4()
    else:
      print("\nBye Bye! See You Next Time")
      print("Your Total Money is:", count_money)
      exit()

    chance = input("Can You Continue This.. Press Yes or No->")
    if chance in ("yes", "Yes", "Y", "y"):
      print("\nYour Next Questions is:")
      print("3...")
      time.sleep(1)
      print("2..")
      time.sleep(0.5)
      print("1.")
      time.sleep(0.3)
      Q5 = [
        "What is Prime Minister of India? ==> a) Mr. Narendra Modi b) Mr. Shivraj Singh chouhan c) Mr. Amit Shah d) Mr. Udhav Thakre"
      ]
      print(Q5[0:])
      ans = input("\nType Your Option a, b, c or d->")

      def ans5():
        while True:
          if ans == "a":
            global count_money
            fifth_prize = 250000
            print("Yo, You are right! You Won The 250000 Rupees")
            count_money += fifth_prize
            print("\nYour Total Money Is:", count_money)
          else:
            print("You Choose Wrong Option")
            print("\nYour Total Money Is:", count_money)
            print("Better Luck Next Time")
            exit()
          break

      ans5()
    else:
      print("\nBye Bye! See You Next Time")
      print("Your Total Money is:", count_money)
      exit()


if __name__ == "__main__":
  start()
