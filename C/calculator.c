#include <stdio.h>

int main() {
    char operator;
    double num1, num2, result;

    // Displaying a menu for the user
    printf("Simple Calculator\n");
    printf("Select an operator (+, -, *, /): ");
    scanf(" %c", &operator); // Space before %c to consume any whitespace

    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2); // Read two double values

    // Perform calculation based on the operator
    switch (operator) {
        case '+':
            result = num1 + num2;
            printf("%.2lf + %.2lf = %.2lf\n", num1, num2, result);
            break;
        case '-':
            result = num1 - num2;
            printf("%.2lf - %.2lf = %.2lf\n", num1, num2, result);
            break;
        case '*':
            result = num1 * num2;
            printf("%.2lf * %.2lf = %.2lf\n", num1, num2, result);
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                printf("%.2lf / %.2lf = %.2lf\n", num1, num2, result);
            } else {
                printf("Error! Division by zero.\n");
            }
            break;
        default:
            printf("Error! Invalid operator.\n");
            break;
    }

    return 0;
}
