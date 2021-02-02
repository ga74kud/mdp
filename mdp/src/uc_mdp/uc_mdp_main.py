# -------------------------------------------------------------
# code developed by Michael Hartmann during his Ph.D.
# Markov Decision Process (MDP)
#
# (C) 2021 Michael Hartmann, Graz, Austria
# Released under GNU GENERAL PUBLIC LICENSE
# email michael.hartmann@v2c2.at
# -------------------------------------------------------------

from mdp.src.uc_mdp.problem import *
import mdp.util.data_input_loader as util_io
class service_MDP(object):
    def __init__(self):
        self.obj=None
    def start_mdp(self, params, mdp_challenge):
        self.obj = problem(mdp_challenge)
        self.obj.set_solver(params)
        dict_mdp=self.obj.start_mdp_solver(mdp_challenge['R'])
        return dict_mdp

if __name__ == '__main__':
    obj=service_MDP()
    obj.show_graph()
