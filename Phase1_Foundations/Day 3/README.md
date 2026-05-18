# Day 3 - Strings + Formatting

Today I practiced Python strings by building a small personal progress card generator.

## Main Concept

Strings are text values. Python lets me store, combine, format, inspect, and transform text.

Key tools from today:

- `len(text)` counts characters.
- `text.upper()` converts text to uppercase.
- `text.lower()` converts text to lowercase.
- `text.title()` converts text to title case.
- `text.strip()` removes extra spaces from the beginning and end.
- `text[index]` gets one character.
- `text[start:end]` slices part of a string.
- `f"{value}"` inserts variables into a formatted string.
- `\n` starts a new line inside a string.

## Project

`task.py` creates a Day 3 sprint card from user input.

It asks for:

- Name
- Current Python topic
- Tiny win
- Concept to revisit
- Confidence score

Then it prints a clean progress card using string formatting.

## Usage

Run the project:

```bash
python task.py
```

Run extra practice:

```bash
python practice.py
```

## Sample Output

```text
========================================
DAY 3 PYTHON SPRINT CARD
========================================
Coder: Sommer Turner
Topic: Strings + Formatting
Tiny Win: I built a script that talks back to me.
Revisit: String slicing
Confidence: 7/10
Proof: Sommer Turner is practicing Strings + Formatting one clear rep at a time.
========================================
```

## What I Learned

Strings are not just words on the screen. They are data I can shape: clean up, slice, measure, combine, and format for a better user experience.

## What I Want To Remember

F-strings are my friend when I want readable output:

```python
print(f"Today I practiced {topic}.")
```

## Tiny Win

I made Day 3 personal instead of only copying a lesson.
