package main

import (
	"fmt"
	"math"
)

/*
INTERFACES:
Busca encerrar en un tipo especifico
a todos esos tipos que compartan un
metodo del mismo nombre
*/
type shape interface {
	area() float64
}

type circle struct {
	radius float64
}

type rect struct {
	width  float64
	height float64
}

func (r *rect) area() float64 {
	return r.width * r.height
}

func (c *circle) area() float64 {
	return c.radius * c.radius * math.Pi
}

func getArea(s shape) float64 {
	return s.area()
}

func main() {
	c1 := circle{4}
	r1 := rect{5, 7}

	//Es buena practica pasar la
	//direccion de memoria
	shapes := []shape{&c1, &r1}

	for _, shape := range shapes {
		fmt.Println(getArea(shape))
	}
}
