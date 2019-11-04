import sys
sys.path.append('../paduaq')
from pdpoints import dims_padua_set

SIMULATIONSDICT = {}
GRIDSIZE=25 # number of data qubits if padua qubits are used. else, total number of regularly arranged sensing qubits
MULTIPLIER=5

for padua_order in ["no_padua", 1, 2, 3, 4, 5, 10] : # Padua order for cheb2chev function
    
    SIMULATIONSDICT[padua_order] = {}
    
    if padua_order == "no_padua":
        SIMULATIONSDICT[padua_order]["max_iterations"] = GRIDSIZE * MULTIPLIER
        SIMULATIONSDICT[padua_order]["num_of_nodes"] = GRIDSIZE
    
    if padua_order != "no_padua":
        SIMULATIONSDICT[padua_order]["max_iterations"] = dims_padua_set(padua_order) * MULTIPLIER
        SIMULATIONSDICT[padua_order]["num_of_nodes"] = dims_padua_set(padua_order) + GRIDSIZE
    
    SIMULATIONSDICT[padua_order]["linear"] = False
    SIMULATIONSDICT[padua_order]["repts"] = 50
    SIMULATIONSDICT[padua_order]["functype"]= 'cheb2fun'
    
    for idx_expandtype in ["Uniform", "TruncGauss"]:
    
        SIMULATIONSDICT[padua_order][idx_expandtype] = {}
        SIMULATIONSDICT[padua_order][idx_expandtype]["optimal"] = {}
        SIMULATIONSDICT[padua_order][idx_expandtype]["optimal"]["idx_1"] = None
        SIMULATIONSDICT[padua_order][idx_expandtype]["optimal"]["idx_2"] = None   
        SIMULATIONSDICT[padua_order][idx_expandtype]["optimal"]["idx_3"] = None  
    
        SIMULATIONSDICT[padua_order][idx_expandtype]["zerolambda"] = {}
        SIMULATIONSDICT[padua_order][idx_expandtype]["zerolambda"]["idx_1"] = None
        SIMULATIONSDICT[padua_order][idx_expandtype]["zerolambda"]["idx_2"] = 0
        SIMULATIONSDICT[padua_order][idx_expandtype]["zerolambda"]["idx_3"] = None   

    SIMULATIONSDICT[padua_order]["GRAPHMIN"] = None # Figure plotting
    SIMULATIONSDICT[padua_order]["GRAPHMAX"] = None #1 # Figure plotting
    SIMULATIONSDICT[padua_order]["R_MAX"] = None # Figure plotting
    SIMULATIONSDICT[padua_order]["F_MAX"] = None # Figure plotting
    


###########################################################
# NUMERICAL OPTIMISATION RESULTS
###########################################################

SIMULATIONSDICT["no_padua"]["Opt_Beta_Expn"] = "TruncGauss"
# Optimal trunc termination error: 7.31968610978 Params: (28, 13, 4)
# Optimal uniform termination error: 8.09703230899 Params: (21, 18, 0)

