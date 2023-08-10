#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
      #if i == 0:
      #  countdown = "Happy New Year!"
      #else:
      #  countdown = str(i)
      countdown = "Happy New Year!" if i == 0 else str(i)
      print(countdown)
      i -= 1
      # output numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"


def square_integers(int_list):
    #sqd_ints = list()
    #for my_num in int_list:
    #  sq_num = my_num ** 2
    #  sqd_ints.append(sq_num)

    sqd_ints = [my_num ** 2 for my_num in int_list]

    return sqd_ints


def fizzbuzz():
    # code goes here!
  #for i in range(100): 
  #  if i % 15 == 0: 
  #    my_item = "FizzBuzz"
  #  elif i % 3 == 0:
  #    my_item = "Fizz"
  #  elif i % 5 == 0:
  #    my_item = "Buzz"
  #  else:
  #    my_item = str(i)
  #  print(my_item, end = '/n')
  for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

fizzbuzz()

def counter_test():
  counter = 0

  while counter < 100:
    print("hi")
    counter += 1

counter_test()