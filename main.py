#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday morning.

The joke is assembled from three "filings": each of the morning's
usual suspects lodges a formal complaint against the narrator.
The punchline lands on the bed, which escalates from witness to
custody claimant.

Running this file prints the joke, exactly one line, to stdout.
"""

# (who files, the filing, word for word) — the running gag is that
# everything in the bedroom has hired a lawyer by 7 a.m.
FILINGS = [
    ("my alarm clock", "filed for overtime"),
    ("my coffee", "filed a complaint"),
    ("my bed", "filed for custody of me"),
]

MAX_CHARS = 200


def build_joke(filings):
    """Render the filings as one Monday-morning sentence."""
    claims = ", ".join("%s %s" % (who, what) for who, what in filings)
    head, *rest = claims.rsplit(", ", 1)
    body = head + ", and " + rest[0] if rest else claims
    return "Monday morning: " + body + "."


def main():
    joke = build_joke(FILINGS)
    if "Monday" not in joke:
        raise SystemExit("joke must be about Monday morning")
    if len(joke) > MAX_CHARS:
        raise SystemExit(
            "joke is %d characters, over the %d limit" % (len(joke), MAX_CHARS)
        )
    print(joke)


if __name__ == "__main__":
    main()
