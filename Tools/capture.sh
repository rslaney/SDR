# Command line spectrum analyzer for the HackRF Pro range


CAPTURE_FILE="capture.iq" # -r, raw signed 8-bit IQ samples
CENTER_FREQ=43300000 # -f, Center freq of interest
SAMP_RATE=2000000 # -s, Sample rate to 2 Msps
NUM_SAMPLES=20000000 # -n, Limit capture to 20 million samples

touch "$CAPTURE_FILE"

hackrf_transfer -r "$CAPTURE_FILE" -f "$CENTER_FREQ" -s "$SAMP_RATE" -n "$NUM_SAMPLES"

echo "Convert with convert_s8_cfile.grc!"