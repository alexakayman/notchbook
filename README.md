What if we could store all of human knowledge in a fraction?

# Introducing NotchBook 📖

Every letter has a number code.

As an example, "create" would be a string of 18 digits.

You could do the same with an entire book, using #'s for markdown.

This digit becomes a decimal which has a an exact fraction.

To read the book, just divide the fraction and decode the decimal.

### How To Run It?

1. Clone the repo
2. Open up VSCode/Your IDE
3. Run the script

## How It Works

1. Use the key to encode a given sentence
2. Find a numerator and denominator whose fraction results in the encoded decimal. Theoretically, these two integers could be etched into a metal rod and the notch length would be measured.
3. Finally, decode that decimal.

Inspiration: https://www.tiktok.com/@mathletters/video/7179953778475437354?is_from_webapp=1&sender_device=pc&web_id=7243081339755234862

### How It Was Built

- Python
- Decimal module
- 1hr build

### Limitations

- Terminal interface only
- Does not handle line breaks
- Capitalizes programmatically, so it may not always match inputted content.
