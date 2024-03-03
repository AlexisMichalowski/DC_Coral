# RAMP starting-kit on coral bleaching predictions

*Authors: Emeline Bruyère, Anaëlle Cossard, Alexis Michalowski-Skarbek, Rosanne Phebe, Rémi Poulard & Marine Tognia-tonou (M2 AMI2B).*  

Coral reefs stand as some of the most diverse and vital ecosystems on the planet, playing an indispensable role in the health of our oceans. Approximately 25% of marine species rely on these vibrant underwater habitats for their survival. Central to the vitality of coral reefs is the intricate symbiotic relationship between corals and photosynthetic algae, which reside within their tissues. In this mutually beneficial partnership, corals provide protection and shelter to the algae, while receiving essential oxygen and nutrients in return.

However, when environmental stressors exert pressure on coral ecosystems, the delicate balance of this symbiosis can falter. This phenomenon, known as coral bleaching, manifests as the gradual breakdown of the relationship between corals and microalgae. Characterized by the loss of pigmentation and symbionts, bleached corals appear pale. Although coral bleaching can be temporary and reversible under certain conditions, prolonged stress can prove fatal for these fragile organisms.

Multiple factors contribute to coral bleaching, with global warming, human activities, and the prevalence of parasites and viruses among the primary culprits. Rising sea temperatures, in particular, have been closely linked to the increase in frequency and severity of coral bleaching events.

The Global Coral-Bleaching Database (GCBD) serves as a repository of invaluable information, compiling over three decades of coral bleaching records from around the world. With data spanning 93 countries and encompassing 14,405 sites, the GCBD offers crucial insights into the prevalence and distribution of coral bleaching. Key environmental parameters, such as site exposure, distance to land, mean turbidity, cyclone frequency, and various sea-surface temperature metrics, are meticulously documented within the database.

In light of the urgency to safeguard coral reef ecosystems, the objective of this RAMP challenge is to leverage the environmental data provided by the GCBD to predict the severity of the bleaching of corals.

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
