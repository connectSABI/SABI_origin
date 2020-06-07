from os import environ

mail = input("Enter email ID: ")
password = input("Enter Password: ")

environ['HOST_EMAIL'] = mail
environ['HOST_EMAIL_PASSWORD'] = password

print('{', environ.get('HOST_EMAIL'), ',',
      environ.get('HOST_EMAIL_PASSWORD'), '}')
