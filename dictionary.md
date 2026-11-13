# Knowledge Base Dictionary

A sourced dictionary of acronyms, jargon, and technical concepts Rick wants to retain.

Each entry is one concept. Acronyms, synonyms, and alternate spellings belong in `aliases`, not in separate entries unless they mean different things in different domains.

## ACC

```yaml
id: acc
type: acronym
canonical: ACC
aliases:
  - Active Copper Cable
  - active copper cable
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-08
sources:
  - title: Active Copper Cables - A New Class of Rack Interconnects for Further Optimizing AI
    publisher: Marvell
    url: https://www.marvell.com/blogs/active-copper-cables-ai-rack-interconnects.html
    accessed: 2026-06-08
  - title: Active Electrical Cables
    publisher: Molex
    url: https://www.molex.com/en-us/products/connectors/high-speed-pluggable-io/active-electrical-cables-aec
    accessed: 2026-06-08
```

**Definition:** ACC stands for Active Copper Cable: a copper cable assembly with active analog electronics, commonly redrivers or linear amplifiers, that improve reach versus passive direct-attach copper.

**Plain English:** ACC is DAC with a signal booster inside the cable.

**Why it matters:** ACC can keep short AI-rack links on copper longer before the system needs more expensive optical links. That can matter for rack cost, power, serviceability, and suppliers of high-speed copper cable assemblies.

**Usage notes:** Rick's pasted Goldman excerpt describes ACC as twinax copper plus redriver with typical reach around 7-15m. Public vendor material supports the redriver/linear-amplifier distinction, but exact reach depends on speed, connector, cable gauge, and system channel budget.

**Related:** DAC, AEC, AOC, Redriver

## AEC

```yaml
id: aec
type: acronym
canonical: AEC
aliases:
  - Active Electrical Cable
  - active electrical cable
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Active Electrical Cables
    publisher: Molex
    url: https://www.molex.com/en-us/products/connectors/high-speed-pluggable-io/active-electrical-cables-aec
    accessed: 2026-06-08
  - title: AEC - Active Electrical Cable
    publisher: AMD
    url: https://docs.amd.com/r/en-US/xapp1404-pollara-cable-guide/AEC-Active-Electrical-Cable
    accessed: 2026-06-08
```

**Definition:** AEC stands for Active Electrical Cable: a copper cable assembly that uses active electronics, typically retimers, to regenerate high-speed electrical signals and extend reach beyond passive DAC or ACC designs.

**Plain English:** AEC is copper with a small signal repair station built into the cable.

**Why it matters:** AECs give AI racks another copper option for high-speed intra-rack and nearby-rack links, reducing the need to move every link to optics at once.

**Usage notes:** Rick's pasted Goldman excerpt says AEC is likely what he meant by "ACE" and describes twinax copper plus retimer with a typical 5-30m range. That is report-context, not a universal standard distance.

**Related:** DAC, ACC, Retimer, AOC

## AOC

```yaml
id: aoc
type: acronym
canonical: AOC
aliases:
  - Active Optical Cable
  - active optical cable
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Cable Types and Length
    publisher: Juniper Networks
    url: https://www.juniper.net/documentation/us/en/hardware/400g-optics-cables-guide/optics/topics/concept/400g-cable-length-type.html
    accessed: 2026-06-08
  - title: Active Optical Cables and Direct-Attached Copper
    publisher: Cisco
    url: https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/CPwE/5-1/Phy_Arch/CPwE-Physical-Infrastructure_Feb2023.pdf
    accessed: 2026-06-08
```

**Definition:** AOC stands for Active Optical Cable: a fiber cable assembly with optical transceiver electronics integrated into the cable ends.

**Plain English:** AOC is a fiber cable that already has the electricity-to-light adapters attached.

**Why it matters:** AOCs reduce cable bulk, electromagnetic-interference sensitivity, and reach limits compared with copper, which helps dense AI racks and data-center cabling.

**Usage notes:** Rick's pasted Goldman excerpt places AOC around 30-100m and often VCSEL-based over multimode fiber. Treat that as the report's distance ladder; actual AOC reach varies by standard and vendor.

**Related:** DAC, ACC, AEC, VCSEL, Optical Module

## ASIC

```yaml
id: asic
type: acronym
canonical: ASIC
aliases:
  - Application-Specific Integrated Circuit
  - application-specific integrated circuit
  - switch ASIC
domain:
  - semiconductors
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: What is an ASIC?
    publisher: Arm
    url: https://www.arm.com/glossary/asic
    accessed: 2026-06-08
```

**Definition:** ASIC stands for Application-Specific Integrated Circuit: a custom chip optimized for a specific task rather than general-purpose computing.

**Plain English:** An ASIC is a purpose-built chip.

**Why it matters:** In AI networking, the switch ASIC is the packet-moving brain of the switch; CPO and NPO matter because optical engines move closer to that ASIC to shorten lossy electrical paths.

**Example:** A data-center Ethernet switch ASIC handles switching logic and high-speed SerDes interfaces for many network ports.

**Related:** CPO, NPO/OBO, SerDes

## ASP

```yaml
id: asp
type: acronym
canonical: ASP
aliases:
  - Average Selling Price
  - average selling price
domain:
  - finance
  - markets
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Average Selling Price (ASP)
    publisher: Corporate Finance Institute
    url: https://corporatefinanceinstitute.com/resources/accounting/average-selling-price-asp/
    accessed: 2026-06-08
  - title: Average Selling Price (ASP)
    publisher: Wall Street Prep
    url: https://www.wallstreetprep.com/knowledge/average-selling-price-asp/
    accessed: 2026-06-08
```

**Definition:** ASP stands for Average Selling Price: average product revenue per unit sold over a period or segment.

**Plain English:** ASP is the average price the company actually gets per unit.

**Why it matters:** In AI-infrastructure models, ASP assumptions drive revenue estimates for modules, cables, switches, GPUs, and other components.

**Example:** If a supplier sells 1,000 modules for $2 million total, ASP is $2,000 per module.

**Related:** TAM, GM, EPS

## BoM

```yaml
id: bom
type: acronym
canonical: BoM
aliases:
  - BOM
  - Bill of Materials
  - bill of materials
domain:
  - finance
  - manufacturing
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Oracle Bills of Material User's Guide
    publisher: Oracle
    url: https://docs.oracle.com/cd/E18727-01/doc.121/e13688/T272930T275774.htm
    accessed: 2026-06-08
  - title: What is a bill of materials (BOM)?
    publisher: TechTarget
    url: https://www.techtarget.com/searcherp/definition/bill-of-materials-BoM
    accessed: 2026-06-08
```

**Definition:** BoM stands for Bill of Materials: the structured list of components, subassemblies, quantities, and sometimes costs required to build a product.

