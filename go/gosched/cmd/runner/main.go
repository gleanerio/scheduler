package main

import (
	"example.org/tasks"
	"github.com/go-co-op/gocron"
	"log"
	"os"
	"time"
)

func init() {
  // not used yet...
}

func main() {

	f, err := os.OpenFile("eventlog.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalf("error opening file: %v", err)
	}
	defer f.Close()

	log.SetOutput(f)

	s := gocron.NewScheduler(time.UTC)
	s.Every(2).Minutes().Do(tasks.Task)
	s.Every(1).Minutes().Do(tasks.Task2)

	// you can start running the scheduler in two different ways:
	// starts the scheduler asynchronously
	// s.StartAsync()
	// starts the scheduler and blocks current execution path
	s.StartBlocking()
}
