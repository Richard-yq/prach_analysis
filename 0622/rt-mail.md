Dear Yi-Quan,

I have carefully reviewed your master’s thesis and presentation materials. From this point forward, I will take over the restructuring and rewriting of the work toward a full journal submission to the Journal of Network and Computer Applications (JNCA).

Your current thesis already contains valuable implementation work, especially the OAI-based RACH attack implementation and the O-RAN-based closed-loop mitigation prototype. However, a JNCA paper cannot be prepared by simply shortening the thesis and polishing the English. The paper must be rebuilt as an evidence-driven network security and network management system paper. Every technical claim must be supported by raw data, logs, figures, tables, or reproducible experiment settings.

Please prepare the following three items carefully. These will become the foundation for the JNCA manuscript.

1. JNCA Evidence Audit Checklist

For every major claim in the future paper, please provide the corresponding evidence. Do not only provide screenshots or final figures. I need the original raw data, logs, scripts, configuration files, and a short explanation of how each result was generated.

Please prepare the following checklist.

No.	Claim to be Used in JNCA Paper	Required Evidence	Current Status	Student Action Required
1	The proposed attacker is not a generic RF noise jammer but a protocol-aware PRACH attacker.	OAI UE code modification summary, relevant source-code files, explanation of PHY/MAC changes, commit ID if available.	To be verified	Provide code path, modified files, and short technical explanation.
2	The attacker can generate multiple valid Zadoff-Chu-based preambles in the same PRACH occasion.	Mathematical model, simulation result, OAI log, gNB detection log, correlation peak evidence.	To be verified	Provide raw logs and explain how the gNB detects multiple preambles.
3	The attacker supports multi-FDM PRACH occasion flooding.	PRACH configuration, msg1-FDM setting, gNB detection logs showing FDM 0/FDM 1 or more occasions.	To be verified	Provide complete configuration and detection evidence.
4	The attack can reduce legitimate RACH access success rate from normal operation to near zero.	RSR raw data, trial records, plotting script, number of trials, confidence/variance information.	Partially available	Provide the complete raw dataset behind the RSR figure.
5	The attack causes gNB resource exhaustion through illegitimate RAR/Msg3 UL grant allocation.	MAC scheduler logs, RAR logs, Msg3 UL grant records, RB consumption table.	Partially available	Provide logs and calculation method for UL RB consumption.
6	The attacker’s preamble energy can mimic legitimate UE preamble characteristics.	Attacker correlation peak data, legitimate UE correlation peak data, comparison figure.	To be verified	Provide both datasets and measurement conditions.
7	The O-RAN-based mitigation system can detect PRACH attack events.	VES event logs, Kafka topic logs, rApp logs, detection timestamp, threshold parameters.	To be verified	Provide event trace from gNB to SMO/rApp.
8	The mitigation system can automatically trigger reconfiguration and recovery.	ROMF/O1 command logs, gNB configuration before/after mitigation, restart log, topology update evidence.	To be verified	Provide complete mitigation execution trace.
9	The average end-to-end recovery latency is approximately 16.66 seconds.	Raw latency records, number of trials, breakdown of detection/analysis/reconfiguration/restart/re-attachment time.	Partially available	Provide raw latency data and calculation script.
10	UE re-attachment cost is measurable and should be considered in mitigation decision-making.	Re-attachment latency raw data, number of trials, average, standard deviation, test condition.	Must be clarified	Confirm the correct value and dataset. Do not mix different versions.
11	The cost-aware policy avoids unnecessary mitigation when active UE sessions exist.	Policy table, active UE count logs, decision logs, example cases of action/no-action.	To be verified	Provide decision examples and logs.
12	The framework can be extended to Msg3 opportunistic attack mitigation.	Msg3 attack logs, HARQ failure logs, rApp alert logs, mitigation result.	To be verified	Provide this as an extension case, not the main contribution.
Please mark each item as one of the following:

Completed with raw data

Completed with only figure/screenshot

Partially completed

Not yet available

Need to rerun experiment

A final JNCA paper cannot rely on “I remember the result” or “it worked during demo.” Reviewer confidence comes from reproducible evidence, not memory.

2. Experimental Reinforcement Table

The current thesis demonstrates the feasibility of the attack and mitigation. However, for JNCA, the evaluation must be stronger. Please prepare or rerun the following experiments if the current data are incomplete.

No.	Experiment	Purpose	Required Output	Priority
1	Normal operation baseline	Establish normal RACH success rate and normal RA behavior.	RSR, RA attempts, success/failure count, gNB logs, UE logs.	Required
2	Single-preamble attacker baseline	Show why multi-preamble attack is stronger than a simple attack.	RSR, detected preamble count, RAR/UL grant usage.	Required
3	AWGN or noise-like PRACH jamming baseline	Differentiate protocol-aware attack from generic RF jamming.	RSR, received energy, comparison with proposed attack.	Strongly required
4	Proposed multi-preamble single-FDM attack	Validate multi-preamble superposition within one FD occasion.	Detection log, preamble energy, RSR, resource usage.	Required
5	Proposed multi-preamble multi-FDM attack	Validate full attack capability across multiple frequency-domain occasions.	FDM-based detection log, 128-preamble evidence if applicable.	Required
6	Legitimate high-load but non-attack scenario	Show that the detector does not confuse normal burst access with attack.	False alarm rate, RSR, active UE count, RA statistics.	Critical
7	Detection threshold sensitivity	Show robustness of threshold selection.	Threshold vs. detection delay, miss rate, false alarm rate.	Critical
8	Attacker power/distance sensitivity	Show whether attack effectiveness depends on unrealistic radio proximity.	RSR vs. attacker distance/power.	Strongly required
9	Different PRACH configuration index settings	Show robustness under different RACH configurations.	RSR and mitigation results under at least two configurations.	Strongly required
10	Different msg1-FDM settings	Show scalability from one/two/four/eight FD occasions if feasible.	Detected preambles, RSR, resource usage.	Optional but valuable
11	Mitigation latency breakdown	Explain where the 16.66-second recovery time comes from.	Breakdown: detection, VES/Kafka, rApp, ROMF/O1, gNB restart, UE re-attachment.	Critical
12	Mitigation without active UE vs. with active UE	Support the cost-aware decision policy.	Decision logs, re-attachment cost, service disruption evidence.	Required
13	Msg3 opportunistic attack extension	Demonstrate framework extensibility.	HARQ failure logs, alert logs, mitigation result.	Secondary
14	Failure case / limitation case	Identify when the current method may not work.	Short discussion with evidence or technical reasoning.	Required
For each experiment, please provide:

