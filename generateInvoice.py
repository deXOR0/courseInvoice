import argparse

parser = argparse.ArgumentParser(description='Program to calculate course pricing and generate invoice')

subparser = parser.add_subparsers(dest='mode')

#Args Group
args_parser = subparser.add_parser('args', help='start program in arguments mode')
args_parser.add_argument('-r', '--recipient', type=str, metavar='', required=True, help='set recipient name')
args_parser.add_argument('-s', '--student', type=str, metavar='', required=True, help='set student name')
args_parser.add_argument('-b', '--begin', type=str, metavar='', help='set begin time')
args_parser.add_argument('-e', '--end', type=str, metavar='', help='set end time')
args_parser.add_argument('-t', '--time', type=float, metavar='', help='set course duration in hours')

#Interactive Group
int_parser = subparser.add_parser('interactive', help='start program in interactive mode')

args = parser.parse_args()

def price(hours):
    # Price calculation using greedy algorithm
    total = 0
    prices = {1.5 : 200000, 1 : 150000, 0.5 : 50000}
    output = {}
    found = {}
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
    output['total'] = total
    output['prices'] = found

    return output

def breakdown(found):
    print('(', end='')
    for i in found:
        print('{} * {} jam'.format(found[i], i), end=' ')
        if (i != list(found.keys())[-1]):
            print(' + ', end=' ')
    print(')')

def process_data_h(recipient, student, hours):
    totalPrice = price(hours)
    msg = "Halo {0}, tadi saya ngelesin {1} {2:g} jam, totalnya Rp. {3:,}".format(recipient, student, hours, totalPrice['total'])
    output(msg, totalPrice['prices'])

def process_data_be(recipient, student, begin, end):
    hours = translate(end) - translate(begin)
    totalPrice = price(hours)
    msg = "Halo {0}, tadi saya ngelesin {1} dari jam {2} sampai " \
          "jam {3} jadi {4:g} jam, totalnya Rp. {5:,}".format(recipient, student, begin, end, hours, totalPrice['total'])
    output(msg, totalPrice['prices'])

def translate(time):
    hours = time[:time.find(':')]
    minute = time[time.find(':') + 1:]
    return float(hours) + (float(minute) / 60)

def interactive():
    recipient = input("Recipient: ")
    student = input("Student: ")
    begin = input("Begin: ")
    end = input("End: ")
    if (begin == "-1" or end == "-1"):
        hours = float(input("Hours: "))
        process_data_h(recipient, student, hours)
    else:
        process_data_be(recipient, student, begin, end)

def output(msg, found):
    print(msg, end=' ')
    breakdown(found)

if __name__ == '__main__':
    if args.mode == 'interactive':
        interactive()
    else:
        if args.begin is not None and args.end is not None:
            process_data_be(args.recipient, args.student, args.begin, args.end)
        else:
            process_data_h(args.recipient, args.student, args.time)
