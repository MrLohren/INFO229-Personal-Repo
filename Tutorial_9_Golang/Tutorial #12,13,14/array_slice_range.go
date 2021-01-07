package main

import "fmt"

func main() {
	//ARREGLOS
	//arr := [5]int{1, 2, 3, 4, 5}

	//arr[len(arr)-1] = 20

	//var sum int64

	//for i := 0; i < len(arr); i++ {
	//	sum += int64(arr[i])
	//}

	//fmt.Println(sum)

	//SLICES
	//Porciones de Arreglos
	//Similar a python (X[::3])
	//i.e: puede agrandarse o achicarse
	//Utiliza punteros (*)

	//arreglo base
	//var x [5]int = [5]int{1, 2, 3, 4, 5}

	//slice ejemplo
	//var s []int = x[:]
	//fmt.Println(s)
	//len(s) -> Tamaño del slice
	//cap(s) -> capacidad del slice (que tan grande
	//puede llegar a ser desde el indice inicial)
	//pueden extenderse
	//Tambien se puede declarar un slice independiente
	// var a []int = []int{5,6,7,8,9}
	//Tambien: a := make([]int, 5) -> slice vacio de largo 5
	//EN ESTE CASO: len(a) == cap(a)

	//Se puede extender slices con numeros
	//y := append(s, 6)
	//fmt.Println(y)

	//RANGE
	var a []int = []int{5, 6, 7, 8, 9}

	//for i := 0; i < len(a); i++ {
	//	fmt.Println(a[i])
	//}

	//for i, element := range a{
	for _, element := range a {
		//Similar a [for i in a] de Python
		//pero tambien te entrega la posicion exacta
		//(i)
		//Si no quiero i, reemplazo con _ (ignorar)
		fmt.Println(element)
	}
}
