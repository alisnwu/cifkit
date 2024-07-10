## [1.0.2] - 2024-07-09

### Added

- Initializing progress statement for `CifEnsemble` to enhance user experience
  [#12](https://github.com/bobleesj/cifkit/issues/12)
- Print option for `compute_connections` in CifEnsemble
  [#13](https://github.com/bobleesj/cifkit/issues/13)
- Preprocessing option for `CifEnsemble` to handle input data more flexibly
  [#15](https://github.com/bobleesj/cifkit/issues/15)

### Fixed

- Error computing polyhedron metrics: index 4 is out of bounds for axis 0 with
  size 4 [#10](https://github.com/bobleesj/cifkit/issues/10)
- Warning for using categorical units to plot a list of strings for histogram
  generation [#11](https://github.com/bobleesj/cifkit/issues/11)
- Misclassification issue during preprocessing: do not move to 'others' folder
  if elements do not belong to Mendeleev table
  [#14](https://github.com/bobleesj/cifkit/issues/14)

## [1.0.1] - 2024-07-05

### Fixed

- Error computing polyhedron metrics: index 4 is out of bounds, see
  [Issue #10](https://github.com/bobleesj/cifkit/issues/10).

## [1.0.0] - 2024-07-04

### Added

- Issue and pull request templates.

### Fixed

- Duplicate connected points in connections, see
  [Issue #7](https://github.com/bobleesj/cifkit/issues/7).
