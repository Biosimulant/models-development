# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Leber2016 Tfh-Tfr differentiation SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leber2016ExpandedModelOfTfhTfrDifferentiatBiomd0000000625Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000625 SBML source."""

    _SBML_ID = 'BIOMD0000000625'
    _TITLE = 'Leber2016 Tfh-Tfr differentiation SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['NaiveCD4', 'nTreg', 'Tfh', 'Tfr', 'Bcl6', 'Blimp1', 'FoxP3', 'STAT3', 'IL4', 'IL6', 'IL10', 'IL21', 'CXCR5', 'ICOS', 'TGFb', 'Tgif1', 'RXR']
    _STATE_OUTPUT_ALIASES = {'NaiveCD4': 'naive_cluster_of_differentiation_four_t_cells', 'nTreg': 'natural_regulatory_t_cells', 'Tfh': 'follicular_helper_t_cells', 'Tfr': 'follicular_regulatory_t_cells', 'Bcl6': 'b_cell_lymphoma_six', 'Blimp1': 'b_lymphocyte_induced_maturation_protein_one', 'FoxP3': 'forkhead_box_p3', 'STAT3': 'signal_transducer_and_activator_of_transcription_3', 'IL4': 'interleukin_4', 'IL6': 'interleukin_6', 'IL10': 'interleukin_10', 'IL21': 'interleukin_21', 'CXCR5': 'chemokine_receptor_type_five', 'ICOS': 'inducible_t_cell_costimulator', 'TGFb': 'transforming_growth_factor_beta', 'Tgif1': 'transforming_growth_factor_beta_induced_factor_homeobox_one', 'RXR': 'retinoid_receptor'}
    _SPECIES_LABELS = {'naive_cluster_of_differentiation_four_t_cells': 'Naive CD4 T cells', 'natural_regulatory_t_cells': 'Natural regulatory T cells', 'follicular_helper_t_cells': 'Follicular helper T cells', 'follicular_regulatory_t_cells': 'Follicular regulatory T cells', 'b_cell_lymphoma_six': 'Bcl6', 'b_lymphocyte_induced_maturation_protein_one': 'Blimp1', 'forkhead_box_p3': 'FOXP3', 'signal_transducer_and_activator_of_transcription_3': 'STAT3', 'interleukin_4': 'IL-4', 'interleukin_6': 'IL-6', 'interleukin_10': 'IL-10', 'interleukin_21': 'IL-21', 'chemokine_receptor_type_five': 'CXCR5', 'inducible_t_cell_costimulator': 'ICOS', 'transforming_growth_factor_beta': 'TGF-beta', 'transforming_growth_factor_beta_induced_factor_homeobox_one': 'Tgif1', 'retinoid_receptor': 'RXR'}
    _PARAMETER_INPUTS = {'interleukin_2_signal': ('IL2', 0.0001, 'native SBML value', 'Constant IL-2 upstream signal in the Tfh/Tfr differentiation network.'), 'stat5_signal': ('STAT5', 0.0, 'native SBML value', 'Constant STAT5 upstream signal in the Tfh/Tfr differentiation network.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'naive_cluster_of_differentiation_four_t_cells': ('NaiveCD4', 'native SBML value', 'Naive CD4 T cells. Maps to SBML symbol `NaiveCD4`.'), 'natural_regulatory_t_cells': ('nTreg', 'native SBML value', 'Natural regulatory T cells. Maps to SBML symbol `nTreg`.'), 'follicular_helper_t_cells': ('Tfh', 'native SBML value', 'Follicular helper T cells. Maps to SBML symbol `Tfh`.'), 'follicular_regulatory_t_cells': ('Tfr', 'native SBML value', 'Follicular regulatory T cells. Maps to SBML symbol `Tfr`.'), 'b_cell_lymphoma_six': ('Bcl6', 'native SBML value', 'Bcl6. Maps to SBML symbol `Bcl6`.'), 'b_lymphocyte_induced_maturation_protein_one': ('Blimp1', 'native SBML value', 'Blimp1. Maps to SBML symbol `Blimp1`.'), 'forkhead_box_p3': ('FoxP3', 'native SBML value', 'FOXP3. Maps to SBML symbol `FoxP3`.'), 'signal_transducer_and_activator_of_transcription_3': ('STAT3', 'native SBML value', 'STAT3. Maps to SBML symbol `STAT3`.'), 'interleukin_6': ('IL6', 'native SBML value', 'IL-6. Maps to SBML symbol `IL6`.'), 'interleukin_21': ('IL21', 'native SBML value', 'IL-21. Maps to SBML symbol `IL21`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000625.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
