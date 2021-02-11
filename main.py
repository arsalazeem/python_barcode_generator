from barcode import EAN13

# Make sure to pass the number as string
number = '5901234123457'

# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)
my_code.default_writer
# Our barcode is ready. Let's save it.
my_code.save("new_code.svg",options={"module_width":0.2 ,"module_height":7})