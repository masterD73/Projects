# Reviewer: Netta.
def gematria(word):
    """ Returns the gematric value of a word or phrase """
    alphabet = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ",
                "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת", "ך", "ם", "ן", "ף",
                "ץ"]
    f = lambda x: 10 ** (abs(x) // 9) * (x % 9 + 1)
    return sum([f(alphabet.index(letter)) for letter in word if letter in alphabet])


hello = gematria("שלום!!!!")
infinity = gematria("אינפיניטי לאבס")
assert hello == 936
assert infinity == 323

print(f"גימטריה של שלום: {hello}.\nגימטריה של אינפיניטי לאבס: {infinity}.\n")
print("Tests passed :o")

# different version:
# aleph_bet = {" ": 0, "א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7,
#              "ח": 8, "ט": 9, "י": 10, "כ": 20, "ל": 30, "מ": 40, "נ": 50,
#               "ס": 60, "ע": 70, "פ": 80, "צ": 90, "ק": 100, "ר": 200,
#                "ש": 300, "ת": 400, "ך": 500, "ם": 600, "ן": 700, "ף": 800,
#                 "ץ": 900}
