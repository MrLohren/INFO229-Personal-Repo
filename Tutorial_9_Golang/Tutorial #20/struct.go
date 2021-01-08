package main

import "fmt"

type Point struct {
	x int32
	y int32
}

type Circle struct {
	radius float64
	center *Point
}

func main() {
	x := Point{1, 2}
	fmt.Println(x.x, x.y)

	c1 := Circle{4.56, &x}
	fmt.Println(c1.radius, c1.center.x)
}
