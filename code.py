def check(hn, mn, hk, mk):
    count = 0
    while hn != hk or mn != mk :
        if mn == 30:
            count += 1
        mn += 1
        if mn == 60:
            mn = 0
            hn += 1
            if hn > 12:
                count += (hn - 12)
            else:
                count += hn
            if hn == 24:
                hn = 0
    return count
