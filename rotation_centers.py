from tomopy.recon.rotation import find_center
import tomopy
import os.path
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

folders = [
    "KO202_LL_control_1",
    # "KO202_LL_control_2",
    # "KO202_LL_control_3",
    # "KO203_LL_control_1",
    # "KO203_LL_control_2",
    # "KO203_LL_control_3",
    # "ko373_LL_smoke_1",
    # "ko373_LL_smoke_2",
    # "ko373_LL_smoke_3",
    # "WT223_LL_control_1",
    # "WT223_LL_control_2",
    # "WT223_LL_control_3",
    # "WT224_LL_control_1",
    # "WT224_LL_control_2",
    # "WT224_LL_control_3",
    # "WT256_LL_smoke_1",
    # "WT256_LL_smoke_2",
    # "WT256_LL_smoke_3",
    # "WT256_LL_smoke_4",
    # "WT353_LL_smoke_1",
    # "WT353_LL_smoke_2",
    # "WT353_LL_smoke_3",
    # "WT355_LL_smoke_1",
    # "WT355_LL_smoke_2",
    # "WT355_LL_smoke_3"
]

for folder in folders:
    base_folder = "/sls/X02DA/data/e13657/Data10/matteo_high_resolution/"
    input_filenames = glob(os.path.join(base_folder, folder, "sin", "*.DMP"))
    input_filename = input_filenames[len(input_filenames) // 2]
    with open(input_filename, "rb") as input_file:
        header = np.fromfile(input_file, dtype=np.int16, count=3)
        shape = (header[1], header[0])
        image = np.fromfile(input_file, dtype=np.float32).reshape(shape)
        plt.imshow(image, cmap='Greys_r')
        plt.show()
        plt.ion()
        input()
        image = image[:, np.newaxis]
        print(image.shape)
        center = find_center(
            image, 
            theta=tomopy.angles(image.shape[0]),
            init=1403,
            tol=0.1,
            # ind=0,
            # mask=True,
            # ratio=0.5,
            # sinogram_order=True,
        )
        print(center)
