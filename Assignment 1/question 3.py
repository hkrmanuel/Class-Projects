days = int(input("Enter The Number of Days:"))
hours = int(input ("Enter The NUmber Of Hours:"))
min = int(input ("Enter The NUmber Of Minutes:"))
sec = int(input ("Enter The NUmber Of Seconds:"))

conv_days = days * 86400
conv_hours = hours * 3600
conv_min = min * 60
total_seconds= conv_days + conv_hours+ conv_min+ sec
print ("The total number of seconds from this duration is ", total_seconds)