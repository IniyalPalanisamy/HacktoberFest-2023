import java.util.Scanner;

public class FoodOrder {
    int burger = 100;
    int pizza = 160;
    int fries = 60;
    int total = 0;
    int quantity;

    public void generateBill() {
        System.out.println("**Thank you for ordering**");
        System.out.println("Your total bill is : " + total);
    }

    public void displayMenu() {
        System.out.println("***Welcome to the menu***");
        System.out.println("1. Burger      100/-");
        System.out.println("2. Pizza       160/-");
        System.out.println("3. Fries        60/-");
        System.out.println("4. Exit");
    }

    Scanner sc = new Scanner(System.in);

    public void order() {
        while (true) { // Loop to allow multiple orders
            displayMenu(); // Display the menu each time
            System.out.println("Enter your choice: ");
            int ch = sc.nextInt();

            switch (ch) {
                case 1:
                    System.out.println("You have selected Burger");
                    System.out.println("Enter the desired quantity: ");
                    quantity = sc.nextInt();
                    total += quantity * burger; // Using += to accumulate total
                    break;

                case 2:
                    System.out.println("You have selected Pizza");
                    System.out.println("Enter the desired quantity: ");
                    quantity = sc.nextInt();
                    total += quantity * pizza; // Using += to accumulate total
                    break;

                case 3:
                    System.out.println("You have selected Fries");
                    System.out.println("Enter the desired quantity: ");
                    quantity = sc.nextInt();
                    total += quantity * fries; // Using += to accumulate total
                    break;

                case 4:
                    generateBill(); // Generate bill before exiting
                    System.exit(0); // Exit the program
                    break;

                default:
                    System.out.println("Invalid choice, please try again.");
                    break;
            }

            System.out.println("You want to order anything else (Yes/No): ");
            String again = sc.next();
            if (again.equalsIgnoreCase("No")) {
                generateBill();
                break; // Exit the loop if the user does not want to order again
            }
        }
    }

    public static void main(String[] args) {
        FoodOrder fo = new FoodOrder();
        fo.order(); // Start the ordering process
    }
}
