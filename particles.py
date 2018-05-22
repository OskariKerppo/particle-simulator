#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Oskari Kerppo
22.5.2018

Particle simulator with python

Work in progress
"""
import numpy as np
from random import random

class particle:

	type = "Particle"

	def __init__(self, name="Hitunen", mass=1):
		self.name = name
		self.position = np.zeros(0)
		self.forces = np.zeros(0)
		self.mass = mass
		for i in range(3):
			self.position = np.append(self.position,random()*2-1)

	def get_position(self):
		return self.position

	def get_forces(self):
		return self.forces

	def update_forces(self)

