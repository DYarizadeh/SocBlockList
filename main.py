secret1 = input("Enter password: ")
secret = "123"
addanother = 1

if secret1 == secret:
    print("Hello, welcome to the EDL for SOC Block.")
    print("Enter an IP address or URL to search against a known good repository of IPs and URLS.")
    print("If the IP or URL is not in the repisotry, it will be added to the SOC Block List in Palo Alto.")
    print("Please note that this program is case sensitive.")

    while addanother == 1:
        value = input("Please enter a URL or IP:\n")

        with open("repo.txt", "r+") as file:
            if value in file.read():
                print("Cannot add to SOC Block List")
                file.close()
            else:
                with open("badlist.txt", "r+") as file1:
                    if value in file1.read():
                        print("IP/URL already in SOC Block List")

                    else:
                        file1.write("\n")
                        file1.write(value)
                        print("Value added to the SOC Block List")
                        file1.close()
        addanother = int(input("Type 1 to input another IP/URL, type 2 to exit \n"))

else:
    print("Wrong password...")
wait = input("Press any key to exit")



