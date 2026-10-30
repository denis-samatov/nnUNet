# Scope of this fork

Upstream: [MIC-DKFZ/nnUNet](https://github.com/MIC-DKFZ/nnUNet). Original authorship and license
remain with upstream; upstream performance/clinical claims are not personal
portfolio results.

Reference fork of the upstream medical segmentation framework. The framework and its published results belong to the upstream authors; this fork does not establish a separately trained or validated model.

## Audited snapshot and limits

Portfolio audit base: `940dcd3ba8e9f9a1c21885ca52acd2f06328b6fc` (2026-10-28, rechecked 2026-10-29).

No patient/cohort-held-out evaluation, clinical qualification, training replay or model deployment by the fork owner is supplied. A future personal experiment must record permitted dataset provenance, splits, configurations, weights, predictions and uncertainty before reporting a result.

The historical audit above did not run the new checks described below. These bounded checks do not certify the full upstream system.

## CPU maintenance qualification (2026-10-30)

This fork has a bounded Python 3.13 CPU maintenance workflow: hash-locked validation tools, current dependency-advisory checks for that profile, critical Python lint across `nnunetv2`, four upstream path/environment contracts, wheel construction and an installed-wheel path import from outside the source tree.

```sh
python -m pip install --require-hashes -r requirements-ci.lock
python -m pip check
python -m pip_audit --no-deps --disable-pip --strict -r requirements-ci.lock
python -m ruff check --select E9,F821,F822,F823 nnunetv2 .ci
python -m pytest nnunetv2/tests/test_paths.py -q
python -m build --wheel --no-isolation
python -m pip install --no-deps dist/*.whl
python .ci/smoke_installed.py
```

The `--no-deps` installation deliberately checks the wheel's CPU path module. This tooling environment omits the full framework runtime (including Torch); it is not suitable for training/inference and does not claim a full-runtime `pip check`. Run that check before this partial package install. GPU behavior, checkpoints, datasets, segmentation accuracy and clinical suitability remain unverified here. Upstream packaging emits license-metadata deprecation warnings, retained in build logs.

Regenerate tooling hashes with `uv pip compile requirements-ci.in --python-version 3.13 --generate-hashes -o requirements-ci.lock`. This validates a small maintenance surface and preserves the upstream framework's attribution.
