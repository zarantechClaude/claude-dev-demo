# Recording hygiene

Trainer reference. These are the risks specific to recording a course **about an AI
coding tool, with live API access, in a browser you are already signed into**. They
are not generic screencast advice.

The operating principle behind all of it:

> **Assume every frame ships, permanently, and cannot be edited later.**

Editing a leaked frame out of a published video is possible. Relying on it is not a
plan, because the leak you have to catch is the one you did not notice. Design the
recording so that a visible mistake is harmless.

There is a second, quieter risk that matters as much as leakage: a frame that dates
the video. A leaked secret costs you a key rotation. A model version on screen costs
you a re-record every release cycle, forever.

---

## 1. Your API key will be on screen

Exercise 10 has the learner create a `.env` and put a real key in it. You are doing
that on camera. The file will be open in an editor, and the folder will be visible
in a file tree.

### What to do

1. **Generate a throwaway key used only for recording.** Not your working key, not
   a team key, not one shared with anything else.
2. **Put a low spend cap on it.** It only has to survive Exercises 10, 11, 12 and
   15 plus retakes.
3. **Revoke it the day you finish recording.** Put that in your calendar on the day
   you start, not the day you plan to finish.
4. **Plan for it to be visible. Make it worthless instead of trying to hide it.**
   This is the whole strategy. Do not rely on blurring, cropping, or editing the
   frame afterwards.

### What the material already does for you, and one thing it does not

The lab and script design deliberately never echoes key material:

1. **No lab step prints a key.** Exercise 10 Step 6 runs `verify_key.py` instead,
   and Step 8's raw `curl` block passes the key through a shell variable rather
   than typing or printing it.
2. **`verify_key.py` is a presence-and-length check by design.** It reports that
   the key loaded and how long it is. Length answers the only question you
   actually have, which is whether the file loaded at all.
3. The Exercise 10 lab text states that the script does not print the key "not even
   the first few characters", and explains why: a truncated key in a screenshot or
   a log aggregator is still a leaked prefix, and it is enough to correlate with a
   full key somewhere else.

This was not always true. An earlier version of the script printed a seven-character
prefix, and both the lab text and the defect register asserted otherwise, so the
trainer would have read a false statement on camera. The script was corrected. It now
prints only:

```python
print("Key loaded. Length {} characters.".format(len(key)))
```

It also warns if the key has stray whitespace or is wrapped in quotes in `.env`,
which are the two most common causes of a key that "loaded" but does not work.

Seven characters is the non-secret vendor prefix rather than the secret portion, so
the practical exposure is low. The problem is that it contradicts the lab narration
you will be reading on camera, and it contradicts decision 18 in
`docs/course-context.md`. Trim the prefix from the print statement so the script
matches what the video says about it. This is a one-line change and it is the
cheapest credibility fix in the programme.

### Also worth knowing

1. Do not run `echo $ANTHROPIC_API_KEY`, `env`, `printenv`, or `cat .env` on camera,
   even to debug. If you do it in a take, restart the take.
2. Your shell history is visible if you scroll it. Start each recording session in
   a fresh shell.
3. The `.env` file for Exercise 15 carries the same key. Same rules apply in Module
   5.

---

## 2. The Claude sidebar will be on screen

Seven exercises run in the browser: 1, 2, 3, 8, 9, 13 and 14. The conversation list
and the project list are visible in **every one of those frames**, not just the
frames where you meant to show them.

What leaks from a sidebar, in rough order of how badly it lands:

1. A client name in a conversation title.
2. An internal project name.
3. A personal chat title, which is worse for the trainer than for the company.
4. Your account email address and plan badge in the account area.
5. The shape of your other work, which is inferable from a list of titles even when
   no single title is sensitive.

### What to do

1. **Record from a fresh browser profile.** Not an incognito window, a separate
   profile, so it stays clean across sessions and does not carry your extensions,
   bookmarks bar or autofill.
2. **Use a clean account or a dedicated project** with nothing in it but this
   course's conversations.
3. Give the recording conversations deliberate titles. They are on screen, so they
   might as well read as course material.
4. Check the bookmarks bar, the tab strip, and any notification badge before the
   first take. Tab titles leak as reliably as sidebars.
5. Turn off desktop notifications at the operating system level. A message preview
   sliding into frame is the classic failure and it is unrecoverable without an
   edit.

