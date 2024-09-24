all: clean run

run:
	as hello.s -o hello.o
	ld -macosx_version_min 13.3.0 -L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib -lSystem -o hello.run hello.o
	rm *.o


clean:
	rm *.run