
all: dummy.oj

main.ll: main.cpp
	clang main.cpp -S -emit-llvm

dummy.oj: main.ll
	python conv_do.py main.ll

