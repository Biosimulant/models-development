# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Laub1998 Dictyostelium cyclic AMP oscillation SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Laub1998SpontaneousoscillationsBiomd0000000099Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000099 SBML source."""

    _SBML_ID = 'BIOMD0000000099'
    _TITLE = 'Laub1998 Dictyostelium cyclic AMP oscillation SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6']
    _STATE_OUTPUT_ALIASES = {'species_0': 'extracellular_cyclic_amp', 'species_1': 'intracellular_cyclic_amp', 'species_2': 'protein_kinase_a_activity', 'species_3': 'cyclic_amp_phosphodiesterase_regulator_a', 'species_4': 'adenylate_cyclase_a', 'species_5': 'cyclic_amp_receptor_one', 'species_6': 'extracellular_signal_regulated_kinase_two'}
    _SPECIES_LABELS = {'extracellular_cyclic_amp': 'Extracellular cyclic AMP', 'intracellular_cyclic_amp': 'Intracellular cyclic AMP', 'protein_kinase_a_activity': 'Protein kinase A activity', 'cyclic_amp_phosphodiesterase_regulator_a': 'cAMP phosphodiesterase REGA', 'adenylate_cyclase_a': 'Adenylate cyclase A', 'cyclic_amp_receptor_one': 'Cyclic AMP receptor 1', 'extracellular_signal_regulated_kinase_two': 'ERK2'}
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'extracellular_cyclic_amp': ('species_0', 'native SBML value', 'Extracellular cyclic AMP. Maps to SBML symbol `species_0`.'), 'intracellular_cyclic_amp': ('species_1', 'native SBML value', 'Intracellular cyclic AMP. Maps to SBML symbol `species_1`.'), 'protein_kinase_a_activity': ('species_2', 'native SBML value', 'Protein kinase A activity. Maps to SBML symbol `species_2`.'), 'cyclic_amp_phosphodiesterase_regulator_a': ('species_3', 'native SBML value', 'cAMP phosphodiesterase REGA. Maps to SBML symbol `species_3`.'), 'adenylate_cyclase_a': ('species_4', 'native SBML value', 'Adenylate cyclase A. Maps to SBML symbol `species_4`.'), 'cyclic_amp_receptor_one': ('species_5', 'native SBML value', 'Cyclic AMP receptor 1. Maps to SBML symbol `species_5`.'), 'extracellular_signal_regulated_kinase_two': ('species_6', 'native SBML value', 'ERK2. Maps to SBML symbol `species_6`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000099.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
