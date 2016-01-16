import java.io.*;
import java.util.*;

class Shape { 
    char type;
    Shape(char t) {
        type = t;
    }
}
class Circle extends Shape { 
    Circle() {
        super('c');
    }
}
class Rectangle extends Shape { 
    Rectangle() {
        super('r');
    }
}

class Node<T> {
    T t;

    void desc() {
        String s = t.getClass().toString();
        System.out.println("I am " + s);
    }

    T descWithReturn() {
        desc();
        return t;
    }
}

class GenericTesting {

    static  void debugShape(Node<? extends Rectangle> s) {
        s.desc();
    }

    static Object debugReturnShape(Node<? super Circle> s) {
        s.desc();
        return s.t;
    }

    public static void main(String[] args) {
        Node<Circle> c = new Node<Circle>();
        c.t = new Circle();
        Node<Rectangle> r = new Node<Rectangle>();
        r.t = new Rectangle();
        Node<? extends Shape> s;
        s = r;

        debugShape(s);
        debugShape(c);
        debugShape(r);

        debugReturnShape(s);
        debugReturnShape(c);
        debugReturnShape(r);
    }
}
