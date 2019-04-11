#!/usr/bin/env python

# Copyright (C)2019 Pierre Barbera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Contact:
# Pierre Barbera <Pierre.Barbera@h-its.org>
# Exelixis Lab, Heidelberg Institute for Theoretical Studies
# Schloss-Wolfsbrunnenweg 35, D-69118 Heidelberg, Germany

import os
import sys
import json
from math import log

script_dir = os.path.dirname(os.path.realpath(__file__))

base_dir = os.path.realpath(os.path.join(script_dir, "../"))


def num_taxa(delim):
    num=0
    for taxa_list in delim.itervalues():
        for taxon in taxa_list:
            num += 1
    return num

def len_intersect(lhs, rhs):
    return len([value for value in lhs if value in rhs])

def entropy(part, N):
    ret_sum=0.0

    for p in part.itervalues():
        ret_sum += ( len(p) / N ) * log( len(p) / N )

    return -ret_sum

# a function to take two delimitations and calculate the NMI between them
def NMI(truth, delim):
    N=float(num_taxa(truth))
    I=0.0
    for t in truth.itervalues():
        for d in delim.itervalues():
            intersize = len_intersect(t, d)
            if intersize > 0:
                I += (intersize / N) * log( (intersize * N) / (len(t) * len(d)) )

    return I / max( entropy(truth, N), entropy(delim, N) )


# print NMI(qry_map, truth)

swarm={
    1:['Lactobacillus crispatus',
       'Lactobacillus jensenii',
       'Lactobacillus iners',
       'Lactobacillus coleohominis',
       'Lactobacillus gasseri',
       'Lactobacillus vaginalis',
       'Streptococcus agalactiae',
       'Streptococcus anginosus',
       'Streptococcus gallolyticus',
       'Streptococcus oralis',
       'Aerococcus christensenii'],
    2:['Lactobacillus crispatus'],
    3:['Gardnerella vaginalis'],
    4:['Leptotrichia amnionii'],
    5:['Megasphaera'],
    6:['Atopobium vaginae'],
    7:['Eggerthella'],
    8:['Sneathia sanguinegens'],
    9:['Prevotella timonensis'],
    10:['Lactobacillus jensenii']
}

vsearch={
    1:['Sneathia sanguinegens',
       'Leptotrichia amnionii'],
    2:['Lactobacillus crispatus'],
    3:['Gardnerella vaginalis'],
    4:['Atopobium vaginae'],
    5:['Megasphaera'],
    6:['Eggerthella'],
    7:['Prevotella bivia', 'Prevotella amnii'],
    8:['Prevotella timonensis'],
    9:['BVAB2'],
    10:['Lactobacillus jensenii']
}

placementfact={
    1:['Lactobacillus crispatus',
       'Lactobacillus jensenii',
       'Lactobacillus kalixensis'],
    2:['Sneathia sanguinegens',
        'Leptotrichia amnionii'],
    3:['Gardnerella vaginalis'],
    4:['Megasphaera'],
    5:['Lactobacillus crispatus'],
    6:['Eggerthella'],
    7:['Prevotella timonensis',
        'Prevotella buccalis'],
    8:['Prevotella bivia',
        'Prevotella amnii'],
    9: ['Atopobium vaginae'],
    10:[' Lactobacillus iners']
}

print "swarm vs. vsearch: {}".format(NMI(swarm, vsearch))
print "swarm vs. placement: {}".format(NMI(swarm, placementfact))
print "vsearch vs. placement: {}".format(NMI(vsearch, placementfact))