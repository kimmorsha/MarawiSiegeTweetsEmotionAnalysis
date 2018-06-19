import string

def fun():
        location = "(['Republic of the Philippines'], Location((12.7503486, 122.7312101, 0.0)))"

        index = find_nth(location, "]", 1)
        place = location[:index]
        index_2 = find_nth(place, "[", 1)
        place = place[index_2+1:]
        index = find_nth(place, "'", 1)
        index_2 = find_nth(place, "'", 2)
        place = place[index+1:index_2]
        print("place String = " + str(place))

        index = location.rfind(',')
        loc = location[:index]
        index_2 = loc.rfind(',')
        longitude = location[index_2+2:index]
        loc = location[:index_2]
        index = find_nth(location, "(", 3)
        latitude = loc[index+1:index_2]
        print("longitude = " + str(longitude))
        print("latitude = " + str(latitude))

        emo = "['disgust', 0.440154]"
        index = find_nth(emo, "'", 1)
        index_2 = find_nth(emo, "'", 2)
        emotion = emo[index+1:index_2]
        print("emotion = " + str(emotion))

        index = find_nth(emo, ",", 1)
        index_2 = find_nth(emo, "]", 1)
        percentage = emo[index+2:index_2]
        print("percentage = " + str(percentage))

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


fun()