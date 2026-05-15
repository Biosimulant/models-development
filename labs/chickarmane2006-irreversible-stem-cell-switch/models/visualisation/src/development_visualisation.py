# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Development lab visualisation BioModule."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec, unwrap_payload


_SUMMARY_SCHEMA = {
    "duration_simulated": "float",
    "observable_count": "int",
    "largest_change_observable": "str",
    "largest_change_magnitude": "float",
    "peak_observable": "str",
    "peak_value": "float",
}


class DevelopmentVisualisationModel(BioModule):
    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        caveat: str,
        observables: list[dict[str, Any]],
        phase: Optional[dict[str, str]] = None,
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = lab_title
        self.question = question
        self.answer_focus = answer_focus
        self.caveat = caveat
        self.observables = list(observables)
        self.phase = dict(phase or {})
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: list[dict[str, float]] = []
        self._summary: dict[str, Any] = {}
        self._labels: dict[str, str] = {str(item["port"]): str(item.get("label") or item["port"]) for item in self.observables}

    def inputs(self) -> dict[str, SignalSpec]:
        state_schema = {str(item["port"]): "float" for item in self.observables}
        label_schema = {str(item["port"]): "str" for item in self.observables}
        return {
            "core_state": SignalSpec.record(
                schema=state_schema,
                description="Current friendly observable values from the core model.",
            ),
            "core_summary": SignalSpec.record(
                schema=_SUMMARY_SCHEMA,
                description="Core model run summary.",
            ),
            "core_species_labels": SignalSpec.record(
                schema=label_schema,
                description="Human-readable labels for core observables.",
            ),
        }

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._inputs = {}
        self._history = []
        self._summary = {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        state_value = unwrap_payload(self._inputs.get("core_state"))
        summary_value = unwrap_payload(self._inputs.get("core_summary"))
        label_value = unwrap_payload(self._inputs.get("core_species_labels"))
        if isinstance(label_value, Mapping):
            self._labels.update({str(key): str(value) for key, value in label_value.items()})
        if isinstance(summary_value, Mapping):
            self._summary = dict(summary_value)
        if not isinstance(state_value, Mapping):
            return
        row = {"t": float(end)}
        for item in self.observables:
            key = str(item["port"])
            try:
                row[key] = float(state_value[key])
            except (KeyError, TypeError, ValueError):
                continue
        if len(row) > 1:
            self._history.append(row)

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        if not self._history:
            return None
        visuals: list[dict[str, Any]] = []
        visuals.append(self._answer_table())
        timeseries = self._timeseries_visual()
        if timeseries is not None:
            visuals.append(timeseries)
        bar = self._range_bar_visual()
        if bar is not None:
            visuals.append(bar)
        scatter = self._phase_visual()
        if scatter is not None:
            visuals.append(scatter)
        return visuals or None

    def _label(self, key: str) -> str:
        return self._labels.get(key, key)

    def _ranges(self) -> dict[str, float]:
        ranges: dict[str, float] = {}
        for item in self.observables:
            key = str(item["port"])
            values = [row[key] for row in self._history if key in row]
            if values:
                ranges[key] = max(values) - min(values)
        return ranges

    def _final_values(self) -> dict[str, float]:
        latest = self._history[-1]
        return {str(item["port"]): float(latest[str(item["port"])]) for item in self.observables if str(item["port"]) in latest}

    def _answer_table(self) -> dict[str, Any]:
        ranges = self._ranges()
        finals = self._final_values()
        dominant_range = max(ranges.items(), key=lambda item: abs(item[1])) if ranges else ("none", 0.0)
        dominant_final = max(finals.items(), key=lambda item: abs(item[1])) if finals else ("none", 0.0)
        observed = (
            f"{self._label(dominant_range[0])} had the largest within-run excursion "
            f"({dominant_range[1]:.6g}); {self._label(dominant_final[0])} had the largest final magnitude "
            f"({dominant_final[1]:.6g})."
        )
        evidence = self.answer_focus
        if self._summary:
            evidence = (
                f"{evidence} Core summary reports largest change "
                f"{self._summary.get('largest_change_observable', 'unknown')}="
                f"{self._summary.get('largest_change_magnitude', 'unknown')}."
            )
        return {
            "render": "table",
            "description": "Direct scientific answer for this development lab run.",
            "data": {
                "title": f"{self.lab_title} - run interpretation",
                "columns": ["Prompt", "Answer"],
                "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", observed],
                    ["Evidence", evidence],
                    ["Dominant module", self._label(dominant_range[0])],
                    ["Caveat", self.caveat],
                ],
            },
        }

    def _timeseries_visual(self) -> Optional[dict[str, Any]]:
        series = []
        for item in self.observables:
            key = str(item["port"])
            points = [[row["t"], row[key]] for row in self._history if key in row]
            if points:
                series.append({"name": self._label(key), "points": points})
        if not series:
            return None
        return {
            "render": "timeseries",
            "description": "Developmental state variables over the simulated run.",
            "data": {
                "title": "Developmental state trajectory",
                "x_label": "Model time",
                "y_label": "Native SBML value",
                "series": series,
            },
        }

    def _range_bar_visual(self) -> Optional[dict[str, Any]]:
        ranges = self._ranges()
        if not ranges:
            return None
        items = [
            {"label": self._label(key), "value": float(value)}
            for key, value in sorted(ranges.items(), key=lambda item: abs(item[1]), reverse=True)
        ]
        if not items:
            return None
        return {
            "render": "bar",
            "description": "Variables ranked by within-run excursion.",
            "data": {
                "title": "Largest activity ranges",
                "items": items,
                "x_label": "Model variable",
                "y_label": "Max-min range",
            },
        }

    def _phase_visual(self) -> Optional[dict[str, Any]]:
        x_key = self.phase.get("x")
        y_key = self.phase.get("y")
        if not x_key or not y_key:
            return None
        points = [
            {"x": row[x_key], "y": row[y_key], "series": "trajectory"}
            for row in self._history
            if x_key in row and y_key in row
        ]
        if not points:
            return None
        return {
            "render": "scatter",
            "description": "Phase-style view of two key developmental observables.",
            "data": {
                "title": self.phase.get("title", "Developmental phase view"),
                "x_label": self.phase.get("x_label", self._label(x_key)),
                "y_label": self.phase.get("y_label", self._label(y_key)),
                "connect_points": True,
                "points": points,
            },
        }
