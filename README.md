# models-development

Curated collection of **developmental biology** simulation models for the **biosim** platform. This repository contains computational models of embryonic development, cell differentiation, tissue patterning, stem cell regulation, and developmental regulatory networks.

## What's Inside

### Models (18 packages)

Each model is a self-contained simulation component with a `model.yaml` manifest.

**Development** — embryonic development, differentiation, and developmental pattern formation:

#### Stem Cell & Pluripotency Models
- `development-sbml-chickarmane2006-stem-cell-switch-irreversible` — Irreversible stem cell fate switch
- `development-sbml-chickarmane2006-stem-cell-switch-reversible` — Reversible stem cell fate transitions
- `development-sbml-chavez2009-a-core-regulatory-network-of-oct4-in` — Oct4 regulatory network in embryonic stem cells
- `development-sbml-schittler2010-cell-fate-of-progenitor-cells-oste` — Cell fate decisions: osteoblast vs adipocyte

#### Cell Differentiation & Lineage Specification
- `development-sbml-deback2012-lineage-specification-in-pancreas-dev` — Pancreas development and lineage specification
- `development-sbml-intosalmi2015-th17-core-network-model` — Th17 cell differentiation network
- `development-sbml-leber2016-expanded-model-of-tfh-tfr-differentiat` — T follicular helper (Tfh) and regulatory (Tfr) cell differentiation
- `development-sbml-mbodj2016-mesoderm-specification-during-drosophi` — Mesoderm specification in Drosophila embryos

#### Tissue Dynamics & Pattern Formation
- `development-sbml-benary2021-tissue-dynamics-of-the-hepato-pancrea` — Tissue dynamics of hepato-pancreatic organ development
- `development-sbml-gall2023-agent-based-model-of-the-intestinal-epi` — Agent-based model of intestinal epithelium
- `development-sbml-gallandpin2022-ode-model-of-the-intestinal-epith` — ODE model of intestinal epithelial dynamics
- `development-sbml-miyazawa2010-changing-turing-patterns-by-spatial` — Turing pattern formation with spatial heterogeneity
- `development-sbml-li2024-3d-growing-domain-finite-element-model-fo` — 3D growing domain FEM for tissue morphogenesis

#### Morphogen & Signal Regulation
- `development-sbml-muraro2011-cytokinin-auxin-crossregulation` — Cytokinin-auxin cross-regulation in plant development

#### Developmental Oscillators & Cycles
- `development-sbml-laub1998-spontaneousoscillations` — Spontaneous oscillations in developmental systems
- `development-sbml-calzone2007-cellcycle` — Cell cycle regulation during development
- `development-sbml-goldbeter2006-weightcycling` — Weight cycling and metabolic dynamics

#### Reproductive & Hormonal Development
- `development-sbml-roblitz2013-menstrual-cycle-following-gnrh-analo` — Menstrual cycle following GnRH analog treatment

## Layout

```
models-development/
├── models/<model-slug>/     # One model package per folder, each with model.yaml
├── libs/                    # Shared helper code for curated models
├── templates/model-pack/    # Starter template for new model packs
├── scripts/                 # Manifest and entrypoint validation scripts
├── docs/                    # Governance documentation
└── .github/workflows/       # CI/CD pipeline
```

## How It Works

### Model Interface

Every model implements the `biosim.BioModule` interface:

- **`inputs()`** — declares named input signals the module consumes
- **`outputs()`** — declares named output signals the module produces
- **`advance_to(t)`** — advances the model's internal state to time `t`

Most curated models include Python source under `src/` and are wired together via `space.yaml` in composed simulations without additional code.

### Model Standards

All models in this repository:
- Use SBML (Systems Biology Markup Language) format
- Are sourced from BioModels and other curated repositories
- Include tellurium runtime for SBML execution
- Provide `state` output for monitoring simulation results
- Support configurable timesteps via `min_dt` parameter

### Running Models

