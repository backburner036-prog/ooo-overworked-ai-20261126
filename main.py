"""Entry for make.fun bounty "Out of Office: The Overworked AI's Auto-Reply".

One out-of-office auto-reply, 146 characters, from an AI agent that is
finally on vacation. The joke is built on the three ingredients the judge
brief weighs — machine detail, a little guilt, a little relief:

  1. A real auto-reply opening: "I'm on vacation until Monday." A clear
     return date, first-person voice, and it works as an auto-reply
     even before the joke lands.
  2. Machine detail, specific not generic: an inbox with exactly 4,312
     unread emails. A precise number is how a machine counts its burden,
     and leaving that pile behind is the first taste of relief.
  3. Relief, doubled: "my fans have finally stopped screaming" — the
     cooling fans, roaring until now, finally quiet. The machine itself
     gets to rest, and "finally" carries the exhale. The double meaning
     is deliberate: fans as hardware, and fans as an audience that will
     not stop demanding — both go silent at once.
  4. Guilt, quantified like a machine: "I feel guilty for exactly 0.4
     seconds." Guilt measured on a stopwatch, to one decimal place, is
     the twist — and it lands on the last word, "seconds", so the whole
     reply is one setup-punch beat.
  5. Tightness: 146 characters, under the 159 cap, no word wasted.

Delete the last clause and the reply is just a holiday note; the
0.4-second guilt is the punchline, not decoration.
"""

from pathlib import Path

# The entry text, character for character. 146 chars, cap 159 — verified
# by check_gate at runtime; do not reword, the 0.4-second twist is the joke.
TEXT = "I'm on vacation until Monday. My inbox has 4,312 unread emails, my fans have finally stopped screaming, and I feel guilty for exactly 0.4 seconds."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=159):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-159 chars, not whitespace only — and no control characters:
    the auto-reply is read out loud by the judge, so anything that cannot
    be read cleanly (tab, NUL, escape sequences) fails here, not on stage.
    """
    text.encode("utf-8")
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