SIMULATIONSDICT["no_padua"]["Uniform"]["optimal"]["idx_1"] = 21
SIMULATIONSDICT["no_padua"]["Uniform"]["optimal"]["idx_2"] = 18
SIMULATIONSDICT["no_padua"]["Uniform"]["optimal"]["idx_3"] = 0
SIMULATIONSDICT["no_padua"]["Uniform"]["zerolambda"]["idx_1"] = 21
SIMULATIONSDICT["no_padua"]["Uniform"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT["no_padua"]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT["no_padua"]["TruncGauss"]["optimal"]["idx_1"] = 28
SIMULATIONSDICT["no_padua"]["TruncGauss"]["optimal"]["idx_2"] = 13
SIMULATIONSDICT["no_padua"]["TruncGauss"]["optimal"]["idx_3"] = 4
SIMULATIONSDICT["no_padua"]["TruncGauss"]["zerolambda"]["idx_1"] = 28
SIMULATIONSDICT["no_padua"]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT["no_padua"]["TruncGauss"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[1]["Opt_Beta_Expn"] = "TruncGauss"
# Optimal trunc termination error: 20.4916893855 Params: (29, 23, 4)
# Optimal uniform termination error: 20.6285757187 Params: (22, 7, 4)

SIMULATIONSDICT[1]["Uniform"]["optimal"]["idx_1"] = 22
SIMULATIONSDICT[1]["Uniform"]["optimal"]["idx_2"] = 7
SIMULATIONSDICT[1]["Uniform"]["optimal"]["idx_3"] = 4
SIMULATIONSDICT[1]["Uniform"]["zerolambda"]["idx_1"] = 22
SIMULATIONSDICT[1]["Uniform"]["zerolambda"]["idx_2"] = 0
SIMULATIONSDICT[1]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[1]["TruncGauss"]["optimal"]["idx_1"] = 29
SIMULATIONSDICT[1]["TruncGauss"]["optimal"]["idx_2"] = 23
SIMULATIONSDICT[1]["TruncGauss"]["optimal"]["idx_3"] = 4
SIMULATIONSDICT[1]["TruncGauss"]["zerolambda"]["idx_1"] = 29
SIMULATIONSDICT[1]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[1]["TruncGauss"]["zerolambda"]["idx_3"] = None


SIMULATIONSDICT[2]["Opt_Beta_Expn"] = "TruncGauss"

# Optimal trunc termination error: 17.675734373 Params: (2, 13, 4)
# Optimal uniform termination error: 17.7089964369 Params: (16, 7, 0)

# *_Rcheb2fun_padua_ord_2_rand_2_13_*.npz done
# *_Rcheb2fun_padua_ord_2_rand_2_0_*.npz done
# *_Rcheb2fun_padua_ord_2_rand_16_7_*.npz done
# *_Rcheb2fun_padua_ord_2_rand_16_0_*.npz done

SIMULATIONSDICT[2]["Uniform"]["optimal"]["idx_1"] = 16
SIMULATIONSDICT[2]["Uniform"]["optimal"]["idx_2"] = 7
SIMULATIONSDICT[2]["Uniform"]["optimal"]["idx_3"] = 0
SIMULATIONSDICT[2]["Uniform"]["zerolambda"]["idx_1"] = 16
SIMULATIONSDICT[2]["Uniform"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[2]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[2]["TruncGauss"]["optimal"]["idx_1"] = 2
SIMULATIONSDICT[2]["TruncGauss"]["optimal"]["idx_2"] = 13
SIMULATIONSDICT[2]["TruncGauss"]["optimal"]["idx_3"] = 4
SIMULATIONSDICT[2]["TruncGauss"]["zerolambda"]["idx_1"] = 2
SIMULATIONSDICT[2]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[2]["TruncGauss"]["zerolambda"]["idx_3"] = None


SIMULATIONSDICT[3]["Opt_Beta_Expn"] = "TruncGauss"
# Optimal trunc termination error: 17.2006810442 Params: (12, 23, 0)
# Optimal uniform termination error: 17.2343209911 Params: (22, 7, 1)
# *_Rcheb2fun_padua_ord_3_rand_22_7_*.npz done
# *_Rcheb2fun_padua_ord_3_rand_22_0_*.npz done
# *_Rcheb2fun_padua_ord_3_rand_12_23_*.npz  done
# *_Rcheb2fun_padua_ord_3_rand_12_0_*.npz done


SIMULATIONSDICT[3]["Uniform"]["optimal"]["idx_1"] = 22
SIMULATIONSDICT[3]["Uniform"]["optimal"]["idx_2"] = 7
SIMULATIONSDICT[3]["Uniform"]["optimal"]["idx_3"] = 1
SIMULATIONSDICT[3]["Uniform"]["zerolambda"]["idx_1"] = 22
SIMULATIONSDICT[3]["Uniform"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[3]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[3]["TruncGauss"]["optimal"]["idx_1"] = 12
SIMULATIONSDICT[3]["TruncGauss"]["optimal"]["idx_2"] = 23
SIMULATIONSDICT[3]["TruncGauss"]["optimal"]["idx_3"] = 0
SIMULATIONSDICT[3]["TruncGauss"]["zerolambda"]["idx_1"] = 12
SIMULATIONSDICT[3]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[3]["TruncGauss"]["zerolambda"]["idx_3"] = None


SIMULATIONSDICT[4]["Opt_Beta_Expn"] = "Uniform"
# Optimal trunc termination error: 18.5568393359 Params: (19, 23, 0)
# Optimal uniform termination error: 18.2337574235 Params: (1, 18, 2)
# *_Rcheb2fun_padua_ord_4_rand_19_23_*.npz done
# *_Rcheb2fun_padua_ord_4_rand_19_0_*.npz done
# *_Rcheb2fun_padua_ord_4_rand_1_18_*.npz done
# *_Rcheb2fun_padua_ord_4_rand_1_0_*.npz done

SIMULATIONSDICT[4]["Uniform"]["optimal"]["idx_1"] = 1
SIMULATIONSDICT[4]["Uniform"]["optimal"]["idx_2"] = 18
SIMULATIONSDICT[4]["Uniform"]["optimal"]["idx_3"] = 2
SIMULATIONSDICT[4]["Uniform"]["zerolambda"]["idx_1"] = 1
SIMULATIONSDICT[4]["Uniform"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[4]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[4]["TruncGauss"]["optimal"]["idx_1"] = 19
SIMULATIONSDICT[4]["TruncGauss"]["optimal"]["idx_2"] = 23
SIMULATIONSDICT[4]["TruncGauss"]["optimal"]["idx_3"] = 0 
SIMULATIONSDICT[4]["TruncGauss"]["zerolambda"]["idx_1"] = 19
SIMULATIONSDICT[4]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[4]["TruncGauss"]["zerolambda"]["idx_3"] = None


SIMULATIONSDICT[5]["Opt_Beta_Expn"] = "Uniform"
# Optimal trunc termination error: 20.4307016309 Params: (0, 18, 0)
# Optimal uniform termination error: 19.7005178226 Params: (11, 18, 0)
# *_Rcheb2fun_padua_ord_5_rand_0_18_*.npz done
# *_Rcheb2fun_padua_ord_5_rand_0_0_*.npz done
# *_Rcheb2fun_padua_ord_5_rand_11_18_*.npz done
# *_Rcheb2fun_padua_ord_5_rand_11_0_*.npz done

SIMULATIONSDICT[5]["Uniform"]["optimal"]["idx_1"] = 0 
SIMULATIONSDICT[5]["Uniform"]["optimal"]["idx_2"] = 18
SIMULATIONSDICT[5]["Uniform"]["optimal"]["idx_3"] = 0
SIMULATIONSDICT[5]["Uniform"]["zerolambda"]["idx_1"] = 0
SIMULATIONSDICT[5]["Uniform"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[5]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[5]["TruncGauss"]["optimal"]["idx_1"] = 11
SIMULATIONSDICT[5]["TruncGauss"]["optimal"]["idx_2"] = 18
SIMULATIONSDICT[5]["TruncGauss"]["optimal"]["idx_3"] = 0 
SIMULATIONSDICT[5]["TruncGauss"]["zerolambda"]["idx_1"] = 11
SIMULATIONSDICT[5]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[5]["TruncGauss"]["zerolambda"]["idx_3"] = None


SIMULATIONSDICT[10]["Opt_Beta_Expn"] = "Uniform"
# Optimal trunc termination error: 33.0076201271 Params: (13, 13, 0)
# Optimal uniform termination error: 31.5247888311 Params: (1, 13, 0)
# *_Rcheb2fun_padua_ord_10_rand_13_13_*.npz done
# *_Rcheb2fun_padua_ord_10_rand_13_0_*.npz done
# *_Rcheb2fun_padua_ord_10_rand_1_13_*.npz done
# *_Rcheb2fun_padua_ord_10_rand_1_0_*.npz done

SIMULATIONSDICT[10]["Uniform"]["optimal"]["idx_1"] = 1 
SIMULATIONSDICT[10]["Uniform"]["optimal"]["idx_2"] = 13
SIMULATIONSDICT[10]["Uniform"]["optimal"]["idx_3"] = 0
SIMULATIONSDICT[10]["Uniform"]["zerolambda"]["idx_1"] = 1
SIMULATIONSDICT[10]["Uniform"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[10]["Uniform"]["zerolambda"]["idx_3"] = None

SIMULATIONSDICT[10]["TruncGauss"]["optimal"]["idx_1"] = 13
SIMULATIONSDICT[10]["TruncGauss"]["optimal"]["idx_2"] = 13
SIMULATIONSDICT[10]["TruncGauss"]["optimal"]["idx_3"] = 0
SIMULATIONSDICT[10]["TruncGauss"]["zerolambda"]["idx_1"] = 13
SIMULATIONSDICT[10]["TruncGauss"]["zerolambda"]["idx_2"] = 0 
SIMULATIONSDICT[10]["TruncGauss"]["zerolambda"]["idx_3"] = None



