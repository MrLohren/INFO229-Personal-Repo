package main

import "fmt"

func main() {
	//\n -> salto de linea (enter)
	//\t -> emula un "TAB"

	//fmt.Printf("%T", 10) //Tipo de variable
	//fmt.Printf("%v", 10) //Valor de la variable
	//fmt.Printf("%t", false) //Para booleanos

	//Enteros (si se usan en mayusculas, el resultado tambien estara en mayus)
	//%b (base 2)
	//%o (base 8)
	//%d (base 10)
	//%x (base 16)

	//Floats
	//%e (notacion cientifica)
	//%f/%F (decimal sin exponente)
	//%g (para exponentes -decimales- grandes)

	//Strings
	//%s (default)
	//%q (incluye las "comillas")

	//Ancho y precision
	//Son para impirir "mas a la derecha" o redondear floats
	//%f (por defecto)
	//%9f (ancho 9 -a la derecha-)
	//%.2f (redondeo al 2 decimal)
	//%9.2f (ancho 9 y redondeo a 2do decimal)
	//%9.f (ancho 9, precision 0)
	var out string = fmt.Sprintf("Number: %07d", 4545) //Guarda toda la logica anterior
	//en una variable

	fmt.Println(out)
}
