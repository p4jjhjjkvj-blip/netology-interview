from stack import Stack


def check_brackets(brackets):
    stack = Stack()

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for bracket in brackets:
        if bracket in "([{":
            stack.push(bracket)

        elif bracket in ")]}":
            if stack.is_empty():
                return "Несбалансированно"

            if stack.pop() != pairs[bracket]:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"

    return "Несбалансированно"


if __name__ == "__main__":
    examples = [
        "(((([{}]))))",
        "[([])((([[[]]])))]",
        "{()}",
        "}{}",
        "((()))"
    ]

    for example in examples:
        print(example, "->", check_brackets(example))