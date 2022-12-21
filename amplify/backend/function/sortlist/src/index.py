import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def handler(event, context):
  print('received event:')
  print(event)
  bucket = 'emp-detail'
  Employee_detail = event['filename']
  csv_object = s3_client.get_object(Bucket=bucket,Key=Employee_detail)
  print(csv_object)
  file_reader = csv_object['Body'].read().decode("utf-8")
  print(file_reader)
  user = file_reader.split("\n")
  print(user)

  list1 = []
  for index in range(1, len(user)):
    if not user[index]:
      continue
    list1.append(int(user[index].split(",")[2]))

  list2 = []
  for index in range(1, len(user)):
    if not user[index]:
      continue
    list2.append(int(user[index].split(",")[4]))

  list3 = []
  for index in range(1, len(user)):
    if not user[index]:
      continue
    list3.append(int(user[index].split(",")[1]))
  
  list4 = []
  for index in range(1, len(user)):
    if not user[index]:
      continue
    list4.append(int(user[index].split(",")[5]))




  filename = event.get("Employee_detail.csv")
  operation = event.get("operation")

  if operation == "average":
    return find_average(list1)
  elif operation == "sort":
    return find_sort(list2)
  elif operation == "greater_than > 5000":
    return find_greater(list3)
  elif operation == "remove element":
    return remove_end(list4)
  elif operation == "maximum value":
    return maximum(list4)
  else:
    return {

    }

def find_average(list1):
  average = sum(list1)/(len(list1))
  return {
    "average_of_list" : average
  }

def find_sort(list2):
  sort_list = []
  for index in sorted(list2):
    sort_list.append(index)
  return {
    "sorting" : sort_list
  }

def find_greater(list3):
  maximum = []
  for index in (list3):
    if index > 5000:
      maximum.append(index)
  return {
    "max >5000" : maximum
  }
      
def remove_end(list4):
  list5 = []
  for index in list4:
    list5 =  list4[1:-1]
    list5.append(index)
  return {
    "remove" :list5
  }

      
  def maximum(list4):
    maxi = list[0]
    for i in list4:
      if i > maxi:
        maxi = i
    return {
      "maximum" : maxi
    }