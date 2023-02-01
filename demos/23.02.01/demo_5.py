class F:
    def __init__(self):
        print("F%s" % super().__init__)
        super().__init__()


class G:
    def __init__(self):
        print("G%s" % super().__init__)
        super().__init__()


class H:
    def __init__(self):
        print("H%s" % super().__init__)
        super().__init__()


class E(G, H):
    def __init__(self):
        print("E%s" % super().__init__)
        super().__init__()


class D(E, F):
    def __init__(self):
        print("D%s" % super().__init__)
        super().__init__()


class C(E, G):
    def __init__(self):
        print("C%s" % super().__init__)
        super().__init__()


class B(C, H):
    def __init__(self):
        print("B%s" % super().__init__)
        super().__init__()


class A(D, B, E):
    def __init__(self):
        print("A%s" % super().__init__)
        super().__init__()


A.mro()