**Plain English:** BoM is the parts list for a product.

**Why it matters:** In AI hardware research, BoM analysis estimates which suppliers capture dollar content as racks, switches, cables, optics, and substrates change.

**Example:** A CPO switch BoM might include the switch ASIC, optical engines, fiber array units, external lasers, connectors, PCB, and cooling hardware.

**Related:** ASP, TAM, GM

## CPO

```yaml
id: cpo
type: acronym
canonical: CPO
aliases:
  - Co-Packaged Optics
  - co-packaged optics
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Scaling AI Factories with Co-Packaged Optics for Better Power Efficiency
    publisher: NVIDIA Technical Blog
    url: https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/
    accessed: 2026-06-08
  - title: How Industry Collaboration Fosters NVIDIA Co-Packaged Optics
    publisher: NVIDIA Technical Blog
    url: https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics/
    accessed: 2026-06-08
```

**Definition:** CPO stands for Co-Packaged Optics: an architecture that integrates optical engines very close to, or in the same package area as, a high-speed switch ASIC or compute chip.

**Plain English:** CPO converts signals to light right next to the chip instead of sending fast electrical signals across a long board path first.

**Why it matters:** At very high bandwidth, long electrical paths burn power and degrade signal quality. CPO can improve power efficiency, bandwidth density, and signal integrity, but it changes repairability and supply-chain value.

**Usage notes:** Rick's pasted Goldman excerpt argues CPO shortens electrical paths from centimeters to millimeters and may coexist with pluggable optics because pluggables are easier to replace.

**Related:** NPO/OBO, SiPh, ELS, FAU, Optical Module, ASIC

## CW Laser

```yaml
id: cw-laser
type: acronym
canonical: CW Laser
aliases:
  - Continuous Wave Laser
  - continuous-wave laser
  - CW
domain:
  - optical-networking
  - photonics
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Continuous-wave laser
    publisher: Britannica
    url: https://www.britannica.com/technology/continuous-wave-laser
    accessed: 2026-06-08
  - title: External Laser Source (ELS)
    publisher: Ayar Labs
    url: https://ayarlabs.com/glossary/external-laser-source-els/
    accessed: 2026-06-08
```

**Definition:** A CW laser is a continuous-wave laser whose optical output is approximately steady rather than emitted in pulses.

**Plain English:** A CW laser supplies steady raw light that another photonic component can modulate into data.

**Why it matters:** Silicon photonics and CPO designs often separate light generation from data modulation, so a CW laser can act as the light source for one or more optical engines.

**Related:** ELS, SiPh, CPO, VCSEL

## DAC

```yaml
id: dac
type: acronym
canonical: DAC
aliases:
  - Direct Attach Copper
  - Direct-Attach Copper
  - direct attach copper
  - twinax cable
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Cable Types and Length
    publisher: Juniper Networks
    url: https://www.juniper.net/documentation/us/en/hardware/400g-optics-cables-guide/optics/topics/concept/400g-cable-length-type.html
    accessed: 2026-06-08
  - title: Maintaining Robust DAC, AOC, AEC and Transceiver Connectivity in Hyperscale Data Centers
    publisher: VIAVI Solutions
    url: https://www.viavisolutions.com/es-es/node/107026
    accessed: 2026-06-08
```

**Definition:** DAC stands for Direct Attach Copper: a short copper twinax cable assembly with pluggable ends that carries electrical signals directly between ports.

**Plain English:** DAC is the simplest high-speed cable: send the electrical signal through copper.

**Why it matters:** DAC is attractive inside AI racks because it is cheap and low-power, but its useful reach shrinks as data rates rise and channel loss becomes harder to manage.

**Usage notes:** Rick's pasted Goldman excerpt places DAC around 0.5-3m for short intra-rack links. Treat that as report context rather than a universal limit.

**Related:** ACC, AEC, AOC, PCB

## DR / FR

```yaml
id: dr-fr
type: acronym
canonical: DR / FR
aliases:
  - DR
  - FR
  - Direct Reach
  - Far Reach
  - 400GBASE-DR4
  - 400GBASE-FR4
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-08
sources:
  - title: Difference Between DR and FR in Optical Transceivers
    publisher: POC Opto-Tech
    url: https://poc.com.sg/silicon-photonics/direct-reach/
    accessed: 2026-06-08
  - title: 400G QSFP-DD FR4 Data Center Optical Guide
    publisher: LINK-PP
    url: https://www.link-pp.com/knowledge/400g-qsfp-dd-fr4-datacenter-optical-guide.html
    accessed: 2026-06-08
```

**Definition:** DR and FR are optical transceiver reach classes commonly used in high-speed Ethernet modules, with DR generally meaning shorter data-center reach and FR meaning longer reach.

**Plain English:** DR is shorter-reach data-center fiber; FR reaches farther.

**Why it matters:** DR versus FR affects module cost, fiber type/count, power, and which optical technologies suppliers use.

**Usage notes:** Rick's pasted Goldman excerpt defines DR around 30-500m and FR around 500m-2km. Public 400G examples often use DR4 up to 500m and FR4 up to 2km, but exact reaches depend on the Ethernet generation and module standard.

**Related:** Optical Module, EML, SiPh, MPO

## Driver

```yaml
id: driver
type: concept
canonical: Driver
aliases:
  - optical driver
  - modulator driver
  - laser driver
  - driver IC
domain:
  - optical-networking
  - photonics
  - semiconductors
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-09
sources:
  - title: Telecom Transceivers
    publisher: RP Photonics
    url: https://www.rp-photonics.com/telecom_transceivers.html
    accessed: 2026-06-09
  - title: Progress in Research on Co-Packaged Optics
    publisher: Micromachines / MDPI
    url: https://www.mdpi.com/2072-666X/15/10/1211
    accessed: 2026-06-09
```

**Definition:** In optical links, a driver is an electronic circuit or IC that shapes and amplifies an electrical signal so it can control a laser or optical modulator at high speed.

**Plain English:** The driver pushes the optical transmitter hard and cleanly enough to switch at data-center speeds.

**Why it matters:** The XPU or switch ASIC produces electrical data, but the modulator or laser often needs a dedicated high-speed drive signal. Driver design affects bandwidth, power, signal integrity, and how tightly electronics can be packaged next to the PIC.

**Usage notes:** Rick's pasted report-context places the driver in the EIC: the XPU sends electrical data to the EIC, and the driver conditions that signal so the modulator can encode it onto light.

**Related:** EIC, Modulator, Laser, PIC, Optical Engine, XPU

## DSP, Redriver, and Retimer

