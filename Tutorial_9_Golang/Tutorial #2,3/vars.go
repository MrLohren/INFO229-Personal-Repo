package main

import "fmt"

func main() {
	//	var name string
	//var number uint16 = 260
	//var number = 260.524841 //go adivina que tipo de numero es 'number'
	//se corre el riesgo de errores al no saber que tipo de variable es
	//number := "jsadk" //La manera mas rapida para declarar vars
	//aunque sigue siendo rigido

	//number = number + 5

	var number uint64 //si no se define un valor especifico, entrega 0
	var bl bool       //falso por defecto

	fmt.Println(number, bl)
}
