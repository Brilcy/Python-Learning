# 2. Write a program to print key, value of dictionary.
#    Example -
#    Input : {"name": "Alex", "dob": "19-10-1980", "zip": 560076}
#    Output : key=name, value=Alex, key=dob, value=19-10-1980, key=zip, value=560076


def key_and_value(dictionary):
    # dictionary = {"name": "Alex", "dob": "19-10-1980", "zip": 560076}
    for i in dictionary:
        print("key = " + i)
        print("value = ", dictionary.get(i))


key_and_value({"name": "Alex", "dob": "19-10-1980", "zip": 560076})
