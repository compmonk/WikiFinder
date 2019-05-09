class OccurrenceList(list):
    def union(self, other):
        """
        Create a union with other list based on the item's index
        :param other: The list to create union with
        :return: The union of self and the other list
        """
        i = 0
        j = 0
        n1 = len(self)
        n2 = len(other)
        unison = OccurrenceList()

        while i < n1 and j < n2:
            if self[i] < other[j]:
                unison.append(self[i])
                i += 1
            elif self[i] == other[j]:
                unison.append(self[i])
                i += 1
                j += 1
            else:
                unison.append(other[j])
                j += 1

        while i < n1:
            unison.append(self[i])
            i += 1
        while j < n2:
            unison.append(other[j])
            j += 1

        return unison

    def intersect(self, other):
        """
        Find intersecting items based on the item's index
        :param other: The other list to intersect with
        :return: The intersection of self with the other list
        """
        i = 0
        j = 0
        intersection = OccurrenceList()

        while i < len(self) and j < len(other):
            if self[i] < other[j]:
                i += 1
            elif self[i] > other[j]:
                j += 1
            elif self[i] == other[j]:
                intersection.append(self[i])
                i += 1
                j += 1
        return intersection

    def index_of(self, value, attr=None):
        """
        Find index of an object in the occurrence list
        matching the attr attribute if any else match
        the object
        :param value: The value to find in the list, in
        case of objects the value of the attr passed
        :param attr: The attribute to match the value
        with for objects
        :return: index of the value or object in the
        list if found else -1
        """
        if attr:
            return next((i for i, item in enumerate(self) if getattr(item, attr) == value), -1)
        return self.index(value) if value in self else -1
