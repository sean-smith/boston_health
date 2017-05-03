import time
import os

start = time.time()
for i in range(100):
    f = open('test.txt', 'w')
    f.write("(define y1::real)")
    f.write("(define y2::real)")
    f.write("(define x1::real)")
    f.write("(define x2::real)")
    f.write("(define px::real)")
    f.write("(define py::real)")

    f.write("(assert (= y1 0.01293124))")
    f.write("(assert (= y2 -123.234234234))")

    f.write("(assert (= x1 9834.234234))")
    f.write("(assert (= x2 -123p34,34r5))")

    f.write("(assert (= py 0.123834578))")
    f.write("(assert (= px -12l,2434212))")

    f.write("(assert (and (or (and (< py y1) (> py y2)) (and (< py y2) (> py y1))) (or (< px x1) (< px x2))))")
    f.write("(check)")

    os.remove("test.txt")

stop = time.time()
print("Took", stop - start, "seconds")