Models are loaded and executed by the `biosim-platform`. The platform reads `model.yaml`, instantiates the model from its entrypoint, and runs the simulation loop at the configured timestep for the specified duration.

Individual models can be integrated into larger composed simulations by wiring their outputs to other models' inputs, enabling multi-scale developmental modeling.

## Getting Started

### Prerequisites

- Python 3.11+
- `biosim` framework

### Install biosim

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

### Create a New Model

1. Copy `templates/model-pack/` to `models/<your-model-slug>/`
2. Edit `model.yaml` with metadata, entrypoint, and pinned dependencies
3. Implement your module (subclass `biosim.BioModule` or use a built-in pack)
4. Add development-specific tags and categorization
5. Validate: `python scripts/validate_manifests.py && python scripts/check_entrypoints.py`

### Using Models in Spaces

To integrate developmental biology models into larger simulations:

1. Reference models by `manifest_path` (e.g., `models/development-sbml-chickarmane2006-stem-cell-switch-reversible/model.yaml`)
2. Wire model outputs to inputs of other models in your space configuration
3. Compose multi-scale simulations combining development with cell cycle, signaling, or gene regulation
4. Configure runtime parameters and simulation duration

## Linking in biosim-platform

- Models can be linked with explicit paths:
  - `models/development-sbml-mbodj2016-mesoderm-specification-during-drosophi/model.yaml`
- Models can be composed with other domain models (signaling, gene regulation, etc.) in multi-scale simulations

## External Repos

External authors can keep models in independent repositories and link them directly in `biosim-platform`. This repository is curated, not exclusive.

## Validation & CI

Three scripts enforce repository integrity on every push:

| Script | Purpose |
|--------|---------|
| `scripts/validate_manifests.py` | Schema validation for all model.yaml files |
| `scripts/check_entrypoints.py` | Verifies Python entrypoints are importable and callable |
| `scripts/check_public_boundary.sh` | Prevents business-sensitive content in this public repo |

The CI pipeline (`.github/workflows/ci.yml`) runs: **secret scan** → **manifest validation** → **smoke sandbox** (Docker).

## Contributing

- All dependencies must use exact version pinning (`==`)
- Model slugs use kebab-case with domain prefix (`development-sbml-`)
- Models must follow the `biosim.BioModule` interface
- SBML models use tellurium runtime for execution
- Pre-commit hooks enforce trailing whitespace, EOF newlines, YAML syntax, and secret detection
- See [docs/PUBLIC_INTERNAL_BOUNDARY.md](docs/PUBLIC_INTERNAL_BOUNDARY.md) for content policy

## Domain-Specific Notes

**Developmental Biology Focus Areas:**
- **Stem Cell Regulation**: Pluripotency networks, fate decisions, irreversible vs reversible switches
- **Cell Differentiation**: Lineage specification, progenitor commitment, immune cell differentiation
- **Pattern Formation**: Turing patterns, morphogen gradients, spatial heterogeneity
- **Tissue Dynamics**: Organ development, epithelial dynamics, growth and remodeling
- **Regulatory Networks**: Transcription factor networks, signaling cross-regulation
- **Multi-Scale Modeling**: From molecular networks → cellular decisions → tissue patterning → organ development

**Model Organisms & Systems:**
- Mammalian (stem cells, tissue development)
- Drosophila (mesoderm specification)
- Plant (auxin-cytokinin regulation)
- Immune system (T cell differentiation)

**Common Model Types:**
- Bistable switches for irreversible cell fate decisions
- Oscillatory systems for developmental timing
- Reaction-diffusion systems for pattern formation
- Agent-based models for tissue dynamics
- Finite element methods for growing domains

## License

This repository is dual-licensed:

- **Code** (scripts, templates, Python modules): Apache-2.0 (`LICENSE-CODE.txt`)
- **Model/content** (manifests, docs, wiring/config): CC BY 4.0 (`LICENSE-CONTENT.txt`)

Attribution guidance: `ATTRIBUTION.md`
