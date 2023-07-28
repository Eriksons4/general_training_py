#This piece of code shows how long have you lived in days, minutes and seconds based on your age in years

print("Let's see how long you have lived in days, minutes and seconds.")
name = input("name: ")
print("Now, enter your age")
age = int(input("age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print(name, "has been alive for", days,"days", minutes, "minutes and", seconds, "seconds! Wow!")

