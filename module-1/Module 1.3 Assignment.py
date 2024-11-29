#Steven Skinner 11/30/24
#Module 1.3 
#No more beers  buy more 



def countdown_bottles(bottles):
    #Loop until the bottle count reaches 0
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print("Take one down, pass it around,")
            bottles -= 1
            print(f"{bottles} bottles of beer on the wall.\n")
        else:
            # When there is 1 bottle left
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around,")
            bottles -= 1
            print("No more bottles of beer on the wall.\n")
            
# Main program
def main():
    #Ask user for the number of bottles
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles < 1:
            print("Please enter a number greater than 0.")
        else:
            # Call the countdown function
            countdown_bottles(bottles)
            print("Buy more beer!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#Run the main function
if __name__ == "__main__":
    main()
