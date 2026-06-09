def info(Ex_price,RTo,insurance,Add_ons):
    print("Ex-Showroom Price::          ","₹",Ex_price)
    print("RTO              ::          ","₹",RTo)
    print("Insurance        ::          ","₹",insurance)
    print("Add Ons          ::          ","₹",Add_ons)
    total=(Ex_price+RTo+insurance+Add_ons)*0.18
    print("Gst(18%)         ::          ","₹",total)
    print("Total Price      ::          ","₹",(Ex_price+RTo+insurance+Add_ons+total))
    print("="*45)
def a():
    print("========HAVE A NICE DAY, KEEP VISITING OUR SHOWROOM=========")
    print("---------------------------------")
    from datetime import datetime
    print("Exit time:            ",datetime.now())
    print("---------------------------------")
    print("*************************************************************")
    print("                 NEW ENTRY               ")
    print("*************************************************************")
def c():
    print("================PAYMENT DONE================")
    print("================THANK YOU For Buying Car From Our Showroom================")
    print("================HAVE A NICE DAY, KEEP VISITING OUR SHOWROOM================")
    print("-------------------------------------------")
    from datetime import datetime
    print("Exit time:            ",datetime.now())
    print("-------------------------------------------")
    print("*************************************************************")
    print("                 NEW ENTRY               ")
    print("*************************************************************")
def b():
     print("========HAVE A NICE DAY, KEEP VISITING OUR SHOWROOM=========")
def c1():
    print("≠=========WRONG INPUT==========")
    print("========HAVE A NICE DAY, KEEP VISITING OUR SHOWROOM=========")

def emi1(principal,rate,years):
    monthly_rate=rate/(12*100)
    months=years*12
    emi=(principal*monthly_rate*(1+monthly_rate)**months)/((1+monthly_rate)**months-1)
    print("       Monthly EMI =", round(emi, 2))
