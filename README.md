# Drum-Pad-Trainer

A program that help you get better at drumming by practicing different Exercises at different BPM.
To use the App, you need to install **npm** and **Python 3** because the frontend is created with **Electron**
and the backend with **Python 3**.

## What it does:

You can create Exercises that you can store in a DB. If you store them, they will be public - everybody
can see them, of course only if they know the exercise's name or ID. If you don't want other people to
see your exercises and you're only using it on one device, you don't have to do that. To download an exercise,
you need to know its ID. (Maybe name will be enough, I don't know)
To practice, you can start a session. Every session has two parts:

- WARMUP MODE: You need to do a few exercises at a BPM that is not too fast. In the settings you can
choose which exercises you want to do to warm up. You can also tell the program to choose a few random exercises.

- PRACTICE MODE: In practice mode you need to practice exercises, which means you try to get faster. The
program automatically changes the BPM after doing the exercise x times at a lower BPM. After each BPM,
you need to tell the App if the BPM was *EASY*, *MEDIUM*, *HARD*, *IMPOSSIBLE*. The starting BPM in a new
session is always between *MEDIUM* and *HARD* (same for WARMUP MODE). Like that the program always knows
what you need to practice and you will get better faster.


## The App:

When you open the App you will see a navigation bar on the top of the screen. There you can go to three pages:

- **NEW SESSION** brings you to a page where you can start a new session.

- **EXERCISES** brings you to a page where you can see and edit your exercises and download an exercise.

- **SETTINGS** brings you to the settings page where you can edit which exercises you want to do for WARMUP and PRACTICE mode.
You can also create an account or log in with an existing one so that you can store them in a DB or use multiple devices.
