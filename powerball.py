#!/usr/bin/env python

# Casey Davis
# 14 August 2016
# Greenphire Powerball Code Challenge

from collections import Counter

employees = dict()  # Employee names --> [Powerball numbers]


def add_entry(name, numbers):
    """
    Adds an entry to the employee dictionary, which maps employee names to
    their respective number selections (list of length 6).
    """
    employees[name] = numbers


def compute_winner():
    """
    Computes the winning ticket by finding the mode (most common) of each of
    the 6 numbers across all employees.
    """
    counters = [Counter([numbers[i] for numbers in employees.values()])
                for i in xrange(6)]  # Creates 1 counter for each of 6 slots
    winner = [counter.most_common(1)[0][0] for counter in counters]
    return winner


def search_by_numbers(numbers):
    """
    Returns list of all names associated with the given set of numbers.
    """
    names = []
    for name, values in employees.iteritems():
        if numbers == values:
            names.append(name)
    return names


def main():
    """
    Main game loop.
    """

    while True:

        # Print lots of messy text
        print "\n#########################\n"
        print "Powerball!\n"
        print "1: Create an entry"
        print "2: Display all entries"
        print "3: Display winning ticket"
        print "4: Exit"
        print "\n#########################\n"
        try:
            selection = int(raw_input("Make a selection: "))
        except:
            print "Invalid selection!"
            continue

        if selection == 1:
            name = raw_input("Enter your name: ")
            if name in employees.keys():
                print "Name already taken!"
                continue
            num_str = raw_input("Enter 5 unique numbers 1-69 separated by spaces: ")
            pb_str = raw_input("Enter Powerball number 1-26: ")
            try:
                first5 = [int(s) for s in num_str.split()]
                pb = int(pb_str)
                assert(len(first5) == 5)  # Ensure only 5 numbers
                for num in first5:
                    assert(num in xrange(1, 70))  # Ensure correct range
                assert(len(first5) == len(set(first5)))  # Ensure uniqueness
                assert(pb in xrange(1, 27))  # Ensure powerball correct range
            except:
                print "Invalid input!"
                continue
            numbers = first5 + [pb]
            add_entry(name, numbers)

        elif selection == 2:
            print "All current entries:\n"
            for name, numbers in employees.iteritems():
                print name + ": " + "".join((str(n) + " " for n in numbers))

        elif selection == 3:
            winners = []
            winning_nums = compute_winner()
            print "Powerball winning number: " + "".join((str(n) + " " for n in winning_nums)) + "\n"
            print "Winners:"
            winners = search_by_numbers(winning_nums)
            if len(winners) == 0:
                print "[None]"
            for name in winners:
                print name

        elif selection == 4:
            exit(0)

        else:
            print "Invalid selection!"
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n"
        exit(0)  # Exit cleanly on Ctrl-C
