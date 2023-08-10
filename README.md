# NuDimuon-Generator

## Dimuon Event Signatures in P-ONE Neutrino Telescope

Summer internship at the University of Alberta (May-August 2023)    
Supervisor: Juan Pablo Yáñez (yaezgarz@ualberta.ca)  
Working with: Sourav Sarkar (ssarkar1@ualberta.ca)

My role with the P-ONE team at the UofA was to develop a charm dimuon event generator. The generator is built in several steps to eventually generate approximately 1,000,000 charm dimuon events. This repository contains all my scripts for the different steps. A lot of other scripts are used, mostly written by Sourav Sarkar; they are linked in the different instruction files. The scripts I have written are to be run on the Illume cluster (UofA cluster), but can be adapted to run elsewhere.

The different steps of the generator are:
- step 1: LeptonInjector (generation of muon (anti)neutrino CC DIS events);
- step 2: PYTHIA (event update with charm quark production);
- step 3: NuDimuon-Generator (addition of the OneWeight to the events);
- step 4: PROPOSAL (propagation of the daughter particles).

## A Word on P-ONE and Dimuons

The Pacific Ocean Neutrino Experiment, or P-ONE, is a proposed neutrino telescope to be deployed off the coast of British Columbia, Canada. The project describes a multi cubic-kilometer Cherenkov detector designed to observe neutrino interactions at energies in the TeV-PeV range. The telescope’s unique spatial and temporal resolutions will enable unprecedented identification of the products of these interactions. With P-ONE, physicists aim to investigate fundamental particle physics at the PeV scale and uncover previously unknown astronomical phenomena.

Dimuons are the result of a specific neutrino interaction. If it is typical for muon neutrinos to interact via deep inelastic scattering to produce a single muon, the Standard Model also predicts that, in certain instances, a pair of closely spaced high-energy muons will be produced from the same neutrino interaction. This phenomenon is referred to as a ’dimuon’. The detection of these events in P-ONE can serve as a way to investigate rare Standard Model neutrino interactions and deviations in their rate could indicate the existence of physics beyond the Standard Model. Such observations could potentially provide valuable insights into new and yet unexplored phenomena in the realm of particle physics.
