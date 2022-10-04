temp = int(input("Please enter the current temperature:"))
if temp>=90:
    print("Wear Shorts")
else:
    if temp>=70:
        print("Short sleeves are fine")
    else:
        if temp>=50:
            print("Wear a jacket")
        else:
            if temp>=32:
                print("Wear a heavy coat")
            else:
                print("Stay Inside")
