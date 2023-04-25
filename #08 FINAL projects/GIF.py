import imageio.v2 as imageio

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

for name in filenames:
    images.append(imageio.imread(name))


imageio.mimsave('test.gif', images, duration = 0.2)