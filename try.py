import numpy as np
def Euler_distance(x1,x2):
    return ( (x1-x2)**2 ).sum( )
def Manhatun_distance(x1,x2):
    return np.abs( (x1-x2) ).sum( )
usr1 = np.array([9,8,8,7])
usr2 = np.array([7,8,7,6])
usr3 = np.array([8,6,8,7])
usr4 = np.array([8,9,6,7])
E_dist_list = [Euler_distance(eval( 'usr{}'.format( i ) ),usr4)  for i in range(1,4)]
M_dist_list = [Manhatun_distance(eval( 'usr{}'.format( i ) ),usr4)  for i in range(1,4)]
