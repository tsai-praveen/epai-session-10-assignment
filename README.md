# epai-session-10-assignment - Making a class iterable using an iterator

## Polygon
This is the given Polygon class which has all the functionality related to Polygon.

## GenericIterator
This is iterator class which can applied to any iterable class as long as it has defined the __len__ function.
The iterable class registers the iterator class (i.e. this class) in its __iter__ function.
So, the next() function call arrives in this class.
Now, this class can check on length of the iterable class and stop once the limit is reached.
It can even reset the index to circle back to the beginning once the items are exhausted.

## Polygons
This is the iterable class that needs to be modified to register the GenericIterator class in the __iter__ method.
The reference to self is passed as a argument while creating the iterator.

## Testing methodology
The classes were tested two ways...
1. By using the stock test code received.
2. By creating the Polygons object once, and running it twice with 2 for loops and two while loops.

## Colab link
https://colab.research.google.com/drive/1cns-SSPX47PTIoEsBUrupGN2bk9M7b04?usp=sharing