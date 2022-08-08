# Комбинации
# (False, False, False),
# (False, False, True),
# (False, True, False),
# (False, True, True),
# (True, False, False),
# (True, False, True),
# (True, True, False),
# (True, True, True)
x, y, z = False, True, False
if (not (x or y or z)) == (not (x) and not (y) and not (z)):
    print (1)
else:
    print (0)
    