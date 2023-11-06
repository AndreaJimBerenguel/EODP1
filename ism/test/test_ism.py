from common.io.writeToa import readToa
from common.io.readMat import readMat
from common.io.readArray import readArray
import numpy as np
import matplotlib.pyplot as plt
from config import globalConfig

my_toa_path=r'C:\workbench\EODP\EODP_TER_2021\EODP-TS-ISM\00my_outputs'
lucia_toa_path=r'C:\workbench\EODP\EODP_TER_2021\EODP-TS-ISM\output'
figures=r'C:\workbench\EODP\EODP_TER_2021\EODP-TS-ISM\figures'

bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']

ism_toa = 'ism_toa_isrf_'


for band in bands:
    #read each output file
    my_toa_output = readToa(my_toa_path, ism_toa + band + '.nc')
    lucia_toa = readToa(lucia_toa_path, ism_toa + band + '.nc')

    #difference between the outputs
    result = lucia_toa-my_toa_output

    mask = np.logical_or(np.isnan(my_toa_output), np.isnan(lucia_toa))
    mask = np.logical_or(mask, my_toa_output == 0)

    # Handle cases where division is not possible
    difference = np.zeros_like(result)
    difference[~mask] = np.divide(result[~mask], my_toa_output[~mask], out=np.zeros_like(result[~mask]), where=my_toa_output[~mask]!=0) * 100

    #checking if the difference is lower than 0.01
    checking_difference=np.array(difference < 0.01)

    #sum the number of "TRUE" which are the values with a difference<0.01
    sum_trues=sum(checking_difference)

    #checking if "difference<0.01" for at least 3-sigma
    sigma3_checking=np.all(sum_trues >= 0.997*len(result))

    if(sigma3_checking== True):
        print("yes, differences with output TOA (", ism_toa + band,") are <0.01% for at least 3-sigma of the points.")
    else:
        print("no, differences with output TOA (", ism_toa + band,") are not <0.01% for at least 3-sigma of the points.")




    my_Hdiff = readMat(my_toa_path, 'Hdiff_' + band + '.nc')
    my_Hdefoc = readMat(my_toa_path, 'Hdefoc_' + band + '.nc')
    my_Hwfe = readMat(my_toa_path, 'Hwfe_' + band + '.nc')
    my_Hdet = readMat(my_toa_path, 'Hdet_' + band + '.nc')
    my_Hsmear = readMat(my_toa_path, 'Hsmear_' + band + '.nc')
    my_Hmotion = readMat(my_toa_path, 'Hmotion_' + band + '.nc')
#    my_Hsys = readMat(my_toa_path, 'Hsys_' + band + '.nc')
    my_fnAct = readArray(my_toa_path, 'fnAct_' + band + '.nc')
    my_fnAlt = readArray(my_toa_path, 'fnAlt_' + band + '.nc')

    #fnAct: 1D normalised frequencies 2D ACT (f/(1/w))
    nlines_ALT = my_Hdiff.shape[0]
    ACT_central_line = int(nlines_ALT / 2)
    nlines_ACT = my_Hdiff.shape[1]
    ALT_central_line = int(nlines_ACT / 2)


    # ACT
    plt.plot(my_fnAct[75:150], my_Hdiff[ACT_central_line, 75:150])
    plt.plot(my_fnAct[75:150], my_Hdefoc[ACT_central_line, 75:150])
    plt.plot(my_fnAct[75:150], my_Hwfe[ACT_central_line, 75:150])
    plt.plot(my_fnAct[75:150], my_Hdet[ACT_central_line, 75:150])
    plt.plot(my_fnAct[75:150], my_Hsmear[ACT_central_line, 75:150])
    plt.plot(my_fnAct[75:150], my_Hmotion[ACT_central_line, 75:150])
    plt.plot(my_fnAct[75:150], my_Hsys[ACT_central_line, 75:150], color='black', linewidth=2.5)
    plt.plot(np.full(2, 0.5), np.linspace(0, 1, 2), linestyle='--', color='black')
    plt.xlabel('Spatial frequencies f/(1/w) [-]')
    plt.ylabel('MTF')
    plt.title("System MTF, slice ACT for " + band + " (for the central pixels of ALT)")
    plt.legend(['Diffraction MTF', 'Defocus MTF', 'WFE Aberration MTF', 'Detector MTF', 'Smearing MTF', 'Motion blur MTF', 'System MTF','f Nyquist'])
    plt.xlim(-0.025, 0.525)
    plt.ylim(-0.025, 1.025)
    plt.savefig("ism_plot_MTF_ACT_" + band + ".png")
    plt.show()


    # ALT
    plt.plot(my_fnAlt[50:100], my_Hdiff[50:100, ALT_central_line])
    plt.plot(my_fnAlt[50:100], my_Hdefoc[50:100, ALT_central_line])
    plt.plot(my_fnAlt[50:100], my_Hwfe[50:100, ALT_central_line])
    plt.plot(my_fnAlt[50:100], my_Hdet[50:100, ALT_central_line])
    plt.plot(my_fnAlt[50:100], my_Hsmear[50:100, ALT_central_line])
    plt.plot(my_fnAlt[50:100], my_Hmotion[50:100, ALT_central_line])
    plt.plot(my_fnAlt[50:100], my_Hsys[50:100, ALT_central_line], color='black', linewidth=2.5)
    plt.plot(np.full(2, 0.5), np.linspace(0, 1, 2), linestyle='--', color='black')
    plt.xlabel('Spatial frequencies f/(1/w) [-]')
    plt.ylabel('MTF')
    plt.title("System MTF, slice ALT for " + band + " (for the central pixels of ACT)")
    plt.legend(
        ['Diffraction MTF', 'Defocus MTF', 'WFE Aberration MTF', 'Detector MTF', 'Smearing MTF', 'Motion blur MTF',
         'System MTF', 'f Nyquist'])
    plt.xlim(-0.025, 0.525)
    plt.ylim(-0.025, 1.025)
    plt.savefig(figures+"ism_plot_MTF_ALT_" + band + ".png")
    plt.show()





