# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML BioModule for Roblitz2013 menstrual-cycle GnRH analogue SBML model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Roblitz2013MenstrualCycleFollowingGnrhAnaloBiomd0000000494Model(TelluriumSBMLBioModule):
    """Faithful wrapper around the bundled BIOMD0000000494 SBML source."""

    _SBML_ID = 'BIOMD0000000494'
    _TITLE = 'Roblitz2013 menstrual-cycle GnRH analogue SBML model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = ['GnRH', 'FSH_bld', 'LH_bld', 'E2', 'P4', 'InhA', 'InhB', 'OvF', 'Lut1', 'Lut4', 'Ago_c', 'Ant_c']
    _STATE_OUTPUT_ALIASES = {'GnRH': 'gonadotropin_releasing_hormone', 'FSH_bld': 'follicle_stimulating_hormone_blood', 'LH_bld': 'luteinizing_hormone_blood', 'E2': 'estradiol', 'P4': 'progesterone', 'InhA': 'inhibin_a', 'InhB': 'inhibin_b', 'OvF': 'ovulatory_follicle', 'Lut1': 'luteal_stage_one', 'Lut4': 'luteal_stage_four', 'Ago_c': 'gonadotropin_releasing_hormone_agonist_central', 'Ant_c': 'gonadotropin_releasing_hormone_antagonist_central'}
    _SPECIES_LABELS = {'gonadotropin_releasing_hormone': 'GnRH', 'follicle_stimulating_hormone_blood': 'Blood FSH', 'luteinizing_hormone_blood': 'Blood LH', 'estradiol': 'Estradiol', 'progesterone': 'Progesterone', 'inhibin_a': 'Inhibin A', 'inhibin_b': 'Inhibin B', 'ovulatory_follicle': 'Ovulatory follicle', 'luteal_stage_one': 'Luteal stage 1', 'luteal_stage_four': 'Luteal stage 4', 'gonadotropin_releasing_hormone_agonist_central': 'GnRH agonist central', 'gonadotropin_releasing_hormone_antagonist_central': 'GnRH antagonist central'}
    _PARAMETER_INPUTS = {'gnrh_agonist_dose': ('p272', 100.0, 'native SBML dose', 'Named GnRH agonist dose parameter.'), 'gnrh_agonist_start_day': ('p269', 91.0, 'day', 'Named GnRH agonist administration start day.'), 'gnrh_antagonist_dose': ('p472', 500.0, 'native SBML dose', 'Named GnRH antagonist dose parameter.'), 'gnrh_antagonist_start_day': ('p469', 34.0, 'day', 'Named GnRH antagonist administration start day.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'gonadotropin_releasing_hormone': ('GnRH', 'native SBML value', 'GnRH. Maps to SBML symbol `GnRH`.'), 'follicle_stimulating_hormone_blood': ('FSH_bld', 'native SBML value', 'Blood FSH. Maps to SBML symbol `FSH_bld`.'), 'luteinizing_hormone_blood': ('LH_bld', 'native SBML value', 'Blood LH. Maps to SBML symbol `LH_bld`.'), 'estradiol': ('E2', 'native SBML value', 'Estradiol. Maps to SBML symbol `E2`.'), 'progesterone': ('P4', 'native SBML value', 'Progesterone. Maps to SBML symbol `P4`.'), 'inhibin_a': ('InhA', 'native SBML value', 'Inhibin A. Maps to SBML symbol `InhA`.'), 'inhibin_b': ('InhB', 'native SBML value', 'Inhibin B. Maps to SBML symbol `InhB`.'), 'ovulatory_follicle': ('OvF', 'native SBML value', 'Ovulatory follicle. Maps to SBML symbol `OvF`.'), 'luteal_stage_one': ('Lut1', 'native SBML value', 'Luteal stage 1. Maps to SBML symbol `Lut1`.'), 'luteal_stage_four': ('Lut4', 'native SBML value', 'Luteal stage 4. Maps to SBML symbol `Lut4`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000494.xml", integration_step: float = 0.25) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
