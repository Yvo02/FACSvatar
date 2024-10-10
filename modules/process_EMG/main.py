import sys
import argparse
import numpy as np

# own imports; if statement for documentation
if __name__ == '__main__':
    sys.path.append("..")
    from facsvatarzeromq import FACSvatarZeroMQ
else:
    from modules.facsvatarzeromq import FACSvatarZeroMQ


# client to message broker server
class FACSvatarMessages(FACSvatarZeroMQ):
    """Receives FACS and Head movement data; forward to output function"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.emgToMessage = EMGtoMessage()





    async def sub(self):
        mu = 0  # Mittelwert
        sigma = 400  # Breitere Standardabweichung
        max_value = 100  # Maximaler Wert für die Kurvenspitze

        # x-Werte erzeugen (von -1000 bis 1000 in 0.1er-Schritten für mehr Datenpunkte)
        x_values = np.arange(-1500, 1500, 0.1)

        # Berechnung der y-Werte
        y_values = max_value * np.exp(-0.5 * ((x_values - mu) / sigma) ** 2)

        for intensity in y_values:
            msg = {"confidence": 0.98, "frame": 0, "timestamp": 0.0, "au_r":
                {"AU01": round(intensity/100, 3),
                 "AU02": 0.0,
                 "AU04": 0.0,
                 "AU05": 0.0,
                 "AU06": 0.0,
                 "AU07": 0.0,
                 "AU09": 0.0,
                 "AU10": 0.0,
                 "AU12": 0.0,
                 "AU14": 0.0,
                 "AU15": 0.0,
                 "AU17": 0.0,
                 "AU20": 0.0,
                 "AU23": 0.0,
                 "AU25": 0.0,
                 "AU26": 0.0,
                 "AU45": 0},
                   "gaze":
                       {"gaze_angle_x": 0.07,
                        "gaze_angle_y": 0.349},
                   "pose":
                       {"pose_Rx": 0.039,
                        "pose_Ry": -0.032,
                        "pose_Rz": -0.0559999999999999},
                   "timestamp_utc": 17244184896509564}
            await self.pub_socket.pub(msg)



if __name__ == '__main__':
    # command line arguments
    parser = argparse.ArgumentParser()

    # publisher setup commandline arguments
    parser.add_argument("--pub_ip", default=argparse.SUPPRESS,
                        help="IP (e.g. 192.168.x.x) of where to pub to; Default: 127.0.0.1 (local)")
    parser.add_argument("--pub_port", default="5570",
                        help="Port of where to pub to; Default: 5570")
    parser.add_argument("--pub_key", default="openface",
                        help="Key for filtering message; Default: openface")
    parser.add_argument("--pub_bind", default=False,
                        help="True: socket.bind() / False: socket.connect(); Default: False")

    args, leftovers = parser.parse_known_args()

    # init FACSvatar message class
    facsvatar_messages = FACSvatarMessages(**vars(args))
    # start processing messages; give list of functions to call async
    facsvatar_messages.start([facsvatar_messages.sub])