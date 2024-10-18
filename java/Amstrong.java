import java.util.Scanner;

public class Armstrong {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n1 = sc.nextInt();
        int num = n1;
        int n = 0;

        // Count the number of digits in the input number
        while (num != 0) {
            num /= 10;
            ++n;
        }

        num = n1; // Reset num to the original input
        int sum = 0;

        // Calculate the sum of the digits raised to the power of n
        while (num != 0) {
            int d = num % 10;
            sum += Math.pow(d, n);
            num /= 10;
        }

        // Check if the original number is equal to the calculated sum
        if (n1 == sum) {
            System.out.println(n1 + " is an Armstrong number.");
        } else {
            System.out.println(n1 + " is not an Armstrong number.");
        }

        sc.close(); // Close the scanner to prevent resource leaks
    }
}
