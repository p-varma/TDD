import numpy

def metrix_multiplication(m1,m2):
    # create new empty metrix having all zero
    m3 = []
    # loop throught rows of m1
    for row in range(len(m1)):
        temp = []
        # loop through column of m2
        for column in range(len(m2[0])):
            temp.append(0)
        m3.append(temp)

    for row in range(len(m1)):
        for column in range(len(m2[0])):
            temp_element = 0
            for item in range(len(m2)):
                temp_element += m1[row][item]* m2[item][column]

            m3[row][column] = temp_element

    print(m3)



m1 =[[2,3,4],
     [6,5,4],
     [6,7,8]]

m2 = [[5,5,4,3,2],
      [7,6,5,4,3],
      [8,8,3,3,4]]

# using numpy
np1 = numpy.array(m1)
np2 = numpy.array(m2)
np3 = numpy.dot(np1,np2)

print("using numpy")
print(np3)
print('using function')

metrix_multiplication(m1,m2)