while True:
    print("~"*45)
    print("      W E L C O M E    T O    A U T O N M I A    S H O W R O O M")     
    print("~"*45)  
    from datetime import datetime
    print("Entry time:            ",datetime.now())
    name=input("Enter Your Name>>")
    add=input("Enter Your Address>>")
    ph=input("Enter Your Phone Number>>")
    no1=len(ph)
    if no1==10 and ph.isdigit():
        pass
    else:
        print("Wrong Input,Try Again")
        continue
    ch=input("Plz Enter to check which brand of car we have!!>>")
    if ch=="":
        print(">>>>>WE HAVE DIFFERENT TYPES OF CAR'S BRAND >>>>>")
        print("~~HERE ARE THESE~~")
        print("1>>~MARUTI SUZUKI~")
        print("2>>~MAHINDRA~")
        print("3>>~KIA~")
        print("4>>~HYUNDAI~")
        print("5>>~HONDA~")
        ch1=int(input("Enter Your choice::"))
        if ch1==1:
            print(">> Which Car from MARUTI SUZUKI >>")
            print("1>>~~WAGON R~~")
            print("2>>~~Baleno~~")
            print("3>>~~Victoris~~")
            print("4>>~~Ertiga~~")
            print("5>>~~Brezza~~")
            print("6>>~~Dzire~~")
            print("7>>~~Alto K10~~")
            print("8>>~~S-Presso~~")
            print("9>>~~Celerio~~")
            print("10>>~~XL6~~")
            print("11>>~~Invicto~~")
            print("12>>~~e Vitara~~")
            print("13>>~~Grand Vitara~~")
            print("14>>~~Eeco~~")
            print("15>>~~Ignis~~")
            print("16>>~~Jimny~~")
            print("17>>~~Ciaz~~")
            ch2=int(input("Enter your Choice::"))
            if ch2==1:
               print("========Wagon R Price========>>")
               info(499000, 49900, 25000, 10000)
            elif ch2==2:
               print("========Baleno Price========>>")
               info(599000, 59900, 30000, 10000)               
            elif ch2==3:
               print("========Victoris Price========>>")
               info(1050000, 105000, 45000, 12000)   
            elif ch2==4:
               print("========Ertiga Price========>>")
               info(880000, 88000, 40000, 10000)      
            elif ch2==5:
               print("========Brezza Price========>>")
               info(826000, 82600, 38000, 10000)       
            elif ch2==6:
               print("========Dzire Price========>>")
               info(626000, 62600, 30000, 10000)      
            elif ch2==7:
               print("========Alto K10 Price========>>")
               info(370000, 37000, 20000, 8000)      
            elif ch2==8:
               print("========S-Presso Price========>>")
               info(350000, 35000, 19000, 8000)      
            elif ch2==9:
               print("========Celerio Price========>>")
               info(470000, 47000, 23000, 8000)      
            elif ch2==10:
               print("========XL6 Price========>>")
               info(1152000, 115200, 50000, 12000)      
            elif ch2==11:
               print("========InvictoR Price========>>")
               info(2497000, 249700, 95000, 20000)      
            elif ch2==12:
               print("========e Vitara Price========>>")
               info(1349000, 13490, 60000, 15000)      
            elif ch2==13:
               print("========Grand Vitara Price========>>")
               info(1077000, 107700, 48000, 12000)      
            elif ch2==14:
               print("========Eeco Price========>>")
               info(521000, 52100, 26000, 8000)      
            elif ch2==15:
               print("========Ignis Price========>>")
               info(584000, 58400, 29000, 10000)      
            elif ch2==16:
               print("========Jimny Price========>>")
               info(1231000, 123100, 52000, 12000)      
            elif ch2==17:
               print("========Ciaz Price========>>")
               info(940000, 94000, 42000, 10000)
            else:
                break   
        elif ch1==2:
            print(">> Which Car from MAHINDRA>>")
            print("1>>~~Mahindra Bolero~~")
            print("2>>~~Mahindra XUV 3XO~~") 
            print("3>>~~Mahindra Bolero Neo~~") 
            print("4>>~~Mahindra Thar~~")
            print("5>>~~Mahindra XUV 3XO Axt~~") 
            print("6>>~~Mahindra Bolero Neo Plus~~") 
            print("7>>~~Mahindra Thar ROXX~~") 
            print("8>>~~Mahindra Scorpio Classic~~") 
            print("9>>~~Mahindra Scorpio N~~") 
            print("10>>~~Mahindra XUV 7XO~~") 
            print("11>>~~Mahindra XUV 3XO EV~~") 
            print("12>>~~Mahindra Marazzo~~") 
            print("13>>~~Mahindra XUV400 EV~~") 
            print("14>>~~Mahindra BE 6~~") 
            print("15>>~~Mahindra XEV 9S~~")
            print("16>>~~Mahindra XEV 9e~~") 
            print("17>>~~Mahindra Bolero Pik-Up~~") 
            print("18>>~~Mahindra Bolero Camper~~") 
            print("19>>~~Mahindra XUV 700 Axt~~") 
            print("20>>~~Mahindra XUV 500~~") 
            print("21>>~~Mahindra XUV 300~~")
            ch2=int(input("Enter your Choice::"))
            if ch2==1:
               print("========Mahindra Bolero Price========>>")
               info(979000, 97900, 45000, 15000)
            elif ch2==2:
               print("========Mahindra XUV 3XO Price========>>")
               info(754000, 75400, 35000, 10000)               
            elif ch2==3:
               print("========Mahindra Bolero Neo Price========>>")
               info(995000, 99500, 48000, 12000)   
            elif ch2==4:
               print("========Mahindra Thar Price========>>")
               info(1135000, 113500, 55000, 15000)      
            elif ch2==5:
               print("========Mahindra XUV 3XO Axt Price========>>")
               info(1260000, 126000, 58000, 15000)       
            elif ch2==6:
               print("========Mahindra Bolero Neo Plus Price========>>")
               info(1139000, 113900, 55000, 15000)      
            elif ch2==7:
               print("========Mahindra Thar ROXX Price========>>")
               info(1239000, 123900, 60000, 15000)      
            elif ch2==8:
               print("========Mahindra Scorpio Classic Price========>>")
               info(1362000, 136200, 65000, 15000)      
            elif ch2==9:
               print("========Mahindra Scorpio N Price========>>")
               info(1385000, 138500, 66000, 15000)      
            elif ch2==10:
               print("========Mahindra XUV 7XO Price========>>")
               info(1399000, 139900, 68000, 15000)      
            elif ch2==11:
               print("========Mahindra XUV 3XO EV Price========>>")
               info(1449000, 14490, 65000, 15000)      
            elif ch2==12:
               print("========Mahindra Marazzo Price========>>")
               info(1450000, 145000, 65000, 15000)      
            elif ch2==13:
               print("========Mahindra XUV400 EV Price========>>")
               info(1549000, 15490, 70000, 15000)      
            elif ch2==14:
               print("========Mahindra BE 6 Price========>>")
               info(1890000, 18900, 85000, 20000)      
            elif ch2==15:
               print("========Mahindra XEV 9S Price========>>")
               info(2190000, 21900, 95000, 20000)      
            elif ch2==16:
               print("========Mahindra XEV 9e Price========>>")
               info(2190000, 21900, 95000, 20000)      
            elif ch2==17:
               print("========Mahindra Bolero Pik-Up Price========>>")
               info(885000, 88500, 40000, 10000)   
            elif ch2==18:
               print("========Mahindra Bolero Camper Price========>>")
               info(1026000, 102600, 45000, 12000)      
            elif ch2==19:
               print("========Mahindra XUV 700 Axt Price========>>")
               info(2154000, 215400, 95000, 25000)   
            elif ch2==20:
               print("========Mahindra XUV 500 Price========>>")
               info(1558000, 155800, 75000, 15000)         
            elif ch2==21:
               print("========Mahindra XUV 300 Price========>>")
               info(799000, 79900, 38000, 10000)
            else:
                break   
        elif ch1==3:
            print(">> Which Car from KIA>>")
            print("1>>~~Kia Sonet~~")
            print("2>>~~Kia Sportage~~")
            print("3>>~~Kia Syros~~")
            print("4>>~~Kia Seltos~~")
            print("5>>~~Kia Telluride~~")
            print("6>>~~Kia Stonic~~")
            print("7>>~~Kia K3~~") 
            print("8>>~~Kia K4~~")
            print("9>>~~Kia K5~~")
            print("10>>~~Kia K6~~")
            print("11>>~~Kia K7~~")
            print("12>>~~Kia K8~~")
            print("13>>~~Kia K9~~")
            print("14>>~~Kia Pegas~~")
            print("15>>~~Kia Ceed~~")
            ch2=int(input("Enter your Choice::"))
            if ch2==1:
               print("========Kia Sonet Price========>>")
               info(732000, 73200, 32000, 10000)
            elif ch2==2:
               print("========Kia Sportage Price========>>")
               info(2500000, 250000, 95000, 25000)               
            elif ch2==3:
               print("========Kia Syros Price========>>")
               info(840000, 84000, 42000, 12000)   
            elif ch2==4:
               print("========Kia Seltos Price========>>")
               info(1099000, 109900, 48000, 15000)      
            elif ch2==5:
               print("========Kia Telluride Price========>>")
               info(3500000, 350000, 110000, 30000)       
            elif ch2==6:
               print("========Kia Stonic Price========>>")
               info(1200000, 120000, 50000, 15000)      
            elif ch2==7:
               print("========Kia K3 Price========>>")
               info(1600000, 160000, 60000, 18000)      
            elif ch2==8:
               print("========Kia K4 Price========>>")
               info(1800000, 180000, 65000, 20000)      
            elif ch2==9:
               print("========Kia K5 Price========>>")
               info(2200000, 220000, 85000, 22000)      
            elif ch2==10:
               print("========Kia K6 Price========>>")
               info(2600000, 260000, 95000, 25000)      
            elif ch2==11:
               print("========Kia K7 Price========>>")
               info(3000000, 300000, 100000, 28000)      
            elif ch2==12:
               print("========Kia K8 Price========>>")
               info(3500000, 350000, 110000, 30000)      
            elif ch2==13:
               print("========Kia K9 Price========>>")
               info(4500000, 450000, 140000, 35000)      
            elif ch2==14:
               print("========Kia Pegas Price========>>")
               info(900000, 90000, 42000, 12000)      
            elif ch2==15:
               print("========Kia Ceed Price========>>")
               info(1500000, 150000, 55000, 18000)
            else:
                break
        elif ch1==4:
            print(">> Which Car from HYUNDAI>>")
            print("1>>~~Hyundai Exter~~")
            print("2>>~~Hyundai Venue~~")
            print("3>>~~Hyundai Creta~~")  
            print("4>>~~Hyundai Alcazar~~")  
            print("5>>~~Hyundai i20 N Line~~")  
            print("6>>~~Hyundai Venue N Line~~")  
            print("7>>~~Hyundai Creta N Line~~")  
            print("8>>~~Hyundai Grand i10 Nios~~")  
            print("9>>~~Hyundai i20~~")  
            print("10>>~~Hyundai Aura~~")  
            print("11>>~~Hyundai Verna~~")  
            print("12>>~~Hyundai Creta Electric~~")  
            print("13>>~~Hyundai Ioniq 5~~")  
            print("14>>~~Hyundai Prime HB~~")  
            print("15>>~~Hyundai Prime SD~~")  
            print("16>>~~Hyundai Inster EV~~")  
            print("17>>~~Hyundai Bayon~~")  
            print("18>>~~Hyundai Ioniq 6~~")  
            ch2=int(input("Enter your Choice::"))
            if ch2==1:
               print("========Hyundai Exter Price========>>")
               info(600000, 60000, 30000, 10000)
            elif ch2==2:
               print("========Hyundai Venue Price========>>")
               info(790000, 79000, 38000, 10000)               
            elif ch2==3:
               print("========Hyundai Creta Price========>>")
               info(1111000, 111100, 50000, 15000)   
            elif ch2==4:
               print("========Hyundai Alcazar Price========>>")
               info(1490000, 149000, 65000, 15000)      
            elif ch2==5:
               print("========Hyundai i20 N Line Price========>>")
               info(1000000, 100000, 45000, 12000)       
            elif ch2==6:
               print("========Hyundai Venue N Line Price========>>")
               info(1200000, 120000, 55000, 15000)      
            elif ch2==7:
               print("========Hyundai Creta N Line Price========>>")
               info(1682000, 168200, 75000, 18000)      
            elif ch2==8:
               print("========Hyundai Grand i10 Nios Price========>>")
               info(592000, 59200, 28000, 10000)      
            elif ch2==9:
               print("========Hyundai i20 Price========>>")
               info(704000, 70400, 32000, 10000)      
            elif ch2==10:
               print("========Hyundai Aura Price========>>")
               info(649000, 64900, 30000, 10000)      
            elif ch2==11:
               print("========Hyundai Verna Price========>>")
               info(1098000, 109800, 48000, 12000)      
            elif ch2==12:
               print("========Hyundai Creta Electric Price========>>")
               info(1799000, 17990, 75000, 15000)      
            elif ch2==13:
               print("========Hyundai Ioniq 5 Price========>>")
               info(4595000, 45950, 130000, 30000)      
            elif ch2==14:
               print("========Hyundai Prime HB Price========>>")
               info(650000, 65000, 30000, 10000)      
            elif ch2==15:
               print("========Hyundai Prime SD Price========>>")
               info(700000, 70000, 32000, 10000)      
            elif ch2==16:
               print("========Hyundai Inster EV Price========>>")
               info(900000, 9000, 40000, 12000)      
            elif ch2==17:
               print("========Hyundai Bayon Price========>>")
               info(1000000, 100000, 45000, 12000)   
            elif ch2==18:
               print("========Hyundai Ioniq 6 Price========>>")
               info(6500000, 65000, 180000, 30000)
            else:
                break
        elif ch1==5:
            print(">> Which Car from HONDA>>")
            print("1>>~~Honda City~~")
            print("2>>~~Honda Amaze~~")
            print("3>>~~Honda Civic~~")
            print("4>>~~Honda Civic Type R~~")
            print("5>>~~Honda Accord~~")
            print("6>>~~Honda Fit / Jazz~~")
            print("7>>~~Honda Elevate~~")
            print("8>>~~Honda CR-V~~")
            print("9>>~~Honda HR-V / ZR-V~~")
            print("10>>~~Honda Pilot~~")
            print("11>>~~Honda Passport~~")
            print("12>>~~Honda Prologue~~")
            print("13>>~~Honda Odyssey~~")
            print("14>>~~Honda Ridgeline~~")
            print("15>>~~Honda Prelude Hybrid~~")
            print("16>>~~Honda 0 Series (Alpha / SUV)~~")
            ch2=int(input("Enter your Choice::"))
            if ch2==1:
               print("========Honda City Price========>>")
               info(1200000, 120000, 55000, 15000)
            elif ch2==2:
               print("========Honda Amaze Price========>>")
               info(751000, 75100, 35000, 10000)               
            elif ch2==3:
               print("========Honda Civic Price========>>")
               info(2200000, 220000, 85000, 20000)   
            elif ch2==4:
               print("========Honda Civic Type R Price========>>")
               info(4500000, 450000, 130000, 25000)      
            elif ch2==5:
               print("========Honda Accord Price========>>")
               info(4000000, 400000, 120000, 25000)       
            elif ch2==6:
               print("========Honda Fit / Jazz Price========>>")
               info(850000, 85000, 40000, 12000)      
            elif ch2==7:
               print("========Honda Elevate Price========>>")
               info(1160000, 116000, 52000, 15000)      
            elif ch2==8:
               print("========Honda CR-V Price========>>")
               info(3500000, 350000, 110000, 25000)      
            elif ch2==9:
               print("========Honda HR-V / ZR-V Price========>>")
               info(2100000, 210000, 80000, 20000)      
            elif ch2==10:
               print("========Honda Pilot Price========>>")
               info(4800000, 480000, 140000, 30000)      
            elif ch2==11:
               print("========Honda Passport Price========>>")
               info(4200000, 420000, 125000, 28000)      
            elif ch2==12:
               print("========Honda Prologue Price========>>")
               info(4500000, 45000, 120000, 25000)      
            elif ch2==13:
               print("========Honda Odyssey Price========>>")
               info(4500000, 450000, 130000, 30000)      
            elif ch2==14:
               print("========Honda Ridgeline Price========>>")
               info(4000000, 400000, 120000, 28000)      
            elif ch2==15:
               print("========Honda Prelude Hybrid Price========>>")
               info(4200000, 420000, 125000, 28000)      
            elif ch2==16:
               print("========Honda 0 Series (Alpha / SUV) Price========>>")
               info(5500000, 55000, 150000, 35000)
            else:
                break
        else:  
            break
    ch3=input("Do You Want To Buy This Car( Yes or No )>>")
    if ch3.lower()=="yes":
        print("**Mode of Payment Please**::")
        print("   1>>UPI(Gpay,paytm)")
        print("   2>>Credit Card")
        print("   3>>Cash Only")
        print("   4>>loan(EMI)")
        pay=int(input("   Enter your choice[1,2,3,4]::"))
        if pay==1:
            print("       Different Apps>>")
            print("       1>>Gpay::")
            print("       2>>Paytm::")
            print("       3>>Phonepe::")
            print("       4>>Exit::")            
            pay1=int(input("   Enter your choice[1,2,3,4]::"))
            if pay1==1:
                c()
            elif pay1==2:
                c()
            elif pay1==3:
                c()        
            else:
                c1()
                continue
        elif pay==2:
            print("       1>>Visa")
            print("       2>>MasterCard")
            print("       3>>RuPay")
            print("       4>>American Express")
            print("       5>>Discover")
            pay1=int(input("       Enter your choice[1,2,3,4,5]::"))  
            c() 
        elif pay==3:
             c()  
        elif pay==4:
             loan=input("       Do you want EMI facility? (yes/no)>>")
             if loan.lower()=="yes":
                total=int(input("       Enter Your Total Amount Of Car>>>>₹"))
                down_pay=int(input("       How Much Down Payment Do You Want To Give>>>>₹"))
                principal=total-down_pay
                rate=float(input("       Enter Interest Rate>>>>"))
                years=int(input("       Enter Loan Duration (Years)>>>>"))
                emi1(principal,rate,years) 
                print("       1>>Yes----")
                print("       2>>No----")
                endch=int(input("       Enter Your Choice[1,2]>>"))
                if endch==1:
                   c()
                elif endch==2:
                     a()
                     continue
                else:
                    c1()
                    continue       
        else:
            c1()
            continue        
    elif ch3.lower()=="no":
        c1()
    else:
        a()
        continue        
