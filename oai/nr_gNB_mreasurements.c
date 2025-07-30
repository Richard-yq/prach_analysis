/*
 * Licensed to the OpenAirInterface (OAI) Software Alliance under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The OpenAirInterface Software Alliance licenses this file to You under
 * the OAI Public License, Version 1.1  (the "License"); you may not use this file
 * except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.openairinterface.org/?page_id=698
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *-------------------------------------------------------------------------------
 * For more information about the OpenAirInterface (OAI) Software Alliance:
 *      contact@openairinterface.org
 */

/*! \file PHY/NR_ESTIMATION/nr_gNB_prach_measurements.c
* \brief gNB PRACH-specific measurement routines for 5G NR
* \author Based on LTE eNB measurements, adapted for 5G
* \date 2025
* \version 0.1
* \company OpenAirInterface
* \note Provides enhanced noise and interference measurements for PRACH detection
* \warning
*/

#include "PHY/types.h"
#include "PHY/defs_gNB.h"
#include "nr_ul_estimation.h"
#include "PHY/sse_intrin.h"
#include "common/utils/LOG/log.h"

// Constants for IIR filtering (same as LTE for compatibility)
#define k1 1024
#define k2 (1024-k1)

static int32_t rx_power_avg_gNB[MAX_MOBILES_PER_GNB];

/*!
 * \brief Dump PRACH I0 statistics for debugging
 * \param fd File descriptor for output
 * \param gNB Pointer to gNB structure
 */
void dump_nr_prach_I0_stats(FILE *fd, PHY_VARS_gNB *gNB) {
    int min_I0 = 1000, max_I0 = 0;
    int amin = 0, amax = 0;
    
    fprintf(fd, "5G NR gNB PRACH I0 Statistics\n");
    fprintf(fd, "============================\n");
    fprintf(fd, "Blacklisted PRBs %d/%d\n", gNB->num_ulprbbl, gNB->frame_parms.N_RB_UL);
    
    // Find min/max I0 values
    for (int i = 0; i < gNB->frame_parms.N_RB_UL; i++) {
        if (gNB->ulprbbl[i] > 0) continue; // Skip blacklisted PRBs
        
        if (gNB->measurements.n0_subband_power_tot_dB[i] < min_I0) {
            min_I0 = gNB->measurements.n0_subband_power_tot_dB[i];
            amin = i;
        }
        
        if (gNB->measurements.n0_subband_power_tot_dB[i] > max_I0) {
            max_I0 = gNB->measurements.n0_subband_power_tot_dB[i];
            amax = i;
        }
    }
    
    // Print I0 values relative to average
    for (int i = 0; i < gNB->frame_parms.N_RB_UL; i++) {
        if (gNB->ulprbbl[i] == 0) {
            fprintf(fd, "%2d.", gNB->measurements.n0_subband_power_tot_dB[i] - gNB->measurements.n0_subband_power_avg_dB);
        } else {
            fprintf(fd, " X.");
        }
        if (i % 25 == 24) fprintf(fd, "\n");
    }
    
    fprintf(fd, "\nmax_I0 %d dB (rb %d), min_I0 %d dB (rb %d), avg I0 %d dB\n", 
            max_I0, amax, min_I0, amin, gNB->measurements.n0_subband_power_avg_dB);
    
    if (gNB->frame_parms.nb_antennas_rx > 1) {
        fprintf(fd, "Per-antenna avg I0: (");
        for (int aarx = 0; aarx < gNB->frame_parms.nb_antennas_rx; aarx++) {
            fprintf(fd, "%d.", gNB->measurements.n0_subband_power_avg_perANT_dB[aarx]);
        }
        fprintf(fd, ")\n");
    }
    
    fprintf(fd, "PRACH I0 = %d.%d dB\n", gNB->measurements.prach_I0/10, gNB->measurements.prach_I0%10);
}

/*!
 * \brief Enhanced 5G NR gNB I0 measurements for PRACH detection
 * \param gNB Pointer to gNB structure
 * \param slot Slot number for measurements
 * \param frame Frame number
 * \param clear Flag to clear previous measurements (1=clear, 0=accumulate)
 * 
 * This function performs comprehensive noise and interference measurements
 * optimized for PRACH detection in 5G NR systems. It's based on the LTE
 * eNB measurements but adapted for NR frame structure and requirements.
 */
