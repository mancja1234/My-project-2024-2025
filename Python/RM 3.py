
# Funksioni për llogaritjen e faktorialit duke përdorur rekursionin
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Funksioni për gjenerimin e serisë Fibonacci deri në n-terme duke përdorur rekursionin
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Funksioni për llogaritjen e shumës së listës
def sum_list(numbers):
    return sum(numbers)

# Funksioni për llogaritjen e mesatares së listës
def average_list(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Funksioni për renditjen e numrave në listë
def sort_numbers(numbers):
    return sorted(numbers)

# Funksioni për validimin e hyrjes së përdoruesit
def validate_input(prompt, type_func=int):
    while True:
        try:
            value = type_func(input(prompt))
            return value
        except ValueError:
            print("Hyrje e pavlefshme. Provoni përsëri.")

# Menu interaktive
def main_menu():
    print("\nMirë se vini në Math Helper!")
    print("Zgjidhni një opsion:")
    print("1. Llogarit Faktorialin")
    print("2. Gjenero Serinë Fibonacci")
    print("3. Llogarit Shumën e Listës")
    print("4. Llogarit Mesataren e Listës")
    print("5. Rendit Listën")
    print("6. Dalje")

    choice = validate_input("Zgjidhni opsionin: ")

    if choice == 1:
        n = validate_input("Vendosni një numër për faktorialin: ")
        print(f"Faktoriali i {n} është {factorial(n)}")
    elif choice == 2:
        n = validate_input("Vendosni numrin e termeve të serisë Fibonacci: ")
        print(f"Seria Fibonacci deri në {n}-terme: {fibonacci(n)}")
    elif choice == 3:
        numbers = list(map(int, input("Vendosni numrat në listë (ndarë me hapësirë): ").split()))
        print(f"Shuma e listës është: {sum_list(numbers)}")
    elif choice == 4:
        numbers = list(map(int, input("Vendosni numrat në listë (ndarë me hapësirë): ").split()))
        print(f"Mesatarja e listës është: {average_list(numbers)}")
    elif choice == 5:
        numbers = list(map(int, input("Vendosni numrat në listë (ndarë me hapësirë): ").split()))
        print(f"Lista e renditur: {sort_numbers(numbers)}")
    elif choice == 6:
        print("Duke dalë nga Math Helper. Mirupafshim!")
        return
    else:
        print("Opsion i pavlefshëm. Provoni përsëri.")

    main_menu()  # Rikthimi në menu pas çdo operacioni

# Ekzekutimi i aplikacionit
if _name_ == "_main_":
    main_menu()




