---

## 3. Model names on screen date the video permanently

This is the most expensive risk in the list, because it does not fail loudly. It
just quietly makes the course look old, and it forces re-records on someone else's
release schedule.

The programme rule is that **no Claude model version name appears anywhere**. See
decisions 14 and 15 in `docs/course-context.md`. Recording adds two practical
mitigations on top of the rule.

### Mitigation 1: one frame carries the identifier, not five

Read the model identifier from **one configuration constant**, which is what every
script in this repo already does through `MODEL` in `.env`. A model change then
means re-recording one shot, not a lecture.

| Do this | Not this |
|---|---|
| One `MODEL` line in `.env`, read by every script | The identifier typed into each script you open |
| Point at the configuration and move on | Read the identifier aloud while it is on screen |
| Show the learner looking the current identifier up in the official documentation | Show the learner copying an identifier from your slide |

### Mitigation 2: narrate the tier, never the version

Say **"the current mid-tier model"** or **"the most capable tier"**. Never read a
version name or number aloud. Narration is harder to patch than a slide, because
re-recording audio inside a take usually means re-recording the take.

| Say | Do not say |
|---|---|
| "the current mid-tier model" | any product version name |
| "the most capable tier, for architecture and debugging" | a named version, for the same purpose |
| "a faster tier, for repetitive well-specified work" | a named version, for the same purpose |
| "look up the current identifier in the documentation" | "use this identifier" |

### The model picker is the trap you will forget

The browser labs put a model picker on screen whether you intend it or not. It
names the current versions and it will date every browser lab. Frame the window so
the picker is out of shot where you can, and do not open it on camera unless the
teaching point is tier selection, in which case keep the shot short and know you
will re-record it.

---

## 4. Terminal and editor hygiene

| Setting | Do | Why |
|---|---|---|
| Editor font | Large enough to read on a phone. Increase it until it feels absurd, then stop | Most on-demand viewing is not on a 27-inch monitor |
| Terminal font | Same, and check it against your smallest target screen once before recording | Traceback frames are the hardest thing to read in any lab |
| Shell prompt | Minimal. Directory name only | A prompt carrying a machine name, a username, a git branch and a virtual environment name is a leak and a distraction |
| Machine name and username | Not in the prompt, not in the window title | Both are personal data and both date the recording |
| Paths | Work from a short path created for the recording. No `/Users/<your name>/` | Personal paths are on screen for the entire course |
| Editor sidebar | Only this repository open. Close every other folder and workspace | Other repository names are the most common accidental leak in developer screencasts |
| Editor tabs | Close everything before each take | Old tab titles carry other clients' file names |
| Recent files and command palette history | Cleared, and do not open the palette on camera unless needed | It lists paths you closed |
| Git status in frame | Fine, and useful. Check the branch name is not internal | |
| Theme | High contrast, light or dark consistently across all five modules | Switching mid-course looks like a different course |
| Window size | Fixed. Set it once and do not resize between takes | Resizing forces the viewer to re-find things |
| Screen resolution | One resolution for all recording | Mixed resolutions make the published set look assembled from parts |

---

## 5. Frames to re-check before every republish

A republish is any re-record, re-edit or re-upload of a module. These are the frames
that go stale or leak, so check them specifically rather than rewatching everything.

| Frame | Where | Why it needs rechecking |
|---|---|---|
| The `.env` contents shot | Exercise 10 Steps 4 and 5, Exercise 15 configuration | Carries both the key and the model identifier. The single highest-risk frame in the programme |
| `verify_key.py` output | Exercise 10 Step 6 | Confirm no prefix is printed once the one-line fix is applied. This is the frame that proves the practice you are teaching |
| The raw `curl` block | Exercise 10 Step 8 | Confirm the header names and the endpoint still match the documentation, and that no expanded key value appears in the output |
| Any model picker in the Claude app | Exercises 1, 2, 3, 8, 9, 13, 14 | Names current versions. Dates fastest of anything on screen |
| Slides that name a model version | Vendor numbering: Module 1 slide 8, Module 4 slide 6. In the REVISED decks these are Module 1 slide 10 and Module 4 slide 7, because added slides shifted the numbering | These two were the known offenders. Confirm the revised decks removed them and that no new slide reintroduced one |
| The Claude sidebar in any browser lab | Exercises 1, 2, 3, 8, 9, 13, 14 | A profile that was clean at first recording may not be clean at re-record |
| Account and plan area | Any browser lab where you open the account menu | Email address and plan tier |
| Any pricing, usage or billing page | Anywhere you open the console | Pricing changes, and quoting it dates the video and risks a claim we should not make |
| Exercise 8 timing output | Module 3 | The elapsed time is machine dependent. If your new machine is much faster, the "you can feel it" beat stops working and the constants need retuning |
| Exercise 7 failure count | Module 3 | The lab teaches that three failures come from two problems. If the count on screen is not 3, the narration is wrong |
| Exercise 15 skeleton test output | Module 5 | The lab depends on 3 passed, 1 failed. A repo change that accidentally fixes it removes the lesson |
| Any terminal frame after a long session | All modules | Scrollback accumulates. Check what is above the visible area if you scroll at all |