void nr_gNB_prach_I0_measurements(PHY_VARS_gNB *gNB,
                                  int slot,
                                  int frame,
                                  unsigned char clear)
{
    NR_DL_FRAME_PARMS *frame_parms = &gNB->frame_parms;
    NR_gNB_COMMON *common_vars = &gNB->common_vars;
    PHY_MEASUREMENTS_gNB *measurements = &gNB->measurements;
    
    uint32_t aarx;
    uint32_t rb;
    c16_t *ul_ch;
    int32_t n0_power_tot;
    int64_t n0_power_tot2;
    int len;
    int offset;
    
    // Initialize total noise power
    measurements->n0_power_tot = 0;
    
    if (common_vars->rxdataF[0] != NULL) {
        for (aarx = 0; aarx < frame_parms->nb_antennas_rx; aarx++) {
            if (clear == 1) {
                measurements->n0_power[aarx] = 0;
            }
            
            // Measure noise power on a reference symbol (similar to LTE approach)
            // Use last symbol of the slot for noise measurement
            int symbol_offset = ((slot & 3) * frame_parms->symbols_per_slot + 
                               frame_parms->symbols_per_slot - 1) * frame_parms->ofdm_symbol_size;
            
            measurements->n0_power[aarx] = ((k1 * signal_energy(&common_vars->rxdataF[0][aarx][symbol_offset],
                                                               frame_parms->ofdm_symbol_size)) + 
                                          k2 * measurements->n0_power[aarx]) >> 10;
            
            measurements->n0_power_dB[aarx] = (unsigned short) dB_fixed(measurements->n0_power[aarx]);
            measurements->n0_power_tot += measurements->n0_power[aarx];
        }
        
        measurements->n0_power_tot_dB = (unsigned short) dB_fixed(measurements->n0_power_tot);
    }
    
    // Per-PRB noise measurements
    allocCast2D(n0_subband_power,
                unsigned int,
                gNB->measurements.n0_subband_power,
                frame_parms->nb_antennas_rx,
                frame_parms->N_RB_UL,
                false);
    allocCast2D(n0_subband_power_dB,
                unsigned int,
                gNB->measurements.n0_subband_power_dB,
                frame_parms->nb_antennas_rx,
                frame_parms->N_RB_UL,
                false);
    
    n0_power_tot2 = 0;
    int nb_rb = 0;
    int32_t n0_subband_tot_perANT[frame_parms->nb_antennas_rx];
    memset(n0_subband_tot_perANT, 0, sizeof(n0_subband_tot_perANT));
    
    for (rb = 0; rb < frame_parms->N_RB_UL; rb++) {
        n0_power_tot = 0;
        
        // Skip blacklisted PRBs
        if (gNB->ulprbbl && gNB->ulprbbl[rb] > 0) {
            continue;
        }
        
        // Skip middle PRB to avoid DC component issues
        if (rb == (frame_parms->N_RB_UL >> 1)) {
            continue;
        }
        
        int offset0 = (frame_parms->first_carrier_offset + (rb * 12)) % frame_parms->ofdm_symbol_size;
        nb_rb++;
        
        for (aarx = 0; aarx < frame_parms->nb_antennas_rx; aarx++) {
            n0_subband_power[aarx][rb] = 0;
            
            // Measure across multiple symbols for better accuracy
            int num_symbols = frame_parms->symbols_per_slot - 2; // Avoid control symbols
            for (int s = 1; s < num_symbols + 1; s++) {
                int symbol_offset = ((slot & 3) * frame_parms->symbols_per_slot + s) * frame_parms->ofdm_symbol_size;
                offset = symbol_offset + offset0;
                ul_ch = (c16_t *)&common_vars->rxdataF[0][aarx][offset];
                len = 12;
                
                // Handle odd number of PRBs for middle PRB
                if (((frame_parms->N_RB_UL & 1) == 1) && 
                    (rb == (frame_parms->N_RB_UL >> 1))) {
                    len = 6;
                }
                
                AssertFatal(ul_ch, "RX signal buffer (freq) problem");
                n0_subband_power[aarx][rb] += signal_energy_nodc(ul_ch, len);
            }
            
            // Average over symbols
            n0_subband_power[aarx][rb] /= num_symbols;
            n0_subband_power_dB[aarx][rb] = dB_fixed(n0_subband_power[aarx][rb]);
            n0_power_tot += n0_subband_power[aarx][rb];
            n0_subband_tot_perANT[aarx] += n0_subband_power[aarx][rb];
        }
        
        // Average across antennas
        n0_power_tot /= frame_parms->nb_antennas_rx;
        n0_power_tot2 += n0_power_tot;
        measurements->n0_subband_power_tot_dB[rb] = dB_fixed(n0_power_tot);
        measurements->n0_subband_power_tot_dBm[rb] = measurements->n0_subband_power_tot_dB[rb] - 
                                                    gNB->rx_total_gain_dB - 
                                                    dB_fixed(frame_parms->N_RB_UL);
    }
    
    // Calculate average noise power
    if (nb_rb > 0) {
        measurements->n0_subband_power_avg_dB = dB_fixed(n0_power_tot2 / nb_rb);
        for (int aarx = 0; aarx < frame_parms->nb_antennas_rx; aarx++) {
            measurements->n0_subband_power_avg_perANT_dB[aarx] = 
                dB_fixed(n0_subband_tot_perANT[aarx] / nb_rb);
        }
    }
    
    LOG_I(NR_PHY, "[%d.%d] NR gNB I0 measurements: avg_I0=%d dB, prach_I0=%d.%d dB, measured_PRBs=%d\n",
          frame, slot, measurements->n0_subband_power_avg_dB, 
          measurements->prach_I0/10, measurements->prach_I0%10, nb_rb);
}

