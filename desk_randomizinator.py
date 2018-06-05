from random import randrange

peeps = ["angel", "emilio", "abdel", "manu", "mar", "patri", "ruben", "susana"]
max_length = len(max(peeps, key=len))

first_line_list = []
for i in xrange(4):
    random_index = randrange(0,len(peeps))
    first_line_list.append(peeps[random_index])
    del peeps[random_index]

second_line_list = []
for i in xrange(4):
    random_index = randrange(0,len(peeps))
    second_line_list.append(peeps[random_index])
    del peeps[random_index]

def pad_with_max_length(peep, max_length, pad_front):
    diff = max_length - len(peep)
    padding = " " * diff
    return "{!s}{!s}".format(padding, peep) if pad_front else "{!s}{!s}".format(peep, padding)

first_line = "{!s}  |  {!s}    {!s}  |  {!s}".format(pad_with_max_length(first_line_list[0], max_length, False), pad_with_max_length(first_line_list[1], max_length, True), pad_with_max_length(first_line_list[2], max_length, False), pad_with_max_length(first_line_list[3], max_length, True))

divider_underscores = "_" * (max_length + 2)
divider_line1 = "{!s}|{!s}    {!s}|{!s}  {!s}".format(divider_underscores, divider_underscores, divider_underscores, divider_underscores, 'w')
divider_spaces = " " * (max_length + 2)
divider_line2 = "{!s}|{!s}    {!s}|{!s}".format(divider_spaces, divider_spaces, divider_spaces, divider_spaces)

second_line = "{!s}  |  {!s}    {!s}  |  {!s}".format(pad_with_max_length(second_line_list[0], max_length, False), pad_with_max_length(second_line_list[1], max_length, True), pad_with_max_length(second_line_list[2], max_length, False), pad_with_max_length(second_line_list[3], max_length, True))

print "\n{!s}\n{!s}\n{!s}\n{!s}".format(first_line, divider_line1, divider_line2, second_line)