```yaml
id: dsp-redriver-retimer
type: concept
canonical: DSP, Redriver, and Retimer
aliases:
  - DSP
  - Digital Signal Processor
  - redriver
  - retimer
  - signal conditioner
domain:
  - optical-networking
  - semiconductors
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Implementing the PCIe Design with Signal Conditioning
    publisher: Texas Instruments
    url: https://www.ti.com/lit/pdf/snla401
    accessed: 2026-06-08
  - title: Digital signal processor
    publisher: Wikipedia
    url: https://en.wikipedia.org/wiki/Digital_signal_processor
    accessed: 2026-06-08
```

**Definition:** In high-speed links, DSPs process digital signals, redrivers boost or equalize degraded analog signals, and retimers recover timing before retransmitting a cleaner signal.

**Plain English:** A redriver is a signal booster, a retimer is a signal rebuilder, and a DSP is the digital cleanup engine.

**Why it matters:** These components compensate for electrical loss and jitter, but they add power, latency, cost, and heat. CPO tries to reduce the need for some of that compensation by shortening the electrical path.

**Usage notes:** Redrivers are commonly associated with ACC-style copper links; retimers are commonly associated with AEC-style copper links. Exact implementation varies by protocol and vendor.

**Related:** ACC, AEC, CPO, SerDes

## EIC

```yaml
id: eic
type: acronym
canonical: EIC
aliases:
  - Electronic Integrated Circuit
  - electrical integrated circuit
  - electronic IC
  - electrical interface chip
domain:
  - optical-networking
  - photonics
  - semiconductors
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-09
sources:
  - title: Photonic Integrated Circuit (PIC)
    publisher: Ayar Labs
    url: https://ayarlabs.com/photonic-integrated-circuit-pic/
    accessed: 2026-06-09
  - title: Progress in Research on Co-Packaged Optics
    publisher: Micromachines / MDPI
    url: https://www.mdpi.com/2072-666X/15/10/1211
    accessed: 2026-06-09
```

**Definition:** EIC stands for Electronic Integrated Circuit: the electronic chip or die that interfaces high-speed electrical signals with photonic components in an optical engine.

**Plain English:** EIC is the electrical control/interface chip next to the light-processing PIC.

**Why it matters:** Optical links are not only optics; they need electrical circuits to drive transmitters and recover received signals. In optical engines, the EIC commonly contains or interfaces with driver and TIA functions that help an XPU or switch ASIC communicate through the PIC.

**Usage notes:** Rick's pasted report-context describes the EIC as the "electrical brain/interface": transmit-side drivers condition XPU electrical data for the modulator, while receive-side TIAs amplify tiny photodetector currents back into usable electrical signals.

**Related:** PIC, Optical Engine, Driver, TIA, Photodetector, Modulator, XPU

## ELS

```yaml
id: els
type: acronym
canonical: ELS
aliases:
  - External Laser Source
  - external laser source
  - ELSFP
domain:
  - optical-networking
  - photonics
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: External Laser Source (ELS)
    publisher: Ayar Labs
    url: https://ayarlabs.com/glossary/external-laser-source-els/
    accessed: 2026-06-08
  - title: External Laser Source (ELS) Module with Ultra-High-Power Laser
    publisher: Lumentum
    url: https://www.lumentum.com/products/external-laser-source-els-module-ultra-high-power-laser
    accessed: 2026-06-08
```

**Definition:** ELS stands for External Laser Source: a separate laser module that supplies continuous optical power to silicon-photonics chips or CPO optical engines.

**Plain English:** ELS is the external light power supply for the optical engine.

**Why it matters:** Moving lasers outside the optical engine can improve serviceability, thermal design, and shared light-source architecture in CPO and silicon-photonics systems.

**Related:** CW Laser, CPO, SiPh

## EML

```yaml
id: eml
type: acronym
canonical: EML
aliases:
  - Electro-absorption Modulated Laser
  - electro-absorption modulated laser
domain:
  - optical-networking
  - photonics
status: verified
confidence: medium
last_verified: 2026-06-08
sources:
  - title: Electro-Absorption-Modulated Lasers (EML)
    publisher: Fraunhofer HHI
    url: https://www.hhi.fraunhofer.de/en/departments/pc/technologies-and-solutions/laser/electro-absorption-modulated-lasers-eml.html
    accessed: 2026-06-08
  - title: Difference Between DR and FR in Optical Transceivers
    publisher: POC Opto-Tech
    url: https://poc.com.sg/silicon-photonics/direct-reach/
    accessed: 2026-06-08
```

**Definition:** EML stands for Electro-absorption Modulated Laser: a laser transmitter approach that integrates a laser with an electro-absorption modulator to encode data onto light.

**Plain English:** EML is a proven optical transmitter technology used in many high-speed transceivers.

**Why it matters:** EML can coexist with silicon photonics, especially where reach, maturity, or proven reliability matter more than maximum integration.

**Usage notes:** Rick's pasted Goldman excerpt frames EML as older and more discrete than SiPh-based approaches. That is a useful investor shorthand, but actual module architectures can mix multiple technologies.

**Related:** SiPh, Optical Module, DR / FR

## EPS

```yaml
id: eps
type: acronym
canonical: EPS
aliases:
  - Earnings Per Share
  - earnings per share
domain:
  - finance
  - markets
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Earnings Per Share
    publisher: Investor.gov
    url: https://www.investor.gov/introduction-investing/investing-basics/glossary/earnings-share
    accessed: 2026-06-08
  - title: Earnings Per Share (EPS)
    publisher: Stock Analysis
    url: https://stockanalysis.com/term/eps-earnings-per-share/
    accessed: 2026-06-08
```

**Definition:** EPS stands for Earnings Per Share: a profitability measure that divides a company's earnings by its share count.

**Plain English:** EPS is the amount of company profit attributable to one share.

**Why it matters:** Equity analysts use EPS estimates and revisions to compare profitability, valuation, and earnings growth.

**Usage notes:** Basic EPS and diluted EPS can differ because diluted EPS accounts for potential share issuance from options, converts, and other instruments.

**Related:** GM, ASP, TAM

## FAU

```yaml
id: fau
type: acronym
canonical: FAU
aliases:
  - Fiber Array Unit
  - fiber array unit
domain:
  - optical-networking
  - photonics
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Fiber Array Units
    publisher: Corning
    url: https://www.corning.com/oem-solutions/worldwide/en/home/products-solutions/optical-communication-components/fiber-arrays.html
    accessed: 2026-06-08
```

**Definition:** FAU stands for Fiber Array Unit: a passive optical component that precisely aligns multiple optical fibers to optical devices or assemblies.

**Plain English:** FAU is the precision fiber alignment block.

**Why it matters:** High-speed optics and CPO need low-loss fiber alignment; small physical misalignments can reduce optical power and yield. In AI-rack optics, FAUs are part of the physical interface between optical engines and fiber cables.

**Usage notes:** Rick's pasted report-context describes FAU as the green precision-interface block between the optical engine and fiber cables, and says Goldman counts FAU together with optical engines as part of the CPO value pool.

