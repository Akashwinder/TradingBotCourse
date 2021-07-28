import logging

from Connectors.binance import BinanceClient
from Connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("93c09e40ae786d5fba641064471d41173fa0f95255c75d500ed306d0fbf6724f",
                            "4a6078132c52c95afc3a58443f9ccc83e8e38ccf30aaf1dafbc44a07b569a01a",
                            testnet=True, futures=True)
    bitmex = BitmexClient("o_05lFTtxFV_lWPKhaBV8TdA", "4hW_Zs7rgnIBfQzSlAwY0iSx3lCbeea3dikFm8ltc9eUmJHh", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
