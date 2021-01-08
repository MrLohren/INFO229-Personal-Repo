package main

import "fmt"

/* Funciones Simples
func test(x, y int) (int, string) {
	return x + y, "bien"
}

func main() {
	a, b := test(1, 2)

	fmt.Println(a, b)
}
*/

//Funciones Avanzadas

func returnFunc(x string) func() {
	return func() { fmt.Println(x) }
}

func test2(myFunc func(int) int) {
	fmt.Println(myFunc(7))
}

func main() {
	returnFunc("hola")()
}
