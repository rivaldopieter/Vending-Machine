def apakah_user_lanjut(jawab) :
    kemungkinan_jawaban = ["Y", "y", "T", "t"]
    if jawab not in kemungkinan_jawaban:
        print("Silahkan Tekan tombol 'Y' untuk melanjutkan dan 'T' untuk berhenti\n")
        return apakah_user_lanjut()
    else:
        if jawab == "y" or jawab == "Y":
            return True
        else:
            return False


def modulo_bil_positif(x,y) :
    sisa_bagi = 0
    while x >= 0 :
        if x < y:
            return sisa_bagi
        if x >= y :
            x = x-y
        sisa_bagi = x
    else :
        return sisa_bagi


def memastikan_kelipatan (nilai) :
    if nilai >= 10_000 and modulo_bil_positif(nilai,10000) == 0  :
        return True
    else :
        return False


def hitung_kembalian_spesifik (user_money, stock ,nominal) :
    jumlah_lembar = 0
    while user_money >= nominal and stock > 0:
        user_money = user_money - nominal
        stock = stock-1
        jumlah_lembar = jumlah_lembar + 1
    return (user_money, stock, jumlah_lembar)


def hitung_kembalian_umum(user_money, stock, nominal) :
    lembar = []
    stock_temp = []
    for x in range (0,len(nominal)) :
        (user_money, stock_sementara, jumlah_lembar) = hitung_kembalian_spesifik(user_money, stock[x], nominal[x])
        lembar.append(jumlah_lembar)
        stock_temp.append(stock_sementara)
    return (lembar, stock_temp)


def total_kembalian (nominal,jumlah_lembar) :
    total_kembalian = 0
    for x in range (0, len(nominal)) :
        total_kembalian = total_kembalian + (nominal[x]*jumlah_lembar[x])
    return total_kembalian


def check_stock (total_kembalian, user_money) :
    if total_kembalian == user_money :
        return True
    else :
        return False


def update_stock(nominal, stock, stock_temp):
    for x in range (0, len(stock)) :
        stock[x] = stock_temp[x]
    rewrite_file(nominal, stock)


def print_kembalian (nominal, jumlah_lembar) :
    for x in range (0, len(nominal)) :
        if jumlah_lembar[x] !=0 :
            print (nominal[x], ':', jumlah_lembar [x] )


def print_stock(nominal,stock):
    print ("\nStock tersedia")
    for x in range (0, len(nominal)):
        print (nominal[x], ':', stock[x])


def read_file() :
    money_stock = {}
    with open('money_stock.txt', 'r') as d:
        for line in d :
            (key,value) = line.split(":")
            money_stock[int(key)] = int(value)
    return money_stock


def rewrite_file (nominal, stock):
    database = open('money_stock.txt', 'w')
    text = ""
    for i in range (len(nominal)-1):
        text = text  + str(nominal[i]) + ":" + str(stock[i]) + '\n'
    text = text + str(nominal[len(nominal)-1]) + ":" + str(stock[len(stock)-1])
    database.write(text)


def list_nominal (money_stock) :
    nominal = sorted(money_stock, reverse=True)
    return nominal


def list_stock (money_stock, nominal) :
    stock = []
    for x in (nominal) :
        stock.append(money_stock[x])
    return (stock)




def main():
    money_stock = read_file()
    nominal = list_nominal(money_stock)
    stock = list_stock(money_stock, nominal)

    jawab = str(input("\nApakah anda ingin melanjutkan? [Y/T] "))
    lanjut = apakah_user_lanjut(jawab)

    while lanjut == True :

        user_money = int(input("\nMasukkan Uang kelipatan 10 rb"))


        if memastikan_kelipatan(user_money) == False :
            break

        (jumlah_lembar, stock_temp) = hitung_kembalian_umum(user_money,stock,nominal)

        kembalian = total_kembalian(nominal, jumlah_lembar)

        is_enough = check_stock(kembalian, user_money)

        if is_enough == True :
            update_stock(nominal, stock, stock_temp)
            print_kembalian(nominal, jumlah_lembar)
            print_stock (nominal,stock)
        else :
            print("Maaf, Stock uang tidak cukup\n")

        jawab = str(input("\nApakah anda ingin melanjutkan? [Y/T] "))
        lanjut = apakah_user_lanjut(jawab)


    print ("Terima Kasih telah menggunakan aplikasi Kami")





#test
def test_lanjut_1 () :
    expected = True
    result = apakah_user_lanjut('y')
    assert result == expected, "Kesalahan pada pertanyaan melanjutkan"

def test_lanjut_2 () :
    expected = False
    result = apakah_user_lanjut('t')
    assert result == expected, 'Kesalahan pada pertanyaan melanjutkan'

def test_modulo_bil_positif () :
    expected = 1
    result = modulo_bil_positif(7,3)
    assert result == expected , "Kesalahan pada modulo bilangan positif"

def test_memastikan_kelipatan_bukan_negatif_1 () :
    expected = True
    result = memastikan_kelipatan(230_000)
    assert result == expected, "Kesalah pada memastikan kelipatan"

def test_memastikan_kelipatan_bukan_negatif_2 () :
    expected = False
    result = memastikan_kelipatan(0)
    assert result == expected, "Kesalahan pada memastikan kelipatan"


def test_hitung_kembalian_umum () :
    user_money = 130_000
    nominal = [50_000, 20_000, 10_000]
    stock = [3, 4, 7]
    expected = ([2, 1, 1],[1,3,6])
    result = hitung_kembalian_umum(user_money, stock, nominal)
    assert result == expected, "Kesalahan pada menghitung kembalian"


def test_total_kembalian () :
    nominal = [50_000, 20_000, 10_000]
    jumlah_lembar = [0, 0, 4]
    expected = 40_000
    result = total_kembalian(nominal, jumlah_lembar)
    assert result == expected, "Kesalahan pada menghitung total kembalian"


def test_check_stock () :
    total_kembalian = 40_000
    user_money = 130_000
    expected = False
    result =  check_stock(total_kembalian, user_money)
    assert result == expected, "Kesalahan pada check stock"


def test_all () :
    test_lanjut_1()
    test_lanjut_2()
    test_modulo_bil_positif()
    test_memastikan_kelipatan_bukan_negatif_1()
    test_memastikan_kelipatan_bukan_negatif_2()
    test_hitung_kembalian_umum()
    test_total_kembalian ()
    test_check_stock()

main()
test_all ()