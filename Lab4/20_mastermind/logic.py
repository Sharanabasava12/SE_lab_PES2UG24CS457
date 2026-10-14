def feedback(code, guess):
    exact = 0
    code_used = [False] * len(code)
    guess_used = [False] * len(guess)

    # First pass: exact matches
    for i in range(len(code)):
        if code[i] == guess[i]:
            exact += 1
            code_used[i] = True
            guess_used[i] = True

    # Second pass: partial matches
    partial = 0

    for i in range(len(guess)):
        if guess_used[i]:
            continue

        for j in range(len(code)):
            if code_used[j]:
                continue

            if guess[i] == code[j]:
                partial += 1
                code_used[j] = True
                guess_used[i] = True
                break

    return exact, partial