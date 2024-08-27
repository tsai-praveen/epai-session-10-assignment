import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
        
class GenericIterator():
    def __init__(self, iterated_obj) -> None:
        # print("Generic Iterator init")
        self._iterated_obj = iterated_obj
        self._idx = 0
    
    # def __len__(self):
    #     print("Generic Iterator Len")
    #     return self._m - 2

    # def __iter__(self):                   # This is purposefully commented and it doesn't seem to be needed
    #     print("Generic Iterator iter")
    #     return self

    def __next__(self):
        # print("Generic Iterator next")
        if self._idx >= len(self._iterated_obj):
            self._idx = 0   # Reset the index
            raise StopIteration
        else:
            self._idx += 1
            return self._iterated_obj._polygons[self._idx - 1]
        
class Polygons:
    def __init__(self, m, R):
        print("Polygons Init")
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        
    def __len__(self):
        # print("Polygons Len")
        return self._m - 2
    
    def __repr__(self):
        # print("Polygons repr")
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __getitem__(self, s):
        # print("Polygons getitem")
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]
    
    # Code to make Polygons iterable                                - New code from here
    def __iter__(self):
        # print("Polygons iter")
        return GenericIterator(self)
    
    def __next__(self):
        # print("Polygons next")
        if self._idx >= len(self._iterated_obj):
            self._idx = 0   # Reset the index
            raise StopIteration
        else:
            self._idx += 1
            return self._iterated_obj._polygons[self._idx - 1]
    
