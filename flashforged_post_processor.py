import sys
import os

def remove_extra_g1_when_multi_material(file_name, env_slicer_pp_output_name):
    with open(file_name, "r") as f:
        read_file_lines = f.readlines()
    
    total_tool_changes = None
    for line in read_file_lines:
        if "START_PRINT" in line:
            start_line_slices = line.split(" ")
            for slice in start_line_slices:
                if "TOTAL_TOOL_CHANGES" in slice:
                    total_tool_changes = slice[-1]
                    break
            break
        
    if total_tool_changes != '0':
        output_slices = env_slicer_pp_output_name.split(".")
        env_slicer_pp_output_name = output_slices[0].replace(" ", "") + "_FIXED" + "." + output_slices[1]

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

try:
    env_slicer_pp_output_name = str(os.getenv('SLIC3R_PP_OUTPUT_NAME'))
    file_name = sys.argv[1]
    
    remove_extra_g1_when_multi_material(file_name, env_slicer_pp_output_name)


except Exception as e:
    print(e)
    input()