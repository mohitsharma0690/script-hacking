
class Rect:
    def __init__(self, x, y, w=1, h=1):
        self.origin_x = x
        self.origin_y = y
        self.width = w
        self.height = h

    def does_rect_contain_rect(self, r):
        ''' Returns True if r is contained within this rect '''
        return self.origin_x <= r.origin_x and \
                self.origin_y <= r.origin_y and \
                r.origin_x + r.width <= self.origin_x + self.width and \
                r.origin_y + r.height <= self.origin_y + self.height

    def mid_point(self):
        return (self.origin_x + self.width / 2, 
                self.origin_y + self.height / 2)

class QuadTree:
    MAX_OBJECTS = 5
    MAX_LEVELS = 5

    def __init__(self, level=0, bounds=Rect(0, 0, 100, 100), parent=None):
        self.__level = level
        self.__bounds = bounds
        self.__parent = parent
        self.__children = [None, None, None, None]
        self.__objects = []

    def clear(self):
        '''Clear the QuadTree'''
        del self.__objects[:]
        for child in self.__children:
            if child:
                child.clear()
        del self.__children[:]


    def find_quad_index(self, rect):
        '''Find the quadrant index where rect lies. Returns -1 if it lies in
        current tree else returns the index of the appropriate child quad.
        '''
        if not self.__bounds.does_rect_contain_rect(rect):
            return None

        mid_x, mid_y = self.__bounds.mid_point()
        if (rect.width + rect.origin_x) < mid_x and \
                (rect.height + rect.origin_y) < mid_y:
            return 1
        elif rect.width + rect.origin_x < mid_x and rect.height > mid_y:
            return 2
        elif rect.origin_x > mid_x and rect.origin_y + rect.height < mid_y:
            return 0
        elif rect.origin_x > mid_x and rect.origin_y > mid_y:
            return 3
        else:
            return -1

    def split(self):
        '''Split the QuadTreeNode into child QuadTreeNodes '''
        new_width = self.__bounds.width / 2
        new_height = self.__bounds.height / 2
        x = self.__bounds.origin_x
        y = self.__bounds.origin_y
        if not self.__children[0]:
            self.__children[0] = QuadTree(self.__level + 1, 
                    Rect(x + new_width,
                        y,
                        new_width,
                        new_height), self)
            self.__children[1] = QuadTree(self.__level + 1, 
                    Rect(x,
                        y,
                        new_width,
                        new_height), self)
            self.__children[2] = QuadTree(self.__level + 1,
                    Rect(x,
                        y + new_height,
                        new_width,
                        new_height), self)
            self.__children[3] = QuadTree(self.__level + 1, 
                    Rect(x + new_width,
                        y + new_height,
                        new_width,
                        new_height), self)
        else:
            raise Exception("Cannot split already split QuadTree with child \
                    count {0}".format(len(self.__children)))

    def insert(self, rect):
        '''Insert rect into the QuadTree'''
        if self.__children[0]: # check if this node has children or not
            idx = self.find_quad_index(rect)
            if idx != -1:
                self.__children[idx].insert(rect)
                return

        self.__objects.append(rect)
        if len(self.__objects) > QuadTree.MAX_OBJECTS and \
                self.__level < QuadTree.MAX_LEVELS:
            if not self.__children[0]:
                self.split()

            i = 0
            while i < len(self.__objects):
                idx = self.find_quad_index(self.__objects[i])
                if idx != -1:
                    self.__children[idx].insert(self.__objects[i])
                    self.__objects.pop(i)
                else:
                    i += 1

def main():
    ''' Test Quad Tree '''
    root = QuadTree()
    root.insert(Rect(2, 4, 10, 10)) # bl
    root.insert(Rect(55, 55, 16, 16)) # tr
    root.insert(Rect(60, 4, 20, 20)) # br
    root.insert(Rect(10, 80, 4, 4)) # tl
    root.insert(Rect(40, 40, 20, 20)) # middle
    root.insert(Rect(30, 30, 40, 40)) # middle
    assert(-1 == root.find_quad_index(Rect(40, 40, 20, 20)))
    assert(1 == root.find_quad_index(Rect(2, 4, 10, 10)))
    print "===== success ====="

if __name__ == '__main__':
    main()

