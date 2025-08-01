def reverse_sentence(a):
    words = a.split()
    rev= words[::-1]
    return ' '.join(rev)

print(reverse_sentence('hi there'))


