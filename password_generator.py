import secrets
import string

def generate_password(length=12, use_symbols=True, use_digits=True):
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("أدخل طول كلمة المرور: "))
    use_symbols = input("هل تريد تضمين الرموز الخاصة؟ (نعم/لا): ").strip().lower() == "نعم"
    use_digits = input("هل تريد تضمين الأرقام؟ (نعم/لا): ").strip().lower() == "نعم"
    
    password = generate_password(length, use_symbols, use_digits)
    print("🔑 كلمة المرور التي تم إنشاؤها:", password)
