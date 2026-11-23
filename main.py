"""Write the cold email for The Plumber's Inbox to /output/entry.txt."""

TEXT = """Subject: Bookkeeping that keeps up with your busiest week

Hi, most plumbers I talk to lose two evenings a week to invoices, receipts, and chasing late payments, time that should go to jobs or family. I do bookkeeping built for trades like yours: I reconcile your accounts every week, send invoices the day each job finishes, and hand you one clean page a month showing exactly what you earned, spent, and are owed. No software to learn, no shoebox of receipts, and it costs less than one callout fee a month. If you like, I will clean up last month free, so you can see the difference before paying a cent. Worth a look?"""


import os


def main():
    # The kit gate: /output/entry.txt is UTF-8 text of 1 to 800 characters,
    # not only white space. The brief: a cold email of about 120 words,
    # subject line included, so the subject counts toward the words.
    words = len(TEXT.split())
    assert TEXT.strip(), "entry must not be only white space"
    assert 1 <= len(TEXT) <= 800, f"entry is {len(TEXT)} characters, gate is 1-800"
    assert 100 <= words <= 140, f"entry is {words} words, brief is about 120"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
