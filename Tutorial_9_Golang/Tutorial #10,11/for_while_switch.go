package main

import "fmt"

func main() {
	x := 33

	//For
	//	for i := 0; i < 100; i++ {
	//		fmt.Println(x)
	//		x++
	//	}
	/* For puede tener una estructura muy parecida a WHILE
	De hecho, GO no tiene WHILE, FOR cumple con esa rutina
	for x <= 5{
		fmt.Println(x)
		x++
	}

	for true{
		//TODO
	}
	For tambien usa break y continue, igual que PYTHON por ej
	*/

	//SWITCH
	//Todos los casos deben cioncidir con el tipo de
	//x
	switch x {
	case 1:
		fmt.Println("uno")
		break
	case 2:
		fmt.Println("dos")
		break
	case 3:
		fmt.Println("tres")
	default:
		fmt.Println("numero equivocado")
		break
	}
}
