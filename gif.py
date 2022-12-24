import os
import imageio
file_list = sorted(os .listdir("images"))


images =[]
for file_name in file_list:
    file_path = 'images/' + file_name
    image = imageio.imread(file_path)
    images.append(image)

imageio.mimsave('mygif.gif', images)