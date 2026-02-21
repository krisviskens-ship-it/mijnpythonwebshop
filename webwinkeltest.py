import os

# 1. Artikelen in onze webwinkel
artikelen = {
    1: {"naam": "Laptop", "prijs": 999.00, "voorraad": 5},
    2: {"naam": "Muis", "prijs": 25.50, "voorraad": 15},
    3: {"naam": "Toetsenbord", "prijs": 49.95, "voorraad": 10},
    4: {"naam": "Monitor", "prijs": 199.00, "voorraad": 8},
    5: {"naam": "Headset", "prijs": 79.00, "voorraad": 12}
}

winkelmandje = []

def toon_dashboard():
    print("\n" + "="*30)
    print("      MIJN PYTHON SHOP")
    print("="*30)
    print(f"{'ID':<4} {'Artikel':<15} {'Prijs':<10} {'Voorraad'}")
    print("-"*30)
    for id, info in artikelen.items():
        print(f"{id:<4} {info['naam']:<15} €{info['prijs']:>7.2f}  {info['voorraad']:>8}")
    print("-"*30)
    print(f"Items in mandje: {len(winkelmandje)}")
    print("="*30)

def main():
    while True:
        toon_dashboard()
        print("\nOpties: [ID] Koop artikel | [W] Winkelmand bekijken | [Q] Afsluiten")
        keuze = input("Wat wilt u doen? ").lower()

        if keuze == 'q':
            print("Bedankt voor het winkelen! Tot ziens.")
            break
        
        elif keuze == 'w':
            if not winkelmandje:
                print("\nJe winkelmandje is nog leeg!")
            else:
                totaal = sum(item['prijs'] for item in winkelmandje)
                print("\n--- JOUW WINKELMANDJE ---")
                for item in winkelmandje:
                    print(f"- {item['naam']}: €{item['prijs']:.2f}")
                print(f"TOTAAL: €{totaal:.2f}")
            input("\nDruk op Enter om verder te gaan...")

        elif keuze.isdigit():
            id = int(keuze)
            if id in artikelen:
                if artikelen[id]['voorraad'] > 0:
                    artikelen[id]['voorraad'] -= 1
                    winkelmandje.append(artikelen[id])
                    print(f"\n✅ {artikelen[id]['naam']} toegevoegd!")
                else:
                    print("\n❌ Helaas, dit artikel is uitverkocht.")
            else:
                print("\n❌ Ongeldig ID.")
        else:
            print("\n❌ Ongeldige invoer.")

if __name__ == "__main__":
    main()
