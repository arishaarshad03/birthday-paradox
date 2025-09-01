from birthdayParadox import BirthdayParadox

def main():
    try:
        
         # Example runs
        bp1 = BirthdayParadox(group_size=50, simulations=100)
        print(bp1)
        bp1.show_probability()

        bp2 = BirthdayParadox()
        print(bp2)
        bp2.show_probability()

        bp3 = BirthdayParadox(bp2)
        print(bp3)
        bp3.show_probability()

        bp4 = BirthdayParadox(group_size=0, simulations=20)     #raising error here and stoping everything after from executing
        print(bp4)
        bp4.show_probability()



    except Exception as e:
        print(f"error:{e}")

if __name__ == "__main__":
    main()