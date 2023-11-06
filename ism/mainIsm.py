
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\workbench\EODP\auxiliary'
indir = r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-ISM\input\gradient_alt100_act150" # small scene
outdir = r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-ISM\00my_outputs"
'''
auxdir = r'C:\workbench\EODP\auxiliary'
indir = r"C:\workbench\EODP_TER_2021\EODP-TS-E2E\sgm_out"  ##r"C:\workbench\EODP-TS-ISM\input\gradient_alt100_act150"
outdir = r"C:\workbench\EODP_TER_2021\EODP-TS-E2E\my_output_aux"  ##r"C:\workbench\EODP-TS-ISM\00my_outputs"
'''

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
