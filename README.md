# RAMP staring-kit on coral bleaching predictions

*Authors: Emeline Bruyère, Anaëlle Cossard, Alexis Michalowski-Skarbek, Rosanne Phebe, Rémi Poulard & Marine Tognia-tonou (M2 AMI2B).*  

Coral reefs, the world's most diverse marine ecosystems, play a crucial role in providing resources and services benefiting millions of people. However, they have recently faced an escalation in thermal-stress events, leading to coral bleaching. The coral bleaching phenomenon results from the breakdown of the symbiotic relationship between corals and microalgae. It is caracterised by the loss of pigments and symbionts, causing corals to appear pale, bleached. Bleaching can be temporary or fatal for corals, but undoubtedly, marine heat waves pose the most significant threat to coral reefs on a global scale.  

The Global Coral-Bleaching Database (GCBD) compiles 34,846 coral bleaching records from 14,405 sites in 93 countries, from 1980–2020. The GCBD provides vital information on the presence or absence of coral bleaching along with site exposure, distance to land, mean turbidity, cyclone frequency, and a suite of sea-surface temperature metrics at the times of survey.

The goal of this RAMP is to predict the percentage of bleached corals from environmental data, based on the data gathered in the GCBD.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install the required dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```
If you are using `conda`, we provide an `environment.yml` file for similar
usage.

### Challenge description

Get started with the [dedicated notebook](coral_bleaching_starting_kit.ipynb)

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```
### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)
