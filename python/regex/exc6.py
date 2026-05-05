# -------------------------
# title: Email Validator
# -------------------------
# -------------------------
# Description: Regex.
# -------------------------
# ------------------------
# Author: Daniel Merchav.
# Reviewer: Anan Yablonko.
# AI2 InfinityLabs.
# ------------------------
import re


def email_validator(email: str) -> bool:
    return re.match(r"^([a-z0-9-]+)"
                    r"(\.?[a-z0-9-])*"
                    r"(@)"
                    r"([a-z0-9-]+)"
                    r"(\.co)"
                    r"(m|\.il|\.uk|\.au)$", email, flags=re.IGNORECASE) is not None


def main():
    email1 = "merdan148@gmail.com"
    email2 = "DF.com"
    email3 = "Daniel@mambo.co.il"
    assert email_validator(email1)
    assert email_validator(email2) is False
    assert email_validator(email3)
    print("Tests done.")


if __name__ == '__main__':
    main()
