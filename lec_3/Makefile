install:
	g++ -c f3.cc -o f3.o
	gcc -shared f3.o -o libf3.so
	g++ -L/${PWD} -Wall f4.cc -o f4.out -lf3
	export LD_LIBRARY_PATH=./:${LD_LIBRARY_PATH}

clean:
	rm -r f3.o libf3.so f4.out 
