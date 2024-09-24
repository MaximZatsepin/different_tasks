.global _main
.align 2

_printf:
    mov X0, #1
    adr X1, helloworld // load address of helloworld into X1
    mov X2, #12 // load length of helloworld into X2
    mov X16, #4 // syscall number for write
    svc 0

_terminate:
    mov X0, #0
    mov X16, #1
    svc 0

_main:
    b _printf
    b _terminate

_reboot:
    mov X0, #1
    mov X16, #55
    svc 0

// hello world string
helloworld: .ascii "Hello world\n"
