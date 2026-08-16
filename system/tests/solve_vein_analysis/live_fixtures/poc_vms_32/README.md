# POC-VMS-32 frozen calibration inputs

This directory contains evaluator-side frozen inputs for the three independent
runtime-asset component tests. A live model workspace receives only the files
listed for that role in the POC protocol. Files whose names start with `gold` or
`expected` are evaluator-only and must never be copied into a model workspace.

This is a calibration pack, not a prospective holdout.
