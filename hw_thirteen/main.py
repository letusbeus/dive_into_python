from rect import Rectangle
import view

if __name__ == '__main__':
    view.task()
    rec_1 = Rectangle(0, 2)
    #exceptions.RectangleValueError: The value cannot be negative or zero.
    print(f'{rec_1.perimeter()= }, {rec_1.rec_sqr()= }')

    rec_2 = Rectangle('ww', 4)
    #exceptions.RectangleTypeError: The value of side can only be a number, you specified <class 'str'>, value: ww
    print(f'{rec_2.perimeter()= }, {rec_2.rec_sqr()= }')
    