import sys
import os

try:
    env_slicer_pp_output_name = str(os.getenv('SLIC3R_PP_OUTPUT_NAME'))
    #for s in sys.argv:
    #    print(s)
    print(env_slicer_pp_output_name)
    with open(sys.argv[1], "r") as f:
        read_file_lines = f.readlines()

    with open(env_slicer_pp_output_name, "w" , encoding='UTF-8') as f:
        first_G1_removed = False
        for line in read_file_lines:
            if first_G1_removed == False:
                if "G1" not in line:
                    f.write(line)
                elif "G1" in line:
                    first_G1_removed = True
            elif first_G1_removed and "set bed temperature" not in line:
                f.write(line)
        f.close()

except Exception as e:
    print(e)
    input()