**Related:** CPO, SiPh, MPO, Optical Module, Optical Engine, PIC

## GB300 NVL72

```yaml
id: gb300-nvl72
type: product
canonical: GB300 NVL72
aliases:
  - NVIDIA GB300 NVL72
  - NVL72 GB300
  - GB300 NVL72 rack-scale system
domain:
  - ai-infrastructure
  - semiconductors
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Designed for AI Reasoning Performance & Efficiency | NVIDIA GB300 NVL72
    publisher: NVIDIA
    url: https://www.nvidia.com/en-us/data-center/gb300-nvl72/
    accessed: 2026-06-08
  - title: Overview - NVIDIA NVL72 AI Factory
    publisher: NVIDIA Docs
    url: https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/overview.html
    accessed: 2026-06-08
  - title: NVIDIA Blackwell Ultra for the Era of AI Reasoning
    publisher: NVIDIA Technical Blog
    url: https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning/
    accessed: 2026-06-08
```

**Definition:** GB300 NVL72 is an NVIDIA liquid-cooled rack-scale AI system built around 72 Blackwell Ultra GPUs and 36 Grace CPUs, not the Blackwell architecture itself.

**Plain English:** Blackwell Ultra is the GPU generation inside the rack; GB300 NVL72 is the specific 72-GPU rack system NVIDIA sells around it.

**Why it matters:** Mixing up the architecture name with the system name can distort supplier mapping and valuation work. GB300 NVL72 implies a full rack-level bill of materials, including compute trays, NVLink, networking, liquid cooling, power, cabling, and service/OEM integration, while Blackwell or Blackwell Ultra refers to the GPU architecture/generation.

**Usage notes:** Use "Blackwell" for NVIDIA's broader GPU architecture, "Blackwell Ultra" for the enhanced generation/platform, and "GB300 NVL72" for the specific rack-scale system based on Blackwell Ultra GPUs.

**Related:** BoM, Scale Up vs Scale Out, SerDes, DAC, ACC, AEC, AOC

## GM

```yaml
id: gm
type: acronym
canonical: GM
aliases:
  - Gross Margin
  - gross margin
  - gross profit margin
domain:
  - finance
  - markets
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Gross Margin
    publisher: Stock Analysis
    url: https://stockanalysis.com/term/gross-margin/
    accessed: 2026-06-08
```

**Definition:** GM stands for Gross Margin: gross profit divided by revenue, usually expressed as a percentage.

**Plain English:** GM is the share of sales left after direct product costs.

**Why it matters:** GM shows how much economic room a supplier has after manufacturing or service-delivery costs, before operating expenses.

**Example:** If revenue is $100 and cost of goods sold is $60, gross margin is 40%.

**Related:** ASP, EPS, BoM

## Laser

```yaml
id: laser
type: concept
canonical: Laser
aliases:
  - laser diode
  - optical laser
  - light source
  - continuous laser
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: Telecom Transmitters
    publisher: RP Photonics
    url: https://www.rp-photonics.com/telecom_transmitters.html
    accessed: 2026-06-09
  - title: Telecom Transceivers
    publisher: RP Photonics
    url: https://www.rp-photonics.com/telecom_transceivers.html
    accessed: 2026-06-09
```

**Definition:** In optical communication, a laser is the light source that emits optical power, either modulated directly or supplied as continuous light for a separate modulator or PIC to encode data.

**Plain English:** The laser provides the raw light.

**Why it matters:** Silicon photonics and CPO designs often separate light generation from light modulation: the laser supplies optical power, while the PIC or modulator writes data onto that light. Laser availability, wavelength control, power, reliability, and packaging can become bottlenecks as AI systems add more optical links.

**Usage notes:** Rick's pasted report-context says Goldman expects supply tightness across EML and CW lasers through 2027 due to AI server ramp, speed migration, more optical connections, and InP substrate constraints. Treat that as report-context rather than a public-source-verified forecast.

**Related:** CW Laser, EML, PIC, Modulator, Optical Engine, ELS

## Modulator

```yaml
id: modulator
type: concept
canonical: Modulator
aliases:
  - optical modulator
  - electro-optic modulator
  - EOM
  - Mach-Zehnder modulator
  - MZM
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: Electro-optic Modulators
    publisher: RP Photonics
    url: https://www.rp-photonics.com/electro_optic_modulators.html
    accessed: 2026-06-09
  - title: Optical Modulator
    publisher: Photonics.com
    url: https://www.photonics.com/Dictionary/optical-modulator/d5818
    accessed: 2026-06-09
  - title: What is a Photonic Integrated Circuit?
    publisher: Ansys
    url: https://www.ansys.com/simulation-topics/what-is-a-photonic-integrated-circuit
    accessed: 2026-06-09
```

**Definition:** A modulator is a photonic component that changes a property of light, such as intensity, phase, polarization, or frequency, so the light carries information.

**Plain English:** The modulator writes electrical 1s and 0s onto a laser beam.

**Why it matters:** In optical transmitters, the laser may provide a clean light source while the modulator encodes high-speed data onto it. Modulator bandwidth, insertion loss, drive voltage, and integration with the driver/EIC affect link speed, power, and optical-engine design.

**Example:** Laser equals a blank flashlight beam; modulator equals the fast switching element that changes the beam so it carries data.

**Usage notes:** Rick's pasted report-context describes the driver as the EIC block that pushes the modulator. Without a suitable driver, the modulator may not switch fast or cleanly enough for high-speed optical transmission.

**Related:** Laser, Driver, PIC, EIC, Optical Engine, XPU

## MPO

```yaml
id: mpo
type: acronym
canonical: MPO
aliases:
  - Multi-fiber Push-On
  - Multi Fiber Push On
  - MPO connector
  - MTP
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-08
sources:
  - title: The MPO connector
    publisher: Black Box
    url: https://www.blackbox.co.uk/gb-gb/page/25878/Resources/Technical-Resources/Black-Box-Explains/Fibre-Optic-Cable/The-MPO-connector
    accessed: 2026-06-08
  - title: Technical Guidance - MTP vs MPO Fiber Connectors
    publisher: Molex Connected Enterprise Solutions
    url: https://www.molexces.com/webfoo/wp-content/uploads/MPO-vs-MTP.pdf
    accessed: 2026-06-08
```

**Definition:** MPO stands for Multi-fiber Push-On: a high-density fiber connector family that terminates multiple optical fibers in one connector.

**Plain English:** MPO is a multi-lane fiber plug.

**Why it matters:** AI clusters and CPO systems can require many optical lanes, so high-density connectors reduce connector count and cable complexity.

**Usage notes:** MTP is a branded/enhanced MPO-style connector, not a separate generic standard.

