import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  if operation == "find_odd_even":
    return find_odd_even(list1)
  elif operation == "average_list":
    return find_average(list1)
  elif operation == "list_square":
    return find_square(list1)
  elif operation == "prime_list":
    return find_prime(list1)
  else:
    return { 
   }
def find_odd_even(data):
    even_list = []
    odd_list = []
    for i in data:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return {
        "even_list" : even_list,
        "odd_list" :  odd_list
    }

def find_average(data):
    average = sum(data)/max(len(data),1)
    return {
        "find_average" : average
    }

def find_square(data):
    square_list = []
    for i in data:
        square_list.append(i*i)
    return {
        "square_list" : square_list
    }

def find_prime(data):
    prime_list = []
    for i in data:
        c = 0
        for j in range(1, i):
            if i%j == 0:
                c += 1
        if c == 1:
            prime_list.append(i)
    return {
        "prime_number" : prime_list
    }