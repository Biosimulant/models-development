# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Calzone2007 Drosophila embryo cell-cycle SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Calzone2007CellcycleBiomd0000000144Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000144 SBML source."""

    _SBML_ID = 'BIOMD0000000144'
    _TITLE = 'Calzone2007 Drosophila embryo cell-cycle SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['MPFc', 'MPFn', 'StgPc', 'Stgc', 'Wee1c', 'Wee1n', 'CycBT', 'N']
    _STATE_OUTPUT_ALIASES = {'MPFc': 'cytoplasmic_maturation_promoting_factor', 'MPFn': 'nuclear_maturation_promoting_factor', 'StgPc': 'cytoplasmic_string_phosphatase', 'Stgc': 'cytoplasmic_string_protein', 'Wee1c': 'cytoplasmic_wee_one_kinase', 'Wee1n': 'nuclear_wee_one_kinase', 'CycBT': 'total_cyclin_b', 'N': 'nuclear_division_state'}
    _SPECIES_LABELS = {'cytoplasmic_maturation_promoting_factor': 'Cytoplasmic MPF', 'nuclear_maturation_promoting_factor': 'Nuclear MPF', 'cytoplasmic_string_phosphatase': 'Cytoplasmic String phosphatase', 'cytoplasmic_string_protein': 'Cytoplasmic String protein', 'cytoplasmic_wee_one_kinase': 'Cytoplasmic Wee1 kinase', 'nuclear_wee_one_kinase': 'Nuclear Wee1 kinase', 'total_cyclin_b': 'Total cyclin B', 'nuclear_division_state': 'Nuclear division state'}
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'cytoplasmic_maturation_promoting_factor': ('MPFc', 'native SBML value', 'Cytoplasmic MPF. Maps to SBML symbol `MPFc`.'), 'nuclear_maturation_promoting_factor': ('MPFn', 'native SBML value', 'Nuclear MPF. Maps to SBML symbol `MPFn`.'), 'cytoplasmic_string_phosphatase': ('StgPc', 'native SBML value', 'Cytoplasmic String phosphatase. Maps to SBML symbol `StgPc`.'), 'cytoplasmic_wee_one_kinase': ('Wee1c', 'native SBML value', 'Cytoplasmic Wee1 kinase. Maps to SBML symbol `Wee1c`.'), 'total_cyclin_b': ('CycBT', 'native SBML value', 'Total cyclin B. Maps to SBML symbol `CycBT`.'), 'nuclear_division_state': ('N', 'native SBML value', 'Nuclear division state. Maps to SBML symbol `N`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000144.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
