# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Muraro2011 auxin-cytokinin root cell-fate SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Muraro2011CytokininAuxinCrossregulationBiomd0000000416Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000416 SBML source."""

    _SBML_ID = 'BIOMD0000000416'
    _TITLE = 'Muraro2011 auxin-cytokinin root cell-fate SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['Aux', 'Ck', 'IAAm', 'IAAp', 'AuxTIR1', 'AuxTIAA', 'ARF', 'PINm', 'PINp', 'ARRAp', 'ARRBp', 'CkAHKph']
    _STATE_OUTPUT_ALIASES = {'Aux': 'auxin', 'Ck': 'cytokinin', 'IAAm': 'indole_3_acetic_acid_messenger_rna', 'IAAp': 'indole_3_acetic_acid_protein', 'AuxTIR1': 'auxin_transport_inhibitor_response_1_complex', 'AuxTIAA': 'auxin_indole_3_acetic_acid_complex', 'ARF': 'auxin_response_factor_activity', 'PINm': 'pinformed_messenger_rna', 'PINp': 'pinformed_protein', 'ARRAp': 'response_regulator_a', 'ARRBp': 'response_regulator_b', 'CkAHKph': 'phosphorylated_cytokinin_histidine_kinase'}
    _SPECIES_LABELS = {'auxin': 'Auxin', 'cytokinin': 'Cytokinin', 'indole_3_acetic_acid_messenger_rna': 'IAA mRNA', 'indole_3_acetic_acid_protein': 'IAA protein', 'auxin_transport_inhibitor_response_1_complex': 'Auxin-TIR1 complex', 'auxin_indole_3_acetic_acid_complex': 'Auxin-IAA complex', 'auxin_response_factor_activity': 'ARF activity', 'pinformed_messenger_rna': 'PIN mRNA', 'pinformed_protein': 'PIN protein', 'response_regulator_a': 'Response regulator A', 'response_regulator_b': 'Response regulator B', 'phosphorylated_cytokinin_histidine_kinase': 'Phosphorylated cytokinin histidine kinase'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'starting_auxin_level': ('Aux', 1.0, 'native SBML value', 'Setup-time initial auxin level for the root-fate network.'), 'starting_cytokinin_level': ('Ck', 1.0, 'native SBML value', 'Setup-time initial cytokinin level for the root-fate network.')}
    _HEADLINE_OUTPUTS = {'auxin': ('Aux', 'native SBML value', 'Auxin. Maps to SBML symbol `Aux`.'), 'cytokinin': ('Ck', 'native SBML value', 'Cytokinin. Maps to SBML symbol `Ck`.'), 'indole_3_acetic_acid_messenger_rna': ('IAAm', 'native SBML value', 'IAA mRNA. Maps to SBML symbol `IAAm`.'), 'indole_3_acetic_acid_protein': ('IAAp', 'native SBML value', 'IAA protein. Maps to SBML symbol `IAAp`.'), 'auxin_transport_inhibitor_response_1_complex': ('AuxTIR1', 'native SBML value', 'Auxin-TIR1 complex. Maps to SBML symbol `AuxTIR1`.'), 'auxin_indole_3_acetic_acid_complex': ('AuxTIAA', 'native SBML value', 'Auxin-IAA complex. Maps to SBML symbol `AuxTIAA`.'), 'auxin_response_factor_activity': ('ARF', 'native SBML value', 'ARF activity. Maps to SBML symbol `ARF`.'), 'pinformed_messenger_rna': ('PINm', 'native SBML value', 'PIN mRNA. Maps to SBML symbol `PINm`.'), 'pinformed_protein': ('PINp', 'native SBML value', 'PIN protein. Maps to SBML symbol `PINp`.'), 'response_regulator_a': ('ARRAp', 'native SBML value', 'Response regulator A. Maps to SBML symbol `ARRAp`.'), 'response_regulator_b': ('ARRBp', 'native SBML value', 'Response regulator B. Maps to SBML symbol `ARRBp`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000416.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
