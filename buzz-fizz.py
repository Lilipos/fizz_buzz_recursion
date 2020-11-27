def test_global_function(x=1):
    if x % 3 == 0 or "3" in str(x) or x % 5 == 0 or "5" in str(x):
        if (x % 3 == 0 or "3" in str(x)) and (x % 5 == 0 or "5" in str(x)):
            print("...Fizz...Buzz.....")
        elif x % 3 == 0 or "3" in str(x):
            print("...Fizz...")
        else:  # x % 5 == 0 or "5" in str(x)
            print("...Buzz...")
    else:
        print(x)
    if x == 100:
        return 0
    else:
        return test_global_function(x + 1)
    
test_global_function()