**Related:** FAU, Optical Module, DR / FR

## MUX / DEMUX

```yaml
id: mux-demux
type: acronym
canonical: MUX / DEMUX
aliases:
  - MUX
  - DEMUX
  - Multiplexer
  - Demultiplexer
  - mux
  - demux
  - optical multiplexer
  - optical demultiplexer
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: What is a Photonic Integrated Circuit?
    publisher: Ansys
    url: https://www.ansys.com/simulation-topics/what-is-a-photonic-integrated-circuit
    accessed: 2026-06-09
  - title: Optical Interconnects Finally Seeing the Light in Silicon Photonics
    publisher: Photonics / PMC
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8840221/
    accessed: 2026-06-09
```

**Definition:** MUX means multiplexer and DEMUX means demultiplexer: optical structures that combine multiple channels into one path or split a combined path back into separate channels.

**Plain English:** MUX merges lanes; DEMUX splits lanes.

**Why it matters:** High-speed optical systems often carry multiple lanes or wavelengths over one fiber or optical path. MUX/DEMUX structures let a PIC or optical module pack more data into limited physical fiber and connector space.

**Usage notes:** In wavelength-division multiplexing, different wavelengths can act like separate lanes. A MUX combines them for transmission; a DEMUX separates them at the receiver.

**Related:** PIC, Waveguide / Coupler, Optical Module, DR / FR, SiPh

## NIC

```yaml
id: nic
type: acronym
canonical: NIC
aliases:
  - Network Interface Card
  - Network Interface Controller
  - network adapter
  - LAN adapter
domain:
  - networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: What is a network interface card (NIC)?
    publisher: TechTarget
    url: https://www.techtarget.com/searchnetworking/definition/network-interface-card
    accessed: 2026-06-08
  - title: ConnectX NICs
    publisher: NVIDIA
    url: https://www.nvidia.com/en-us/networking/multi-host/
    accessed: 2026-06-08
```

**Definition:** NIC stands for Network Interface Card or Network Interface Controller: hardware that connects a computer or server to a network.

**Plain English:** NIC is the network adapter.

**Why it matters:** AI servers depend on high-throughput, low-latency NICs to move training and inference traffic between GPUs, servers, and switches.

**Related:** ToR / EoR, SerDes, ASIC

## NPO / OBO

```yaml
id: npo-obo
type: acronym
canonical: NPO / OBO
aliases:
  - NPO
  - OBO
  - Near-Packaged Optics
  - On-Board Optics
  - near-package optics
  - onboard optics
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-08
sources:
  - title: Co-Packaged Optics - when solving the wrong problems stalls deployment
    publisher: arXiv
    url: https://arxiv.org/abs/2603.21313
    accessed: 2026-06-08
  - title: Scaling AI Factories with Co-Packaged Optics for Better Power Efficiency
    publisher: NVIDIA Technical Blog
    url: https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/
    accessed: 2026-06-08
```

**Definition:** NPO and OBO refer to optical architectures that place optical engines on the board near the ASIC, between front-panel pluggable optics and fully co-packaged optics.

**Plain English:** NPO/OBO is the halfway step: optics move closer to the chip, but are not as deeply integrated as CPO.

**Why it matters:** NPO/OBO can improve electrical path efficiency versus pluggables while keeping less integration risk than full CPO, but repairability is worse than a swappable front-panel module.

**Usage notes:** Terminology is less standardized than DAC, AOC, or QSFP-DD. Treat NPO/OBO definitions as architecture categories rather than strict standards.

**Related:** CPO, Optical Module, SiPh, ASIC

## Optical Engine

```yaml
id: optical-engine
type: concept
canonical: Optical Engine
aliases:
  - optical engine
  - light engine
  - photonic engine
  - optical I/O engine
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-09
sources:
  - title: Progress in Research on Co-Packaged Optics
    publisher: Micromachines / MDPI
    url: https://www.mdpi.com/2072-666X/15/10/1211
    accessed: 2026-06-09
  - title: Co-packaged optics switch solution based on analog optical engines
    publisher: Justia Patents
    url: https://patents.justia.com/patent/11630261
    accessed: 2026-06-09
  - title: Photonic Integrated Circuit (PIC)
    publisher: Ayar Labs
    url: https://ayarlabs.com/photonic-integrated-circuit-pic/
    accessed: 2026-06-09
```

**Definition:** An optical engine is the electro-optical conversion module that transmits and receives optical signals by combining photonic components, electronic interface circuitry, and fiber/light interfaces.

**Plain English:** The optical engine is the electricity-to-light and light-to-electricity conversion block.

**Why it matters:** In CPO and NPO architectures, optical engines move closer to the switch ASIC or XPU to shorten high-speed electrical paths and reduce power loss. They can become a major value pool because they combine PIC, EIC, packaging, optical coupling, and test complexity.

**Usage notes:** Rick's pasted report-context describes the optical engine as the purple conversion block and says Goldman lists optical engines as the largest value component in the Quantum-X Photonics CPO switch BoM at 43%. I did not independently verify the exact 43% figure from a public primary source, so keep it as report-context.

**Related:** PIC, EIC, CPO, NPO / OBO, FAU, Modulator, Photodetector, XPU

## Optical Module

```yaml
id: optical-module
type: concept
canonical: Optical Module
aliases:
  - pluggable optical module
  - optical transceiver
  - pluggable transceiver
  - QSFP-DD
  - OSFP
domain:
  - optical-networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: 800G Optical Transceivers and Cables Guide
    publisher: Juniper Networks
    url: https://www.juniper.net/documentation/us/en/hardware/800g-optics-cables-guide/800g-optics-cables-guide.pdf
    accessed: 2026-06-08
  - title: Optical module
    publisher: Wikipedia
    url: https://en.wikipedia.org/wiki/Optical_module
    accessed: 2026-06-08
```

**Definition:** An optical module is a pluggable optical transceiver that converts electrical signals from network equipment into optical signals for fiber transmission and converts received light back into electrical signals.

**Plain English:** A pluggable optical module is a removable electricity-to-light adapter.

**Why it matters:** Pluggables remain important in scale-out networks because they are standardized, serviceable, and deployable across switches, NICs, and fiber reaches even as CPO grows.

**Usage notes:** Common high-speed form factors include QSFP-DD and OSFP; speeds such as 800G, 1.6T, and 3.2T depend on module generation and lane technology.

**Related:** AOC, CPO, DR / FR, EML, SiPh

## PCB

```yaml
id: pcb
type: acronym
canonical: PCB
aliases:
  - Printed Circuit Board
  - printed circuit board
  - circuit board
domain:
  - electronics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Printed Circuit Board
    publisher: Analog Devices
    url: https://www.analog.com/en/resources/glossary/printed-circuit.html
    accessed: 2026-06-08
  - title: What is printed circuit board (PCB)?
    publisher: TechTarget
    url: https://www.techtarget.com/whatis/definition/printed-circuit-board-PCB
    accessed: 2026-06-08
```

