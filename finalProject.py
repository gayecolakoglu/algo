import sqlite3
#DATABASE CONNECTION
conn = sqlite3.connect('rehberSistemi.db')
c = conn.cursor()
#command = "CREATE TABLE rehber (name text, phone text, email text, city text)"
#c.execute(command)

#Class for Person
class Person:
    def __init__(self, name):
        self.name = name
        self.phone_num = "";
        self.email = "";
        self.city = "";
    def setPhone(self, phone):
        self.phone_num = phone
    def setEmail(self, email):
        self.email = email
    def setCity(self, city):
        self.city = city
    def getPhone(self):
        return self.phone_num
    def getEmail(self):
        return self.email
    def getCity(self):
        return self.city
    def getName(self):
        return self.name


def exit():
    print("******GÜN SONU RAPORU*******")
    print("Bugün rehbere eklediğiniz kişiler aşağıdaki gibidir:")
    for k in direc_dict.keys():
        print(k)
    print("Çıkış yapılıyor ...")


def displayContacts():
    print("Kişiler sıralanıyor...")
    for k in direc_dict.keys():
        print(k)

def throwException():
    raise Exception("Error")

direc_dict={}
x = 1
y = 0


while x == 1 or y == 4:
    special_information_dict={}
    person = input("Lütfen rehbere eklemek istediğiniz kişinin isim ve soyismini giriniz:")
    if person not in direc_dict.keys():
        x = 4
        #crate a Person instance
        contact_person = Person(person)
        while x == 4:
            try:
                phone_num=int(input("Lütfen kişinin telefon numarasını giriniz(5XXXXXXXXX):"))
                phone_num = str(phone_num)
                contact_person.setPhone(phone_num)
                #Eğer telefon numarası 5 ile başlamıyorsa ve 10 haneli değilse throw exception
                if(phone_num[0] != "5" or len(phone_num) != 10):
                    throwException()
            except:
                print("Lütfen telefon numarasını doğru girdiğinizden emin olunuz....")
                continue

            eMail = input("Lütfen kişinin e-mail adresini giriniz:")
            contact_person.setEmail(eMail)


            cityInfromation=input("Lütfen kişinin şehir bilgisini giriniz:")
            contact_person.setCity(cityInfromation)
            x = int(input("Yeni kişi eklemek için 1, kişi listesini görmek için 2 ve çıkış yapmak için 3 tıklayınız:"))


        special_information_dict["telefon numarası"] = contact_person.getPhone()
        special_information_dict["e-mail"] = contact_person.getEmail()
        special_information_dict["şehir"] = contact_person.getCity()

        #Database'e kaydet
        command = "INSERT INTO rehber VALUES ('{}', '{}', '{}', '{}')".format(
            person, contact_person.getPhone(), contact_person.getEmail(),
            contact_person.getCity())
        c.execute(command)


        direc_dict[person]=special_information_dict
    else:
        print("Kişi rehberde mevcut!")
    if x == 3:
        exit()
        break
    elif x == 2:
        y = 2
        while y == 2:
            try:
                displayContacts()
                isim = input("Lütfen bilgilerini öğrenmek istediğiniz kişinin isim ve soyismini rehberdeki gibi giriniz, çıkış için 'çıkış':")
                if isim == "çıkış":
                    exit()
                    break
                if isim not in direc_dict:
                    throwException()
                y = 1
            except:
                print("Bu isim rehberde mevcut değil, tekrar deneyiniz.")
                continue


            while y == 1:
                try:
                    m = input("Kişinin telefon numarası için 'telefon numarası', e-mail için 'e-mail', şehir bilgisi için 'şehir', tüm bilgiler için 'hepsi' yazınız:")
                    print(m)
                    if(m == "telefon numarası" or m == "e-mail" or m == "şehir" or m == "hepsi"):
                        if m == "telefon numarası":
                            print(isim,"isimli kişinin telefon numarası =>", direc_dict[isim][m])
                        elif m == "e-mail":
                            print(isim, "isimli kişinin e-postası =>", direc_dict[isim][m])
                        elif m == "şehir":
                            print(isim, "isimli kişinin bulunduğu şehir =>", direc_dict[isim][m])
                        elif m == "hepsi":
                            print(isim, "isimli kişinin bilgileri", direc_dict[isim])
                    else:
                        throwException()
                except:
                    print("Yanlış bilgi girdiniz, lütfen tekrar deneyiniz.")
                    continue
                y=int(input("Aynı kişinin farklı bilgilerine erişmek için 1, yeni kişiye geçiş yapmak için 2, çıkış için 3 ve rehbere yeni kişi eklemek için 4 tıklayınız:"))
        if y == 3:
            exit()


print("******** DATABASE'DEN rehber TABLOSUNDAKİ TÜM BİLGİLER ÇEKİLİYOR ********")
c.execute("SELECT * FROM rehber")
conn.commit()
print(c.fetchall())
conn.close()