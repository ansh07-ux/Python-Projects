def bill_info(price,ser_char,breadp=0):
      print("~"*50)
      from datetime import datetime
      print("Entry Time:         ",datetime.now())
      print("~"*50)
      print("Dishes Price                    ::","₹",price)
      print("breads Price                    ::","₹",breadp)
      print("Service Charge                  ::","₹",ser_char)
      gst=(price+breadp)*0.18
      print("GST Price                       ::","₹",gst)
      print("Total Amount                    ::","₹",(price+breadp+gst+ser_char))
      print("~"*50)

def c():
    print("================PAYMENT DONE================")
    print("================HAVE A NICE DAY, KEEP VISITING OUR HOTEL================")
    from datetime import datetime
    print("~"*65)
    print("Exit time:            ",datetime.now())
    print("~"*65)
    print("*************************************************************")
    print("                 NEW ENTRY               ")
    print("*************************************************************")

while True: 
      print("|"*65)
      from datetime import datetime
      print("~"*65)
      print("Entry Time:         ",datetime.now())
      print("~"*65)
      print("          W E L C O M E    T O   O U R   A L L F O O D I E")
      print("|"*65)
      nm=input("Enter Your Name>>")
      add=input("Enter Your Showroom>>")
      ph=input("Enter Your Phone Number>>")
      if not len(ph)==10:
          continue
      print("|"*65)
      print("SELECT THE CUISINE THAT YOU WANT TO CHOOSE...")
      print("1>>Chinese")
      print("2>>Japanese")
      print("3>>Korean")
      print("4>>Taiwanese")
      print("5>>Mongolian")
      print("6>>North Indian")
      print("7>>South Indian")
      print("8>>Punjabi")
      print("9>>Bengali")
      print("10>>Gujarati")
      print("11>>Kashmiri")
      print("12>>Sri Lankan")
      print("13>>Nepalese & Tibetan")
      print("14>>Bhutanese & Maldivian")
      print("15>>Vietnamese")
      print("16>>Thai")
      print("17>>Indonesian")
      print("18>>Filipino")
      print("19>>Malaysian")
      print("20>>Cambodian")
      print("21>>Singaporean")
      print("22>>Afghan")
      print("23>>Australian")
      print("24>>New Zealand")
      print("25>>Italian")
      print("26>>Spanish")
      print("27>>Greek")
      print("28>>Cypriot")
      print("29>>Portuguese")
      print("30>>French")
      print("31>>German")
      print("32>>Austrian")
      print("33>>Irish")
      print("34>>Belgian")
      print("35>>Dutch")
      print("36>>Swiss")
      print("37>>Ukrainian")
      print("38>>Polish")
      print("39>>Czech")
      print("40>>Hungarian")
      print("41>>Romanian")
      print("42>>Swedish")
      print("43>>Norwegian")
      print("44>>Danish")
      print("45>>Finnish")
      print("46>>United States")
      print("47>>Canadian")
      print("48>>Mexican")
      print("49>>Central American")
      print("50>>Jamaican")
      print("51>>Dominican")
      print("52>>Haitian")
      print("53>>Peruvian")
      print("54>>Argentinian")
      print("55>>Brazilian")
      print("56>>Colombian")
      print("57>>Venezuelan")
      print("58>>Turkish")
      print("59>>Arabian Peninsula")
      print("60>>Israeli")
      print("61>>African")
      print("62>>Jain")
      print("63>>Buddhist")
      print("64>>Cuban")
      print("65>>Puerto Rican")
      print("66>>Ethiopian")
      print("67>>Moroccan")
      print("68>>Lebanese")
      print("69>>Egyptian")
      print("70>>Russian")
      print("71>>Georgian")
      print("72>>Nigerian")
      print("73>>South African")
      ch=int(input("Enter Your Choice>>"))
      if ch==1:
              print(">>Enter The Dishes You Want>>")
              print("1>Mápó Dòufu")
              print("2>Gōngbǎo Jīdīng(Kung Pao Chicken)")
              print("3>Huíguō Ròu(Twice-Cooked Pork")
              print("4>Shuǐzhǔ Yú( Water-Boiled Fish or Pork)")
              print("5>Kǒushuǐ Jī(Mouth-Watering Chicken)")
              print("6>Sichuan Hot Pot")
              print("7>Xiājiǎo(Har Gow & Shumai)")
              print("8>Shāomài(BBQ Pork Buns)")
              print("9>Cháshīubāo(White Cut Chicken)")
              print("10>Báichéng Jī( Steamed Whole Fish)")
              print("11>Qīngzhēng Yú Beef Chow Fun)")
              print("12>Cháofěn(Braised Sea Cucumber with Scallions)")
              print("13>Sīwáwá")
              print("14>Cóngbāo Hǎishēn")
              print("15>Tángcù Lǐyú ( Sweet and Sour Carp")
              print("16>Jiǔzhuǎn Dácháng (Nine-Loop Intestines)")
              print("17>Dezhou Braised Chicken ")
              print("18>Shīzītóu (Lion’s Head Meatballs)")
              print("19>Dōngpō Ròu ")
              print("20>Wēizhōu Cùyú (West Lake Fish in Vinegar Sauce)")
              print("21>Lóngjǐng Xiārén ( Longjing Shrimp)")
              print("22>Wéntán Dòufu (Wensi Tofu)")
              print("23>Hunan ")
              print("24>Anhui ")
              print("25>Fujian ")
              print("26>Noodles ")
              print("27>Dumplings ")
              print("28>Rice ")
              print("29>Northern Roast")
              print("30>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(200,20)
              elif ch1==6:
                    bill_info(800,80)
              elif ch1==7:
                    bill_info(150,15)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(220,22)
              elif ch1==10:
                    bill_info(450,45)
              elif ch1==11:
                    bill_info(280,28)
              elif ch1==12:
                    bill_info(500,50)
              elif ch1==13:
                    bill_info(100,10)
              elif ch1==14:
                    bill_info(600,60)
              elif ch1==15:
                    bill_info(350,35)
              elif ch1==16:
                    bill_info(320,32)
              elif ch1==17:
                    bill_info(400,40)
              elif ch1==18:
                    bill_info(380,38)
              elif ch1==19:
                    bill_info(450,45)
              elif ch1==20:
                    bill_info(420,42)
              elif ch1==21:
                    bill_info(300,30)
              elif ch1==22:
                    bill_info(200,20)
              elif ch1==23:
                    bill_info(250,25)
              elif ch1==24:
                    bill_info(250,25)
              elif ch1==25:
                    bill_info(250,25)
              elif ch1==26:
                    bill_info(150,15)
              elif ch1==27:
                    bill_info(180,18)
              elif ch1==28:
                    bill_info(100,10)
              elif ch1==29:
                    bill_info(500,50)
              else:
                    break
      elif ch==2:
              print(">>Enter The Dishes You Want>>")
              print("1>Nigiri ")
              print("2>Sashimi ")
              print("3>Maki & Temaki ")
              print("4>Chirashi Bowl ")
              print("5>Ramen ")
              print("6>Udon ")
              print("7>Soba ")
              print("8>Tempura ")
              print("9>Tonkatsu ")
              print("10>Yakitori ")
              print("11>Takoyaki & Okonomiyaki ")
              print("12>Sukiyaki ")
              print("13>Shabu-Shabu ")
              print("14>Oden ")
              print("15>Gyudon ")
              print("16>Japanese Curry ")
              print("17>Gyoza ")
              print("18>Misoshiru ")
              print("19>Kaiseki")
              print("20>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(700,70)
              elif ch1==2:
                    bill_info(850,85)
              elif ch1==3:
                    bill_info(500,50)
              elif ch1==4:
                    bill_info(900,90)
              elif ch1==5:
                    bill_info(600,60)
              elif ch1==6:
                    bill_info(550,55)
              elif ch1==7:
                    bill_info(400,40)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(300,30)
              elif ch1==11:
                    bill_info(250,25)
              elif ch1==12:
                    bill_info(950,95)
              elif ch1==13:
                    bill_info(1000,100)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(450,45)
              elif ch1==16:
                    bill_info(400,40)
              elif ch1==17:
                    bill_info(250,25)
              elif ch1==18:
                    bill_info(150,15)
              elif ch1==19:
                    bill_info(1500,150)
              else:
                    break

      elif ch==3:
              print(">>Enter The Dishes You Want>>")
              print("1>Baechu Kimchi ")
              print("2>Kkakdugi ")
              print("3>Namul ")
              print("4>Musaengchae ")
              print("5>Kimchi Jjigae ")
              print("6>Doenjang Jjigae ")
              print("7>Sundubu Jjigae ")
              print("8>Samgyetang ")
              print("9>Seolleongtang ")
              print("10>Samgyeopsal ")
              print("11>Bulgogi ")
              print("12>Galbi")
              print("13>Dakgalbi ")
              print("14>Bibimbap ")
              print("15>Gimbap ")
              print("16>Naengmyeon ")
              print("17>Japchae ")
              print("18>Jajangmyeon ")
              print("19>Tteokbokki ")
              print("20>Korean Fried Chicken ")
              print("21>Jeon ")
              print("22>Eomuk/Odeng ")
              print("23>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(200,20)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(450,45)
              elif ch1==6:
                    bill_info(450,45)
              elif ch1==7:
                    bill_info(400,40)
              elif ch1==8:
                    bill_info(600,60)
              elif ch1==9:
                    bill_info(550,55)
              elif ch1==10:
                    bill_info(700,70)
              elif ch1==11:
                    bill_info(750,75)
              elif ch1==12:
                    bill_info(800,80)
              elif ch1==13:
                    bill_info(650,65)
              elif ch1==14:
                    bill_info(500,50)
              elif ch1==15:
                    bill_info(250,25)
              elif ch1==16:
                    bill_info(350,35)
              elif ch1==17:
                    bill_info(300,30)
              elif ch1==18:
                    bill_info(350,35)
              elif ch1==19:
                    bill_info(250,25)
              elif ch1==20:
                    bill_info(500,50)
              elif ch1==21:
                    bill_info(200,20)
              elif ch1==22:
                    bill_info(150,15)
              else:
                    break

      elif ch==4:
              print(">>Enter The Dishes You Want>>")
              print("1>Lǔ Ròu Fàn (Braised Pork Rice)")
              print("2>Kòng Ròu Fàn ( Soy-Braised Pork Belly Rice")
              print("3>Ōu Ā Jiān (Oyster Omelet)")
              print("4>Gùa Bāo (Taiwanese Pork Belly Slider")
              print("5>Chòudòufu ( Stinky Tofu)")
              print("6>Yán Sū Jī ( Taiwanese Popcorn Chicken)")
              print("7>Ōu Ā Mí Suàn ( Oyster & Intestine Vermicelli)")
              print("8>Dàcháng Bāocháng ( Sausage in a Sticky Rice Wrap)")
              print("9>Tiān Bù Là ( Taiwanese Fish Cakes)")
              print("10>Hújiāo Bǐng ( Pepper Cakes)")
              print("11>Zhà Jīpái ( XXL Crispy Chicken Cutlet)")
              print("12>Niǔ Ròu Miàn ( Taiwanese Beef Noodle Soup)")
              print("13>Sān Bēi Jī ( Three Cup Chicken)")
              print("14>Cāng Yíng Tóu (Fly’s Heads)")
              print("15>Fènglí Xiāqiú (Pineapple Shrimp Balls)")
              print("16>Kèjiā Xiǎochǎo ( Hakka Stir-Fry)")
              print("17>Táiwān Rùn Bǐng ( Taiwanese Popiah)")
              print("18>Lǔ Wèi ( Soy Braised Platters)")
              print("19>Dànbǐng (Taiwanese Egg Crepe)")
              print("20>Shāobǐng Yóutiáo ")
              print("21>Xiáng Dòujiāng ( Savory Soy Milk)")
              print("22>Fàntuán (Sticky Rice Roll)")
              print("23>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(150,15)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(220,22)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(150,15)
              elif ch1==10:
                    bill_info(120,12)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(400,40)
              elif ch1==13:
                    bill_info(380,38)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(450,45)
              elif ch1==16:
                    bill_info(350,35)
              elif ch1==17:
                    bill_info(180,18)
              elif ch1==18:
                    bill_info(300,30)
              elif ch1==19:
                    bill_info(150,15)
              elif ch1==20:
                    bill_info(100,10)
              elif ch1==21:
                    bill_info(80,8)
              elif ch1==22:
                    bill_info(120,12)
              else:
                    break

      elif ch==5:
              print(">>Enter The Dishes You Want>>")
              print("1>Buuz ")
              print("2>Khuushuur ")
              print("3>Bansh ")
              print("4>Tsuivan ")
              print("5>Khorkhog ")
              print("6>Boodog ")
              print("7>Suutei Tsai ( Milk Tea)")
              print("8>Airag ")
              print("9>Aaruul ")
              print("10>Urum ")
              print("11>Byaslag ")
              print("12>Guriltai Shul ")
              print("13>Budaatai Tsai ")
              print("14>Boortsog ")
              print("15>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(220,22)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(800,80)
              elif ch1==6:
                    bill_info(900,90)
              elif ch1==7:
                    bill_info(100,10)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(120,12)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(200,20)
              elif ch1==12:
                    bill_info(280,28)
              elif ch1==13:
                    bill_info(150,15)
              elif ch1==14:
                    bill_info(100,10)
              elif ch1==15:
                     continue
              else:
                    break

      elif ch==6:
              print(">>Enter The Dishes You Want>>")
              print("1>Butter Chicken (Murgh Makhani)")
              print("2>Rogan Josh")
              print("3>Kadhai Chicken")
              print("4>Nihari")
              print("5>Dal Makhani")
              print("6>Paneer Tikka Masala")
              print("7>Palak Paneer")
              print("8>Malai Kofta")
              print("9>Rajma Chawal")
              print("10>Aloo Paratha")
              print("11>Tandoori Chicken")
              print("12>Chole Bhature")
              print("13>Samosa")
              print("14>Gol Gappe (Pani Puri)")
              print("15>Aloo Tikki Chaat")
              print("16>Biryani (Awadhi/Mughlai style)")
              print("17>Pulao")
              print("18>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1<18:
                  b_price=0
                  if ch1 not in [9,10,12,13,14,15,16,17]: 
                          print(">>Which type of breads do you want?>>")
                          print("1> Naan")
                          print("2> Tandoori Roti")
                          print("3> Lachha Paratha")
                          print("4> Roomali roti")
                          print("5> No Bread")
                          b_ch = int(input("Enter your bread choice>> "))
                          qty=int(input("Enter Your Quantity::"))                                                                                                                                  
                          if b_ch==1:
                                b_price=qty*40; 
                          elif b_ch==2:
                                b_price=qty*20; 
                          elif b_ch==3:
                                b_price=qty*50;
                          elif b_ch==4:
                              b_price=Qty*20;
                          elif b_ch==5:
                               pass
                          else:
                              break    
                  if ch1==1:
                        bill_info(350,35,b_price)
                  elif ch1==2:
                        bill_info(450,45,b_price)
                  elif ch1==3:
                        bill_info(320,32,b_price)
                  elif ch1==4:
                        bill_info(500,50,b_price)
                  elif ch1==5:
                        bill_info(250,25,b_price)
                  elif ch1==6:
                        bill_info(300,30,b_price)
                  elif ch1==7:
                        bill_info(280,28,b_price)
                  elif ch1==8:
                        bill_info(320,32,b_price)
                  elif ch1==9:
                        bill_info(180,18,0)
                  elif ch1==10:
                        bill_info(100,10,0)
                  elif ch1==11:
                        bill_info(400,40,0)
                  elif ch1==12:
                        bill_info(150,15,0)
                  elif ch1==13:
                        bill_info(50,5,0)
                  elif ch1==14:
                        bill_info(60,6,0)
                  elif ch1==15:
                        bill_info(80,8,0)
                  elif ch1==16:
                        bill_info(400,40,0)
                  elif ch1==17:
                        bill_info(220,22,0)
                  elif ch1==18:
                        continue
                  else:
                      break
      elif ch==7:
              print(">>Enter The Dishes You Want>>")
              print("1>Masala Dosa")
              print("2>Idli")
              print("3>Medu Vada")
              print("4>Sambar")
              print("5>Rasam")
              print("6>Uttapam")
              print("7>Upma")
              print("8>Bisi Bele Bath")
              print("9>Hyderabadi Biryani")
              print("10>Chettinad Chicken")
              print("11>Appam")
              print("12>Puttu")
              print("13>Pongal")
              print("14>Curd Rice")
              print("15>Payasam")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1<16:
                  b_price=0
                  if ch1 in [4,5,10]: 
                          print(">>Which type of breads do you want?>>")
                          print("1> Malabar Parotta")
                          print("2> Appam")
                          print("3> No Bread")
                          b_ch = int(input("Enter your bread choice>> "))
                          qty=int(input("Enter Your Quantity::")) 
                          if b_ch==1:
                              b_price=qty*40
                          elif b_ch==2:
                              b_price=qty*30
                          else:
                              break
                  if ch1==1:
                      bill_info(80,8,0)
                  elif ch1==2:
                        bill_info(80,8,0)
                  elif ch1==3:
                        bill_info(90,9,0)
                  elif ch1==4:
                        bill_info(100,10,b_price)
                  elif ch1==5:
                        bill_info(80,8,b_price)
                  elif ch1==6:
                        bill_info(130,13,0)
                  elif ch1==7:
                        bill_info(100,10,0)
                  elif ch1==8:
                        bill_info(180,18,0)
                  elif ch1==9:
                        bill_info(350,35,0)
                  elif ch1==10:
                        bill_info(320,32,b_price)
                  elif ch1==11:
                        bill_info(80,8,0)
                  elif ch1==12:
                        bill_info(120,12,0)
                  elif ch1==13:
                        bill_info(150,15,0)
                  elif ch1==14:
                        bill_info(100,10,0)
                  elif ch1==15:
                        bill_info(120,12,0)
                  else:
                      continue
      elif ch==8:
              print(">>Enter The Dishes You Want>>")
              print("1>Chole Bhature")
              print("2>Makki di Roti")
              print("3>Sarson da Saag")
              print("4>Dal Makhani")
              print("5>Paneer Tikka")
              print("6>Butter Chicken")
              print("7>Amritsari Kulcha")
              print("8>Punjabi Lassi")
              print("9>Rajma Chawal")
              print("10>Kadhi Pakora")
              print("11>Aloo Paratha")
              print("12>Pinni")
              print("13>Kheer")
              print("14>Tandoori Chicken")
              print("15>Matar Paneer")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch<16:
                  b_price=0
                  if ch1 in [3,4,6,14,10,15]: 
                          print(">>Which type of breads do you want?>>")
                          print("1> Makki di Roti")
                          print("2> Garlic Naan")
                          print("3>No Bread")
                          b_ch = int(input("Enter your bread choice>> "))
                          qty=int(input("Enter Your Quantity::")) 
                          if b_ch==1:
                              b_price=qty*60
                          elif b_ch==2:
                              b_price=qty*60
                          else:
                              break                                
                  if ch1==1:
                        bill_info(180,18,0)
                  elif ch1==2:
                        bill_info(60,6,0)
                  elif ch1==3:
                        bill_info(250,25,b_price)
                  elif ch1==4:
                        bill_info(220,22,b_price)
                  elif ch1==5:
                        bill_info(280,28,0)
                  elif ch1==6:
                        bill_info(350,35,b_price)
                  elif ch1==7:
                        bill_info(120,12,0)
                  elif ch1==8:
                        bill_info(80,8,0)
                  elif ch1==9:
                        bill_info(160,16,0)
                  elif ch1==10:
                        bill_info(180,18,b_price)
                  elif ch1==11:
                        bill_info(100,10,0)
                  elif ch1==12:
                        bill_info(150,15,0)
                  elif ch1==13:
                        bill_info(120,12,0)
                  elif ch1==14:
                        bill_info(400,40,0)
                  elif ch1==15:
                        bill_info(260,26,b_price)
                  else:
                      break
      elif ch==9:
              print(">>Enter The Dishes You Want>>")
              print("1>Macher Jhol")
              print("2>Shorshe Ilish")
              print("3>Chingri Malai Curry")
              print("4>Kosha Mangsho")
              print("5>Rasgulla")
              print("6>Sandesh")
              print("7>Mishti Doi")
              print("8>Luchi")
              print("9>Chholar Dal")
              print("10>Shukto")
              print("11>Aloo Posto")
              print("12>Muri Ghonto")
              print("13>Begun Bhaja")
              print("14>Patishapta")
              print("15>Chomchom")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch<16:
                  b_price=0
                  if ch1 in [1,2,3,4,9,10,11,12]:
                          print(">>Which type of breads do you want?>>")
                          print("1> Luchi")
                          print("2> Porota")
                          print("3> No Bread")
                          b_ch = int(input("Enter your bread choice>> "))
                          qty=int(input("Enter Your Quantity::")) 
                          if b_ch==1:
                              b_price=qty*20
                          elif b_ch==2:
                              b_price=qty*25
                          else:
                              break  
                  if ch1==1:
                        bill_info(250,25,b_price)
                  elif ch1==2:
                        bill_info(450,45,b_price)
                  elif ch1==3:
                        bill_info(400,40,b_price)
                  elif ch1==4:
                        bill_info(380,38,b_price)
                  elif ch1==5:
                        bill_info(50,5,0)
                  elif ch1==6:
                        bill_info(60,6,0)
                  elif ch1==7:
                        bill_info(80,8,0)
                  elif ch1==8:
                        bill_info(100,10,0)
                  elif ch1==9:
                        bill_info(150,15,b_price)
                  elif ch1==10:
                        bill_info(200,20,b_price)
                  elif ch1==11:
                        bill_info(220,22,b_price)
                  elif ch1==12:
                        bill_info(300,30,b_price)
                  elif ch1==13:
                        bill_info(120,12,0)
                  elif ch1==14:
                        bill_info(150,15,0)
                  elif ch1==15:
                        bill_info(100,10,0)
                  else:
                      break
      elif ch==10:
              print(">>Enter The Dishes You Want>>")
              print("1>Dhokla")
              print("2>Khandvi")
              print("3>Thepla")
              print("4>Undhiyu")
              print("5>Fafda")
              print("6>Jalebi")
              print("7>Khakhra")
              print("8>Handvo")
              print("9>Locho")
              print("10>Dabeli")
              print("11>Sev Khamani")
              print("12>Patra")
              print("13>Muthiya")
              print("14>Basundi")
              print("15>Shrikhand")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch<15:
                  b_price=0
                  if ch1 in [4,13]:
                          print(">>Which type of breads do you want?>>")
                          print("1>Thepla")
                          print("2>Puri")
                          print("3>No Bread")
                          b_ch = int(input("Enter your bread choice>> "))
                          qty=int(input("Enter Your Quantity::")) 
                          if b_ch==1:
                              b_price=qty*20
                          elif b_ch==2:
                              b_price=qty*20
                          else:
                              break
                  if ch1==1:
                        bill_info(120,12,0)
                  elif ch1==2:
                        bill_info(150,15,0)
                  elif ch1==3:
                        bill_info(100,10,0)
                  elif ch1==4:
                        bill_info(250,25,b_price)
                  elif ch1==5:
                        bill_info(180,18,0)
                  elif ch1==6:
                        bill_info(120,12,0)
                  elif ch1==7:
                        bill_info(80,8,0)
                  elif ch1==8:
                        bill_info(150,15,0)
                  elif ch1==9:
                        bill_info(130,13,0)
                  elif ch1==10:
                        bill_info(60,6,0)
                  elif ch1==11:
                        bill_info(140,14,0)
                  elif ch1==12:
                        bill_info(150,15,0)
                  elif ch1==13:
                        bill_info(120,12,b_price)
                  elif ch1==14:
                        bill_info(180,18,0)
                  elif ch1==15:
                        bill_info(160,16,0)
                  else:
                      break
      elif ch==11:
              print(">>Enter The Dishes You Want>>")
              print("1>Rogan Josh")
              print("2>Yakhni")
              print("3>Dum Aloo")
              print("4>Modur Pulao")
              print("5>Gushtaba")
              print("6>Matschgand")
              print("7>Kahwa")
              print("8>Tabakh Maaz")
              print("9>Haak Saag")
              print("10>Nadru Yakhni")
              print("11>Kashmiri Pulao")
              print("12>Wazwan")
              print("13>Aab Gosht")
              print("14>Lyodur Tschaman")
              print("15>Phirni")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch<16:
                  b_price=0
                  if ch1 in [1,2,3,5,6,9,10,13,14]:
                          print(">>Which type of breads do you want?>>")
                          print("1> Bakarkhani")
                          print("2> Lavasa")
                          print("3> No Bread")
                          b_ch = int(input("Enter your bread choice>> "))
                          qty=int(input("Enter Your Quantity::")) 
                          if b_ch==1:
                              b_price=qty*60
                          elif b_ch==2:
                              b_price=qty*35
                          else:
                              break
                  if ch1==1:
                        bill_info(400,40,b_price)
                  elif ch1==2:
                        bill_info(380,38,b_price)
                  elif ch1==3:
                        bill_info(250,25,b_price)
                  elif ch1==4:
                        bill_info(220,22,0)
                  elif ch1==5:
                        bill_info(450,45,b_price)
                  elif ch1==6:
                        bill_info(400,40,b_price)
                  elif ch1==7:
                        bill_info(150,15,0)
                  elif ch1==8:
                        bill_info(500,50,0)
                  elif ch1==9:
                        bill_info(200,20,b_price)
                  elif ch1==10:
                        bill_info(250,25,b_price)
                  elif ch1==11:
                        bill_info(300,30,0)
                  elif ch1==12:
                        bill_info(1200,120,b_price)
                  elif ch1==13:
                        bill_info(450,45,b_price)
                  elif ch1==14:
                        bill_info(350,35,b_price)
                  elif ch1==15:
                        bill_info(180,18,0)
                  else:
                      break
      elif ch==12:
              print(">>Enter The Dishes You Want>>")
              print("1>Hoppers (Aappa)")
              print("2>String Hoppers (Idiyappam)")
              print("3>Pol Roti")
              print("4>Kottu Roti")
              print("5>Kukul Mas Curry (Chicken Curry)")
              print("6>Ambul Thiyal (Sour Fish Curry)")
              print("7>Jaffna Crab Curry")
              print("8>Parippu (Dhal Curry)")
              print("9>Polos Curry (Jackfruit Curry)")
              print("10>Pol Sambol")
              print("11>Lunu Miris")
              print("12>Seeni Sambol")
              print("13>Gotu Kola Mallung")
              print("14>Watalappan")
              print("15>Kokis")
              print("16>Kavum")
              print("17>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(150,15)
              elif ch1==2:
                    bill_info(120,12)
              elif ch1==3:
                    bill_info(80,8)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(600,60)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(220,22)
              elif ch1==10:
                    bill_info(100,10)
              elif ch1==11:
                    bill_info(90,9)
              elif ch1==12:
                    bill_info(110,11)
              elif ch1==13:
                    bill_info(130,13)
              elif ch1==14:
                    bill_info(150,15)
              elif ch1==15:
                    bill_info(200,20)
              elif ch1==16:
                    bill_info(180,18)
              else:
                    break

      elif ch==13:
              print(">>Enter The Dishes You Want>>")
              print("1>Dal Bhat Tarkari")
              print("2>Momo")
              print("3>Chatamari")
              print("4>Yomari")
              print("5>Dhido")
              print("6>Choila")
              print("7>Thukpa")
              print("8>Tsampa")
              print("9>Shabaley")
              print("10>Tingmo")
              print("11>Gyathuk")
              print("12>Po Cha")
              print("13>Chhaang / Tongba")
              print("14>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(180,18)
              elif ch1==3:
                    bill_info(200,20)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(220,22)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(240,24)
              elif ch1==8:
                    bill_info(100,10)
              elif ch1==9:
                    bill_info(260,26)
              elif ch1==10:
                    bill_info(120,12)
              elif ch1==11:
                    bill_info(250,25)
              elif ch1==12:
                    bill_info(80,8)
              elif ch1==13:
                    bill_info(350,35)
              else:
                    break

      elif ch==14:
              print(">>Enter The Dishes You Want>>")
              print("1>Chili Cheese Stew")
              print("2>Potato Cheese Stew")
              print("3>Mushroom Cheese Stew")
              print("4>Fern Cheese Stew")
              print("5>Bean Cheese Stew")
              print("6>Pork Belly with Radish")
              print("7>Dried Beef Strips")
              print("8>Crispy Dried Pork")
              print("9>Ginger Chicken Stew")
              print("10>Bhutanese Chicken Curry")
              print("11>Yak Meat Stew")
              print("12>Buckwheat Dumplings")
              print("13>Buckwheat Dumplings")
              print("14>Buckwheat Pancakes")
              print("15>Tuna Coconut Salad")
              print("16>Fried Fish Paste Salad")
              print("17>Crispy Flatbread")
              print("18>Thick Coconut Flatbread")
              print("19>Clear Fish Broth")
              print("20>Traditional Fish Curry")
              print("21>Spicy Seared Tuna")
              print("22>Spicy Seared Tuna")
              print("23>Creamy Vegetable Curry")
              print("24>Tuna Pastry Triangles")
              print("25>Fish Cake Balls")
              print("26>Spicy Fish Cakes")
              print("27>Spicy Fish Cakes")
              print("28>Fish and Rice Pockets")
              print("29>Coconut Crepe Rolls")
              print("30>Bondibai")
              print("31>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(250,25)
              elif ch1==3:
                    bill_info(280,28)
              elif ch1==4:
                    bill_info(260,26)
              elif ch1==5:
                    bill_info(240,24)
              elif ch1==6:
                    bill_info(450,45)
              elif ch1==7:
                    bill_info(500,50)
              elif ch1==8:
                    bill_info(480,48)
              elif ch1==9:
                    bill_info(400,40)
              elif ch1==10:
                    bill_info(420,42)
              elif ch1==11:
                    bill_info(600,60)
              elif ch1==12:
                    bill_info(200,20)
              elif ch1==13:
                    bill_info(200,20)
              elif ch1==14:
                    bill_info(150,15)
              elif ch1==15:
                    bill_info(250,25)
              elif ch1==16:
                    bill_info(220,22)
              elif ch1==17:
                    bill_info(50,5)
              elif ch1==18:
                    bill_info(70,7)
              elif ch1==19:
                    bill_info(180,18)
              elif ch1==20:
                    bill_info(350,35)
              elif ch1==21:
                    bill_info(400,40)
              elif ch1==22:
                    bill_info(400,40)
              elif ch1==23:
                    bill_info(150,15)
              elif ch1==25:
                    bill_info(180,18)
              elif ch1==26:
                    bill_info(200,20)
              elif ch1==27:
                    bill_info(200,20)
              elif ch1==28:
                    bill_info(220,22)
              elif ch1==29:
                    bill_info(150,15)
              elif ch1==30:
                    bill_info(200,20)
              else:
                    break

      elif ch==15:
              print(">>Enter The Dishes You Want>>")
              print("1>Beef Noodle Soup")
              print("2>Chicken Noodle Soup")
              print("3>Fiery Lemongrass Beef Noodle")
              print("4>Pork and Seafood Tapioca Noodles")
              print("5>Crab and Tomato Noodle Soup")
              print("6>Vietnamese Baguette Sandwich")
              print("7>Fresh Summer Rolls")
              print("8>Crispy Fried Spring Rolls")
              print("9>Sizzling Savory Crepe")
              print("10>Hanoi Grilled Pork Noodles")
              print("11>Cold Noodles with Grilled Pork")
              print("12>Southern Broken Rice Platter")
              print("13>Caramelized Fish in Claypot")
              print("14>Caramelized Pork Belly with Eggs")
              print("15>Mekong Tangy Sour Soup")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(400,40)
              elif ch1==4:
                    bill_info(350,35)
              elif ch1==5:
                    bill_info(380,38)
              elif ch1==6:
                    bill_info(200,20)
              elif ch1==7:
                    bill_info(150,15)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(450,45)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(400,40)
              elif ch1==13:
                    bill_info(500,50)
              elif ch1==14:
                    bill_info(450,45)
              elif ch1==15:
                    bill_info(300,30)
              else:
                    break

      elif ch==16:
              print(">>Enter The Dishes You Want>>")
              print("1>Pad Thai")
              print("2>Tom Yum Goong")
              print("3>Green Curry")
              print("4>Som Tum")
              print("5>Massaman Curry")
              print("6>Panang Curry")
              print("7>Khao Pad")
              print("8>Pad Krapow")
              print("9>Tom Kha Gai")
              print("10>Khao Soi")
              print("11>Mango Sticky Rice")
              print("12>Tod Mun Pla")
              print("13>Yam Nua")
              print("14>Gai Med Ma Moung")
              print("15>Kuay Teow Reua")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(400,40)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(500,50)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(550,55)
              elif ch1==6:
                    bill_info(500,50)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(450,45)
              elif ch1==9:
                    bill_info(400,40)
              elif ch1==10:
                    bill_info(450,45)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(350,35)
              elif ch1==13:
                    bill_info(400,40)
              elif ch1==14:
                    bill_info(480,48)
              elif ch1==15:
                    bill_info(380,38)
              else:
                    break

      elif ch==17:
              print(">>Enter The Dishes You Want>>")
              print("1>Nasi Goreng")
              print("2>Satay")
              print("3>Rendang")
              print("4>Gado-Gado")
              print("5>Soto Ayam")
              print("6>Bakso")
              print("7>Nasi Uduk")
              print("8>Nasi Padang")
              print("9>Martabak")
              print("10>Pempek")
              print("11>Ayam Taliwang")
              print("12>Rawon")
              print("13>Gudeg")
              print("14>Sayur Asem")
              print("15>Es Cendol")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(450,45)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(280,28)
              elif ch1==6:
                    bill_info(220,22)
              elif ch1==7:
                    bill_info(250,25)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(400,40)
              elif ch1==12:
                    bill_info(350,35)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(200,20)
              elif ch1==15:
                    bill_info(150,15)
              else:
                    break

      elif ch==18:
              print(">>Enter The Dishes You Want>>")
              print("1>Adobo")
              print("2>Sinigang")
              print("3>Lechon")
              print("4>Sisig")
              print("5>Kare-Kare")
              print("6>Pancit Canton")
              print("7>Lumpia")
              print("8>Halo-Halo")
              print("9>Crispy Pata")
              print("10>Tinola")
              print("11>Bulalo")
              print("12>Dinuguan")
              print("13>Longganisa")
              print("14>Tocino")
              print("15>Bicol Express")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(600,60)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(450,45)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(500,50)
              elif ch1==10:
                    bill_info(320,32)
              elif ch1==11:
                    bill_info(480,48)
              elif ch1==12:
                    bill_info(350,35)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(350,35)
              else:
                    break

      elif ch==19:
              print(">>Enter The Dishes You Want>>")
              print("1>Nasi Lemak")
              print("2>Laksa")
              print("3>Char Kway Teow")
              print("4>Hainanese Chicken Rice")
              print("5>Roti Canai")
              print("6>Beef Rendang")
              print("7>Satay")
              print("8>Mee Goreng")
              print("9>Bak Kut Teh")
              print("10>Nasi Kandar")
              print("11>Ikan Bakar")
              print("12>Curry Mee")
              print("13>Cendol")
              print("14>Apam Balik")
              print("15>Rojak")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(280,28)
              elif ch1==4:
                    bill_info(350,35)
              elif ch1==5:
                    bill_info(150,15)
              elif ch1==6:
                    bill_info(450,45)
              elif ch1==7:
                    bill_info(300,30)
              elif ch1==8:
                    bill_info(250,25)
              elif ch1==9:
                    bill_info(400,40)
              elif ch1==10:
                    bill_info(380,38)
              elif ch1==11:
                    bill_info(450,45)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(150,15)
              elif ch1==14:
                    bill_info(180,18)
              elif ch1==15:
                    bill_info(200,20)
              else:
                    break

      elif ch==20:
              print(">>Enter The Dishes You Want>>")
              print("1>Fish Amok")
              print("2>Lok Lak")
              print("3>Kuy Teav")
              print("4>Nom Banh Chok")
              print("5>Bai Sach Chrouk")
              print("6>Lap Khmer")
              print("7>Somlor Machu")
              print("8>Kdam Chaa")
              print("9>Prahok Ktiss")
              print("10>Ya Hon")
              print("11>Num Ansom")
              print("12>Kralan")
              print("13>Bok Lahong")
              print("14>Chha Kadot")
              print("15>Mi Kola")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(280,28)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(350,35)
              elif ch1==7:
                    bill_info(320,32)
              elif ch1==8:
                    bill_info(450,45)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(500,50)
              elif ch1==11:
                    bill_info(200,20)
              elif ch1==12:
                    bill_info(180,18)
              elif ch1==13:
                    bill_info(220,22)
              elif ch1==14:
                    bill_info(380,38)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==21:
              print(">>Enter The Dishes You Want>>")
              print("1>Chilli Crab")
              print("2>Hainanese Chicken Rice")
              print("3>Laksa")
              print("4>Char Kway Teow")
              print("5>Hokkien Mee")
              print("6>Satay")
              print("7>Bak Kut Teh")
              print("8>Roti Prata")
              print("9>Nasi Lemak")
              print("10>Kaya Toast")
              print("11>Mee Rebus")
              print("12>Rojak")
              print("13>Oyster Omelette")
              print("14>Murtabak")
              print("15>Ice Kacang")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(650,65)
              elif ch1==2:
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(320,32)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(180,18)
              elif ch1==11:
                    bill_info(250,25)
              elif ch1==12:
                    bill_info(200,20)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(220,22)
              else:
                    break
      elif ch==22:
              print(">>Enter The Dishes You Want>>")
              print("1>Kabuli Pulao")
              print("2>Mantu")
              print("3>Bolani")
              print("4>Qabili Palaw")
              print("5>Ashak")
              print("6>Kebab")
              print("7>Afghan Bread")
              print("8>Borani Banjan")
              print("9>Sheer Khurma")
              print("10>Chopan Kebab")
              print("11>Aush")
              print("12>Haft Mewa")
              print("13>Firnee")
              print("14>Qorma-e-Sabzi")
              print("15>Quroot")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(450,45)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(80,8)
              elif ch1==8:
                    bill_info(250,25)
              elif ch1==9:
                    bill_info(180,18)
              elif ch1==10:
                    bill_info(500,50)
              elif ch1==11:
                    bill_info(280,28)
              elif ch1==12:
                    bill_info(200,20)
              elif ch1==13:
                    bill_info(150,15)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(100,10)
              else:
                    break

      elif ch==23:
              print(">>Enter The Dishes You Want>>")
              print("1>Meat Pie")
              print("2>Vegemite on Toast")
              print("3>Lamington")
              print("4>Pavlova")
              print("5>Barramundi")
              print("6>Anzac Biscuits")
              print("7>Kangaroo Steak")
              print("8>Chicken Parmigiana")
              print("9>Fairy Bread")
              print("10>Tim Tams")
              print("11>Sausage Sizzle")
              print("12>Chiko Roll")
              print("13>Damper")
              print("14>Macadamia Nuts")
              print("15>Vanilla Slice")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(100,10)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(600,60)
              elif ch1==6:
                    bill_info(120,12)
              elif ch1==7:
                    bill_info(750,75)
              elif ch1==8:
                    bill_info(450,45)
              elif ch1==9:
                    bill_info(80,8)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(200,20)
              elif ch1==13:
                    bill_info(180,18)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(220,22)
              else:
                    break

      elif ch==24:
              print(">>Enter The Dishes You Want>>")
              print("1>Hangi")
              print("2>Pavlova")
              print("3>Green-lipped Mussels")
              print("4>Meat Pie")
              print("5>Fish and Chips")
              print("6>Kiwi Burger")
              print("7>Hokey Pokey Ice Cream")
              print("8>Lolly Cake")
              print("9>Whitebait Fritters")
              print("10>Roast Lamb")
              print("11>Kumara Chips")
              print("12>Sausage Sizzle")
              print("13>Anzac Biscuits")
              print("14>Manuka Honey")
              print("15>Cheese Rolls")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(500,50)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(450,45)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(600,60)
              elif ch1==10:
                    bill_info(700,70)
              elif ch1==11:
                    bill_info(180,18)
              elif ch1==12:
                    bill_info(150,15)
              elif ch1==13:
                    bill_info(120,12)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(220,22)
              else:
                    break

      elif ch==25:
              print(">>Enter The Dishes You Want>>")
              print("1>Pizza Margherita")
              print("2>Spaghetti Carbonara")
              print("3>Lasagna")
              print("4>Risotto")
              print("5>Tiramisu")
              print("6>Gelato")
              print("7>Ravioli")
              print("8>Gnocchi")
              print("9>Ossobuco")
              print("10>Focaccia")
              print("11>Bruschetta")
              print("12>Panna Cotta")
              print("13>Minestrone")
              print("14>Arancini")
              print("15>Cannoli")    
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(500,50)
              elif ch1==3:
                    bill_info(550,55)
              elif ch1==4:
                    bill_info(480,48)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(400,40)
              elif ch1==9:
                    bill_info(800,80)
              elif ch1==10:
                    bill_info(200,20)
              elif ch1==11:
                    bill_info(250,25)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(320,32)
              elif ch1==15:
                    bill_info(280,28)
              else:
                    break

      elif ch==26:
              print(">>Enter The Dishes You Want>>")
              print("1>Paella")
              print("2>Tapas")
              print("3>Tortilla Espanola")
              print("4>Gazpacho")
              print("5>Churros")
              print("6>Jamon Iberico")
              print("7>Patatas Bravas")
              print("8>Croquetas")
              print("9>Pulpo a la Gallega")
              print("10>Fabada")
              print("11>Pisto")
              print("12>Crema Catalana")
              print("13>Empanadas")
              print("14>Salmorejo")
              print("15>Gambas al Ajillo")     
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(600,60)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(300,30)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(200,20)
              elif ch1==6:
                    bill_info(800,80)
              elif ch1==7:
                    bill_info(280,28)
              elif ch1==8:
                    bill_info(320,32)
              elif ch1==9:
                    bill_info(650,65)
              elif ch1==10:
                    bill_info(450,45)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(250,25)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(550,55)
              else:
                    break

      elif ch==27:
              print(">>Enter The Dishes You Want>>")
              print("1>Moussaka")
              print("2>Souvlaki")
              print("3>Gyro")
              print("4>Tzatziki")
              print("5>Greek Salad")
              print("6>Spanakopita")
              print("7>Baklava")
              print("8>Fasolada")
              print("9>Dolmades")
              print("10>Taramasalata")
              print("11>Kleftiko")
              print("12>Pastitsio")
              print("13>Loukoumades")
              print("14>Saganaki")
              print("15>Melomakarona")    
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(380,38)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(350,35)
              elif ch1==7:
                    bill_info(280,28)
              elif ch1==8:
                    bill_info(320,32)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(600,60)
              elif ch1==12:
                    bill_info(450,45)
              elif ch1==13:
                    bill_info(220,22)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==28:
              print(">>Enter The Dishes You Want>>")
              print("1>Halloumi")
              print("2>Souvla")
              print("3>Sheftalia")
              print("4>Kleftiko")
              print("5>Makaronia Tou Fournou")
              print("6>Koupepia")
              print("7>Louvi")
              print("8>Tzatziki")
              print("9>Taramosalata")
              print("10>Tahini")
              print("11>Flaounes")
              print("12>Loukoumades")
              print("13>Shoushoukos")
              print("14>Pasteli")
              print("15>Commandaria")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(380,38)
              elif ch1==4:
                    bill_info(600,60)
              elif ch1==5:
                    bill_info(450,45)
              elif ch1==6:
                    bill_info(350,35)
              elif ch1==7:
                    bill_info(280,28)
              elif ch1==8:
                    bill_info(200,20)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(220,22)
              elif ch1==13:
                    bill_info(250,25)
              elif ch1==14:
                    bill_info(180,18)
              elif ch1==15:
                    bill_info(400,40)
              else:
                    break

      elif ch==29:
              print(">>Enter The Dishes You Want>>")
              print("1>Bacalhau a Bras")
              print("2>Pasteis de Nata")
              print("3>Francesinha")
              print("4>Caldo Verde")
              print("5>Frango Assado")
              print("6>Arroz de Pato")
              print("7>Polvo a Lagareiro")
              print("8>Alheira")
              print("9>Feijoada")
              print("10>Bifana")
              print("11>Cataplana")
              print("12>Sardinhas Assadas")
              print("13>Bolo do Caco")
              print("14>Cozido a Portuguesa")
              print("15>Queijadas")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(500,50)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(450,45)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(400,40)
              elif ch1==6:
                    bill_info(450,45)
              elif ch1==7:
                    bill_info(650,65)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(400,40)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(700,70)
              elif ch1==12:
                    bill_info(400,40)
              elif ch1==13:
                    bill_info(200,20)
              elif ch1==14:
                    bill_info(550,55)
              elif ch1==15:
                    bill_info(220,22)
              else:
                    break

      elif ch==30:
              print(">>Enter The Dishes You Want>>")
              print("1>Coq au Vin")
              print("2>Boeuf Bourguignon")
              print("3>Croissant")
              print("4>Escargot")
              print("5>Quiche Lorraine")
              print("6>Ratatouille")
              print("7>Bouillabaisse")
              print("8>Crème Brulee")
              print("9>Soupe a l'Oignon")
              print("10>Macarons")
              print("11>Tarte Tatin")
              print("12>Cassoulet")
              print("13>Salade Nicoise")
              print("14>Foie Gras")
              print("15>Crepes")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(650,65)
              elif ch1==2:
                    bill_info(700,70)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(550,55)
              elif ch1==5:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(800,80)
              elif ch1==8:
                    bill_info(300,30)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(280,28)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(600,60)
              elif ch1==13:
                    bill_info(450,45)
              elif ch1==14:
                    bill_info(900,90)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==31:
              print(">>Enter The Dishes You Want>>")
              print("1>Bratwurst")
              print("2>Sauerbraten")
              print("3>Pretzel")
              print("4>Schnitzel")
              print("5>Schwarzwälder Kirschtorte")
              print("6>Currywurst")
              print("7>Kartoffelsalat")
              print("8>Spätzle")
              print("9>Rouladen")
              print("10>Eisbein")
              print("11>Maultaschen")
              print("12>Apfelstrudel")
              print("13>Leberkäse")
              print("14>Rote Grütze")
              print("15>Stollen")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(550,55)
              elif ch1==3:
                    bill_info(180,18)
              elif ch1==4:
                    bill_info(450,45)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(250,25)
              elif ch1==8:
                    bill_info(280,28)
              elif ch1==9:
                    bill_info(500,50)
              elif ch1==10:
                    bill_info(600,60)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(320,32)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(400,40)
              else:
                    break

      elif ch==32:
              print(">>Enter The Dishes You Want>>")
              print("1>Wiener Schnitzel")
              print("2>Sachertorte")
              print("3>Apfelstrudel")
              print("4>Tafelspitz")
              print("5>Kaiserschmarrn")
              print("6>Knödel")
              print("7>Gulasch")
              print("8>Käsespätzle")
              print("9>Linzer Torte")
              print("10>Frittatensuppe")
              print("11>Buchteln")
              print("12>Germknödel")
              print("13>Schweinsbraten")
              print("14>Krautfleckerl")
              print("15>Topfenstrudel")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                  bill_info(500,50)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(300,30)
              elif ch1==4:
                    bill_info(650,65)
              elif ch1==5:
                    bill_info(380,38)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(280,28)
              elif ch1==12:
                    bill_info(320,32)
              elif ch1==13:
                    bill_info(500,50)
              elif ch1==14:
                    bill_info(280,28)
              elif ch1==15:
                    bill_info(300,30)
              else:
                    break

      elif ch==33:
              print(">>Enter The Dishes You Want>>")
              print("1>Irish Stew")
              print("2>Soda Bread")
              print("3>Colcannon")
              print("4>Boxty")
              print("5>Coddle")
              print("6>Black Pudding")
              print("7>Barmbrack")
              print("8>Irish Coffee")
              print("9>Shepherd's Pie")
              print("10>Bacon and Cabbage")
              print("11>Seafood Chowder")
              print("12>Champ")
              print("13>Farl")
              print("14>Guinness Pie")
              print("15>Potato Soup")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(150,15)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(400,40)
              elif ch1==6:
                    bill_info(350,35)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(300,30)
              elif ch1==9:
                    bill_info(500,50)
              elif ch1==10:
                    bill_info(450,45)
              elif ch1==11:
                    bill_info(550,55)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(150,15)
              elif ch1==14:
                    bill_info(550,55)
              elif ch1==15:
                    bill_info(280,28)
              else:
                    break

      elif ch==34:
              print(">>Enter The Dishes You Want>>")
              print("1>Waffles")
              print("2>Frites")
              print("3>Moules-Frites")
              print("4>Belgian Chocolate")
              print("5>Waterzooi")
              print("6>Carbonade Flamande")
              print("7>Speculoos")
              print("8>Stoemp")
              print("9>Croquettes")
              print("10>Boudin")
              print("11>Paling in 't Groen")
              print("12>Filet Americain")
              print("13>Mattentaart")
              print("14>Tarte au Riz")
              print("15>Liege Syrup")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(650,65)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(500,50)
              elif ch1==6:
                    bill_info(550,55)
              elif ch1==7:
                    bill_info(150,15)
              elif ch1==8:
                    bill_info(250,25)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(400,40)
              elif ch1==11:
                    bill_info(600,60)
              elif ch1==12:
                    bill_info(450,45)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(150,15)
              else:
                    break

      elif ch==35:
              print(">>Enter The Dishes You Want>>")
              print("1>Stroopwafel")
              print("2>Bitterballen")
              print("3>Poffertjes")
              print("4>Haring")
              print("5>Stamppot")
              print("6>Erwtensoep")
              print("7>Gouda Cheese")
              print("8>Drop")
              print("9>Oliebollen")
              print("10>Kroket")
              print("11>Appeltaart")
              print("12>Pannenkoeken")
              print("13>Rijsttafel")
              print("14>Hagelslag")
              print("15>Frikandel")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(150,15)
              elif ch1==2:
                    bill_info(250,25)
              elif ch1==3:
                    bill_info(200,20)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(100,10)
              elif ch1==9:
                    bill_info(180,18)
              elif ch1==10:
                    bill_info(220,22)
              elif ch1==11:
                    bill_info(280,28)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(700,70)
              elif ch1==14:
                    bill_info(120,12)
              elif ch1==15:
                    bill_info(200,20)
              else:
                    break

      elif ch==36:
              print(">>Enter The Dishes You Want>>")
              print("1>Fondue")
              print("2>Raclette")
              print("3>Rösti")
              print("4>Zürcher Geschnetzeltes")
              print("5>Swiss Chocolate")
              print("6>Birchermüesli")
              print("7>Älplermagronen")
              print("8>Tartiflette")
              print("9>Bündner Nusstorte")
              print("10>Basler Leckerli")
              print("11>Zopf")
              print("12>Saffron Risotto")
              print("13>Polenta")
              print("14>Capuns")
              print("15>Malakoff")    
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(800,80)
              elif ch1==2:
                    bill_info(700,70)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(650,65)
              elif ch1==5:
                    bill_info(400,40)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(550,55)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(200,20)
              elif ch1==11:
                    bill_info(180,18)
              elif ch1==12:
                    bill_info(500,50)
              elif ch1==13:
                    bill_info(300,30)
              elif ch1==14:
                    bill_info(450,45)
              elif ch1==15:
                    bill_info(300,30)
              else:
                    break

      elif ch==37:
              print(">>Enter The Dishes You Want>>")
              print("1>Borscht")
              print("2>Varenyky")
              print("3>Holubtsi")
              print("4>Salo")
              print("5>Deruny")
              print("6>Kyiv Cake")
              print("7>Chicken Kyiv")
              print("8>Pampushky")
              print("9>Banosh")
              print("10>Uzvar")
              print("11>Kutia")
              print("12>Nalyisnyky")
              print("13>Kholodets")
              print("14>Syrnyky")
              print("15>Zrazy")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(250,25)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(220,22)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(280,28)
              elif ch1==10:
                    bill_info(120,12)
              elif ch1==11:
                    bill_info(200,20)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(220,22)
              elif ch1==15:
                    bill_info(300,30)
              else:
                    break

      elif ch==38:
              print(">>Enter The Dishes You Want>>")
              print("1>Pierogi")
              print("2>Bigos")
              print("3>Kielbasa")
              print("4>Kotlet Schabowy")
              print("5>Zurek")
              print("6>Placki Ziemniaczane")
              print("7>Golabki")
              print("8>Makowiec")
              print("9>Paczki")
              print("10>Barszcz")
              print("11>Rosol")
              print("12>Oscypek")
              print("13>Sernik")
              print("14>Kopytka")
              print("15>Zapiekanka")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(280,28)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(200,20)
              elif ch1==9:
                    bill_info(150,15)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(220,22)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(200,20)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==39:
              print(">>Enter The Dishes You Want>>")
              print("1>Vepro Knedlo Zelo")
              print("2>Svickova")
              print("3>Trdelnik")
              print("4>Gulas")
              print("5>Smazeny Syr")
              print("6>Bramboraky")
              print("7>Kulajda")
              print("8>Knedliky")
              print("9>Utopenci")
              print("10>Sekana")
              print("11>Moravsky Vrabec")
              print("12>Chlebicky")
              print("13>Buchty")
              print("14>Medovnik")
              print("15>Kofola")    
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(500,50)
              elif ch1==3:
                    bill_info(200,20)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(280,28)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(200,20)
              elif ch1==10:
                    bill_info(350,35)
              elif ch1==11:
                    bill_info(400,40)
              elif ch1==12:
                    bill_info(180,18)
              elif ch1==13:
                    bill_info(220,22)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(150,15)
              else:
                    break

      elif ch==40:
              print(">>Enter The Dishes You Want>>")
              print("1>Goulash")
              print("2>Chicken Paprikash")
              print("3>Langos")
              print("4>Dobos Torte")
              print("5>Halaszle")
              print("6>Somloi Galuska")
              print("7>Töltött Kaposzta")
              print("8>Pörkölt")
              print("9>Kürtöskalacs")
              print("10>Palacsinta")
              print("11>Túró Rudi")
              print("12>Rakott Krumpli")
              print("13>Lecso")
              print("14>Fözelek")
              print("15>Beigli")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(350,35)
              elif ch1==5:
                    bill_info(500,50)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(380,38)
              elif ch1==8:
                    bill_info(420,42)
              elif ch1==9:
                    bill_info(200,20)
              elif ch1==10:
                    bill_info(220,22)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(300,30)
              else:
                    break

      elif ch==41:
              print(">>Enter The Dishes You Want>>")
              print("1>Sarmale")
              print("2>Mamaliga")
              print("3>Mici")
              print("4>Ciorba de Burta")
              print("5>Papanasi")
              print("6>Cozonac")
              print("7>Salata de Boeuf")
              print("8>Drob")
              print("9>Tochitura")
              print("10>Zacusca")
              print("11>Ciorba Radauteana")
              print("12>Placinta")
              print("13>Slanina")
              print("14>Fasole cu Carnati")
              print("15>Jumari")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(150,15)
              elif ch1==3:
                    bill_info(300,30)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(280,28)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(200,20)
              elif ch1==11:
                    bill_info(380,38)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(200,20)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(220,22)
              else:
                    break

      elif ch==42:
              print(">>Enter The Dishes You Want>>")
              print("1>Meatballs")
              print("2>Gravlax")
              print("3>Smörgåsbord")
              print("4>Knäckebröd")
              print("5>Kanelbulle")
              print("6>Surströmming")
              print("7>Prinsesstårta")
              print("8>Lingonberry Jam")
              print("9>Pyttipanna")
              print("10>Räksmörgås")
              print("11>Ärtsoppa")
              print("12>Pannkakor")
              print("13>Sill")
              print("14>Kroppkakor")
              print("15>Blåbärssoppa")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(500,50)
              elif ch1==3:
                    bill_info(800,80)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(200,20)
              elif ch1==6:
                    bill_info(600,60)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(120,12)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(400,40)
              elif ch1==11:
                    bill_info(250,25)
              elif ch1==12:
                    bill_info(220,22)
              elif ch1==13:
                    bill_info(300,30)
              elif ch1==14:
                    bill_info(280,28)
              elif ch1==15:
                    bill_info(200,20)
              else:
                    break

      elif ch==43:
              print(">>Enter The Dishes You Want>>")
              print("1>Fårikål")
              print("2>Smalahove")
              print("3>Rakfisk")
              print("4>Lutefisk")
              print("5>Krumkake")
              print("6>Brunost")
              print("7>Lefse")
              print("8>Kjøttkaker")
              print("9>Pinnekjøtt")
              print("10>Rømmegrøt")
              print("11>Fiskesuppe")
              print("12>Sveler")
              print("13>Multekrem")
              print("14>Raspeball")
              print("15>Aquavit")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(500,50)
              elif ch1==2:
                    bill_info(550,55)
              elif ch1==4:
                    bill_info(450,45)
              elif ch1==5:
                    bill_info(200,20)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(150,15)
              elif ch1==8:
                    bill_info(400,40)
              elif ch1==9:
                    bill_info(700,70)
              elif ch1==10:
                    bill_info(300,30)
              elif ch1==11:
                    bill_info(450,45)
              elif ch1==12:
                    bill_info(180,18)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(350,35)
              else:
                    break

      elif ch==44:
              print(">>Enter The Dishes You Want>>")
              print("1>Smørrebrød")
              print("2>Frikadeller")
              print("3>Stegt Flæsk")
              print("4>Æbleskiver")
              print("5>Rødgrød med Fløde")
              print("6>Koldskål")
              print("7>Flæskesteg")
              print("8>Leverpostej")
              print("9>Wienerbrød")
              print("10>Rugbrød")
              print("11>Hakkebøf")
              print("12>Kransekage")
              print("13>Tarteletter")
              print("14>Pølse")
              print("15>Medisterpølse")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(450,45)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(180,18)
              elif ch1==7:
                    bill_info(500,50)
              elif ch1==8:
                    bill_info(220,22)
              elif ch1==9:
                    bill_info(280,28)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(400,40)
              elif ch1==12:
                    bill_info(350,35)
              elif ch1==13:
                    bill_info(300,30)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(280,28)
              else:
                    break

      elif ch==45:
              print(">>Enter The Dishes You Want>>")
              print("1>Karjalanpiirakka")
              print("2>Kalakukko")
              print("3>Poronkäristys")
              print("4>Ruisleipä")
              print("5>Salmiakki")
              print("6>Leipäjuusto")
              print("7>Mämmi")
              print("8>Lihapullat")
              print("9>Hernekeitto")
              print("10>Graavilohi")
              print("11>Korvapuusti")
              print("12>Mustikkapiirakka")
              print("13>Vispipuuro")
              print("14>Muikku")
              print("15>Lörtsy")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(200,20)
              elif ch1==2:
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(650,65)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(120,12)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(180,18)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(220,22)
              elif ch1==10:
                    bill_info(450,45)
              elif ch1==11:
                    bill_info(200,20)
              elif ch1==12:
                    bill_info(280,28)
              elif ch1==13:
                    bill_info(200,20)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(180,18)
              else:
                    break

      elif ch==46:
              print(">>Enter The Dishes You Want>>")
              print("1>Hamburger")
              print("2>Hot Dog")
              print("3>Apple Pie")
              print("4>Fried Chicken")
              print("5>Macaroni and Cheese")
              print("6>BBQ Ribs")
              print("7>Clam Chowder")
              print("8>Thanksgiving Turkey")
              print("9>Cheesesteak")
              print("10>Buffalo Wings")
              print("11>Chocolate Chip Cookies")
              print("12>Pancakes")
              print("13>Peanut Butter and Jelly")
              print("14>Pecan Pie")
              print("15>Cornbread")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(280,28)
              elif ch1==6:
                    bill_info(600,60)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(800,80)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(380,38)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(150,15)
              elif ch1==14:
                    bill_info(280,28)
              elif ch1==15:
                    bill_info(180,18)
              else:
                    break

      elif ch==47:
              print(">>Enter The Dishes You Want>>")
              print("1>Poutine")
              print("2>Maple Syrup")
              print("3>Butter Tarts")
              print("4>Nanaimo Bars")
              print("5>Tourtière")
              print("6>Montreal Smoked Meat")
              print("7>Peameal Bacon")
              print("8>BeaverTails")
              print("9>Ketchup Chips")
              print("10>Caesar Cocktail")
              print("11>Bannock")
              print("12>Saskatoon Berry Pie")
              print("13>Split Pea Soup")
              print("14>Donair")
              print("15>Timbits")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==16: break
              elif ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(180,18)
              elif ch1==4:
                    bill_info(220,22)
              elif ch1==5:
                    bill_info(450,45)
              elif ch1==6:
                    bill_info(500,50)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(250,25)
              elif ch1==9:
                    (100,10)
              elif ch1==10:
                    bill_info(300,30)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(280,28)
              elif ch1==13:
                    bill_info(250,25)
              elif ch1==14:
                    bill_info(400,40)
              elif ch1==15:
                    bill_info(120,12)
              else:
                    break

      elif ch==48:
              print(">>Enter The Dishes You Want>>")
              print("1>Tacos")
              print("2>Enchiladas")
              print("3>Guacamole")
              print("4>Churros")
              print("5>Tamales")
              print("6>Quesadillas")
              print("7>Chiles Rellenos")
              print("8>Mole")
              print("9>Pozole")
              print("10>Tostadas")
              print("11>Fajitas")
              print("12>Sopes")
              print("13>Elote")
              print("14>Carnitas")
              print("15>Flan")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(200,20)
              elif ch1==4:
                    bill_info(180,18)
              elif ch1==5:
                    bill_info(220,22)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(450,45)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(400,40)
              elif ch1==12:
                    bill_info(220,22)
              elif ch1==13:
                    bill_info(150,15)
              elif ch1==14:
                    bill_info(380,38)
              elif ch1==15:
                    bill_info(200,20)
              else:
                    break

      elif ch==49:
              print(">>Enter The Dishes You Want>>")
              print("1>Pupusas")
              print("2>Gallo Pinto")
              print("3>Tamales")
              print("4>Empanadas")
              print("5>Yuca Frita")
              print("6>Vigorón")
              print("7>Sopa de Caracol")
              print("8>Nacatamal")
              print("9>Baleadas")
              print("10>Rondon")
              print("11>Tostones")
              print("12>Tres Leches Cake")
              print("13>Ceviche")
              print("14>Chifrijo")
              print("15>Horchata")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(200,20)
              elif ch1==2:
                    bill_info(180,18)
              elif ch1==3:
                    bill_info(220,22)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(180,18)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(250,25)
              elif ch1==9:
                    bill_info(200,20)
              elif ch1==10:
                    bill_info(500,50)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(280,28)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(300,30)
              elif ch1==15:
                    bill_info(120,12)
              else:
                    break

      elif ch==50:

              print(">>Enter The Dishes You Want>>")
              print("1>Jerk Chicken")
              print("2>Ackee and Saltfish")
              print("3>Jamaican Patty")
              print("4>Curry Goat")
              print("5>Oxtail Stew")
              print("6>Rice and Peas")
              print("7>Bammy")
              print("8>Callaloo")
              print("9>Escovitch Fish")
              print("10>Festival")
              print("11>Mannish Water")
              print("12>Blue Mountain Coffee")
              print("13>Rum Punch")
              print("14>Plantain Tarts")
              print("15>Gizzada")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(400,40)
              elif ch1==2:
                    bill_info(500,50)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(550,55)
              elif ch1==5:
                    bill_info(600,60)
              elif ch1==6:
                    bill_info(250,25)
              elif ch1==7:
                    bill_info(180,18)
              elif ch1==8:
                    bill_info(200,20)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(200,20)
              elif ch1==15:
                    bill_info(180,18)
              else:
                    break

      elif ch==51:
              print(">>Enter The Dishes You Want>>")
              print("1>Mangu")
              print("2>Sancocho")
              print("3>Tostones")
              print("4>Mofongo")
              print("5>Arroz con Pollo")
              print("6>Habichuelas con Dulce")
              print("7>Pescado Frito")
              print("8>Chicharron")
              print("9>Yuca")
              print("10>Pasteles en Hoja")
              print("11>Morir Sonando")
              print("12>La Bandera")
              print("13>Chimichurri Burger")
              print("14>Tres Leches")
              print("15>Majarete")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(350,35)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(200,20)
              elif ch1==7:
                    bill_info(400,40)
              elif ch1==8:
                    bill_info(350,35)
              elif ch1==9:
                    bill_info(180,18)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(220,22)
              elif ch1==12:
                    bill_info(500,50)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(280,28)
              elif ch1==15:
                    bill_info(200,20)
              else:
                    break

      elif ch==52:
              print(">>Enter The Dishes You Want>>")
              print("1>Griot")
              print("2>Diri ak Djon Djon")
              print("3>Soup Joumou")
              print("4>Pikliz")
              print("5>Legim")
              print("6>Banan Pese")
              print("7>Tassot")
              print("8>Akra")
              print("9>Lalo")
              print("10>Poulet Aux Noix")
              print("11>Bouyon")
              print("12>Epis")
              print("13>Macaroni au Gratin")
              print("14>Pain Patate")
              print("15>Kremas")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(400,40)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(280,28)
              elif ch1==6:
                    bill_info(180,18)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(200,20)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(500,50)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(150,15)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(220,22)
              elif ch1==15:
                    bill_info(300,30)
              else:
                    break

      elif ch==53:
              print(">>Enter The Dishes You Want>>")
              print("1>Ceviche")
              print("2>Lomo Saltado")
              print("3>Aji de Gallina")
              print("4>Anticuchos")
              print("5>Causa")
              print("6>Rocoto Relleno")
              print("7>Papa a la Huancaina")
              print("8>Pollo a la Brasa")
              print("9>Pisco Sour")
              print("10>Alfajores")
              print("11>Cuy Asado")
              print("12>Tacu Tacu")
              print("13>Suspiro a la Limena")
              print("14>Arroz con Pato")
              print("15>Chicha Morada")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(400,40)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(380,38)
              elif ch1==7:
                    bill_info(280,28)
              elif ch1==8:
                    bill_info(500,50)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(200,20)
              elif ch1==11:
                    bill_info(650,65)
              elif ch1==12:
                    bill_info(350,35)
              elif ch1==13:
                    bill_info(250,25)
              elif ch1==14:
                    bill_info(450,45)
              elif ch1==15:
                    bill_info(150,15)
              else:
                    break

      elif ch==54:
              print(">>Enter The Dishes You Want>>")
              print("1>Asado")
              print("2>Empanadas")
              print("3>Chimichurri")
              print("4>Dulce de Leche")
              print("5>Alfajores")
              print("6>Milanesa")
              print("7>Choripan")
              print("8>Provoleta")
              print("9>Locro")
              print("10>Mate")
              print("11>Matambre")
              print("12>Flan")
              print("13>Carbonada")
              print("14>Medialunas")
              print("15>Vitel Tone")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(800,80)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(180,18)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(450,45)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(300,30)
              elif ch1==9:
                    bill_info(400,40)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(550,55)
              elif ch1==12:
                    bill_info(200,20)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(180,18)
              elif ch1==15:
                    bill_info(450,45)
              else:
                    break

      elif ch==55:
              print(">>Enter The Dishes You Want>>")
              print("1>Feijoada")
              print("2>Pao de Queijo")
              print("3>Churrasco")
              print("4>Brigadeiro")
              print("5>Coxinha")
              print("6>Moqueca")
              print("7>Acaraje")
              print("8>Farofa")
              print("9>Tapioca")
              print("10>Guaraná")
              print("11>Caipirinha")
              print("12>Quindim")
              print("13>Empadao")
              print("14>Pastel")
              print("15>Vatapá")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(500,50)
              elif ch1==2:
                    bill_info(250,25)
              elif ch1==3:
                    bill_info(850,85)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(180,18)
              elif ch1==6:
                    bill_info(600,60)
              elif ch1==7:
                    bill_info(300,30)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(120,12)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(220,22)
              elif ch1==13:
                    bill_info(350,35)
              elif ch1==14:
                    bill_info(200,20)
              elif ch1==15:
                    bill_info(450,45)
              else:
                    break

      elif ch==56:
              print(">>Enter The Dishes You Want>>")
              print("1>Bandeja Paisa")
              print("2>Arepas")
              print("3>Ajiaco")
              print("4>Sancocho")
              print("5>Empanadas")
              print("6>Buñuelos")
              print("7>Natilla")
              print("8>Pandebono")
              print("9>Tamales")
              print("10>Changua")
              print("11>Obleas")
              print("12>Patacones")
              print("13>Lechona")
              print("14>Hormigas Culonas")
              print("15>Lulo Juice")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(650,65)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(400,40)
              elif ch1==4:
                    bill_info(450,45)
              elif ch1==5:
                    bill_info(180,18)
              elif ch1==6:
                    bill_info(150,15)
              elif ch1==7:
                    bill_info(220,22)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(300,30)
              elif ch1==11:
                    bill_info(180,18)
              elif ch1==12:
                    bill_info(200,20)
              elif ch1==13:
                    bill_info(500,50)
              elif ch1==14:
                    bill_info(600,60)
              elif ch1==15:
                    bill_info(150,15)
              else:
                    break

      elif ch==57:
              print(">>Enter The Dishes You Want>>")
              print("1>Arepas")
              print("2>Pabellon Criollo")
              print("3>Tequeños")
              print("4>Hallacas")
              print("5>Cachapas")
              print("6>Tres Leches")
              print("7>Empanadas")
              print("8>Pan de Jamon")
              print("9>Asado Negro")
              print("10>Pisca Andina")
              print("11>Mandocas")
              print("12>Quesillo")
              print("13>Chicha")
              print("14>Golfeados")
              print("15>Bienmesabe")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(200,20)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(180,18)
              elif ch1==8:
                    bill_info(250,25)
              elif ch1==9:
                    bill_info(500,50)
              elif ch1==10:
                    bill_info(350,35)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(220,22)
              elif ch1==13:
                    bill_info(120,12)
              elif ch1==14:
                    bill_info(180,18)
              elif ch1==15:
                    bill_info(280,28)
              else:
                    break

      elif ch==58:
              print(">>Enter The Dishes You Want>>")
              print("1>Kebab")
              print("2>Baklava")
              print("3>Lahmacun")
              print("4>Manti")
              print("5>Dolma")
              print("6>Pide")
              print("7>Börek")
              print("8>Lokum")
              print("9>Meze")
              print("10>Menemen")
              print("11>Kumpir")
              print("12>Simit")
              print("13>Ayran")
              print("14>Imam Bayildi")
              print("15>Gözleme")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(350,35)
              elif ch1==5:
                    bill_info(280,28)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(400,40)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(100,10)
              elif ch1==13:
                    bill_info(80,8)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(220,22)
              else:
                    break

      elif ch==59:
              print(">>Enter The Dishes You Want>>")
              print("1>Kabsa")
              print("2>Mandi")
              print("3>Shawarma")
              print("4>Falafel")
              print("5>Hummus")
              print("6>Mutabbaq")
              print("7>Harees")
              print("8>Majboos")
              print("9>Luqaimat")
              print("10>Balaleet")
              print("11>Saloona")
              print("12>Machboos")
              print("13>Madrouba")
              print("14>Thareed")
              print("15>Gahwa")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(600,60)
              elif ch1==2:
                    bill_info(650,65)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(200,20)
              elif ch1==6:
                    bill_info(350,35)
              elif ch1==7:
                    bill_info(400,40)
              elif ch1==8:
                    bill_info(600,60)
              elif ch1==9:
                    bill_info(180,18)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(450,45)
              elif ch1==12:
                    bill_info(600,60)
              elif ch1==13:
                    bill_info(500,50)
              elif ch1==14:
                    bill_info(450,45)
              elif ch1==15:
                    bill_info(100,10)
              else:
                    break

      elif ch==60:
              print(">>Enter The Dishes You Want>>")
              print("1>Falafel")
              print("2>Hummus")
              print("3>Shakshuka")
              print("4>Sabich")
              print("5>Shawarma")
              print("6>Challah")
              print("7>Rugelach")
              print("8>Babka")
              print("9>Schnitzel")
              print("10>Matzah Ball Soup")
              print("11>Cholent")
              print("12>Latkes")
              print("13>Bourekas")
              print("14>Malabi")
              print("15>Sufganiyot")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(150,15)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(180,18)
              elif ch1==7:
                    bill_info(220,22)
              elif ch1==8:
                    bill_info(300,30)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(300,30)
              elif ch1==11:
                    bill_info(500,50)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(200,20)
              elif ch1==14:
                    bill_info(180,18)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==61:
              print(">>Enter The Dishes You Want>>")
              print("1>Jollof Rice")
              print("2>Fufu")
              print("3>Injera")
              print("4>Bunny Chow")
              print("5>Tagine")
              print("6>Couscous")
              print("7>Biltong")
              print("8>Bobotie")
              print("9>Ugali")
              print("10>Suya")
              print("11>Kapenta")
              print("12>Ndole")
              print("13>Yassa")
              print("14>Chapati")
              print("15>Malva Pudding")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(550,55)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(450,45)
              elif ch1==8:
                    bill_info(500,50)
              elif ch1==9:
                    bill_info(200,20)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(400,40)
              elif ch1==13:
                    bill_info(450,45)
              elif ch1==14:
                    bill_info(100,10)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==62:
              print(">>Enter The Dishes You Want>>")
              print("1>Undhiyu")
              print("2>Dhokla")
              print("3>Khandvi")
              print("4>Thepla")
              print("5>Sabudana Khichdi")
              print("6>Kela Methi Nu Shaak")
              print("7>Dal Dhokli")
              print("8>Paneer Tikka (No Onion/Garlic)")
              print("9>Jain Pav Bhaji")
              print("10>Jain Chole")
              print("11>Makhana Kheer")
              print("12>Moong Dal Halwa")
              print("13>Khakhra")
              print("14>Fafda")
              print("15>Sev Tomato Shaak")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(280,28)
              elif ch1==2:
                    bill_info(120,12)
              elif ch1==3:
                    bill_info(150,15)
              elif ch1==4:
                    bill_info(100,10)
              elif ch1==5:
                    bill_info(180,18)
              elif ch1==6:
                    bill_info(220,22)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(300,30)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(220,22)
              elif ch1==11:
                    bill_info(250,25)
              elif ch1==12:
                    bill_info(180,18)
              elif ch1==13:
                    bill_info(80,8)
              elif ch1==14:
                    bill_info(150,15)
              elif ch1==15:
                    bill_info(180,18)
              else:
                    break

      elif ch==63:
          while True:
              print(">>Enter The Dishes You Want>>")
              print("1>Shojin Ryori")
              print("2>Luohan Zhai (Buddha's Delight)")
              print("3>Vegetarian Spring Rolls")
              print("4>Tofu Stir Fry")
              print("5>Congee")
              print("6>Steamed Veggie Dumplings")
              print("7>Miso Soup")
              print("8>Seaweed Salad")
              print("9>Zaru Soba")
              print("10>Inari Sushi")
              print("11>Lotus Root Stir Fry")
              print("12>Veggie Tempura")
              print("13>Braised Bamboo Shoots")
              print("14>Sticky Rice")
              print("15>Green Tea Mochi")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(800,80)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(200,20)
              elif ch1==4:
                    bill_info(300,30)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(150,15)
              elif ch1==8:
                    bill_info(220,22)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(300,30)
              elif ch1==12:
                    bill_info(350,35)
              elif ch1==13:
                    bill_info(320,32)
              elif ch1==14:
                    bill_info(150,15)
              elif ch1==15:
                    bill_info(280,28)
              else:
                    break

      elif ch==64:
              print(">>Enter The Dishes You Want>>")
              print("1>Ropa Vieja")
              print("2>Picadillo")
              print("3>Lechon Asado")
              print("4>Yuca con Mojo")
              print("5>Tostones")
              print("6>Arroz con Pollo")
              print("7>Congri")
              print("8>Vaca Frita")
              print("9>Pan con Lechon")
              print("10>Medianoche")
              print("11>Flan")
              print("12>Churros")
              print("13>Maduros")
              print("14>Tamales")
              print("15>Ajiaco")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(500,50)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(180,18)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(250,25)
              elif ch1==8:
                    bill_info(450,45)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(350,35)
              elif ch1==11:
                    bill_info(220,22)
              elif ch1==12:
                    bill_info(150,15)
              elif ch1==13:
                    bill_info(180,18)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                     bill_info(450,45)
              else:
                    break

      elif ch==65:
              print(">>Enter The Dishes You Want>>")
              print("1>Mofongo")
              print("2>Arroz con Gandules")
              print("3>Pernil")
              print("4>Tostones")
              print("5>Alcapurrias")
              print("6>Pasteles")
              print("7>Bacalaitos")
              print("8>Asopao")
              print("9>Coquito")
              print("10>Tembleque")
              print("11>Empanadillas")
              print("12>Sancocho")
              print("13>Sorullitos")
              print("14>Tripleta")
              print("15>Flan de Queso")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(400,40)
              elif ch1==2:
                    bill_info(300,30)
              elif ch1==3:
                    bill_info(550,55)
              elif ch1==4:
                    bill_info(180,18)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(300,30)
              elif ch1==7:
                    bill_info(220,22)
              elif ch1==8:
                    bill_info(450,45)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(200,20)
              elif ch1==11:
                    bill_info(180,18)
              elif ch1==12:
                    bill_info(500,50)
              elif ch1==13:
                    bill_info(200,20)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(250,25)
              else:
                    break

      elif ch==66:
              print(">>Enter The Dishes You Want>>")
              print("1>Injera")
              print("2>Doro Wat")
              print("3>Misir Wat")
              print("4>Tibs")
              print("5>Shiro")
              print("6>Kitfo")
              print("7>Gomen")
              print("8>Ayib")
              print("9>Kik Alicha")
              print("10>Chechebsa")
              print("11>Genfo")
              print("12>Firfir")
              print("13>Tere Sega")
              print("14>Tej")
              print("15>Beso")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(150,15)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(400,40)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(500,50)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(300,30)
              elif ch1==10:
                    bill_info(350,35)
              elif ch1==11:
                    bill_info(280,28)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(450,45)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(150,15)
              else:
                    break

      elif ch==67:
              print(">>Enter The Dishes You Want>>")
              print("1>Moroccan Tagine")
              print("2>Couscous")
              print("3>Harira")
              print("4>Pastilla")
              print("5>Zaalouk")
              print("6>Rfissa")
              print("7>Mechoui")
              print("8>Khobz")
              print("9>Briouat")
              print("10>Makouda")
              print("11>Bissara")
              print("12>Chebakia")
              print("13>Mint Tea")
              print("14>Sardines Chermoula")
              print("15>Msemen")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(550,55)
              elif ch1==2:
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(500,50)
              elif ch1==5:
                    bill_info(280,28)
              elif ch1==6:
                    bill_info(450,45)
              elif ch1==7:
                    bill_info(800,80)
              elif ch1==8:
                    bill_info(100,10)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(200,20)
              elif ch1==12:
                    bill_info(180,18)
              elif ch1==13:
                    bill_info(120,12)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(200,20)
              else:
                    break

      elif ch==68:
              print(">>Enter The Dishes You Want>>")
              print("1>Tabbouleh")
              print("2>Fattoush")
              print("3>Kibbeh")
              print("4>Hummus")
              print("5>Baba Ghanoush")
              print("6>Shish Taouk")
              print("7>Shawarma")
              print("8>Falafel")
              print("9>Manakish")
              print("10>Kafta")
              print("11>Batata Harra")
              print("12>Warak Enab")
              print("13>Baklava")
              print("14>Knafeh")
              print("15>Arak")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(250,25)
              elif ch1==2:
                    bill_info(280,28)
              elif ch1==3:
                    bill_info(350,35)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(250,25)
              elif ch1==10:
                    bill_info(380,38)
              elif ch1==11:
                    bill_info(220,22)
              elif ch1==12:
                    bill_info(300,30)
              elif ch1==13:
                    bill_info(280,28)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(450,45)
              else:
                    break

      elif ch==69:
              print(">>Enter The Dishes You Want>>")
              print("1>Koshari")
              print("2>Ful Medames")
              print("3>Molokhia")
              print("4>Taameya")
              print("5>Hawawshi")
              print("6>Macarona Béchamel")
              print("7>Feseekh")
              print("8>Roz Bel Laban")
              print("9>Basbousa")
              print("10>Om Ali")
              print("11>Mahshi")
              print("12>Shawarma")
              print("13>Kofta")
              print("14>Bamia")
              print("15>Sayadiya")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::")) 
              if ch1==1:
                    bill_info(300,30)
              elif ch1==2:
                    bill_info(200,20)
              elif ch1==3:
                    bill_info(280,28)
              elif ch1==4:
                    bill_info(150,15)
              elif ch1==5:
                    bill_info(350,35)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(500,50)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(220,22)
              elif ch1==10:
                    bill_info(250,25)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(380,38)
              elif ch1==13:
                    bill_info(400,40)
              elif ch1==14:
                    bill_info(350,35)
              elif ch1==15:
                    bill_info(450,45)
              else:
                    break

      elif ch==70:
              print(">>Enter The Dishes You Want>>")
              print("1>Russian Borscht")
              print("2>Pelmeni")
              print("3>Blini")
              print("4>Beef Stroganoff")
              print("5>Olivier Salad")
              print("6>Syrniki")
              print("7>Pirozhki")
              print("8>Kvass")
              print("9>Kholodets")
              print("10>Solyanka")
              print("11>Varenyky")
              print("12>Shchi")
              print("13>Medovik")
              print("14>Okroshka")
              print("15>Golubtsy")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:                 
                    bill_info(400,40)
              elif ch1==3:
                    bill_info(250,25)
              elif ch1==4:
                    bill_info(550,55)
              elif ch1==5:
                    bill_info(300,30)
              elif ch1==6:
                    bill_info(280,28)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(150,15)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(380,38)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(280,28)
              elif ch1==13:
                    bill_info(320,32)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(350,35)
              else:
                    break

      elif ch==71:
              print(">>Enter The Dishes You Want>>")
              print("1>Khachapuri")
              print("2>Khinkali")
              print("3>Pkhali")
              print("4>Lobio")
              print("5>Satsivi")
              print("6>Churchkhela")
              print("7>Mtsvadi")
              print("8>Chakhokhbili")
              print("9>Ajapsandali")
              print("10>Badrijani Nigvzit")
              print("11>Tkemali")
              print("12>Sulguni")
              print("13>Shotis Puri")
              print("14>Chikhirtma")
              print("15>Kharcho")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(400,40)
              elif ch1==2:
                    bill_info(450,45)
              elif ch1==3:
                    bill_info(280,28)
              elif ch1==4:
                    bill_info(250,25)
              elif ch1==5:
                    bill_info(450,45)
              elif ch1==6:
                    bill_info(150,15)
              elif ch1==7:
                    bill_info(500,50)
              elif ch1==8:
                    bill_info(400,40)
              elif ch1==9:
                    bill_info(350,35)
              elif ch1==10:
                    bill_info(300,30)
              elif ch1==11:
                    bill_info(180,18)
              elif ch1==12:
                    bill_info(250,25)
              elif ch1==13:
                    bill_info(100,10)
              elif ch1==14:
                    bill_info(380,38)
              elif ch1==15:
                    bill_info(450,45)
              else:
                    break

      elif ch==72:
              print(">>Enter The Dishes You Want>>")
              print("1>Nigerian Jollof Rice")
              print("2>Pounded Yam")
              print("3>Egusi Soup")
              print("4>Suya")
              print("5>Akara")
              print("6>Moi Moi")
              print("7>Pepper Soup")
              print("8>Efo Riro")
              print("9>Afang Soup")
              print("10>Nkwobi")
              print("11>Boli")
              print("12>Zobo")
              print("13>Ogbono Soup")
              print("14>Asaro")
              print("15>Chin Chin")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(350,35)
              elif ch1==2:
                    bill_info(250,25)
              elif ch1==3:
                    bill_info(450,45)
              elif ch1==4:
                    bill_info(200,20)
              elif ch1==5:
                    bill_info(150,15)
              elif ch1==6:
                    bill_info(180,18)
              elif ch1==7:
                    bill_info(350,35)
              elif ch1==8:
                    bill_info(400,40)
              elif ch1==9:
                    bill_info(450,45)
              elif ch1==10:
                    bill_info(500,50)
              elif ch1==11:
                    bill_info(150,15)
              elif ch1==12:
                    bill_info(120,12)
              elif ch1==13:
                    bill_info(400,40)
              elif ch1==14:
                    bill_info(250,25)
              elif ch1==15:
                    bill_info(100,10)
              else:
                    break

      elif ch==73:
              print(">>Enter The Dishes You Want>>")
              print("1>South African Biltong")
              print("2>Boerewors")
              print("3>Bunny Chow")
              print("4>Bobotie")
              print("5>Malva Pudding")
              print("6>Potjiekos")
              print("7>Melktert")
              print("8>Chakalaka")
              print("9>Pap")
              print("10>Vetkoek")
              print("11>Sosatie")
              print("12>Koeksister")
              print("13>Gatsby")
              print("14>Snoek")
              print("15>Amarula")
              print("16>Go Back")
              ch1=int(input("Enter Your choice::"))
              if ch1==1:
                    bill_info(450,45)
              elif ch1==2:
                    bill_info(350,35)
              elif ch1==3:
                    bill_info(300,30)
              elif ch1==4:
                    bill_info(380,38)
              elif ch1==5:
                    bill_info(250,25)
              elif ch1==6:
                    bill_info(400,40)
              elif ch1==7:
                    bill_info(200,20)
              elif ch1==8:
                    bill_info(180,18)
              elif ch1==9:
                    bill_info(150,15)
              elif ch1==10:
                    bill_info(150,15)
              elif ch1==11:
                    bill_info(350,35)
              elif ch1==12:
                    bill_info(180,18)
              elif ch1==13:
                    bill_info(500,50)
              elif ch1==14:
                    bill_info(450,45)
              elif ch1==15:
                    bill_info(600,60)
              else:
                    break              
      else:
          continue
      print("**Mode of Payment Please**::")
      print("   1>>UPI(Gpay,paytm)")
      print("   2>>Credit Card")
      print("   3>>Cash Only")
      pay=int(input("   Enter your choice[1,2,3]::"))
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
  
