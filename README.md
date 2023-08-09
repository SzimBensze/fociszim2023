# fociszim2023
A rework of an old Python project of a text-based football simulator.

## Disclaimer
This is a private project, you may examine the code and clone the repository for personal use. Do not copy, edit or share without permission!

## Short introduction
This text-base game was a hobby project way back in 2020, the main idea is based off of FIFA 18's match simulation. The original instance, "fociszimulator.py" is really linear and has very primitive code as I was quite novice at that time. This rework, "fociszim2023.py" was made in November 2022 and it has been tweaked and modified since. I consider the current stage final, but I may occasionaly add and rework some blocks of code. It is still not the most condense and convenient code and there's always room for improvent, but just like any other program, nothing is perfect. Both programs are solely in Hungarian and I don't plan on translating them. My newest implementation is written in Java and can be found on my "fociszim2024" repo. It'll feature mostly the same gameplay, but fully in English.

## How to use
Simple steps on how to play a match:
1. Give a name for the home team
2. Input three values "attack", "midfield" and "defense" between 1-100 just like in FIFA
3. Repeat the same for the visitors
4. Enter the formation for the home team, please follow the pattern in order to work
5. Repeat the same for the visitors
6. Enter "igen" to see numeric values for live statistics during the match, "nem" to skip this
7. Have fun!

Check the example text file to see how a match is set up and simulated.

## The mechanism
The program simulates a match between the given two teams using their FIFA values and their formation. It generates a base chance at the beginning which always rises or falls each minute passed. This chance is a really small number between 0 and 1 and each minute an RNG is made for each team. The teams try and reach the opponent's goal, if conditions are met they will attempt to shoot at the goal in which case another RNG occurs and if the conditions are met once again, they will score a goal. This process is repeated each minute until 90 minutes are passed. There are also some random events which can happen anytime and they are fully independent from this system, but can have an impact on the teams' chances. If the teams are tied you can opt for extra time, where the same mechanism is used, with some minor alterations to the numbers. If the extra time is over and there is still no winner, you can do penalties, which work a little different. Each team will take turns with a similarly calculated chance and will try to score as many goals as possible within 5 tries. If they are tied, the process will repeat until one team fails, so eventually there will be a winner.

If you're interested in more details or have any questions feel free to ask me! My Discord: SzimBensze#7577
