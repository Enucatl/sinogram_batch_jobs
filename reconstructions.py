import numpy as np
import subprocess

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

centers = np.loadtxt("centers.log")
for center, folder in zip(centers, folders):
    command="prj2sinSGE -d -k 0 -I 0 -R 0 -g 0 -f 1801,0,0,0,0 -p {0}####.fltp.DMP -Z 0.5 -c {1} -F schepp -t 16 --jobname={0}_reco --queue=tomcat_offline.q -o /sls/X02DA/Data10/e13657/matteo_high_resolution/{0}/sino_tmp/ -O /sls/X02DA/Data10/e13657/matteo_high_resolution/{0}/rec_16bit/ /sls/X02DA/Data10/e13657/matteo_high_resolution/{0}/fltp/;".format(folder, center)
    print(command)
    subprocess.call(command.format(folder), shell=True)
