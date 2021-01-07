package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//Entrada y conversion
func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("Ingrese año de nacimiento: ")
	scanner.Scan()
	input := scanner.Text()

	intinput, _ := strconv.ParseInt(input, 10, 64)

	fmt.Printf("Tienes : %d años\n", 2020-intinput)
}
