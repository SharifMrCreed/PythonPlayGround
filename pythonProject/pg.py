def find_changed_parts(string1, string2):
    changed_parts = ""
    if len(string1) > len(string2):
        reference_string = string1
        shorter_string = string2
    else:
        reference_string = string2
        shorter_string = string1
    for i in range(len(shorter_string)):
        if shorter_string[i] != reference_string[i]:
            changed_parts += reference_string[i]
    if len(reference_string) > len(shorter_string):
        changed_parts += reference_string[len(shorter_string):]
    return changed_parts


# Example usage:
a = "hello"
b = "banange banange omusajja bamutwala"
changes = find_changed_parts(a, b)
print("Changed parts: " + changes)
