section .text

section .data

msg db "Hello, World!", 0xa
len equ $ - msg

global _start

_start:
	
	mov ecx, msg
	mov edx, len
	mov ebx, 1
	mov eax, 4
	int 0x80

	mov ebx, 0
	mov eax, 1
	int 0x80

