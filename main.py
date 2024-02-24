def calc(x, y, islem):
    # İşlem operatörü kontrolü
    if islem not in '+-/*':
        return 'Choose operator: +, -, *, /!'
    # Toplama işlemi
    if islem == '+':
        return str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x + y)
    # Çıkarma işlemi
    if islem == '-':
        return str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x - y)
    # Çarpma işlemi
    if islem == '*':
        return str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x * y)
    # Bölme işlemi
    if islem == '/':
        return str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x / y)
# Kullanıcıdan sürekli giriş alınması
while True:
    # İşlem ifadesinin girilmesi
    expr = input('Lütfen yapmak istediğiniz işlemi giriniz: ')
    # Boşlukların temizlenmesi
    expr = expr.replace(" ", "")
    try:
        # İşlemin hesaplanması
        result = eval(expr)
        # Sonucun ekrana yazdırılması
        print(expr, "=", result)
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        # Hata durumunda kullanıcıya hata mesajının gösterilmesi
        print("Bir hata oluştu. Lütfen tekrar deneyiniz.")