---

## 6. Pre-record checklist

Work top to bottom. The last two steps are verification runs, deliberately placed
last, so that the final thing you do before recording Module 3 is confirm the
artefacts still behave the way the labs say they do.

### Key and account

1. Generate a throwaway API key. Set a low spend cap.
2. Put the revocation date in your calendar now.
3. Create a fresh browser profile. Sign in with a clean account or select a
   dedicated project with nothing else in it.
4. Confirm the sidebar, tab strip and bookmarks bar are empty of anything you would
   not publish.

### Machine

5. Disable all desktop and application notifications.
6. Set editor and terminal fonts large. Check readability on your smallest target
   screen.
7. Reduce the shell prompt to the directory name. Remove machine name, username,
   branch and virtual environment decoration.
8. Close every folder and workspace except this repository. Close all editor tabs.
9. Fix the window size and screen resolution. Do not change either for the rest of
   the recording.
10. Start a fresh shell so there is no history to scroll into.

### Repository and code

11. Apply the `verify_key.py` prefix fix so the script matches what the Exercise 10
    lab says about it.
12. Confirm no script in any `starter/` folder hardcodes a model identifier.
13. Confirm `ANTHROPIC_API_KEY` is the variable name in Exercises 10, 11, 12 and
    15. Breaking one breaks the chain.
14. Create `.env` with `ANTHROPIC_API_KEY` and `MODEL`. Look the model identifier up
    in the official documentation on your record date rather than reusing an old
    one.
15. Confirm `.gitignore` contains `.env` before `.env` exists.

### Environment

16. Python 3.11 or later. Confirm `python --version` on camera-ready terminal shows
    what you expect.
17. `pip install anthropic python-dotenv pytest flask`
18. Confirm Claude Code runs, needed for Exercises 4, 5 and 6.
19. Test your Mermaid render path, needed for Exercise 13.

### Verification runs, do these last

20. **Exercise 7.** From
    `module-3-debugging/03-labs/exercise-07-debug-buggy-sample/starter/`, run
    `python -m pytest -q`. **Expected: 3 failed.** Two `KeyError` failures and one
    assertion failure of `2 == 3`. If you see one failure, or two, the artefact has
    changed and the Module 3 narration is wrong. Do not record until this is 3.

21. **Exercise 8.** From
    `module-3-debugging/03-labs/exercise-08-slow-implementation/starter/`, run
    `python slow_lookup.py`. **Expected: `matches: 24326`, elapsed roughly 2 to 3
    seconds.** The count is the part that must be exact, because the lab's whole
    correctness trap depends on 24326 being the right answer. The elapsed time is
    machine dependent: if it drops below about 1.5 seconds the audience will not
    feel the delay, and if it rises above about 5 seconds you are sitting in
    silence. Retune the constants at the top of the file if either happens, then
    re-run and confirm the count is still 24326.

Then record. Take the intro first, since it is the shortest and it calibrates your
pace, and take the Module 1 lab videos before the Module 1 deck videos, so the deck
narration can reference what learners will actually do.

**Before Module 5, run the same check on the capstone skeleton.** From
`module-5-advanced-capstone/03-labs/exercise-15-summarizer-microservice/starter/capstone_skeleton/`,
run `python -m pytest -q` and expect **3 passed, 1 failed** with
`assert 502 == 200`. It fails without a key and without network access, so it
reproduces identically for every learner. If it passes, someone has fixed the
planted patch-target problem and the lab has lost its point.
