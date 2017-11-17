import subprocess
import os.path

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
    if os.path.isdir(
        os.path.join(
            "..",
            folder,
            "sin")):
        continue
    
    command = "prj2sinSGE -d -C -f 1801,30,100,0,0 -I 1 -p {0}####.tif --jobname={0}_fltp --queue=tomcat_offline.q -Y 11.999,0.65E-6,3.7e-8,2.3e-10,0.008 -g 3 -o /sls/X02DA/data/e13657/Data10/matteo_high_resolution/{0}/fltp/ /sls/X02DA/data/e13657/Data10/matteo_high_resolution/{0}/tif/;prj2sinSGE -d -g 0 -I 0 -f 1801,0,0,0,0 -k 1 --hold={0}_fltp --jobname={0}_sin --queue=tomcat_offline.q -j 50 -p {0}####.fltp.DMP -o /sls/X02DA/data/e13657/Data10/matteo_high_resolution/{0}/sin/ /sls/X02DA/data/e13657/Data10/matteo_high_resolution/{0}/fltp/;"

    subprocess.call(command.format(folder), shell=True)
