#tela_inicio_yes_e_pergunta_1

print("To properly carry out the following program,\n"
      "you will need to answer 'yes' or 'no'\n"
      "according to the question below."
      "\n")

start = input("To start the program write 'yes': ")
if start == "yes":
      sp1 = input("\n"
      "1. Do you believe that the state is\n"
      "the only one that can provide 'essential'\n"
      "services like roads, hospitals or security?: ")

      # Perguntas_yes1

      if sp1 != "yes":
            print("\n"
                  "So you agree that people would pay for it voluntarily, great!")
      if sp1 == "yes":
            sp2 = input("\n"
                        "Do you believe that any of these services is essential? ")
            if sp2 != "yes":
                  print("\n"
                        "The state should not spend money on things that are not important.")
            if sp2 == "yes":
                  sp3 = input("\n"
                              "Would you be willing to pay, even if you were not forced? ")
                  if sp3 == "yes":
                        print("\n"
                              "So you agree that people would pay for it voluntarily!")
                  if sp3 != "yes":
                        print("\n"
                              "Do you really think these services are essential? Think about it and start again!")



#tela_inicio_no_e_pergunta_1
while start != "yes":
      sn = input("To start the program write 'yes': ")
      if sn == "yes":
            sn1 = input("\n"
                        "1. Do you believe that the state is\n"
                        "the only one that can provide 'essential'\n"
                        "services like roads, hospitals or security?: ")

            # Perguntas_yes2

            if sn1 != "yes":
                  print("\n"
                        "So you agree that people would pay for it voluntarily, great!")
            if sn1 == "yes":
                  sn2 = input("\n"
                              "Do you believe that any of these services is essential? ")
                  if sn2 != "yes":
                        print("\n"
                              "The state should not spend money on things that are not important.")
                  if sn2 == "yes":
                        sn3 = input("\n"
                                    "Would you be willing to pay, even if you were not forced? ")
                        if sn3 != "yes":
                              print("\n"
                                    "Do you really think these services are essential? Think about it and start again!")
                        if sn3 == "yes":
                              print("\n"
                                    "So you agree that people would pay for it voluntarily!")
      break

