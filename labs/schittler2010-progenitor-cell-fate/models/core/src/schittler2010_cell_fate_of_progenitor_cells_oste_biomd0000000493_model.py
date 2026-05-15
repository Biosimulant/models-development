# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Schittler2010 progenitor cell-fate SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schittler2010CellFateOfProgenitorCellsOsteBiomd0000000493Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000493 SBML source."""

    _SBML_ID = 'BIOMD0000000493'
    _TITLE = 'Schittler2010 progenitor cell-fate SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['P', 'O', 'C']
    _STATE_OUTPUT_ALIASES = {'P': 'progenitor_cells', 'O': 'osteoblast_cells', 'C': 'chondrocyte_cells'}
    _SPECIES_LABELS = {'progenitor_cells': 'Progenitor cells', 'osteoblast_cells': 'Osteoblast cells', 'chondrocyte_cells': 'Chondrocyte cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'starting_progenitor_cells': ('P', 12.03, 'native SBML value', 'Setup-time initial progenitor-cell state.'), 'starting_bone_fate_cells': ('O', 0.14, 'native SBML value', 'Setup-time initial osteoblast or bone-fate cell state.'), 'starting_cartilage_fate_cells': ('C', 0.14, 'native SBML value', 'Setup-time initial chondrocyte or cartilage-fate cell state.')}
    _HEADLINE_OUTPUTS = {'progenitor_cells': ('P', 'native SBML value', 'Progenitor cells. Maps to SBML symbol `P`.'), 'osteoblast_cells': ('O', 'native SBML value', 'Osteoblast cells. Maps to SBML symbol `O`.'), 'chondrocyte_cells': ('C', 'native SBML value', 'Chondrocyte cells. Maps to SBML symbol `C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000493.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
