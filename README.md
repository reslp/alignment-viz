alignment-viz
=========

This repository contains python/processing scripts to help to visualize alignments for phylogenetics.


Description
===========

With this scripts you will be able to investigate your alignments for completeness. It is still in a very early development stage, so beware of bugs and problems.


How does it work?
================

 `calc_miss.py` takes a non-truncated FASTA alignment as input and calculates the relative completeness (number of available nucleotides relative to the number of taxa) per nucleotide position. This can then be used in `viz_aln.pde`, which will create a plot showing the acquired values for each alignment position.

Requirements and installation
============

- MacOS X or other Unix like operating system (Windows Version in the works)
- [python](www.python.org) 2.7.8+, which comes with most Unix like systems
- [Processing2](http://processing.org)



Usage
=======
Create your completeness data:
`./calc_miss.py your_alignment.fas > out.txt`

Visualize alignment:

Execute `align_viz.pde` in Processing, if you have multiple loci, ajust to locus boundaries in your alignment.

How do I cite this?
=========
Alignment visualization and the corresponding scripts have first been used in this paper:

Philipp Resl, Kevin Schneider, Martin Westberg, Christian Printzen, Zdeněk Palice, Göran Thor, Alan Fryday, Helmut Mayrhofer and Toby Spribille (2015) Diagnostics for a troubled backbone: testing topological hypotheses of trapelioid lichenized fungi in a large-scale phylogeny of Ostropomycetidae (Lecanoromycetes). Fungal Diversity (in press)


COPYRIGTH AND LICENSE
=====================

Copyright (C) 2014 Philipp Resl

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program in the file LICENSE. If not, see http://www.gnu.org/licenses/.


