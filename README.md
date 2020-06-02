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

## How to install it:

Right now the first version is just in development, so you need to wait until a release is there.
This is what I think it might be like at the beginning:

- clone the Repo

- run setup.py ?

- run run.py to open the app.

## The App:

When you open the App you will see a navigation bar on the top of the screen. There you can go to three pages:

- **NEW SESSION** brings you to a page where you can start a new session.

- **EXERCISES** brings you to a page where you can see and edit your exercises and download an exercise.

- **SETTINGS** brings you to the settings page where you can edit which exercises you want to do for WARMUP and PRACTICE mode.
You can also create an account or log in with an existing one so that you can store them in a DB or use multiple devices.
To create an account you just need username and password.

## Some random other stuff:

### How exercises are stored:

Exercises are stored like this: (This is a paradiddle, it is in 4/4 but there are 16th notes -> same as 16/16,
it only has 1 bar (the bar has 4 quarter notes), replaid 8 times)

```json
{
    "name": "Paradiddle",
    "rythm": [4, 4],
    "replay": 8,
    "startBPM": 80,
    "bars": [
        [
            "EXPLANATION: an empty 16th Note would be an empty list, not no list at all!"
            "EXPLANATION: 1st quarter Note: 1th - 4th 16thNote",

            [
                {"type": "16thNote", "hand": "right", "sound": "accent"}
            ],
            [
                {"type": "16thNote", "hand": "left", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "right", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "right", "sound": "normal"}
            ],

            "EXPLANATION: 2nd quarter Note: 5th - 8th 16thNotes",

            [
                {"type": "16thNote", "hand": "left", "sound": "accent"}
            ],
            [
                {"type": "16thNote", "hand": "right", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "left", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "left", "sound": "normal"}
            ],

            "EXPLANATION: 3rd quarter Note: 9th - 12th 16thNotes",

            [
                {"type": "16thNote", "hand": "right", "sound": "accent"}
            ],
            [
                {"type": "16thNote", "hand": "left", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "right", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "right", "sound": "normal"}
            ],

            "EXPLANATION: 4th quarter Note: 13th - 16th 16thNotes",

            [
                {"type": "16thNote", "hand": "left", "sound": "accent"}
            ],
            [
                {"type": "16thNote", "hand": "right", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "left", "sound": "normal"}
            ],
            [
                {"type": "16thNote", "hand": "left", "sound": "normal"}
            ]
        ],
        "EXPLANATION: here could be more bars, above is just the 1st bar"
    ]
}
```

-------------------

**Empty example:**

```json
{
    "name": "",
    "rythm": [],
    "replay": 0,
    "startBPM": 0,
    "bars": [
        [
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            []
        ]
    ]
}
```
