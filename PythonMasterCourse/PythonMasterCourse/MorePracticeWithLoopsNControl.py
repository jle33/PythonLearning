#Program just prints out the amount of segments in a valid IP Address and how long a segment is.
ip = input("Please Enter an IP Address: ")
count = 1
segment = 0
if ip == '':
    print("Invalid")
else:
    for dot in ip:
        if dot == '.':
            print("Segment {0} has length {1}".format(count, segment))
            count += 1
            segment = 0
        else:
            segment += 1
    else:
        print("Segment {0} has length {1}".format(count, segment))

