
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\workbench\EODP\auxiliary'
indir = r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-E2E\my_output_aux"
outdir = r"C:\workbench\EODP\EODP_TER_2021\EODP-TS-E2E\l1b_out"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
