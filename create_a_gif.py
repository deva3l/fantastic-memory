import imageio as io

filenames = ['Image 2025-07-20 at 22.40.19_4637cf55.jpg', 'WhatsApp Image 2025-07-20 at 22.40.19_5292a40a.jpg']
images = []
for filename in filenames:
    images.append(io.imread(filename))

io.mimsave('team.gif', images, duration=250, loop=0)
# The GIF will be saved as 'team.gif' with a duration of 0.5 seconds per frame and will loop indefinitely.
print("GIF created successfully!")
