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
  print(file_reader)
  user = file_reader.split("\n")
  print(user)

#  test_sum = 0
#  for index in range(1,len(user)):
#    if not (user[index]):
#      continue
#    test_sum =test_sum + int(user[index].split(",")[2])
  
#  average_list = test_sum/(len(user)-1)
#  print(average_list)
  
  

  

  

  list1 = []
  for index in range(1, len(user)):
    if not user[index]:
      continue
    list1.append(int(user[index].split(",")[2]))
  
  filename = event.get("survey.csv")
  operation = event.get("operation")

  if operation == "sort_list":
    return find_sort(list1)
  elif operation == "average":
    return find_average(list1)
  elif operation == "reverse_list":
    return reverse_number(list1)
  elif operation == "odd_even":
    return find_odd_even(list1)
  else:
    return {

    }

def find_average(list1):
  average = sum(list1)/(len(list1))
  return {
    "average_list" : average
  }


def find_odd_even(list1):
  even_list = []
  odd_list = []
  for index in list1:
    if index % 2 == 0:
      even_list.append(index)
    else:
      odd_list.append(index)

  return {
    "even" : even_list,
    "odds" : odd_list
  }

def reverse_number(list1):
  reverse_list = []
  for index in reversed(list1):
    reverse_list.append(index)
  return {
    "list_reverse" : reverse_list
  }

def find_sort(list1):
  sort_list = []
  for index in sorted(list1):
    sort_list.append(index)
  return {
    "sorting_list" : sort_list
  }