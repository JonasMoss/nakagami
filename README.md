
<!-- README.md is generated from README.Rmd. Please edit that file -->

# nakagami <img src="man/figures/logo.png" align="right" width="100" height="53.4" />

[![Build
Status](https://travis-ci.com/JonasMoss/nakagami.svg?branch=master)](https://travis-ci.com/JonasMoss/nakagami)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/JonasMoss/nakagami?branch=master&svg=true)](https://ci.appveyor.com/project/JonasMoss/nakagami)
[![Coverage
Status](https://codecov.io/gh/JonasMoss/nakagami/branch/master/graph/badge.svg)](https://codecov.io/gh/JonasMoss/nakagami?branch=master)
[![Project Status: Active – The project has reached a stable, usable
state and is being actively
developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/nakagami)](https://cran.r-project.org/package=nakagami)

## Overview

An `R`-package for the [Nakagami
distribution](https://en.wikipedia.org/wiki/Nakagami_distribution).

## Installation

Use the following command from inside `R`:

``` r
# install.packages("devtools")
devtools::install_github("JonasMoss/nakagami")
```

## Usage

The density function is `dnaka`, the probability distribution is
`pnaka`, the quantile function is `qnaka` and random deviate generator
is `rnaka`. Use them just like the `*gamma` functions in the `stats`
package.

``` r
set.seed(313)
x = seq(0, 3, by = 0.01)
hist(nakagami::rnaka(10^5, shape = 4, scale = 2), freq = FALSE, breaks = "FD")
lines(x, nakagami::dnaka(x, shape = 4, scale = 2), type = "l", lwd = 2)
```

<img src="man/figures/README-unnamed-chunk-2-1.png" width="750px" />

## Note

All of these functions are implemented in the `R` package
[`VGAM`](https://cran.r-project.org/package=VGAM). As of `VGAM` version
1.1-2, the implementations in `nakagami` are faster, more thoroughly
tested, and use a standardized set of arguments following the template
of `dgamma` et cetera.

The `rnaka` of `nakagami` is much faster than the `rnaka` of `VGAM`:

``` r
#install.packages("VGAM")

microbenchmark::microbenchmark(nakagami::rnaka(100, 2, 4), 
                               VGAM::rnaka(100, 4, 2))
#> Unit: microseconds
#>                        expr    min      lq      mean  median      uq
#>  nakagami::rnaka(100, 2, 4)  267.0  298.10   596.232  339.25  398.95
#>      VGAM::rnaka(100, 4, 2) 1942.8 2319.95 17219.140 2580.60 2980.30
#>        max neval
#>    16680.8   100
#>  1451304.4   100
```

And the quantile function of `nakagami` is slightly faster.

``` r
p = 1:10/11
microbenchmark::microbenchmark(nakagami::qnaka(0.01, 10, 4), 
                               VGAM::qnaka(0.01, 4, 10))
#> Unit: microseconds
#>                          expr   min     lq    mean median    uq    max
#>  nakagami::qnaka(0.01, 10, 4) 147.2 177.45 211.647 186.30 207.9 1883.9
#>      VGAM::qnaka(0.01, 4, 10) 340.5 371.20 456.141 435.05 470.3 2512.6
#>  neval
#>    100
#>    100
```

Moreover, `VGAM::qnaka` fails to implement the standard argument `log.p`
and `VGAM::rnaka` uses the non-standard arguments `Smallno` and `...`.

## How to Contribute or Get Help

If you encounter a bug, have a feature request or need some help, open a
[Github issue](https://github.com/JonasMoss/nakagami/issues).

This project follows a [Contributor Code of
Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html).

## References

  - Nakagami, N. 1960. “The m-Distribution, a General Formula of
    Intensity of Rapid Fading.” In Statistical Methods in Radio Wave
    Propagation: Proceedings of a Symposium Held at the University of
    California, June 18–20, 1958, edited by William C. Hoffman, 3–36.
    Permagon Press.
    <https://doi.org/10.1016/B978-0-08-009306-2.50005-4>.

  - Yee TW (2010). “The VGAM Package for Categorical Data Analysis.”
    Journal of Statistical Software, 32(10), 1–34.
    <https://www.jstatsoft.org/v32/i10/>.
