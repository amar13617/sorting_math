import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def handler(event, context):
  print('received event:')
  print(event)
  bucket = 'surveysort'
  survey = event['filename']
  csv_object = s3_client.get_object(Bucket=bucket,Key=survey)
  print(csv_object)
  file_reader = csv_object['Body'].read().decode("utf-8")
  emp_details = file_reader.split("\n")
  print(emp_details)
  
  test_sum = 0
  for index in range(1, len(emp_details)):
    if not (emp_details[index]):
        continue
    test_sum = test_sum + int(emp_details[index].split(",")[2])

  average_list = test_sum/(len(emp_details)-1)

  filename = event.get("survey.csv")
  operation = event.get("operation")
  list1 = []
  for index in range(1, len(emp_details)):
    if not (emp_details[index]):
        continue
    
    list1.append(int(emp_details[index].split(",")[2]))
  print(list1)
  #list1 = event.get("data")
  if operation == "find_odd_even":
    return find_odd_even(list1)
  elif operation == "average_list":
    return find_average(list1)
  elif operation == "list_square":
    return find_square(list1)
  elif operation == "prime_list":
    return find_prime(list1)
  elif operation == "list_reverse":
    return find_reverse(list1)
  elif operation == "find_sort":
    return find_sort(list1)
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

def find_reverse(data):
    reverse = []
    for i in reversed(data):
        reverse.append(i)
    return {
        "reverse_list" : reverse
    }

def find_sort(data):
    sort_numbers = []
    for i in sorted(data):
        sort_numbers.append(i)
    return {
        "sort_number" : sort_numbers
    }