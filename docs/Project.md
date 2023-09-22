# Code Tank
## About
__Code Tank__ is a simple CLI program for Windows that allows users to run a code "fish tank" effect in any of their CLIs. It was designed to consume as few resources as possible so that you can do what you do best without any slowdowns.

Basically, it offers a lightweight effect in your console that can add to the immersion of your coding sessions. You can customize the effect to fit your needs and own personal taste.

## Features & Todo
Here are a list of features and options that we are currently working on:
* Run the program from the command line to generate the effect.
* Changes various aspects of the effect including:
* * Color of the effect (Text color of everything(df:white), error colors(df:red), success colors(df: green), pending color(df:yellow).)
* * Style of the effect (current ideas: Matrix Rain, Cyberpunk, Hacker, and Tony Stark OS)
* * Speed of the effect (How fast each line generates)
* * Optimal memory management for all users.

## Moving Parts
+ Function that generates text and bars, line by line, for an indefinite amount of time but has a delay in processing time to allow for it to be read by humans.

+ The Effect is broken down into 3 parts: Startup sequence, proxy iteration, and termination sequence. Each one is played in order when the program starts but the program iteration runs idefinitely until the user presses the terminate command.

+ Memory should be cleared and resassigned frequently to prevent memory leaks and reduce memory usage. Variable declarations on the stack should be kept to a minimum.

+ Text and all data will be read from a file and potentially stored in dynamic memory (heap).

## Helpful Resources & Tools
+ [Hiragana and Katakana Converter](https://www.lexilogos.com/keyboard/japanese.php)
+ [Glitch Text Generator](https://lingojam.com/GlitchTextGenerator)
+ [Hacking Scenes for Inspiration](https://www.youtube.com/watch?v=j7BVMYcdPxs)
+ [Matrix Intro Scene for Inspiration](https://www.youtube.com/watch?v=Smwrw4sNCxE)
+ [Iron Man Scene for Inspiraion](https://www.youtube.com/watch?v=EfmVRQjoNcY)