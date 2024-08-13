CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c11
CLIBS = -lm

%.out : %.c
	$(CC) $(CFLAGS) $< -o $@
	chmod u+x $@

clean:
	rm ./*/*/*.out