#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Complete the function that accepts a string parameter, and reverses each word in
the string. All spaces in the string should be retained. Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
*/

char* reverseWords(const char* text);

int main() {
    const char str0[6] = "Hello";
    const char str1[20] = "This is an example!";
    const char str2[15] = "double  spaces";
    char *new_str0 = reverseWords(str0);
    char *new_str1 = reverseWords(str1);
    char *new_str2 = reverseWords(str2);
    printf("%s - %s\n", str0, new_str0);
    printf("%s - %s\n", str1, new_str1);
    printf("%s - %s\n", str2, new_str2);
    printf("TEST 0: %s\n", strcmp(new_str0, "olleH") == 0 ? "Success" : "Fail");
    printf("TEST 1: %s\n", strcmp(new_str1, "sihT si na !elpmaxe") == 0 ? "Success" : "Fail");
    printf("TEST 2: %s\n", strcmp(new_str2, "elbuod  secaps") == 0 ? "Success" : "Fail");

    free(new_str0);
    free(new_str1);
    free(new_str2);

    return 0;
}

char* reverseWords(const char* text) {
    int count = 0;
    for (const char* temp = text; *temp; count++, temp++)
        ;
    char* reverse_text = calloc(count, sizeof(char));

    int j = 0;
    int word_count = 0;
    for (int i = 0; i < count; i++) {
        if (text[i] == ' ') {
            reverse_text[j++] = ' ';
        } else if (text[i] != ' ') {
            do {
                // printf("i: %d, count: %d, symb: %c\n", i, word_count, text[i]);
                i++;
                word_count++;
            } while (text[i] != ' ' && text[i] != '\0');
            for (int k = 1; k <= word_count; k++) {
                reverse_text[j++] = text[i - k];
                // printf("char: %c\n", text[i - k]);
            }
            if (text[i] != '\0') {
                reverse_text[j++] = ' ';
            }
            word_count = 0;
        }
    }

    reverse_text[j] = '\0';

    return reverse_text;
}