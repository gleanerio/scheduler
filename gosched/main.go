package main

import (
	"github.com/jasonlvhit/gocron"
  
)


func main() {
	s := gocron.NewScheduler()
	s.Every(2).Minutes().Do(task)
  s.Every(1).Minutes().Do(task2)

	<-s.Start()
}