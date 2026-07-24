# Command line spectrum analyzer for the HackRF Pro range


AMP_ENABLE=0 # 0 Disable, 1 Enable
FREQ_MIN=1 # Min Freq in MHz
FREQ_MAX=6000 # Max Freq in MHz
ANT_PORT_POWER=0 # Antenna port power, 1=Enable, 0=Disable
IF_GAIN=0 # IF Gain, 0-40dB, 8dB steps
BB_GAIN=0 # BB Gain, 0-62dB, 2dB steps
BIN_WIDTH=2445 # FFT Bin width (Freq resolution), Hz, 2445-5000000
NUM_SWEEPS=5 
OUT_FILE="sweeps/test.dat" # Stores in local subdirectory



touch "$OUT_FILE"

hackrf_sweep -a "$AMP_ENABLE" -f "$FREQ_MIN":"$FREQ_MAX" -p "$ANT_PORT_POWER" -l "$IF_GAIN" -g "$BB_GAIN" -w "$BIN_WIDTH" -N "$NUM_SWEEPS" -r "$OUT_FILE"