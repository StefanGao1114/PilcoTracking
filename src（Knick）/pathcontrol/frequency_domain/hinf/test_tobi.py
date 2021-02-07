from PIL import Image
import cv2
import numpy
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

SIZE = (int(216), int(384))
image = cv2.imread("/home/ilja/02_diss_ws/src/04_path_tracking/pathtracking_all/src/pathcontrol/frequency_domain/hinf/image-086.jpeg", 0)
a = numpy.asarray(image)
print(a.shape)
image = cv2.resize(image,(SIZE[1], SIZE[0]))



img = cv2.imread("/home/ilja/02_diss_ws/src/04_path_tracking/pathtracking_all/src/pathcontrol/frequency_domain/hinf/image-086_mask1.jpeg",0)
img = cv2.resize(img,(SIZE[1], SIZE[0]))
im = img
schwad = np.array(im)
print("schwad shape:", schwad.shape)


new_im = Image.fromarray(schwad)
imgplot = plt.imshow(new_im)
# plt.show()




indices = []
for idx, val in np.ndenumerate(schwad):
    if val > 250:
        indices.append([idx[0], idx[1]])
indices = np.array(indices)
print(indices.shape)




import numpy as np
from sklearn.neighbors import KDTree
tree = KDTree(indices)


test= np.random.random((19, 1))
nearest_dist, nearest_ind = tree.query(test, k=1)  # k=2 nearest neighbors where k1 = identity

# for num



