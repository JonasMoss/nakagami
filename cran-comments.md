## Update

This updates nakagami from 1.1.0 to 1.2.0. It fixes support boundaries,
independent argument recycling, and numerical overflow/underflow, removes the
assertthat runtime dependency, and updates documentation and the package logo.

## Test environment

* Ubuntu 26.04.1 LTS, R 4.6.1 (2026-06-24), x86_64-pc-linux-gnu.
* GitHub Actions matrix: Linux (release, oldrel-1, devel), Windows (release),
  and macOS (release). Results are available on the release/1.2.0 branch:
  https://github.com/JonasMoss/nakagami/actions?query=branch%3Arelease%2F1.2.0

## R CMD check results

R CMD check --as-cran on the source tarball, including the PDF manual:
0 errors, 0 warnings, 1 NOTE.

The NOTE reports skipped HTML manual validation because HTML Tidy and the R
package V8 are unavailable on this workstation. The PDF manual checks pass.
All package URL checks pass.

## Reverse dependencies

CRAN lists one reverse dependency: univariateML 1.5.0. It was checked against
both nakagami 1.1.0 and this 1.2.0 candidate in separate libraries. There are
no new errors, warnings, or notes. Examples and all 639 tests pass.

Both runs have the same vignette warning because the optional copula package
is not installed. The other vignette code checks pass; vignette rebuilding
was disabled for this reverse-dependency check.
