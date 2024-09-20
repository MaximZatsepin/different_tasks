#include <stdio.h>

int solution(int number);

int main(){
    printf("TEST 0: %d - %s\n", 3, solution(3) == 0 ? "Valid" : "Not Valid");
    printf("TEST 1: %d - %s\n", 4, solution(4) == 3 ? "Valid" : "Not Valid");
    printf("TEST 2: %d - %s\n", 5, solution(5) == 3 ? "Valid" : "Not Valid");
    printf("TEST 3: %d - %s\n", -1, solution(-1) == 0 ? "Valid" : "Not Valid");
    printf("TEST 3: %d - %s\n", 20, solution(20) == 78 ? "Valid" : "Not Valid");
    // printf("%d\n",solution(20));
    // printf("%d\n",solution(10));

    return 0;
}

int solution(int number) {
    int num = 0;
    if (number > 0){
        for(int i = 0; i < number; i++){
            if (i % 3 == 0) {num += i;}
            else if (i % 5 == 0) {num += i;}
        }
    }
    return num;
}