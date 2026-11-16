# calculator
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطأ: لا يمكن القسمة على صفر!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "خطأ: لا يوجد جذر تربيعي حقيقي لعدد سالب!"
    return math.sqrt(x)

def percentage(percent, total):
    return (percent / 100) * total

def format_num(n):
    if isinstance(n, float):
        if n.is_integer():
            return int(n)
        return round(n, 4)
    return n

def main():
    while True:
        print("\n--- الآلة الحاسبة المتقدمة ---")
        print("1. جمع (+)")
        print("2. طرح (-)")
        print("3. ضرب (*)")
        print("4. قسمة (/)")
        print("5. الأسس (^)")
        print("6. الجذر التربيعي (√)")
        print("7. النسبة المئوية (%)")
        print("8. خروج")

        choice = input("اختر رقم العملية (1-8): ")
        print()

        if choice == '8':
            print("تم إغلاق الآلة الحاسبة. شكراً لاستخدامك!")
            break

        if choice == '6':
            try:
                num = float(input("أدخل الرقم لحساب جذره: "))
                print()
            except ValueError:
                print("خطأ: يرجى إدخال رقم صحيح!\n")
                continue

            n = format_num(num)
            res = format_num(square_root(num))
            print(f"النتيجة: √{n} = {res}\n")

        elif choice in ('1', '2', '3', '4', '5', '7'):
            try:
                if choice == '5':
                    num1 = float(input("أدخل الأساس (الرقم): "))
                    num2 = float(input("أدخل الأس (القوة): "))
                elif choice == '7':
                    num1 = float(input("أدخل النسبة المئوية (مثلاً 15): "))
                    num2 = float(input("أدخل العدد الكلي: "))
                else:
                    num1 = float(input("أدخل الرقم الأول: "))
                    num2 = float(input("أدخل الرقم الثاني: "))
                print()
            except ValueError:
                print("خطأ: يرجى إدخال أرقام صحيحة فقط!\n")
                continue

            n1 = format_num(num1)
            n2 = format_num(num2)

            if choice == '1':
                print(f"النتيجة: {n1} + {n2} = {format_num(add(num1, num2))}\n")
            elif choice == '2':
                print(f"النتيجة: {n1} - {n2} = {format_num(subtract(num1, num2))}\n")
            elif choice == '3':
                print(f"النتيجة: {n1} * {n2} = {format_num(multiply(num1, num2))}\n")
            elif choice == '4':
                print(f"النتيجة: {n1} / {n2} = {format_num(divide(num1, num2))}\n")
            elif choice == '5':
                print(f"النتيجة: {n1} ^ {n2} = {format_num(power(num1, num2))}\n")
            elif choice == '7':
                print(f"النتيجة: {n1}% من {n2} = {format_num(percentage(num1, num2))}\n")
        else:
            print("خيار غير صالح، يرجى اختيار رقم من 1 إلى 8.\n")

if __name__ == "__main__":
    main()
