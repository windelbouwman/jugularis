
all: dummy.oj

rusthello.ll: rusthello.rs
	rustc rusthello.rs --emit llvm-ir

dummy.oj: rusthello.ll
	python conv_do.py rusthello.ll