**Definition:** PCB stands for Printed Circuit Board: a layered insulating board with conductive traces, usually copper, that mechanically supports and electrically connects electronic components.

**Plain English:** PCB is the road system inside electronics.

**Why it matters:** GPUs, switches, memory, connectors, and retimers need high-speed short-distance electrical paths. PCB traces are cheap and power-efficient for short links, but high-speed signal integrity becomes harder as speed and distance increase.

**Usage notes:** Rick's pasted Goldman excerpt highlights dielectric loss, conductor loss, skin effect, and EMI sensitivity as high-speed PCB challenges.

**Related:** PCB Midplane, DAC, SerDes, ASIC

## PCB Midplane

```yaml
id: pcb-midplane
type: concept
canonical: PCB Midplane
aliases:
  - midplane
  - PCB backplane
  - backplane
domain:
  - electronics
  - ai-infrastructure
status: verified
confidence: medium
last_verified: 2026-06-08
sources:
  - title: Printed Circuit Board
    publisher: Analog Devices
    url: https://www.analog.com/en/resources/glossary/printed-circuit.html
    accessed: 2026-06-08
  - title: Printed circuit board manufacturing
    publisher: Wikipedia
    url: https://en.wikipedia.org/wiki/Printed_circuit_board_manufacturing
    accessed: 2026-06-08
```

**Definition:** A PCB midplane is a central printed-circuit-board interconnect structure that connects multiple boards, trays, or blades from both sides or across a chassis/rack section.

**Plain English:** A PCB midplane is like a motherboard for a larger server or rack section.

**Why it matters:** Dense AI racks can use high-layer-count, high-performance PCB midplanes for short scale-up links, shifting value toward advanced PCB makers, laminates, and high-speed materials.

**Usage notes:** Rick's pasted Goldman excerpt says Rubin Ultra NVL144 uses a PCB midplane for scale-up connections. I did not independently verify that platform-specific claim in public sources here, so treat it as report-context.

**Related:** PCB, Scale Up vs Scale Out, SerDes

## Photodetector

```yaml
id: photodetector
type: concept
canonical: Photodetector
aliases:
  - photodetector
  - photodiode
  - optical detector
  - PD
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: What is a Photonic Integrated Circuit?
    publisher: Ansys
    url: https://www.ansys.com/simulation-topics/what-is-a-photonic-integrated-circuit
    accessed: 2026-06-09
  - title: Telecom Transceivers
    publisher: RP Photonics
    url: https://www.rp-photonics.com/telecom_transceivers.html
    accessed: 2026-06-09
  - title: Optical Interconnects Finally Seeing the Light in Silicon Photonics
    publisher: Photonics / PMC
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8840221/
    accessed: 2026-06-09
```

**Definition:** A photodetector is a device that receives optical energy and converts it into an electrical signal, commonly as a small current.

**Plain English:** The photodetector turns incoming light back into electricity.

**Why it matters:** The receive side of an optical link depends on photodetectors to recover data from light arriving over fiber or an on-chip waveguide. The photodetector output is typically weak, so receiver electronics such as a TIA are needed before the signal is usable by an XPU or switch ASIC.

**Example:** Optical data arrives -> photodetector creates a tiny electrical current -> TIA amplifies/converts it -> XPU receives usable data.

**Related:** TIA, PIC, EIC, Optical Engine, XPU, Modulator

## PIC

```yaml
id: pic
type: acronym
canonical: PIC
aliases:
  - Photonic Integrated Circuit
  - photonic integrated circuit
  - integrated optical circuit
  - planar lightwave circuit
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: What is a Photonic Integrated Circuit?
    publisher: Ansys
    url: https://www.ansys.com/simulation-topics/what-is-a-photonic-integrated-circuit
    accessed: 2026-06-09
  - title: Photonic Integrated Circuits: Silicon-Adjacent Devices for High Beam-Bandwidth Communication and Sensing
    publisher: IEEE Communications Society
    url: https://www.comsoc.org/publications/ctn/photonic-integrated-circuits-silicon-adjacent-devices-high-beam-bandwidth
    accessed: 2026-06-09
  - title: What is a Photonic Integrated Circuit (PIC) and How Does It Work?
    publisher: Synopsys
    url: https://www.synopsys.com/glossary/what-is-a-photonic-integrated-circuit.html
    accessed: 2026-06-09
  - title: Photonic Integrated Circuit (PIC)
    publisher: Ayar Labs
    url: https://ayarlabs.com/glossary/photonic-integrated-circuit-pic/
    accessed: 2026-06-09
```

**Definition:** PIC stands for Photonic Integrated Circuit: a chip that integrates multiple light-based components into a functional optical circuit for generating, routing, modulating, multiplexing, demultiplexing, or detecting optical signals.

**Plain English:** A PIC is the light-processing chip inside an optical communication system.

**Why it matters:** PICs let optical modules, silicon photonics, and CPO-style systems move more optical functions onto one chip, improving density, power efficiency, manufacturability, and signal integrity. In AI infrastructure, the PIC is where much of the optical signal handling happens after high-speed electrical data is converted into light.

**Example:** A data-center optical module can use a PIC with waveguides/couplers to route light, modulators to encode data, MUX/DEMUX structures to combine or split wavelengths, and photodetectors to convert received light back into electrical signals.

**Usage notes:** A PIC is not the full optical module by itself. It is one chip or die inside a broader package that may also include lasers or external laser inputs, EICs, drivers, TIAs, DSPs, fibers/connectors, thermal management, and control electronics. Rick's pasted report-context says PIC and EIC lifecycles differ and frames the PIC as more delicate, which is one reason pluggable optical modules are serviceable: if the optical part fails, the module can be replaced instead of replacing the whole switch/XPU system.

**Related:** SiPh, Optical Module, CPO, EML, CW Laser, ELS, FAU, EIC, Modulator, Photodetector, MUX / DEMUX, Waveguide / Coupler

## Scale Up vs Scale Out

```yaml
id: scale-up-vs-scale-out
type: concept
canonical: Scale Up vs Scale Out
aliases:
  - scale up
  - scale out
  - vertical scaling
  - horizontal scaling
domain:
  - ai-infrastructure
  - cloud
  - software-engineering
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Vertical Scaling (Scale-up) vs. Horizontal Scaling (Scale-out)
    publisher: IBM
    url: https://www.ibm.com/think/topics/scale-up-vs-scale-out
    accessed: 2026-06-08
  - title: Design to scale out
    publisher: Microsoft Learn
    url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out
    accessed: 2026-06-08
```

