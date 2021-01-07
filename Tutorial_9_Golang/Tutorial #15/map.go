package main

import "fmt"

func main() {
	//MAP: Similar a la Logica de los Diccionarios
	//de PYTHON
	//OJO: map no contempla el orden de los datos
	//al imprimir, el orden es diferente

	var mp map[string]int = map[string]int{
		"apple":  5,
		"pear":   6,
		"orange": 9,
	}
	//Forma sencilla de declarar un map vacio
	//	mp := make(map[string]int)

	fmt.Println(mp["apple"])

	mp["apple"] = 900

	fmt.Println(mp["apple"])

	delete(mp, "apple")

	fmt.Println(mp)
	//fmt.Println(mp)

	//Checkear si una key existe
	val, ok := mp["naranja"]
	//val : valor de la key, si existe, 0 si no
	//ok : bool de si la key existe o no
	fmt.Println(val, ok)
}
