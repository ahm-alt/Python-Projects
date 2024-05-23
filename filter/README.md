# filter.py

## CS50
>This was my final project for conclude the CS50 Introduction to Computer Sciense using python course.
## Demonstration on youtube
[My Final Project presentation](https://www.youtube.com/watch?v=VIAgjS7TaB8)


## Description
My final project is a filter.py that allow the user to enter an image file and choose filter to apply to it between (BLUR - CONTOUR - DETAIL - EDGE_ENHANCE - EDGE_ENHANCE_MORE - EMBOSS - FIND_EDGES - SHARPEN - SMOOTH - SMOOTH_MORE) filter and then output a file of image with filter

### filter.py
-In filter.py i import (from sys I import exit, argv - from PIL I import Image, ImageFilter)

-my app take two argv(file.py, image file)

-I define a global variable (filters) of type dict that contain all filter that we can apply (BLUR - CONTOUR - DETAIL - EDGE_ENHANCE   - EDGE_ENHANCE_MORE - EMBOSS - FIND_EDGES - SHARPEN - SMOOTH - SMOOTH_MORE)

-I define main function that call all other function and desplay output to the terminal and take input(Inter index of filter that you want to apply to image) and render error messages if there is invalid image file or filter and also save the new amage

-I define check function that take as argrment list of argv . it return None if there are more than 2 item or if there are FileNotFoundError else it open image and return it

-I define convert function that take as argrment str(n) and convert it into int and check it valid or not
it return int(n) if valid else return None

-I define apply_filter function that take as argrment (image, filter to apply) it return image with choosen filter(BLUR - CONTOUR - DETAIL - EDGE_ENHANCE   - EDGE_ENHANCE_MORE - EMBOSS - FIND_EDGES - SHARPEN - SMOOTH - SMOOTH_MORE)

### test_filter.py
in test_filters.py
-I import (check-convert-apply_filter) from filter.py
-I import image_filter from PIL
-I define test_check that test check function from filter.py
-I define test_convert that test convert function from filter.py
-I define test_apply_filter that test apply_filter function from filter.py
-program ran as excepect

### requirment.txt
-only install PIL



### bridge.bmp
its the image that i test my code


## Documentation
https://python.org

https://docs.python.org/3/


## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

- Where I get CS50 course?
https://cs50.harvard.edu/