**Definition:** Scale up means increasing capacity inside a system or tightly coupled node; scale out means increasing capacity by adding more nodes and connecting them as a larger distributed system.

**Plain English:** Scale up makes the box bigger; scale out connects more boxes.

**Why it matters:** AI infrastructure needs both: scale-up networking makes many GPUs act like one machine, while scale-out networking connects many racks or clusters.

**Usage notes:** In AI-rack investing, the key question is often not "copper or optics" but which links are scale-up, which are scale-out, and how both grow as clusters get larger.

**Related:** ToR / EoR, CPO, PCB Midplane, Optical Module

## SBC

```yaml
id: sbc
type: acronym
canonical: SBC
aliases:
  - stock-based compensation
  - Stock-Based Compensation
  - share-based compensation
domain:
  - finance
  - accounting
status: user-provided
confidence: high
last_verified: 2026-07-10
sources: []
```

**Definition:** SBC stands for stock-based compensation: employee or executive compensation paid in company equity, such as restricted stock units, stock options, or performance shares.

**Plain English:** SBC is paying people with stock instead of only cash.

**Why it matters:** SBC is often added back in non-GAAP earnings and free-cash-flow narratives, but it still dilutes shareholders unless offset by buybacks.

**Related:** EPS, FCF, Dilution, Non-GAAP

## SerDes

```yaml
id: serdes
type: acronym
canonical: SerDes
aliases:
  - Serializer/Deserializer
  - serializer-deserializer
  - serializer deserializer
domain:
  - semiconductors
  - networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: What is SerDes (Serializer/Deserializer)?
    publisher: Synopsys
    url: https://www.synopsys.com/glossary/what-is-serdes.html
    accessed: 2026-06-08
  - title: What is SerDes (serializer/deserializer)?
    publisher: TechTarget
    url: https://www.techtarget.com/searchstorage/definition/SerDes
    accessed: 2026-06-08
```

**Definition:** SerDes stands for Serializer/Deserializer: a high-speed circuit block that converts parallel data to serial data for transmission and converts it back at the receiver.

**Plain English:** SerDes turns many slower internal bits into a few very fast external lanes, then reverses the process at the other end.

**Why it matters:** Faster SerDes increases bandwidth but makes signal integrity harder, which drives demand for better PCB materials, retimers, active cables, and optics.

**Related:** PCB, ASIC, DSP, Redriver, and Retimer

## SiPh

```yaml
id: siph
type: acronym
canonical: SiPh
aliases:
  - Silicon Photonics
  - silicon photonics
  - integrated photonics
domain:
  - optical-networking
  - photonics
  - semiconductors
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Intel Silicon Photonics
    publisher: Intel
    url: https://www.intel.com/content/www/us/en/products/details/network-io/silicon-photonics.html
    accessed: 2026-06-08
  - title: What Is Silicon Photonics?
    publisher: Ansys
    url: https://www.ansys.com/en-gb/simulation-topics/what-is-silicon-photonics
    accessed: 2026-06-08
```

**Definition:** SiPh stands for Silicon Photonics: a platform for building photonic integrated circuits using silicon-based semiconductor manufacturing techniques.

**Plain English:** SiPh puts optical networking functions onto a chip-like manufacturing platform.

**Why it matters:** As optical modules and CPO engines move to higher speeds, silicon photonics can improve integration, bandwidth density, power, and manufacturing scalability.

**Usage notes:** Rick's pasted Goldman excerpt says SiPh penetration in optical transceiver modules rises from 6% in 1Q24 to 45% in 4Q28. I stored that as report-context and did not independently verify Goldman's forecast.

**Related:** CPO, ELS, CW Laser, EML, Optical Module

## TAC

```yaml
id: tac
type: acronym
canonical: TAC
aliases:
  - Traffic Acquisition Cost
  - traffic acquisition cost
  - Traffic Acquisition Costs
  - traffic acquisition costs
domain:
  - finance
  - accounting
  - internet-platforms
status: user-provided
confidence: medium
last_verified: 2026-07-10
sources: []
```

**Definition:** TAC stands for Traffic Acquisition Cost: payments a company makes to partners, publishers, device makers, browsers, carriers, or other distributors to acquire user traffic or monetize ad inventory.

**Plain English:** TAC is the toll paid to get traffic.

**Why it matters:** On an income statement, TAC is usually a major cost item for search, advertising, and internet-platform companies. Higher TAC can pressure gross margin or revenue ex-TAC, even when reported revenue is growing.

**Usage notes:** TAC is especially common in ad-tech and search analysis. For companies like Alphabet, analysts often compare gross revenue, TAC, and revenue ex-TAC to understand how much economics the platform keeps after paying distribution and network partners.

**Related:** Revenue, Gross Margin, Operating Margin, SBC

## TAM

```yaml
id: tam
type: acronym
canonical: TAM
aliases:
  - Total Addressable Market
  - total available market
  - total addressable market
domain:
  - finance
  - markets
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Total Addressable Market (TAM)
    publisher: Corporate Finance Institute
    url: https://corporatefinanceinstitute.com/resources/knowledge/strategy/total-addressable-market-tam/
    accessed: 2026-06-08
  - title: Total Addressable Market
    publisher: Chase for Business
    url: https://www.chase.com/business/knowledge-center/start/determining-your-total-addressable-market-tam
    accessed: 2026-06-08
```

**Definition:** TAM stands for Total Addressable Market: the total revenue opportunity available to a product or service if it captured the full defined market.

**Plain English:** TAM is the size of the whole revenue pool under the market definition being used.

**Why it matters:** In AI-hardware research, TAM estimates often multiply expected unit counts by dollar content, ASP, or BoM assumptions to size supplier opportunities.

**Usage notes:** TAM is only useful if the market boundary, time period, and assumptions are explicit.

**Related:** ASP, BoM, GM, EPS

## TIA

```yaml
id: tia
type: acronym
canonical: TIA
aliases:
  - Transimpedance Amplifier
  - transimpedance amplifier
  - optical receiver amplifier
  - receiver-side amplifier
domain:
  - optical-networking
  - photonics
  - semiconductors
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: Photodiode Amplifiers
    publisher: RP Photonics
    url: https://www.rp-photonics.com/photodiode_amplifiers.html
    accessed: 2026-06-09
  - title: Review of CMOS Integrated Circuit Technologies for High-Speed Photo-Detection
    publisher: Sensors / PMC
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5620527/
    accessed: 2026-06-09
  - title: Telecom Transceivers
    publisher: RP Photonics
    url: https://www.rp-photonics.com/telecom_transceivers.html
    accessed: 2026-06-09
```

**Definition:** TIA stands for Transimpedance Amplifier: a receiver-side electronic amplifier that converts a small photodetector current into a larger, usable voltage signal.

