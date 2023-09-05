# NuDimuon-Generator

## Dimuon Event Signatures in P-ONE Neutrino Telescope

Summer internship at the University of Alberta (May-August 2023)    
Supervisor: Juan Pablo Yáñez (yaezgarz@ualberta.ca)  
Working with: Sourav Sarkar (ssarkar1@ualberta.ca)

My role with the P-ONE team at the UofA was to develop a charm dimuon event generator. The generator is built in several steps to eventually generate approximately 1,000,000 charm dimuon events. This repository contains all my scripts for the different steps. A lot of other scripts are used, mostly written by Sourav Sarkar; they are linked in the different README.md files. The scripts I have written are to be run on the Illume cluster (UofA cluster).

The different steps of the generator are:
- step 1: LeptonInjector (energy and geometry sampling);
- step 2: PYTHIA (primary interaction and hadronization);
- step 3: NuDimuon-Generator & IceTray (charm hadron decay and interaction, event weight calculation);
- step 4: PROPOSAL & DoubleTrack-Run (daughter particle propagation, event rate calculation).

## A Word on P-ONE and Dimuons

The Pacific Ocean Neutrino Experiment, or P-ONE, is a proposed neutrino telescope to be deployed off the coast of British Columbia, Canada. The project describes a multi cubic-kilometre Cherenkov detector designed to observe neutrino interactions at energies in the TeV-PeV range. The telescope’s unique spatial and temporal resolutions will enable unprecedented identification of the products of these interactions. With P-ONE, physicists aim to investigate fundamental particle physics at the PeV scale and uncover previously unknown astronomical phenomena.

Some of the neutrino interactions that will be closely studied in P-ONE are those which result in dimuon events. If it is typical for muon neutrinos to interact via charged current deep inelastic scattering (CC DIS) to produce a single muon, the Standard Model also predicts that, in certain instances, a pair of closely spaced high-energy muons will be produced from the same neutrino interaction. This phenomenon is referred to as a 'dimuon'. The detection of these events in P-ONE can serve as a way to investigate rare Standard Model neutrino interactions and deviations in their rate could indicate the existence of physics beyond the Standard Model.

They are several neutrino interactions which may result in dimuon events. The dominant mechanism, and the one I focused on, involves the presence of a charm quark. A muon neutrino will first interact via CC DIS to produce a primary muon and a charm quark. The latter will hadronize to produce a charm hadron (in a hadronic shower), which will then decay or interact to produce a secondary muon and another hadronic shower. In P-ONE, the muons will travel great distances in the water, producing two long, clear tracks as their Cherenkov light propagates in the medium and is dedected by photomultiplier tubes. The hadronic showers will produce 'cascades', which are shorter and more gathered. These key features will allow the (somewhat tedious) identification of dimuon events.
