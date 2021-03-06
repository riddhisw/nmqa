import sys
import os
import copy
import traceback
import numpy as np

########################
# Find qslam modules
########################
sys.path.append('../qslam')

from singlerun import SingleRunAnalysis
from riskanalysis import EngineeredTruth
from qslamdesignparams import GLOBALDICT

########################
# Taking in bash parameters
########################
idx_prefix = int(sys.argv[1])
# truth flag type (five options)
# 0 - Linear 1D field, 25 qubit array
# 1 - Square 2D field, 25 qubit array
# 2 - Gaussian 2D array, 25 qubit array
# 3 - Square 2D field, 9 qubit array
# 4 - Square 2D field, 16 qubit array

idx_job_array = int(sys.argv[2]) # job array starts from 1

########################
# Truth Parameters
########################

# Choose defaults to match floor case (heights didn't work)
TRUTHKWARGS = {}

BARRIER_FLOOR = 0.25*np.pi
BARRIER_HEIGHT = 0.75*np.pi
FLOOR_RATIO = 0.4 # matches floor case

TRUTHKWARGS["OneStepdheight"] = {"low": BARRIER_FLOOR, 
                                 "high": BARRIER_HEIGHT} 
TRUTHKWARGS["OneStepdfloorarea"] = FLOOR_RATIO 


########################
# Save to path 
########################

path = '/scratch/QCL_RG/qslamdatapaper_v3/' # on Artemis
# path = './data_ALPHA_test/'

########################
# Set true field
########################

if idx_prefix == 0:
    change_gridconfig = True # 1D
    TRUTHFLAG = None # use TRUTHKWARGS
    TRUTHKWARGS["truthtype"] = 'OneStepd' 

if idx_prefix == 1: 
    change_gridconfig = False # 2D
    TRUTHFLAG = None # use TRUTHKWARGS
    TRUTHKWARGS["truthtype"] = 'OneStepq' 

if idx_prefix == 2:
    change_gridconfig = False # 2D
    TRUTHFLAG = None # use TRUTHKWARGS
    TRUTHKWARGS["truthtype"] = 'Gaussian' 
    
if idx_prefix > 2: # Covers all truth flag options except 2.
    change_gridconfig = False # 2D
    TRUTHFLAG = None # use TRUTHKWARGS
    TRUTHKWARGS["truthtype"] = 'OneStepq' 

########################
# Set 1D Hardware if req
########################

num_of_nodes = len(GLOBALDICT["GRIDDICT"])

if change_gridconfig is True:
    
    GLOBALDICT["GRIDDICT"] = {}
    
    for idx_posy in range(num_of_nodes):
        
        if idx_posy < 10 :
            
            GLOBALDICT["GRIDDICT"]["QUBIT_0" + str(idx_posy)] = (0.0, float(idx_posy))
            
        if idx_posy >= 10 :
            
            GLOBALDICT["GRIDDICT"]["QUBIT_" + str(idx_posy)] = (0.0, float(idx_posy))

########################
# Change 2D Grid Size if req
########################

if idx_prefix == 3:
    from qslamdesignparams import GRIDDICT_9
    GLOBALDICT["GRIDDICT"] = copy.deepcopy(GRIDDICT_9)
    num_of_nodes = len(GLOBALDICT["GRIDDICT"])

if idx_prefix == 4:
    from qslamdesignparams import GRIDDICT_16
    GLOBALDICT["GRIDDICT"] = copy.deepcopy(GRIDDICT_16)
    num_of_nodes = len(GLOBALDICT["GRIDDICT"])

########################
# Set Defaults
########################

GLOBALDICT["MODELDESIGN"]["MAX_NUM_ITERATIONS"] = 75
GLOBALDICT["MODELDESIGN"]["MSMTS_PER_NODE"] = 1
GLOBALDICT["MODELDESIGN"]["MULTIPLER_R_MAX"] = 4.

repts = 50
particleconfigs = [ [3,2], [9,6], [15,10], [21,14], [30, 20]]

prefix = '_idx_prefix_'+str(idx_prefix)+'_'
lambda_paris_2 = np.load('lambda_pairs_2.npz')
random_variances = np.load('random_variances.npz')

IDX1_SHP = len(random_variances['g1var'])
IDX2_SHP = 30 # len(lambda_paris_2['lambda_1']) not doing all 250
IDX3_SHP = len(particleconfigs)



########################
# Run Script
########################

truemap_generator = EngineeredTruth(num_of_nodes, TRUTHKWARGS)
true_map_ = truemap_generator.get_map()

idx_1, idx_2 = np.unravel_index(idx_job_array - 1 , (IDX1_SHP, IDX2_SHP) )


GLOBALDICT["NOISEPARAMS"]["SIGMOID_APPROX_ERROR"]["SIGMA"] = random_variances['g2var'][idx_1]
GLOBALDICT["NOISEPARAMS"]["QUANTISATION_UNCERTY"]["SIGMA"] = random_variances['g1var'][idx_1]
GLOBALDICT["MODELDESIGN"]["LAMBDA_1"] = lambda_paris_2['lambda_1'][idx_2]
GLOBALDICT["MODELDESIGN"]["LAMBDA_2"] = lambda_paris_2['lambda_2'][idx_2]

fname_likelihood = 'rand_'+str(idx_1)+'_'+str(idx_2)+'_'


for idx_3 in range(IDX3_SHP):

    GLOBALDICT["MODELDESIGN"]["P_ALPHA"] = particleconfigs[idx_3][0]
    GLOBALDICT["MODELDESIGN"]["P_BETA"] = particleconfigs[idx_3][1]


    SAMPLE_GLOBAL_MODEL = copy.deepcopy(GLOBALDICT)


    uniform_r_expt = SingleRunAnalysis(SAMPLE_GLOBAL_MODEL, true_map_, repts, beta_expansion_mode=False, beta_skew_adjust=False)
    uniform_r_expt.run_analysis(path+'Uni_R'+prefix+fname_likelihood+str(idx_3))

    trunc_r_expt = SingleRunAnalysis(SAMPLE_GLOBAL_MODEL, true_map_, repts, beta_expansion_mode=True, beta_skew_adjust=False)
    trunc_r_expt.run_analysis(path+'Trunc_R'+prefix+fname_likelihood+str(idx_3))

