# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
# if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling.
# Return True if we are in trouble.
#
#
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False
smile = True
not_smile = False

a_monkeys = smile
b_monkeys = not_smile

if a_monkeys and not a_monkeys:
    print(True)
elif not a_monkeys and not b_monkeys:
    print(True)
elif a_monkeys and not b_monkeys:
    print(False)


