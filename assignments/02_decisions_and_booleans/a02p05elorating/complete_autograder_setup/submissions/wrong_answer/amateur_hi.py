rating = int(input())

if rating < 1000:
    print("Invalid")
elif rating < 2401:
    print("Amateur")
elif rating < 2500:
    print("International grandmaster")
elif rating < 2700:
    print("Grandmaster")
else:
    print("Super grandmaster")
