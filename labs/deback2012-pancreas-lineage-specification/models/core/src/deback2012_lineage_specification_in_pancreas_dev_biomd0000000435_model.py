# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for deBack2012 pancreas lineage specification SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Deback2012LineageSpecificationInPancreasDevBiomd0000000435Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000435 SBML source."""

    _SBML_ID = 'BIOMD0000000435'
    _TITLE = 'deBack2012 pancreas lineage specification SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4']
    _STATE_OUTPUT_ALIASES = {'species_1': 'cell_i_first_lineage_signal', 'species_2': 'cell_i_second_lineage_signal', 'species_3': 'cell_j_first_lineage_signal', 'species_4': 'cell_j_second_lineage_signal'}
    _SPECIES_LABELS = {'cell_i_first_lineage_signal': 'Cell i first lineage signal', 'cell_i_second_lineage_signal': 'Cell i second lineage signal', 'cell_j_first_lineage_signal': 'Cell j first lineage signal', 'cell_j_second_lineage_signal': 'Cell j second lineage signal'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'starting_first_cell_first_fate_signal': ('species_1', 0.0, 'native SBML value', 'Setup-time initial value for the first lineage signal in neighboring cell i.'), 'starting_first_cell_second_fate_signal': ('species_2', 0.0, 'native SBML value', 'Setup-time initial value for the second lineage signal in neighboring cell i.'), 'starting_second_cell_first_fate_signal': ('species_3', 0.0, 'native SBML value', 'Setup-time initial value for the first lineage signal in neighboring cell j.'), 'starting_second_cell_second_fate_signal': ('species_4', 0.0, 'native SBML value', 'Setup-time initial value for the second lineage signal in neighboring cell j.')}
    _HEADLINE_OUTPUTS = {'cell_i_first_lineage_signal': ('species_1', 'native SBML value', 'Cell i first lineage signal. Maps to SBML symbol `species_1`.'), 'cell_i_second_lineage_signal': ('species_2', 'native SBML value', 'Cell i second lineage signal. Maps to SBML symbol `species_2`.'), 'cell_j_first_lineage_signal': ('species_3', 'native SBML value', 'Cell j first lineage signal. Maps to SBML symbol `species_3`.'), 'cell_j_second_lineage_signal': ('species_4', 'native SBML value', 'Cell j second lineage signal. Maps to SBML symbol `species_4`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000435.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
