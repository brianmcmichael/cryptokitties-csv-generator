# cryptokitties-csv-generator

Script to generate a complete cryptokitties csv dataset for genetic data crunching.

Get the .csv (~170mb) and .zip (~70mb) in [Releases](https://github.com/brianmcmichael/cryptokitties-csv-generator/releases)

## Install and run (python3)

* Requires local ethereum node on default port
* `pip install web3`
* `python kittylist.py`

## Output

* Filename: `kittylist.csv`
* CSV Format: `"id", "isGestating", "isReady", "cooldownIndex", "nextActionAt", "siringWithId", "birthTime", "matronId", "sireId", "generation", "genes", "kai_genes"`
