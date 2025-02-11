balance = 10000  # Bilanci fillestar

while True:
    print("\n1. Trego Balancën")
    print("2. Tërhiq Para")
    print("3. Depozito")
    print("4. Dalje")
    
    choice = input("Zgjidhni një opsion: ")
    
    if choice == "1":
        print(f"Bilanci juaj është: {balance} ALL")
    elif choice == "2":
        amount = int(input("Shkruani shumën që dëshironi të tërhiqni: "))
        if amount > balance:
            print("Fondet e pamjaftueshme!")
        else:
            balance -= amount
            print(f"Keni tërhequr {amount} ALL. Bilanci i ri: {balance} ALL")
    elif choice == "3":
        amount = int(input("Shkruani shumën që dëshironi të depozitoni: "))
        balance += amount
        print(f"Keni depozituar {amount} ALL. Bilanci i ri: {balance} ALL")
    elif choice == "4":
        print("Faleminderit që përdorët ATM-në!\n")
        break
    else:
        print("Opsion i pavlefshëm, provoni përsëri!")
