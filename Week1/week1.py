def basics():
    # lists
    a = [1, 'a', 2, 'b']
    b = [1, 'a', 2, 'b']
    print(type(a))  # <class 'list'>

    a.append(3.3)
    print(a == (b + [3.3]))

    # strings as lists
    s = 'This is a string'
    print(s[0])  # first character
    print(s[0:1])  # first character, but we have explicitly set the end character
    print(s[0:2])  # first two characters

    print(s[-1])  # last character
    print(s[-4:-2])  # slice starting from the 4th element from the end and stopping before the 2nd element from the end

    # dictionaries
    d = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
    print(d)
    d['Kevyn Collins-Thompson'] = None
    print(d)

    for name in d:
        print('Name: ' + name)
        if d[name] is None:
            print('email is None')
        else:
            print('email via indexing: {}'.format(d[name]))

    for email in d.values():
        if email is None:
            print('email is None')
            continue
        print('email: ' + email)

    for name, email in d.items():
        print(name)
        print(email)

    # maps and lambdas
    store1 = [10.00, 11.00, 12.34, 2.34]
    store2 = [9.00, 11.10, 12.34, 2.01]
    cheapest = map(min, store1, store2)
    print('type of map = {}'.format(type(cheapest)))
    for item in cheapest:
        print(item)

    forget_last = lambda a, b, c : a + b
    print('forget_last = {}'.format(forget_last(4, 5, 6)))

    # list comprehensions
    even_numbers = [number for number in range(0,10) if number % 2 == 0]
    print(even_numbers)


def csv_examples():
    import csv

    # MPG - miles per gallon

    with open('resources/mpg.csv') as csvfile:
        mpg = list(csv.DictReader(csvfile))
        # By using DictReader, we convert the data into a dictionary and then use list() on that to convert it into a
        # list of dictionaries. Now, mpg is an OrderedDict which is a list of dictionaries in the original sense but
        # is output as a list of tuples where the first element in the tuple is the key and the second element is the
        # value.
    print('Csv has {} lines'.format(len(mpg)))
    print('Csv keys are {}'.format(mpg[0].keys()))

    def mpg_to_l100km(mpg):
        litres_in_gallon = 3.7854
        kms_in_mile = 1.609

        res = float(mpg) * kms_in_mile  # kms per gallon
        res = 1 / res  # gallons per km
        res = litres_in_gallon * res  # litres per km
        return res * 100  # litres per 100 km

    print('first three dictionaries in csv list {}'.format(mpg[:3]))

    print('average city fuel economy = {}'.format(sum(float(d['cty']) for d in mpg) / len(mpg)))
    print('average city fuel economy in litres = {}'.format(sum(mpg_to_l100km(float(d['cty'])) for d in mpg) / len(mpg)))
    print('average highway fuel economy = {}'.format(sum(float(d['hwy']) for d in mpg) / len(mpg)))
    print('average highway fuel economy in litres = {}'.format(sum(mpg_to_l100km(float(d['hwy'])) for d in mpg) / len(mpg)))

    cylinders = set(d['cyl'] for d in mpg)
    CtyByCyl = []
    for c in cylinders:  # iterate over all the cylinder levels
        summpg = 0
        sumkm = 0
        cyltypecount = 0
        for d in mpg:  # iterate over all dictionaries
            if d['cyl'] == c:  # if the cylinder level type matches,
                summpg += float(d['cty'])  # add the cty mpg
                sumkm += mpg_to_l100km(float(d['cty']))  # add the cty l/100km
                cyltypecount += 1  # increment the count
        CtyByCyl.append((c, summpg / cyltypecount, sumkm / cyltypecount))  # append the tuple ('cylinder', 'avg mpg', avg l/100km)

    CtyByCyl.sort(key=lambda x: x[0])
    print(CtyByCyl)

    vehicleclass = set(d['class'] for d in mpg)
    print('vehicle class types are {}'.format(vehicleclass))

    HwyByClass = []
    for t in vehicleclass:  # iterate over all the vehicle classes
        summpg = 0
        sumkm = 0
        vclasscount = 0
        for d in mpg:  # iterate over all dictionaries
            if d['class'] == t:  # if the vehicle type matches,
                summpg += float(d['hwy'])  # add the hwy mpg
                sumkm += mpg_to_l100km(float(d['hwy']))  # add the hwy l/100km
                vclasscount += 1  # increment the count
        HwyByClass.append((t, summpg / vclasscount, sumkm / vclasscount))  # append the tuple ('class', 'avg mpg', 'l/100km')

    HwyByClass.sort(key=lambda x: x[1])
    print(HwyByClass)


