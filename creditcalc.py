import math
import sys

def test1():
    global diffcount
    list1 = ["--type=diff","--type=annuity"]
    difflist1 = ["creditcalc\creditcalc.py","creditcalc.py","--type=annuity","--type=diff","--principal","--periods","--interest"]
    annlist1 = ["creditcalc\creditcalc.py","creditcalc.py","--type=annuity","--payment","--periods","--interest"]
    diffcount = 0
    if sys.argv[1] not in list1:
        print("Incorrect parameters.")
    elif sys.argv[1] == "--type=diff":
            diffcount +=1
            for arg in sys.argv:
                if "--principal" in arg:
                    diffcount +=1
                elif "--periods" in arg:
                    diffcount +=1
                elif "--interest" in arg:
                    diffcount +=1
                elif "--payment" in arg:
                    diffcount +=100
                elif arg not in difflist1:
                    diffcount +=100
    elif sys.argv[1] == "--type=annuity":
            diffcount +=1
            for arg in sys.argv:
                if "--payment" in arg:
                    diffcount +=1
                elif "--periods" in arg:
                    diffcount +=1
                elif "--interest" in arg:
                    diffcount +=1
                elif "--principal" in arg:
                    diffcount +=1
                elif arg not in difflist1:
                    diffcount +=100

def goteverything():
    global diffcount
    if diffcount == 4:
        if sys.argv[1] == "--type=annuity":
            if "--payment" in sys.argv[2]:
                separate1()
                annuitystyle2()
            elif "--princ" in sys.argv[2]:
                if "--payment" in sys.argv[3]:
                    separate1()
                    annuitystlye3()
                elif "--periods" in sys.argv[3]:

                    separate1()
                    annuitystyle1()
        elif sys.argv[1] == "--type=diff":
            separate1()
            diffstyle1()
    else:
        print("Incorrect parameters.")

def separate1():
    global principal
    global interest
    global payment
    global periods
    for arg in sys.argv:
        if "princ" in arg:
            PrincipalList = []
            for ch in arg:
                if ch.isnumeric():
                    PrincipalList.append(ch)
            separator = ""
            principal = separator.join(PrincipalList)
            principal = int(principal)
        if "periods" in arg:
            PeriodsList = []
            for ch in arg:
                if ch.isnumeric():
                    PeriodsList.append(ch)
            separator = ""
            periods = separator.join(PeriodsList)
            periods = int(periods)
        if "interest" in arg:
            interestList = []
            chars = set('0123456789.,')
            for ch in arg:
                if ch in chars:
                    interestList.append(ch)
            separator = ""
            interest = separator.join(interestList)
            interest = float(interest)
        if "payment" in arg:
            paymentList = []
            for ch in arg:
                if ch.isnumeric():
                    paymentList.append(ch)
            separator = ""
            payment = separator.join(paymentList)
            payment = int(payment)

def diffstyle1():
    credit_principle = float(principal)
    credit_interest = float(interest)
    i = float((credit_interest/12)/100)
    month_count = periods
    start_month = 1
    overpayment = 0
    while start_month != month_count+1:
        stageone = credit_principle/periods
        stagetwo = credit_principle-((credit_principle*(start_month-1))/periods)
        stagethree = i*stagetwo
        stagefour = (math.ceil(stageone+stagethree))
        print (f"Month {start_month}: paid out {stagefour}")
        stagefive = stagefour-stageone
        overpayment += stagefive
        start_month += 1
    print("")
    print(f"Overpayment = {math.ceil(overpayment)}")



def annuitystyle1():
    credit_principle = float(principal)
    credit_interest = interest
    i = float((credit_interest/12)/100)
    stagethree = (i*(math.pow(1+i,periods)))/((math.pow(1+i,periods))-1)
    stagefour = float(math.ceil(credit_principle*stagethree))
    stagefive = int(stagefour)
    print("Your annuity payment = ",stagefive,"!",sep="")
    overpayment = int((stagefour*periods)-credit_principle)
    print ("Overpayment =", round(overpayment,0))

def annuitystyle2():
    monthly_payment = payment
    credit_interest = interest
    i = float((credit_interest/12)/100)
    stagethree = (i*(math.pow(1+i,periods)))/((math.pow(1+i,periods))-1)
    stagefour = int(monthly_payment/stagethree)
    print("Your credit principal = ",stagefour,"!",sep="")
    overpayment = int((monthly_payment*periods)-stagefour)
    print ("Overpayment =", round(overpayment,0))

def annuitystlye3():
    i = float((interest/12)/100)
    parttwo = (payment/(payment-(i*principal)))
    stagethree = math.log(parttwo,1+i)
    numbermonths = math.ceil(stagethree)
    years = int(numbermonths/12)
    months = int(numbermonths-(years*12))
    if years > 1:
        if months > 1:
            print (f"You need {years} years and {months} months to repay this credit!")
        elif months == 1:
            print (f"You need {years} years and {months} month to repay this credit!")
        elif months == 0:
            print (f"You need {years} years to repay this credit!")
    elif years == 1:
        if months > 1:
            print (f"You need {years} year and {months} months to repay this credit!")
        elif months == 1:
            print (f"You need {years} year and {months} month to repay this credit!")
        elif months == 0:
            print (f"You need {years} year to repay this credit!")
    elif years == 0:
        if months > 1:
            print (f"You need {months} months to repay this credit!")
        elif months == 1:
            print (f"You need {months} month to repay this credit!")
    overpayment = int((payment*numbermonths)-principal)
    print ("Overpayment =", round(overpayment,0))


test1()
goteverything()
