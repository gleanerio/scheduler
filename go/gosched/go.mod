module main

go 1.16

require (
  github.com/jasonlvhit/gocron v0.0.1  
  example.org/tasks v0.0.0
)

replace (
   example.org/tasks => ./internal/tasks
)