import imageio.v3 as iio

filenames = ['pic1.jpg', 'pic2.jpg','pic3.jpg','pic4.jpg','pic5.jpg','pic6.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('chicken.gif', images, duration = 500, loop = 0)