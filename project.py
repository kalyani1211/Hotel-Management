class hotel:
      def __init__(s,r=0,name='',address=''):
        print("\n\nwelcome to StarA\n")
        s.r=r
        s.name=name
        s.address=address
      def inputdata(s):
        s.name=input("enter your name:")
        s.address=input("enter your address")
    
      def vegmenu(s):
         print("1.roti-------------------------->20")
         print("2.rice-------------------------->30")
         print("3.paneer handi------------------>90")
         print("4.kaju masala-------------------->110")
         print("5.palak paneer---------------------->150")
      def nonvegMenu(s):
         print("1.chicken chilli-------------------------->20")
         print("2.chicken handi-------------------------->30")
         print("3.chicken lolipop------------------>90")
         print("4.chicken masala-------------------->110")
         print("5.chicken biryani---------------------->150")
      def menu(s):
        print("1.veg \n 2.nonoveg \n 0 exit")
        i=int(input("enter your choice"))
        while i!=0:
            if i==1:
                s.vegmenu()
                print("***************veg menu*****************")
                sel=int(input())
                while(sel==1):
                  c=int(input("enter your choice:"))
                  if(c==1):
                    d=int(input("enter the quantity:"))
                    s.r=s.r+20*d
                  elif(c==2):
                    d=int(input("enter quantity:"))
                    s.r= s.r+10*d
                  elif(c==3):
                    d=int(input("enter quantity:"))
                    s.r= s.r+90*d
                  elif(c==4):
                    d=int(input("enter quantity:"))
                    s.r= s.r+110*d
                  elif(c==5):
                    d=int(input("enter quantity:"))
                    s.r= s.r+150*d
                  elif(c==6):
                    break;
                print("total food cost=Rs",s.r)
            elif i==2:
                    s.nonvegMenu()
                    print("***************Nonveg menu*****************")
                    sel=int(input())
                    while(sel==1):
                       c=int(input("enter your choice:"))
                       if(c==1):
                         d=int(input("enter the quantity:"))
                         s.r=s.r+20*d
                       elif(c==2):
                         d=int(input("enter quantity:"))
                         s.r= s.r+10*d
                       elif(c==3):
                          d=int(input("enter quantity:"))
                          s.r= s.r+90*d
                       elif(c==4):
                          d=int(input("enter quantity:"))
                          s.r= s.r+110*d
                       elif(c==5):
                         d=int(input("enter quantity:"))
                         s.r= s.r+150*d
                       elif(c==6):
                          break;
                    print("total food cost=Rs",s.r)
            else:
                print("please select correct option")
                i=0   
         
            
                
    
      
h=hotel()
h.inputdata()
h.menu()