/*!
 * \brief Enhanced PRACH energy detection with improved statistics
 * \param gNB Pointer to gNB structure
 * \param frame Frame number
 * \param slot Slot number
 * \param max_preamble_energy Array of maximum preamble energies
 * \param detection_threshold Detection threshold in dB
 * \return 1 if PRACH detected above threshold, 0 otherwise
 * 
 * This function provides enhanced PRACH detection capabilities with
 * improved noise floor estimation and adaptive threshold management.
 */
int nr_gNB_enhanced_prach_detection(PHY_VARS_gNB *gNB,
                                   int frame,
                                   int slot,
                                   uint16_t *max_preamble_energy,
                                   int detection_threshold)
{
    PHY_MEASUREMENTS_gNB *measurements = &gNB->measurements;
    
    // Update PRACH I0 with improved filtering
    if (max_preamble_energy[0] > 0) {
        // Use more conservative filtering for stable noise floor estimation
        measurements->prach_I0 = ((measurements->prach_I0 * 950) >> 10) + 
                                ((max_preamble_energy[0] * 74) >> 10);
        
        // Log enhanced statistics
        if (frame % 100 == 0) {
            LOG_I(NR_PHY, "[Enhanced] Frame %d: PRACH I0 = %d.%d dB, energy = %d.%d dB, threshold = %d dB\n",
                  frame, measurements->prach_I0/10, measurements->prach_I0%10,
                  max_preamble_energy[0]/10, max_preamble_energy[0]%10, detection_threshold);
        }
    }
    
    // Enhanced detection logic
    int detection_margin = max_preamble_energy[0] - (measurements->prach_I0 + detection_threshold);
    
    if (detection_margin > 0) {
        LOG_I(NR_PHY, "[Enhanced PRACH] Detection: energy=%d.%d dB, I0=%d.%d dB, margin=%d.%d dB\n",
              max_preamble_energy[0]/10, max_preamble_energy[0]%10,
              measurements->prach_I0/10, measurements->prach_I0%10,
              detection_margin/10, detection_margin%10);
        return 1;
    }
    
    return 0;
}

/*!
 * \brief Initialize PRACH measurement structures
 * \param gNB Pointer to gNB structure
 */
void nr_gNB_prach_measurements_init(PHY_VARS_gNB *gNB)
{
    PHY_MEASUREMENTS_gNB *measurements = &gNB->measurements;
    
    // Initialize PRACH I0 to a reasonable default value (e.g., -100 dBm equivalent)
    measurements->prach_I0 = 1000; // 100.0 dB
    
    // Initialize other measurement parameters
    for (int i = 0; i < MAX_MOBILES_PER_GNB; i++) {
        rx_power_avg_gNB[i] = 0;
    }
    
    LOG_I(NR_PHY, "NR gNB PRACH measurements initialized\n");
}
