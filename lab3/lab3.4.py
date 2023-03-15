class myString(str):
    def append(self, other):
        return self + other

    def pop(self, index=-1):
        if index < 0:
            index += len(self)
        return self[:index] + self[index+1:]
