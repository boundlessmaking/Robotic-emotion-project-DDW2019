# Dictionary of every letter+ Number with a list of coordinate lists- {a : [ [0,1], [1,1], ...] }


class ThingToWrite:

    def __init__(self,string, z_hop = 0.01):
        self.string = string
        self.alphabet =  {
    "a": [[[0.719512, -0.932927], [0.719512, -0.594512], [0.416159, -0.314024], [0.106707, -0.631098], [0.416159, -0.95122], [0.530488, -0.922256]]],
    "b": [[[0.315549, -0.339939], [0.717226, -0.496951], [0.650152, -0.866616], [0.307165, -0.927591], [0.128049, -0.60061], [0.128049, 0]]],
    "c": [[[0.493902, -0.332317], [0.426829, -0.332317], [0.135671, -0.634146], [0.445122, -0.932927], [0.493902, -0.932927]]],
    "d": [[[0.532012, -0.339939], [0.130335, -0.496951], [0.197409, -0.866616], [0.540396, -0.927591], [0.719512, -0.60061], [0.719512, 0]]],
    "e": [[[0.317073, -0.672256], [0.685976, -0.467988], [0.425305, -0.317073], [0.114329, -0.634146], [0.425305, -0.95122], [0.724085, -0.731707]]],
    "f": [[[0.365854, -0.332317], [0.146341, -0.332317]], [[0.384146, 0], [0.347561, 0], [0.146341, -0.198171], [0.146341, -0.932927]]],
    "g": [[[0.532012, -0.932927], [0.141006, -0.772866], [0.204268, -0.403201], [0.54497, -0.342226], [0.719512, -0.631098], [0.719512, -0.964939], [0.400915, -1.283537], [0.243902, -1.262195]]],
    "h": [[[0.135671, 0], [0.135671, -0.932927]], [[0.135671, -0.932927], [0.135671, -0.573171], [0.385671, -0.317073], [0.626524, -0.573171], [0.626524, -0.932927]]],
    "i": [[[0.21189, -0.932927], [0.21189, -0.335366]], [[0.198171, -0.105183], [0.21189, -0.091463], [0.22561, -0.105183], [0.21189, -0.118902], [0.198171, -0.105183]], [[0.198171, -0.105183], [0.21189, -0.118902], [0.22561, -0.105183], [0.21189, -0.091463], [0.198171, -0.105183]]],
    "j": [[[0.170732, -0.335366], [0.170732, -1.047256], [-0.032012, -1.26372]], [[0.157012, -0.105183], [0.170732, -0.091463], [0.184451, -0.105183], [0.170732, -0.118902], [0.157012, -0.105183]], [[0.157012, -0.105183], [0.170732, -0.118902], [0.184451, -0.105183], [0.170732, -0.091463], [0.157012, -0.105183]]],
    "k": [[[0.551829, -0.932927], [0.551829, -0.792683], [0.365854, -0.603659], [0.146341, -0.603659]], [[0.545732, -0.335366], [0.474085, -0.458841], [0.269817, -0.603659], [0.146341, -0.603659]], [[0.146341, 0], [0.146341, -0.932927]]],
    "l": [[[0.169207, 0], [0.169207, -0.932927]]],
    "m": [[[0.958841, -0.932927], [0.958841, -0.518293], [0.762195, -0.317073], [0.550305, -0.553354], [0.550305, -0.932927], [0.550305, -0.553354], [0.338415, -0.317073], [0.141768, -0.518293], [0.141768, -0.932927]]],
    "n": [[[0.626524, -0.932927], [0.626524, -0.573171], [0.381098, -0.315549], [0.135671, -0.573171], [0.135671, -0.932927]]],
    "o": [[[0.114329, -0.634146], [0.42378, -0.317073], [0.733232, -0.634146], [0.42378, -0.95122], [0.114329, -0.634146]], [[0.114329, -0.634146], [0.42378, -0.95122], [0.733232, -0.634146], [0.42378, -0.317073], [0.114329, -0.634146]]],
    "p": [[[0.315549, -0.928354], [0.717226, -0.770579], [0.650152, -0.401677], [0.307165, -0.340701], [0.128049, -0.667683], [0.128049, -1.268293]]],
    "q": [[[0.532012, -0.928354], [0.130335, -0.770579], [0.197409, -0.401677], [0.540396, -0.340701], [0.719512, -0.667683], [0.719512, -1.268293]]],
    "r": [[[0.359756, -0.318598], [0.134146, -0.646341], [0.134146, -0.932927]], [[0.134146, -0.335366], [0.134146, -0.932927]]],
    "s": [[[0.541159, -0.335366], [0.280488, -0.335366], [0.112805, -0.463415], [0.34375, -0.627287], [0.45503, -0.662348], [0.574695, -0.79878], [0.417683, -0.932927], [0.109756, -0.932927]]],
    "t": [[[0.419207, -0.332317], [0.157012, -0.332317]], [[0.157012, -0.152439], [0.157012, -0.771341], [0.315549, -0.932927], [0.419207, -0.932927]]],
    "u": [[[0.626524, -0.335366], [0.626524, -0.695122], [0.381098, -0.95122], [0.135671, -0.695122], [0.135671, -0.335366]]],
    "v": [[[0.599085, -0.335366], [0.391768, -0.891768], [0.338415, -0.95122], [0.28811, -0.891768], [0.079268, -0.335366]]],
    "w": [[[0.958841, -0.335366], [0.958841, -0.75], [0.762195, -0.95122], [0.550305, -0.714939], [0.550305, -0.335366], [0.550305, -0.714939], [0.338415, -0.95122], [0.141768, -0.75], [0.141768, -0.335366]]],
    "x": [[[0.079268, -0.932927], [0.297256, -0.634146], [0.079268, -0.335366]], [[0.515244, -0.932927], [0.297256, -0.634146], [0.515244, -0.335366]]],
    "y": [[[0.381098, -0.95122], [0.381098, -1.260671]], [[0.618902, -0.339939], [0.618902, -0.707317], [0.381098, -0.95122], [0.143293, -0.707317], [0.143293, -0.339939]]],
    "z": [[[0.120427, -0.339939], [0.403963, -0.339939], [0.474085, -0.381098], [0.463415, -0.420732], [0.13872, -0.817073], [0.114329, -0.919207], [0.158537, -0.932927], [0.487805, -0.932927]]],
    "0": [[[0.128049, -0.304878], [0.128049, -0.621951], [0.42378, -0.95122], [0.719512, -0.621951], [0.719512, -0.304878], [0.42378, 0.018293], [0.128049, -0.304878]], [[0.128049, -0.304878], [0.42378, 0.018293], [0.719512, -0.304878], [0.719512, -0.621951], [0.42378, -0.95122], [0.128049, -0.621951], [0.128049, -0.304878]]],
    "1": [[[0.434451, -0.932927], [0.434451, 0], [0.256098, 0]]],
    "2": [[[0.285061, -0.5], [0.162348, -0.133384], [0.530488, 0.003049], [0.708841, -0.251524], [0.528963, -0.547256], [0.193598, -0.809451], [0.115854, -0.885671], [0.192073, -0.932927], [0.708841, -0.932927]]],
    "3": [[[0.160061, 0], [0.553354, 0], [0.628049, -0.057927], [0.564024, -0.146341], [0.32622, -0.36128], [0.32622, -0.414634], [0.408537, -0.414634], [0.705793, -0.661585], [0.440549, -0.932927], [0.134146, -0.932927]]],
    "4": [[[0.571646, -0.158537], [0.571646, -0.932927]], [[0.737805, -0.685976], [0.147866, -0.685976], [0.097561, -0.641768], [0.120427, -0.585366], [0.446646, 0]]],
    "5": [[[0.621951, 0], [0.204268, 0], [0.204268, -0.411585], [0.402439, -0.411585], [0.71189, -0.678354], [0.454268, -0.932927], [0.152439, -0.932927]]],
    "6": [[[0.474085, -0.318598], [0.737805, -0.63872], [0.419207, -0.95122], [0.109756, -0.644817], [0.228659, -0.35061], [0.477134, 0]]],
    "7": [[[0.134146, 0], [0.606707, 0], [0.689024, -0.054878], [0.643293, -0.176829], [0.306402, -0.932927]]],
    "8": [[[0.121951, -0.678354], [0.422256, -0.405488], [0.72561, -0.678354], [0.42378, -0.95122], [0.121951, -0.678354]], [[0.192073, -0.185976], [0.422256, 0.018293], [0.64939, -0.185976], [0.422256, -0.405488], [0.192073, -0.185976]], [[0.192073, -0.185976], [0.422256, -0.405488], [0.64939, -0.185976], [0.422256, 0.018293], [0.192073, -0.185976]], [[0.121951, -0.678354], [0.42378, -0.95122], [0.72561, -0.678354], [0.422256, -0.405488], [0.121951, -0.678354]]],
    "9": [[[0.373476, -0.614329], [0.109756, -0.294207], [0.428354, 0.018293], [0.737805, -0.28811], [0.620427, -0.582317], [0.370427, -0.932927]]],
    ".": [[[0.189024, -0.919207], [0.21189, -0.896341], [0.234756, -0.919207], [0.21189, -0.942073], [0.189024, -0.919207]], [[0.189024, -0.919207], [0.21189, -0.942073], [0.234756, -0.919207], [0.21189, -0.896341], [0.189024, -0.919207]]],
    ",": [[[0.213415, -0.920732], [0.170732, -1.085366]]],
    "-": [[[0.315549, -0.634146], [0.108232, -0.634146]]],
    "=": [[[0.756098, -0.785061], [0.158537, -0.785061]], [[0.756098, -0.483232], [0.158537, -0.483232]]],
    "(": [[[0.420732, -1.198171], [0.228659, -0.26753], [0.420732, 0.004573]]],
    ")": [[[0.172256, -1.198171], [0.364329, -0.26753], [0.172256, 0.004573]]],
    "#": [[[0.685976, -0.625], [0.118902, -0.625]], [[0.730183, -0.307927], [0.161585, -0.307927]], [[0.641768, 0], [0.510671, -0.932927]], [[0.35061, 0], [0.219512, -0.932927]]],
    "+": [[[0.756098, -0.634146], [0.158537, -0.634146]], [[0.457317, -0.335366], [0.457317, -0.932927]]],
    "*": [[[0.579268, -0.109756], [0.182927, -0.347561]], [[0.381098, 0], [0.381098, -0.454268]], [[0.579268, -0.347561], [0.182927, -0.109756]]],
    "%": [[[0.281729, -0.501395], [0.055788, -0.251743], [0.295676, 0.015342], [0.520223, -0.237099], [0.281729, -0.501395]], [[0.291492, -0.061367], [0.148536, -0.245467], [0.288703, -0.423989], [0.428173, -0.239888], [0.291492, -0.061367]], [[0.951185, 0], [0.309623, -1.006974], [0.209902, -1.006974], [0.850767, 0], [0.951185, 0]], [[0.877266, -1.015342], [0.651325, -0.76569], [0.891213, -0.497211], [1.11576, -0.751743], [0.877266, -1.015342]], [[0.887029, -0.576011], [0.744073, -0.760112], [0.88424, -0.937238], [1.02371, -0.753138], [0.887029, -0.576011]]],
    "_": [[[0.695122, -1.152439], [0.067073, -1.152439]]]
}  # Dictionary of every letter+ Number with a list of coordinate lists- {a : [ [0,1], [1,1], ...] }
        self.z_hop = z_hop # defines how far the pen retracts after each line

    def letter_to_coordinates(self, letter, origin):
        # gets a letter, translates the coordinates to the new origin, adds a z hop at beginning and end of each line
        letter_coords = alphabet[letter]
        x_offset = origin[0]
        y_offset = origin[1]
        letter_coord_list = []

        for line in letter_coords:
            i = 0  # just a value to tell me if this is the first or last point of the line
            line_length = len(line) - 1

            for point in line:
                print(i)
                if i == 0:
                    hop_point = [0, 0, 0]
                    hop_point[0] = point[0] + x_offset
                    hop_point[1] = point[1] + y_offset
                    hop_point[2] = (self.z_hop)
                    print(hop_point)
                    letter_coord_list.append(hop_point)

                point[0] = point[0] + x_offset
                point[1] = point[1] + y_offset
                point.append(0)
                print(point)
                letter_coord_list.append(point)

                if i == line_length:
                    hop_point = point
                    hop_point[2] = self.z_hop
                    print(hop_point)
                    letter_coord_list.append(hop_point)
                i +=1

        print(letter_coord_list)
        return letter_coord_list
    # letter_to_coordinates("%",[2,2])

    # converts a string of text into coordinates as lines
    # returns a list of coordinates (x,y,z) which trace the string in space
    def string_to_coordinates(self,origin=[0,0]):
        motion_path = []
        offset_amount = 0.1
        text = self.string.split() # splits the string at each space
        print("text: ", text)
        print(origin)
        x_offset = origin[0]
        y_offset = origin[1]


        for fragment in text:
            for letter in fragment:
                motion_path.extend(self.letter_to_coordinates(letter,[x_offset, y_offset]))
                x_offset += offset_amount
                print("x_offset", x_offset)

            x_offset += offset_amount # add a whitespace move here
        print("motion_path", motion_path)
        return motion_path


# Testing:
#text_to_write: ThingToWrite("Hello, my friend % : welcome home!")
#print(text_to_write.string_to_coordinates([0, 0]))
