from common.io.writeToa import readToa
import numpy as np
import matplotlib.pyplot as plt
from config import globalConfig
my_toa_path=r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-L1B\00my_outputs"
isrf_path=r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-L1B\input"
reference_toa_path=r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-L1B\output"
bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
l1b_toa = 'l1b_toa_'
ism_toa = 'ism_toa_isrf_'

for band in bands:
    my_toa_output = readToa(my_toa_path, l1b_toa + band + '.nc')
    my_toa_input = readToa(isrf_path, ism_toa + band + '.nc')

    reference_toa = readToa(reference_toa_path, l1b_toa + band + '.nc')
    result = reference_toa-my_toa_output

    difference=result/my_toa_output*100

    print(np.all(difference < 0.01))

    middle_row_mytoa=my_toa_output[len(my_toa_output) // 2]
    middle_row_isrf = my_toa_input[len(my_toa_input) // 2]

    x = np.arange(150)
    plt.plot(x, middle_row_mytoa, color='blue', label='Vector 1', linestyle='-')
    plt.plot(x, middle_row_isrf, color='red', label='Vector 2', linestyle='-')

    plt.xlabel('ACT pixel [-]')
    plt.ylabel('TOA [mW/m2/sr]')
    plt.title('Vector Plot')

    plt.savefig('mytoa_vs_isrf%s.png' % band)
    plt.clf()
   # plt.show()

    # plotear la linea central
    #  For the central ALT position, plot the restored signal (l1b_toa), and the TOA after the ISRF
    # (ism_toa_isrf). Explain the differences.

    # Do another run of the L1B with the equalization enabled to false. Plot the restored signal for this case
    # and for the case with the equalization set to True. Compare.