def time_examples():
    import datetime as dt
    import time as tm

    current_time = tm.time()
    dtnow = dt.datetime.fromtimestamp(current_time)
    print('Current timestamp is {}, date is {}'.format(current_time, dtnow))

    delta = dt.timedelta(days=100)
    current_local_date = dt.date.today()
    hundred_days_ago = current_local_date - delta
    print('Today is {}, hundred days ago it was {}'.format(current_local_date, hundred_days_ago))
    print(current_local_date > hundred_days_ago)


def numpy_basics():
    import numpy as np

    mylist = [1, 2, 3]
    x = np.array(mylist)
    print('python list: {}'.format(mylist))
    print('np.array: {}'.format(x))

    m = np.array([[7, 8, 9], [10, 11, 12]])
    print("multidim array:\n{}\nIts shape is {}".format(m, m.shape))

    n = np.arange(0, 30, 2)  # start at 0 count up by 2, stop before 30
    print('vector: {}'.format(n))
    n = n.reshape(3, 5)
    print('Same vector reshaped to 3x5:\n{}'.format(n))

    o = np.linspace(0, 4, 9)  # return 9 evenly spaced values from 0 to 4 including
    print('Evenly spaced vector: {}'.format(o))
    o.resize(3, 3)
    print('Vector reshaped to 3x3 in-place:\n{}\n'.format(o))
    # both reshape and resize require multiplication of dimensions of the new array to be equal to length of the vector

    print('Matrix of ones (float):\n{}\n'.format(np.ones((3, 2))))
    print('Matrix of ones (int):\n{}\n'.format(np.ones([3, 2], int)))
    print(np.zeros((2, 3)))
    print('\nIdentity Matrix of size 3:\n{}'.format(np.eye(3)))
    print('\nDiagonal of\n{} is {}\n'.format(o, np.diag(o)))
    print('Diagonal array from {} is\n{}\n'.format(x, np.diag(x)))

    print('One-dim array of a repeated list: {}'.format(np.array([1, 2, 3] * 3)))
    print('One-dim array of a list, elements repeated: {}'.format(np.repeat([1, 2, 3], 3)))
    print('Vertical stack (2-D array of a list and its copy with numbers doubled:\n{}'.format(np.vstack([x, 2*x])))
    print('Horizontal stack (1-D array of a list and its copy with numbers doubled:\n{}\n'.format(np.hstack([x, 2*x])))

    # Operations
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print('element-wise addition: {}'.format(x + y))
    print('element-wise subtraction: {}'.format(x - y))
    print('element-wise multiplication: {}'.format(x * y))
    print('element-wise power: {}'.format(x**2))
    print('Dot product: {}'.format(x.dot(y)))  # dot product  1*4 + 2*5 + 3*6 = 32
    z = np.array([y, y ** 2])
    print('before transposing array`s shape is {}, type of elements is {} and it is:\n{}'.format(z.shape, z.dtype, z))
    zT = z.T
    print('after transposing array`s shape is {} and it is:\n{}'.format(zT.shape, zT))
    print('Type of changed elements is {}\n'.format(z.astype('f').dtype))

    # Math functions
    a = np.array([-4, -2, 1, 3, 5])
    print('a.sum() = {}'.format(a.sum()))
    print('a.max() = {}'.format(a.max()))  # PyCharm highlights it by mistake
    print('a.min() = {}'.format(a.min()))  # PyCharm highlights it by mistake
    print('a.argmax() = {}'.format(a.argmax()))
    print('a.argmin() = {}'.format(a.argmin()))
    print('a.mean() = {}'.format(a.mean()))
    print('a.std() = {}'.format(a.std()))

    r = np.arange(36)
    r.resize((6, 6))
    print('2-D array:\n{}\nand its slice:\n{}\n'.format(r, r[:2, 3:6]))
    r1 = r.copy()
    r1[r1 > 30] = 30
    print('Show all values greater than 30:\n{}\nand set them to 30:\n{}\n'.format(r[r > 30], r1))

    test = np.random.randint(0, 10, (4, 3))
    print('Random array by rows:')
    for row in test:
        print(row)
    print('Same array by index:')
    for i in range(len(test)):
        print(test[i])
    print('Same array by row and index:')
    for i, row in enumerate(test):
        print('row', i, 'is', row)
    test2 = test ** 2
    print('Zip:')
    for i, j in zip(test, test2):
        print(i, '+', j, '=', i + j)


if __name__ == '__main__':
    basics()
    csv_examples()
    time_examples()
    numpy_basics()
