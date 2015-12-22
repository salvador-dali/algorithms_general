def drawing(n):
    head = "  /\\\n  ||"
    middle = " /||\\\n/:||:\\"
    tail = "|/||\|\n  **\n  **"
    add_1 = "  ||"
    add_2 = "|:||:|"
    print head
    for i in xrange(n-1):
        print add_1
    print middle
    for i in xrange(n-1):
        print add_2
    print tail


drawing(input())