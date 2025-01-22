def calculatePay():
    # This first line is provided for you
    try :
        hrs = float(input("Enter Hours:"))
        pay_rate = float(input("Enter Pay Rate:"))
    except :
        print("Error, please enter numeric input")
        quit()

    try :
        if hrs > 40 :
            pay = (40 * pay_rate) + ((hrs - 40) * (pay_rate * 1.5))
        else :
            pay = hrs * pay_rate
        print(f"Pay: {pay}")
    except :
        print("Error, please enter numeric input")
        quit()
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
