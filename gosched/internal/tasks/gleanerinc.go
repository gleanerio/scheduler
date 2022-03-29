package tasks

import (
	"log"
	"os/exec"
)


// Task runs Gleaner in incremental mode
func Task() {
	// fmt.Println("Task is being performed.")
	out, err := exec.Command("ls", "-l").Output()

	if err != nil {
		log.Fatal(err)
	}

	log.Println(string(out))

}

// Task2 runs Nabu in prefix mode
func Task2() {
	log.Println("Call sparql and load results to minio")
}


// Task3 runs Nabu in prune mode

