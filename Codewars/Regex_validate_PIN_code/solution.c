#include <stdbool.h>
#include <stdio.h>

bool validate_pin(const char *pin);

int main() {
    printf("TEST 0: %s - %s\n", "1111", validate_pin("1111") ? "Valid" : "Not Valid");
    printf("TEST 1: %s - %s\n", "1a11", validate_pin("1a11") ? "Valid" : "Not Valid");
    printf("TEST 2: %s - %s\n", "1234", validate_pin("1234") ? "Valid" : "Not Valid");

    return 0;
}

bool validate_pin(const char *pin) {
    int flag = 1;
    int count = 0;
    const char *temp = pin;
    while (*temp) {
        if (*temp < '0' || *temp > '9') {
            flag = 0;
        }
        temp++;
        count++;
    }
    if (count != 4 && count != 6) {
        flag = 0;
    }

    return flag;
}
