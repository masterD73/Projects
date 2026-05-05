# reviewer: Anan + Alexander.
def is_pass_ok(password) -> bool:
    if len(password) < 8:
        raise Exception("Password length is too short. 8 chars minimum.")
    if any(c.islower() for c in password) is not True:
        raise Exception("Password must also contain a lower-case char.")
    if any(c.isupper() for c in password) is not True:
        raise Exception("Password must also contain an upper-case char.")
    if any(c.isnumeric() for c in password) is not True:
        raise Exception("Password must also contain a digit.")
    if any(c in "@#%&" for c in password) is not True:
        raise Exception("Password must contain a special char. (@#%&)")
    return True


assert is_pass_ok("/////abc") is False
assert is_pass_ok("@#%&aD0\\") is True
tests = ["/////abc", "4fdas!@", "12345678", "brain fuel", "123Def@!", "@#%&aD0\\"]
for test in tests:
    print(f'password: {test}. result: {is_pass_ok(test)}')
