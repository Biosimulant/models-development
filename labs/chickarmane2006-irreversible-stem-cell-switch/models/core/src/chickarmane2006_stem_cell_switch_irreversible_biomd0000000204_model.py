# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Chickarmane2006 irreversible stem-cell switch SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chickarmane2006StemCellSwitchIrreversibleBiomd0000000204Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000204 SBML source."""

    _SBML_ID = 'BIOMD0000000204'
    _TITLE = 'Chickarmane2006 irreversible stem-cell switch SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['OCT4', 'SOX2', 'NANOG', 'OCT4_SOX2', 'Protein']
    _STATE_OUTPUT_ALIASES = {'OCT4': 'octamer_binding_transcription_factor_4', 'SOX2': 'sry_box_transcription_factor_2', 'NANOG': 'nanog_homeobox', 'OCT4_SOX2': 'octamer_binding_transcription_factor_4_sry_box_transcription_factor_2_complex', 'Protein': 'differentiation_protein'}
    _SPECIES_LABELS = {'octamer_binding_transcription_factor_4': 'OCT4', 'sry_box_transcription_factor_2': 'SOX2', 'nanog_homeobox': 'NANOG', 'octamer_binding_transcription_factor_4_sry_box_transcription_factor_2_complex': 'OCT4-SOX2 complex', 'differentiation_protein': 'Differentiation protein'}
    _PARAMETER_INPUTS = {'p53_signal': ('p53', 0.0, 'native SBML value', 'Fixed p53 boundary signal used by the stem-cell switch reactions.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'octamer_binding_transcription_factor_4': ('OCT4', 'native SBML value', 'OCT4. Maps to SBML symbol `OCT4`.'), 'sry_box_transcription_factor_2': ('SOX2', 'native SBML value', 'SOX2. Maps to SBML symbol `SOX2`.'), 'nanog_homeobox': ('NANOG', 'native SBML value', 'NANOG. Maps to SBML symbol `NANOG`.'), 'octamer_binding_transcription_factor_4_sry_box_transcription_factor_2_complex': ('OCT4_SOX2', 'native SBML value', 'OCT4-SOX2 complex. Maps to SBML symbol `OCT4_SOX2`.'), 'differentiation_protein': ('Protein', 'native SBML value', 'Differentiation protein. Maps to SBML symbol `Protein`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000204.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
