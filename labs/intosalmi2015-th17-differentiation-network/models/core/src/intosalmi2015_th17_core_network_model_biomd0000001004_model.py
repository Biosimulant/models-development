# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Intosalmi2015 Th17 differentiation network SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Intosalmi2015Th17CoreNetworkModelBiomd0000001004Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000001004 SBML source."""

    _SBML_ID = 'BIOMD0000001004'
    _TITLE = 'Intosalmi2015 Th17 differentiation network SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['IL6ext', 'IL6int', 'STAT3mRNA', 'STAT3prot_star', 'STAT3prot', 'TGFbext', 'TGFbint', 'RORgtmRNA', 'FOXP3prot_star', 'FOXP3mRNA']
    _STATE_OUTPUT_ALIASES = {'IL6ext': 'external_interleukin_6', 'IL6int': 'internal_interleukin_6', 'STAT3mRNA': 'signal_transducer_and_activator_of_transcription_3_messenger_rna', 'STAT3prot_star': 'active_signal_transducer_and_activator_of_transcription_3', 'STAT3prot': 'signal_transducer_and_activator_of_transcription_3_protein', 'TGFbext': 'external_transforming_growth_factor_beta', 'TGFbint': 'internal_transforming_growth_factor_beta', 'RORgtmRNA': 'retinoic_acid_receptor_related_orphan_receptor_gamma_t_messenger_rna', 'FOXP3prot_star': 'active_forkhead_box_p3', 'FOXP3mRNA': 'forkhead_box_p3_messenger_rna'}
    _SPECIES_LABELS = {'external_interleukin_6': 'External IL-6', 'internal_interleukin_6': 'Internal IL-6', 'signal_transducer_and_activator_of_transcription_3_messenger_rna': 'STAT3 mRNA', 'active_signal_transducer_and_activator_of_transcription_3': 'Active STAT3', 'signal_transducer_and_activator_of_transcription_3_protein': 'STAT3 protein', 'external_transforming_growth_factor_beta': 'External TGF-beta', 'internal_transforming_growth_factor_beta': 'Internal TGF-beta', 'retinoic_acid_receptor_related_orphan_receptor_gamma_t_messenger_rna': 'ROR-gamma-t mRNA', 'active_forkhead_box_p3': 'Active FOXP3', 'forkhead_box_p3_messenger_rna': 'FOXP3 mRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'starting_interleukin_6_signal': ('IL6ext', 1.0, 'native SBML value', 'Setup-time initial extracellular IL-6 signal for the Th17 network.'), 'starting_transforming_growth_factor_beta_signal': ('TGFbext', 1.0, 'native SBML value', 'Setup-time initial extracellular TGF-beta signal for the Th17 network.')}
    _HEADLINE_OUTPUTS = {'external_interleukin_6': ('IL6ext', 'native SBML value', 'External IL-6. Maps to SBML symbol `IL6ext`.'), 'internal_interleukin_6': ('IL6int', 'native SBML value', 'Internal IL-6. Maps to SBML symbol `IL6int`.'), 'signal_transducer_and_activator_of_transcription_3_messenger_rna': ('STAT3mRNA', 'native SBML value', 'STAT3 mRNA. Maps to SBML symbol `STAT3mRNA`.'), 'active_signal_transducer_and_activator_of_transcription_3': ('STAT3prot_star', 'native SBML value', 'Active STAT3. Maps to SBML symbol `STAT3prot_star`.'), 'external_transforming_growth_factor_beta': ('TGFbext', 'native SBML value', 'External TGF-beta. Maps to SBML symbol `TGFbext`.'), 'internal_transforming_growth_factor_beta': ('TGFbint', 'native SBML value', 'Internal TGF-beta. Maps to SBML symbol `TGFbint`.'), 'retinoic_acid_receptor_related_orphan_receptor_gamma_t_messenger_rna': ('RORgtmRNA', 'native SBML value', 'ROR-gamma-t mRNA. Maps to SBML symbol `RORgtmRNA`.'), 'active_forkhead_box_p3': ('FOXP3prot_star', 'native SBML value', 'Active FOXP3. Maps to SBML symbol `FOXP3prot_star`.'), 'forkhead_box_p3_messenger_rna': ('FOXP3mRNA', 'native SBML value', 'FOXP3 mRNA. Maps to SBML symbol `FOXP3mRNA`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000001004.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
