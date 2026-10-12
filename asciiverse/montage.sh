#!/bin/sh
# montage.sh SWARM: three challenges solved by their built-in solutions, one
# after another. Recorded asciiverse/swarm.cast as
#   asciinema rec --window-size 100x30 --command "asciiverse/montage.sh ./swarm" ...
# in a 100x30 tmux session, pressing Enter on each "Congratulations!" dialog
# two seconds after it appears (Enter picks Quit, and the next one starts).
for s in Challenges/Logic/Sokoban/foresight Challenges/Mechanics/wave Challenges/Logic/hanoi; do
  "$1" --scenario "$s" --autoplay --hide-goal
done