Objective

Testbed configuration

Hardware/software versions

PRACH parameters

UE type and number of UEs

Attacker configuration

Number of trials

Raw data location

Plotting script location

Final figure/table candidate for JNCA

Please do not only send images. Images are useful for presentation, but raw data are necessary for journal writing.

3. Claim Control Table

JNCA reviewers will challenge overstatements. Therefore, we must control every claim carefully. Please use the table below to revise the claims from your thesis into journal-safe claims.

No.	Original / Risky Claim	Problem	JNCA-Safe Claim
1	This system solves RACH jamming attacks in 5G/6G networks.	Too broad; experiments are conducted in a controlled OAI/O-RAN testbed.	This work demonstrates a practical closed-loop mitigation prototype for protocol-aware RACH resource-exhaustion attacks in a controlled 5G NR OAI/O-RAN testbed.
2	The proposed system accurately detects the attack.	“Accurately” requires false positive/false negative evidence.	The proposed detector identifies the tested PRACH flooding attack under the evaluated testbed conditions.
3	The mitigation restores the network in real time.	16.66 seconds is not always “real time”; needs precise wording.	The mitigation restores RACH accessibility with an average end-to-end recovery latency of approximately 16.66 seconds in the tested setup.
4	The attacker blocks all legitimate UEs.	Too absolute unless tested across many UE types and conditions.	In the evaluated testbed, the attack reduces the measured legitimate RACH success rate from the normal baseline to near zero.
5	The method is suitable for 6G networks.	No 6G system was tested.	The findings provide design insights for future resilient access mechanisms in open and programmable RAN architectures.
6	The O-RAN framework provides complete protection.	Too strong; mitigation relies on reconfiguration and restart.	The O-RAN-based framework provides an automated recovery mechanism for the evaluated attack scenario.
7	The proposed attacker is stealthy.	Stealth must be measured.	The attacker uses valid PRACH preamble structures that can trigger standard gNB preamble detection behavior.
8	The cost-aware policy is optimal.	No optimization proof.	The cost-aware policy reduces unnecessary mitigation actions by considering active UE sessions and re-attachment cost.
9	The Msg3 mitigation proves generality.	One extension case does not prove generality.	The Msg3 case study suggests that the event-driven mitigation framework can be extended to other random-access-stage anomalies.
10	The proposed design is deployable in commercial networks.	Commercial deployment not validated.	The proposed design demonstrates feasibility using open-source 5G and O-RAN components and highlights deployment considerations for future work.
Please review your thesis and slides and list all claims that may be too strong. For each claim, provide the original wording, the evidence you currently have, and a safer journal-paper version.

4. Required File Organization

Please organize the materials in the following structure:

JNCA_RACH_Paper/
  01_Thesis_and_Slides/
  02_Raw_Data/
    RSR_Normal/
    RSR_Attack/
    RSR_Mitigation/
    Threshold_Sensitivity/
    Reattachment_Latency/
    Msg3_Extension/
  03_Logs/
    OAI_gNB/
    OAI_UE_Attacker/
    VES_Kafka/
    rApp/
    ROMF_O1/
  04_Config_Files/
    gNB_Config_Before/
    gNB_Config_After/
    PRACH_Settings/
  05_Code_Modification/
    OAI_UE_Attacker/
    gNB_Detector/
    rApp/
  06_Plotting_Scripts/
  07_Figures_For_JNCA/
  08_Tables_For_JNCA/
  09_Evidence_Audit_Checklist/
  10_Claim_Control_Table/
Every figure in the future JNCA paper must be traceable to raw data and scripts. Every claim must be traceable to evidence.

5. Expected Direction of the JNCA Paper

The future paper should not be written as a thesis summary. It should be positioned as:

“Protocol-aware RACH resource-exhaustion attacks and O-RAN-enabled closed-loop mitigation for resilient 5G access networks.”

The main story should be:

RACH is a critical pre-authentication access procedure in 5G NR.

A protocol-aware attacker can exploit valid PRACH preamble structures to trigger gNB resource exhaustion.

A multi-preamble and multi-FDM attacker is implemented using OAI UE modifications.

The attack impact is validated using an end-to-end 5G testbed.

An O-RAN-based event-driven mitigation framework is implemented using SMO, VES, ROMF/O1, and a Non-RT RIC rApp.

The system recovers access service under the evaluated attack conditions.

The remaining limitations and deployment considerations are discussed honestly.

This is the story that can become a JNCA paper. The thesis already gives us useful building blocks, but the journal paper must be sharper, more controlled, and more evidence-driven.

Please start by completing the three tables above. The priority is not beautiful formatting at this stage. The priority is evidence completeness. A reviewer will not accept a paper because the story sounds interesting; the reviewer will accept it only when the claims, experiments, and evidence all line up.

Please send me the completed checklist, the experiment status table, and the claim control table when ready. Once I confirm the evidence status, I will start restructuring the paper into the JNCA format.

Best regards,
RT