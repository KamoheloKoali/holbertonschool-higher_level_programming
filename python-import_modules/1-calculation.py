#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    print("{fir} + {sec} = {res}".format(fir=a, sec=b, res=cal.add(a, b)))
    print("{fir} - {sec} = {res}".format(fir=a, sec=b, res=cal.sub(a, b)))
    print("{fir} * {sec} = {res}".format(fir=a, sec=b, res=cal.mul(a, b)))
    print("{fir} / {sec} = {res}".format(fir=a, sec=b, res=cal.div(a, b)))
