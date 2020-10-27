f = open("image.txt" , "r")

image = f.read()
size = len(image)

layer_size = 25 * 6

layers = [image[(i-1) * layer_size:(i * layer_size)] for i in range(1 , size // layer_size)]

few_zeros = [i.count('0') for i in layers]

few_zeros_layer = few_zeros.index(min(few_zeros))

print(few_zeros_layer)

print((layers[few_zeros_layer]).count('1') * (layers[few_zeros_layer]).count('2')) 

