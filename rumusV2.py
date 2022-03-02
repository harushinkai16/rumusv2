#rumus luas benda
def luas(x,y):
  return x*x

#rumus luas segitiga
def segitiga(x,y,z):
  return x*y*z

#rumus luas trapesium
def trapesium(x,y,z):
    return x+y/2*z

#rumus luas lingkaran
def ling1(x):
    return 22/7*x*x

def ling2(x):
    return 3.14*x*x

#luas persegi
def l_persegi():
  sisi = float(input("sisi :"))
  print("luas yang di cari adalah :",luas(sisi))
  print("ketik y/n untuk melanjutkan :")
  print("atau ketik r untuk mencoba lagi :")
  pilih = input("input :")
  if pilih == "y":
    pilihan()
  elif pilih == "n":
    print("program finish")
  elif pilih == "r":
    l_persegi()
    

#luas jajar genjang
def jj_gen():
  alas = float(input("alas :"))
  tinggi = float(input("tinggi :"))
  print("luas yang di cari adalah :",luas(alas,tinggi))
  print("ketik y/n untuk melanjutkan :")
  print("atau ketik r untuk mencoba lagi :")
  pilih = input("input :")
  if pilih == "y":
    pilihan()
  elif pilih == "n":
    print("program finish")
  elif pilih == "r":
    jj_gen()



#luas persegi panjang
def l_per_pan():
  panjang = float(input("panjang :"))
  lebar = float(input("lebar :"))
  print("luas yang di cari adalah :",luas(panjang,lebar))
  print("ketik y/n untuk melanjutkan :")
  print("atau ketik r untuk mencoba lagi :")
  pilih = input("input :")
  if pilih == "y":
    pilihan()
  elif pilih == "n":
    print("program finish")
  elif pilih == "r":
    l_per_pan()
    
#luas segitiga
def luassegitiga():
    rumus = 1/2
    alas = float(input("alas :"))
    tinggi = float(input("tinggi :"))
    print("luas yang dicari :",segitiga(rumus,alas,tinggi))
    print("ketik y/n untuk melanjutkan :")
    print("atau ketik r untuk mencoba lagi :")
    pilih = input("input :")
    if pilih == "y":
        h
        pilihan()
    elif pilih == "n":
        print("program finish")
    elif pilih == "r":
        luassegitiga()
    
#luas belah ketupat
def l_belahket():
    rumus = 1/2
    d1 = float(input("diagonal 1 :"))
    d2 = float(input("diagonal 2 :"))
    print("luas yang di cari",segitiga(rumus,d1,d2))
    print("ketik y/n untuk melanjutkan :")
    print("atau ketik r untuk mencoba lagi :")
    pilih = input("input :")
    if pilih == "y":
        pilihan()
    elif pilih == "n":
        print("program finish")
    elif pilih == "r":
        l_belahket()
        
#rumus  layang-layang     
def l_layang():
    rumus = 1/2
    d1 = float(input("diagonal 1 :"))
    d2 = float(input("diagonal 2 :"))
    print("luas yang di cari",segitiga(rumus,d1,d2))
    print("ketik y/n untuk melanjutkan :")
    print("atau ketik r untuk mencoba lagi :")
    pilih = input("input :")
    if pilih == "y":
        pilihan()
    elif pilih == "n":
        print("program finish")
    elif pilih == "r":
        l_layang()

#rumus trapesium
def l_trapesium ():
    a = float(input("nilai a :"))
    b = float(input("nilai b :"))
    t = float(input("nilai t :"))
    print("luas yang di cari :",trapesium(a,b,t))
    print("ketik y/n intuk melanjutkan ")
    print("atau ketik r untuk mencoba lagi :")
    pilih = input("input :")
    if pilih == "y":
        pilihan()
    elif pilih == "n":
        print("program finish")
    elif pilih == "r":
     l_trapesium
     
#rumus lingkaran 22/7
def l_lingkaran1():
    r = float(input("masukkan nilai r :"))
    print("luas yang di cari :",ling1(r))

#rumus lingkaran 3.14
def l_lingkaran2():
    r = float(input("masukkan nilai r :"))
    print("luas yang di cari :",ling2(r))


#menu rumus luas benda
def pilihan():
  print("pilih sesuai menu di bawah")
  print("==========================")
  print("{+}~1. luas persegi")
  print("{+}~2. luas persegi panjang")
  print("{+}~3. luas jajar genjang")
  print("{+}~4. luas segitiga")
  print("{+}~5. luas belah ketupat")
  print("{+}~6. luas layang-layang")
  print("{+}~7. luas trapesium")
  print("{+}~8. luas lingkaran")
  print("==========================")
  
  pilih = input("pilih :")
  
  if pilih == '1':
    print("luas persegi =")
    print("sisi X sisi")
    l_persegi()
    
  elif pilih == '2':
    print("luas persegi panjang")
    print("panjang X lebar")
    l_per_pan()
    
  elif pilih == '3':
    print("luas jajar genjang")
    print("alas X tinggi")
    jj_gen()
    
  elif pilih == '4':
    print("luas segitiga")
    print("1/2 X alas X tinggi")
    luassegitiga()
    
  elif pilih == '5':
    print("luas belah ketupat")
    print("1/2 X d1 X d2")
    l_belahket()
    
  elif pilih == '6':
    print("luas layang-layang")
    print("1/2 X d1 X d2")
    l_layang()
    
  elif pilih == '7':
      print("luas trapesium")
      print("a + b / 2 X t")
      l_trapesium()
      
  elif pilih == '8':
      print("luas lingkaran")
      print("pilih rumus")
      print("1. menggunakan 22/7")
      print("2. menggunakan 3.14")
      pilih = input("pilih :")
      if pilih == '1':
          print("rumus = 22/7 X r²")
          l_lingkaran1()
      elif pilih == '2':
          print("rumus = 3.14 X r²")
          l_lingkaran2()
          
          
          
#rumus keliling benda
def m_keliling():
      print("pilih sesuai menu di bawah")
      print("======================") 
      print("{+}1. keliling persegi")
      print("{+}2. keliling persegi panjang")
      print("{+}3. keliling")
      print("{+}4. keliling")
      print("{+}5. keliling")
      print("{+}6. keliling")
      print("{+}7. keliling")
      print("{+}8. keliling")
      
                        
#menu matematika
def r_matematika():
    print("{+}1. rumus luas benda")
    print("{+}2. rumus keliling benda")
    pilih = input("pilih :")
    if pilih == '1':
        pilihan()
    elif pilih == '2':
        m_keliling()
    



#menu pilihan
def menu():
    print("=====================")
    print("~~~KALKULATOR RUMUS~~~")
    print("    ALPHA VERSION")
    print("________2.0_________")
    print("")
    print("")
    print("MENU PILIHAN")
    print("1. rumus matematika")
    print("2. rumus fisika")
    pilih = input("pilih nomor :")
    
    if pilih == '1':
        r_matematika()
    elif pilih == '2':
        print("next project 🙏")
        menu()

menu()