# Network-Speed-Tester
Created By     : x_4rch4n63l_x
Created On     : 1/7/2025 - 1:20AM
Script Purpose : Measure network download and upload speeds
Description    : This script uses the 'speedtest-cli' library to measure and report the 
                 network's download and upload speeds in megabits per second (Mbps). 
                 It also provides the ping time in milliseconds (ms).
                 
                 The script finds the best server for testing, performs the download and 
                 upload tests with visual effects, and displays the results. It then 
                 pauses to ensure the results are visible before the script closes.
                 
Features       :
                 - Finds the best server for testing.
                 - Measures download speed in Mbps.
                 - Measures upload speed in Mbps.
                 - Reports ping time in milliseconds.
                 - Loading spinner effects during tests.
                 - Pauses to display results.
Requirements   :
                 - Python 3.x
                 - 'speedtest-cli' library (install using `pip install speedtest-cli`)
                 - 'halo' library (install using `pip install halo`)
