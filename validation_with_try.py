def average(x, y, z):
    if x < 0:
        raise ValueError
    elif y < 0:
        raise ValueError
    elif z < 0:
        raise ValueError
    a = (x + y + z) / 3
    return a


if __name__ == '__main__':
    try:
        average_score = average()
    except:
        print('A ValueError was raised')
