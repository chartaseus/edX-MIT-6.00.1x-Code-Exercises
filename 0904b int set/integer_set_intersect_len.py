class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
    
    # Define an `intersect` method that returns a new intSet containing elements 
    # that appear in both sets. In other words, s1.intersect(s2) would return
    # a new intSet of integers that appear in both s1 and s2.
    def intersect(self, other):
        """
        other: another set of integers
        Returns a new intSet containing elements that appear in both sets. Returns an empty list if no elements in common.

        """
        newSet = intSet()
        for e in self.vals:
            if other.member(e):
                newSet.insert(e)
        return newSet
    
    # Add the appropriate method(s) so that len(s) returns the number of elements in s.
    def __len__(self):
        """Returns number of elements in self"""
        return len(self.vals)


s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
# s.remove(3)
# print(s)
#s.remove(3)
t = intSet()

t.insert(4)

t.insert(7)

t.insert(8)

print(t)