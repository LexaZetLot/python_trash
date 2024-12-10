#include "iostream.h"
#include "number.h"

main()
{
    Number *num;
    int res, val;

    num = new Number(1);
    num->add(4);
    num->display();
    num->sub(2);
    num->display();

    res = num->square();
    cout << "square: " << res << endl;

    num->data = 99;
    val = num->data;
    cout << "data:   " << val << endl;
    cout << "data+1: " << val + 1 << endl;

    num->display();
    cout << num << endl;
    delete num;
}