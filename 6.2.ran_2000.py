from timeit import default_timer as timerf

def timer(f, *argument):
    start=timerf()
    f(argument)
    end=timerf()
    return(end-start)


def main():
    #print(timer(print,"Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))

if __name__ == "__main__":
    main()
