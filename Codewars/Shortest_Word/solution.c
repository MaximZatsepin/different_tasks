#include <stdio.h>
#include <string.h>
#include <sys/types.h>

ssize_t find_short(const char *s);

int main() {
    const char *str1 = "bitcoin take over the world maybe who knows perhaps";
    printf("%s - %zd\n", str1, find_short(str1));
    const char *str2 = "Let's travel abroad shall we";
    printf("%s - %zd\n", str2, find_short(str2));
}

ssize_t find_short(const char *s) {
    const char *temp = s;
    size_t size = 0;
    size_t min_size = 2147483647;
    while (*temp) {
        // printf("char = %c\n",*temp);
        if(*temp == ' '){
            if(size != 0 && size < min_size){
                min_size = size;
                // printf("min size = %ld\n",min_size);
            }
            size = 0;
        }else{
            size++;
        }
        temp++;
    }

    // printf("final size - %ld\n",size);

    if (size == 0) {
        min_size = -1;
    }else if (size < min_size){
        min_size = size;
    }

    return min_size;
}