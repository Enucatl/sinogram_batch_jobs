from tomopy.recon.rotation import find_center_pc
import os.path
from glob import glob
import tifffile

folders = [
    "KO202_LL_control_1",
    "KO202_LL_control_2",
    "KO202_LL_control_3",
    "KO203_LL_control_1",
    "KO203_LL_control_2",
    "KO203_LL_control_3",
    "ko373_LL_smoke_1",
    "ko373_LL_smoke_2",
    "ko373_LL_smoke_3",
    "WT223_LL_control_1",
    "WT223_LL_control_2",
    "WT223_LL_control_3",
    "WT224_LL_control_1",
    "WT224_LL_control_2",
    "WT224_LL_control_3",
    "WT256_LL_smoke_1",
    "WT256_LL_smoke_2",
    "WT256_LL_smoke_3",
    "WT256_LL_smoke_4",
    "WT353_LL_smoke_1",
    "WT353_LL_smoke_2",
    "WT353_LL_smoke_3",
    "WT355_LL_smoke_1",
    "WT355_LL_smoke_2",
    "WT355_LL_smoke_3"
]

for folder in folders:
    base_folder = "/sls/X02DA/data/e13657/Data10/matteo_high_resolution/"
    input_filenames = sorted(glob(os.path.join(base_folder, folder, "tif", "*.tif")))
    first_name = input_filenames[130]
    last_name = input_filenames[130 + 1800]
    first = tifffile.imread(first_name)
    last = tifffile.imread(last_name)
    center = find_center_pc(
        first, last,
        tol=0.1,
    )
    print(center)
