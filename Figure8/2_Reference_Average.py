import os

if __name__ == '__main__':
    rootpath = "/Volumes/OneTouch/Resampled"
    for dir2 in os.listdir(rootpath):
        path2 = rootpath + "/" + dir2
        if os.path.isdir(path2):
            for dir3 in os.listdir(path2):
                path3 = path2 + "/" + dir3
                path4 = path2 + "/" + dir3
                if os.path.isdir(path3):
                    for dir4 in os.listdir(path3):
                        if len(dir4) > 20 and dir4.endswith(".nc") and (not dir4.startswith("._")):
                            input_path = path3 + "/" + dir4
                            output_path = path2 + "/" + dir4.replace("1981-2010", "ReferenceAverage")
                            print("********"+path4)
                            #cmd1 = "cdo -timselavg,29 -select,startdate=1982-01-16,enddate=2010-12-01 " + input_path + " " + output_path
                            cmd1 = "cdo -timselavg,30 -select,startdate=1981-07-16,enddate=2010-07-16 " + input_path + " " + output_path
                            print("cmd1:   " + cmd1)
                            os.system(cmd1)
                            print("+++++++++++++++++++++++++++++")