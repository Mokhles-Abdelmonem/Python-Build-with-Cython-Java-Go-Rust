package main

import "C"

//export Add
func Add(a, b int) int {
    sum := 0
    for i := a; i < b; i++ {
        sum += i
    }
    return sum
}

func main() {}
