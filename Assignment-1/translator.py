class Interpreter:

	def convert(self):
		f_32 = open('/home/ironman/Desktop/hello_32.asm', 'r')
		f_64 = open('/home/ironman/Desktop/hello_64bit.asm', 'w')

		lines = f_32.readlines()

		print >> f_64, "extern printf"

		for line in lines:
			if "section .txt" in line:
				print >> f_64, line

			if "section .data" in line:
				print >> f_64, line

			if "msg db" in line:
				print >> f_64, "msg: 	db 'Hello, World!', 0"

			if "len equ" in line:
				print >> f_64, 'fmt: 	db "%s", 10, 0'

			if "global _start" in line:
				print >> f_64, "global main"

			if "_start:" in line:
				print >> f_64, "main:"
				print >> f_64, "push rbp"

			if "mov ecx" in line:
				print >> f_64, "mov rsi, msg"

			if "mov edx" in line:
				print >> f_64, "mov rdi, fmt"

			if "mov ebx, 1" in line:
				print >> f_64, "mov rax, 0"
				print >> f_64, "call printf"
				print >> f_64, "pop rbp"

			if "mov ebx, 0" in line:
				print >> f_64, "mov rax, 0"
				print >> f_64, "ret"
				break

		f_64.close()
		f_32.close()

if __name__=="__main__":
    c=Interpreter()
    c.convert()
