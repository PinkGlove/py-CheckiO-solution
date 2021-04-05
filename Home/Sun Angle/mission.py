def sun_angle(time):
    #replace this for solution
    current_time = time.split(':')
    time1 = int(current_time[0])
    time2 = int(current_time[1])
    if time1 <= 5 or time1 > 18 or (time1 == 18 and time2 != 0):
        return 'I don\'t see the sun!'
    else:
        return round(((time1 - 6) * 60 + time2) / 4, 2)

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("01:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
