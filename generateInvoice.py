found = {}

def price(hours):
    # Price calculation using greedy algorithm
    total = 0
    prices = {1.5 : 200000, 1 : 150000, 0.5 : 50000}
    while (hours > 0):
        for i in prices:
            if hours >= i:
                total += prices[i]
                hours -= i
                if i in found:
                    found[i] += 1
                else:
                    found[i] = 1
                break
    return total

def breakdown(found):
    print('(', end='')
    for i in found:
        print('{} * {} jam'.format(found[i], i), end=' ')
        if (i != list(found.keys())[-1]):
            print(' + ', end=' ')
    print(')')

def translate(time):
    hours = time[:time.find(':')]
    minute = time[time.find(':') + 1:]
    return float(hours) + (float(minute) / 60)

recipient = input("Recipient: ")
student = input("Student: ")
start = input("Start: ")
end = input("End: ")
if (start == "-1" or end == "-1"):
    hours = float(input("Hours: "))
    totalPrice = price(hours)
    msg = "Halo {0}, tadi saya ngelesin {1} {2:g} jam, totalnya Rp. {3:,}".format(recipient, student, hours, totalPrice)
else:
    hours = translate(end) - translate(start)
    totalPrice = price(hours)
    msg = "Halo {0}, tadi saya ngelesin {1} dari jam {2} sampai " \
          "jam {3} jadi {4:g} jam, totalnya Rp. {5:,}".format(recipient, student, start, end, hours, totalPrice)

print(msg, end=' ')
breakdown(found)

