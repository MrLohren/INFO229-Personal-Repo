package main

import "fmt"

type Student struct {
	name   string
	grades []int
	age    int
}

//Metodo
func (s *Student) setAge(age int) {
	s.age = age
}

func main() {
	s1 := Student{"Loh", []int{1, 2, 3, 43, 5}, 23}
	s1.setAge(40)
	fmt.Println(s1.age)
}
