def main():
    x=0

  #  while(x<5):
    #    print(x)
    #    x+=1

    # define a for loop
    for x in range (5,10):
       # if(x==7):break
        if (x%2==0):continue
        print(x)

    days=["mon","tue","wed","thur","fri","sat","sun"]
    for x in days:
        print (x)

    for i,d in enumerate(days):
        print(i,d)
if __name__ == "__main__":
    main()


