import temp_converter

while True:
    while True:
        try:
            temp = float(input("Enter the current temperature: "))
            break
        except ValueError:
            print("Big bruh moment...")
    while True:
        scale = input("To convert to, use (C) for celsius or (F) for fahrenheit: ").capitalize()

        if scale == "C":
            Celsius = temp_converter.f_to_c(temp)
            print(str(temp) + " degrees Fahrenheit is: " + str(Celsius) + " degrees Celsius")
            break
        elif scale == "F":
            fahrenheit = temp_converter.c_to_f(temp)
            print(str(temp) + " degrees Celsius is: " + str(fahrenheit) + " degrees Fahrenheit")
            break
        else:
            print("Invalid input! Follow the prompt!")

    while True:
        convert_again = input("Do you wanna convert again (yes/no)?: ").lower()

        if convert_again == "no":
            print("Goodbye for good!")
            break
        elif convert_again == "yes":
            print("Ok, here we go again.")
            break
        else:
            print("You couldn't help yourself? Could you?")

    if convert_again == "no":
        break
