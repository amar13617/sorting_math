import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  if operation == "find_odd_even":
    return find_odd_even(list1)
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
        "even_list" : even_list
        "odd_list" : odd_list
    }

