
def check(a):
    # Base Case
    if len(a) < 2:
        return True

    # Recursive Call
    if a[0] == a[-1]:
        check(a[1:-1])
    else:
        return False

    return check(a[1:-1])


def paliprint(a):
    pass

if check('sorrows'):
    print('pass')
else:
    print('fail')

if check ('rats live on no evil star'):
    print('pass')
else:
    print('fail')
