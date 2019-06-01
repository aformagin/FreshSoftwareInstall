# This is the main python file of my install script
run = True
def main():
    print("\033[1;31;40m## Welcome to A117's Python Installer Script##\n")
    
    print("\033[1;37;40m## Follow the directions below if you wish to download or install \n" +
            "this set of software")

    print("Please enter either 1, 2, or 3 to select yor option\n")
    print("\033[0;37;40m## Option 1: Download(This clones the git repos from AUR)\n" +
            "## Option 2: Install(Builds the packages with makepkg -si)\n" +
            "## Option 3: Exit(Exits this script)\n" +
            "\033[5;36;40m## IT IS YOUR RESPONSIBILITY TO CHECK THE BUILDPKGs BEFORE INSTALLING ##\n")

    while(run):
        # The following is the selection statement for the user option
        option = input("\033[0;37;40mSelect your option: ")

        if option == "1":
            print(option)
            #download.folderCreate()
            #download.download()
        elif option == "2":
            print(option)
            #install.install()
        elif option == "3":
            print("Exiting... Thank you for using my script!"\n)
            break;
        else:
            print(option, "is not valid number please")
main()
