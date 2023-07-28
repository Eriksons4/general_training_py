#This piece of code shows end time of an event based on longevity of it + beginning time

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
endhour = hour + (dura // 60)
endminute = mins + (dura % 60)
endhour += endminute // 60
endminute = endminute % 60
endhour = endhour % 24
print('{}:{}'.format(endhour, endminute))