**Plain English:** The TIA makes the photodetector's tiny signal usable.

**Why it matters:** A photodetector usually produces a weak current, not a clean logic-level signal. The TIA is one of the first critical receive-side electronics blocks in an optical link, so its noise, gain, bandwidth, and power affect link quality.

**Example:** Photodetector receives light -> produces tiny current -> TIA converts/amplifies it into voltage -> downstream electronics recover the data.

**Usage notes:** Rick's pasted report-context places the TIA in the EIC on the receive side. Transmit side: driver controls modulator. Receive side: photodetector receives light and TIA amplifies the converted electrical signal.

**Related:** Photodetector, EIC, Driver, PIC, Optical Engine, XPU

## ToR / EoR

```yaml
id: tor-eor
type: acronym
canonical: ToR / EoR
aliases:
  - ToR
  - EoR
  - Top-of-Rack
  - End-of-Row
  - top-of-rack switch
  - end-of-row switch
domain:
  - networking
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: What is Top-of-Rack Switching?
    publisher: TechTarget
    url: https://www.techtarget.com/searchnetworking/definition/top-of-rack-switching
    accessed: 2026-06-08
  - title: Data Center Service Integration - Service Chassis Design
    publisher: Cisco
    url: https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Data_Center/dc_servchas/service-chassis_design.pdf
    accessed: 2026-06-08
```

**Definition:** ToR means Top-of-Rack switching, where servers in or near a rack connect to an in-rack switch; EoR means End-of-Row switching, where multiple racks connect to a switch or chassis at the row level.

**Plain English:** ToR is the local rack switch; EoR aggregates racks from the end of the row.

**Why it matters:** AI network distance, cabling, and optics requirements change depending on whether traffic goes to a nearby rack switch or a farther row-level aggregation point.

**Usage notes:** Leaf, spine, and super-spine are higher network layers above local rack or row switching.

**Related:** NIC, Scale Up vs Scale Out, Optical Module

## VCSEL

```yaml
id: vcsel
type: acronym
canonical: VCSEL
aliases:
  - Vertical-Cavity Surface-Emitting Laser
  - vertical cavity surface emitting laser
domain:
  - optical-networking
  - photonics
status: verified
confidence: high
last_verified: 2026-06-08
sources:
  - title: Vertical Cavity Surface-emitting Lasers
    publisher: RP Photonics
    url: https://www.rp-photonics.com/vertical_cavity_surface_emitting_lasers.html
    accessed: 2026-06-08
  - title: VCSEL - Vertical Cavity Surface Emitting Laser
    publisher: US-Lasers
    url: https://www.us-lasers.com/vcsels.htm
    accessed: 2026-06-08
```

**Definition:** VCSEL stands for Vertical-Cavity Surface-Emitting Laser: a semiconductor laser diode that emits light perpendicular to the wafer surface.

**Plain English:** VCSEL is a compact, efficient short-distance light source.

**Why it matters:** VCSELs are widely used for short-reach optical links, often with multimode fiber, making them relevant for AOCs and dense data-center interconnects.

**Related:** AOC, CW Laser, Optical Module

## Waveguide / Coupler

```yaml
id: waveguide-coupler
type: concept
canonical: Waveguide / Coupler
aliases:
  - waveguide
  - waveguides
  - optical waveguide
  - coupler
  - optical coupler
  - grating coupler
  - edge coupler
domain:
  - optical-networking
  - photonics
  - ai-infrastructure
status: verified
confidence: high
last_verified: 2026-06-09
sources:
  - title: Silicon Photonics
    publisher: RP Photonics Encyclopedia
    url: https://www.rp-photonics.com/silicon_photonics.html
    accessed: 2026-06-09
  - title: What is a Photonic Integrated Circuit?
    publisher: Ansys
    url: https://www.ansys.com/simulation-topics/what-is-a-photonic-integrated-circuit
    accessed: 2026-06-09
  - title: Optical Interconnects Finally Seeing the Light in Silicon Photonics
    publisher: Photonics / PMC
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8840221/
    accessed: 2026-06-09
  - title: Photonic Integrated Circuit (PIC)
    publisher: Ayar Labs
    url: https://ayarlabs.com/photonic-integrated-circuit-pic/
    accessed: 2026-06-09
```

**Definition:** A waveguide is an on-chip path that confines and guides light along a predetermined route; a coupler transfers light between waveguides, fibers, lasers, or other optical structures.

**Plain English:** A waveguide is an optical wire on the silicon chip: it guides light waves along a planned path, similar to how wires guide electrical signals. A coupler is the optical handoff point between chip, fiber, or light source.

**Why it matters:** PICs replace many discrete optical paths with tiny on-chip paths. Waveguides route light through the PIC, while couplers determine how efficiently light enters, exits, splits, or combines, directly affecting optical loss and packaging difficulty.

**Usage notes:** Rick's pasted report-context frames waveguides as tiny roads for light inside the PIC and couplers as the interfaces that move light between the PIC, fiber, or laser.

**Related:** PIC, MUX / DEMUX, FAU, Optical Engine, SiPh

## XPU

```yaml
id: xpu
type: jargon
canonical: XPU
aliases:
  - xPU
  - accelerator
  - compute chip
  - AI accelerator
  - heterogeneous processor
domain:
  - ai-infrastructure
  - semiconductors
  - compute
status: verified
confidence: medium
last_verified: 2026-06-09
sources:
  - title: Artificial Intelligence (AI) Accelerators
    publisher: Intel
    url: https://www.intel.com/content/www/us/en/learn/ai-accelerators.html
    accessed: 2026-06-09
  - title: Unified Acceleration (UXL) Foundation
    publisher: Intel
    url: https://www.intel.com/content/www/us/en/developer/articles/news/unified-acceleration-uxl-foundation.html
    accessed: 2026-06-09
  - title: XPU Offload Analysis
    publisher: Intel
    url: https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2025-4/xpu-offload-analysis.html
    accessed: 2026-06-09
```

**Definition:** XPU is a broad industry shorthand for a compute processor or accelerator, often used when the exact processor type could be a CPU, GPU, FPGA, NPU, TPU, ASIC, or custom accelerator.

**Plain English:** XPU means "the compute chip," without committing to which kind.

**Why it matters:** AI infrastructure is heterogeneous: different chips do different compute jobs, but all need to move data to memory, switches, NICs, optical engines, or other chips. The XPU computes in the electrical domain, so fiber communication requires an optical engine to translate electrical signals into optical signals and back.

**Usage notes:** Rick's pasted report-context says CPO can eventually be packaged with a switch ASIC or even with the XPU itself, but that increases serviceability risk: if the optical part fails, the failure may affect the XPU package rather than a replaceable pluggable module.

**Related:** Optical Engine, EIC, PIC, CPO, ASIC, NIC, SerDes
