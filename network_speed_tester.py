# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 1/7/2025 - 1:20AM
# Script Purpose : Measure network download and upload speeds
# Description    : This script uses the 'speedtest-cli' library to measure and report the 
#                  network's download and upload speeds in megabits per second (Mbps). 
#                  It also provides the ping time in milliseconds (ms).
#                  
#                  The script finds the best server for testing, performs the download and 
#                  upload tests with visual effects, and displays the results. It then 
#                  pauses to ensure the results are visible before the script closes.
#                  
# Features       :
#                  - Finds the best server for testing.
#                  - Measures download speed in Mbps.
#                  - Measures upload speed in Mbps.
#                  - Reports ping time in milliseconds.
#                  - Loading spinner effects during tests.
#                  - Pauses to display results.
# Requirements   :
#                  - Python 3.x
#                  - 'speedtest-cli' library (install using `pip install speedtest-cli`)
#                  - 'halo' library (install using `pip install halo`)
# ===================================================================================
import speedtest
from halo import Halo
import sys

def test_speed():
    try:
        st = speedtest.Speedtest()

        spinner = Halo(text='Finding the best server...', spinner='dots')
        spinner.start()
        st.get_best_server()
        spinner.succeed('Best server found.')

        spinner.text = 'Performing download test...'
        spinner.start()
        download_speed = st.download() / 1_000_000
        spinner.succeed(f'Download speed: {download_speed:.2f} Mbps')

        spinner.text = 'Performing upload test...'
        spinner.start()
        upload_speed = st.upload() / 1_000_000
        spinner.succeed(f'Upload speed: {upload_speed:.2f} Mbps')

        ping = st.results.ping
        print(f"Ping: {ping:.2f} ms")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    input("Press Enter to exit...")

if __name__ == '__main__':
    test_speed()
