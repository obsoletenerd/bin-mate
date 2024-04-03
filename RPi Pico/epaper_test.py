#   .-------------.---------------------------------------------.
#   | Project     |   Bin Mate / epaper_test.py                 |
#   | Author      |   SenWerks - senwerks.com                   |
#   | Description |   Quick test that your ePaper hat works     |
#   | Source      |   https://github.com/senwerks/Bin-Mate      |
#   |-------------|---------------------------------------------|
#   | Version     |   V1.0                                      |
#   | Release     |   2024-04-03                                |
#   '-------------'---------------------------------------------'

from pico_epaper import EPD_2in13

# Initialise the epaper library
epd = EPD_2in13()
epd.init(epd.full_update)

# Fill buffer with white
epd.fill(0xFF)

# Add text to buffer at column 4, row 32, in black
epd.text("Hello Universe!", 4, 32, 0x00)

# Send buffer to the display
epd.display(epd.buffer)

# Delay to stop the universe exploding
epd.delay_ms(1000)

# Fin
epd.sleep()