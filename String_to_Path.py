# Dictionary of every letter+ Number with a list of coordinate lists- {a : [ [0,1], [1,1], ...] }

# TODO: Letters are upside down, fix that.

class ThingToWrite:

    def __init__(self,string, z_hop = -0.02):
        self.string = string
        self.alphabet =  {
            "A": [[[0.734756, 0.60061], [0.185213, 0.60061]], [[0, 1], [0.458079, 0.003811], [0.927591, 1]]],
            "B": [[[0.692835, 0.465701], [0.818598, 0.52096], [0.883765, 0.703125], [0.86814, 0.814024], [0.81593, 0.91311], [0.72904, 0.97561], [0.29497, 1.003049], [0.097561, 1.003049], [0.097561, 0.010671], [0.521341, 0.010671], [0.702744, 0.032012], [0.807165, 0.14253], [0.835366, 0.229802], [0.820884, 0.352896], [0.777439, 0.41997], [0.692835, 0.465701]], [[0.692835, 0.464939], [0.101372, 0.466463], [0.120427, 0.466463]]],
            "C": [[[0.953506, 0.682927], [0.896913, 0.82298], [0.807927, 0.927591], [0.687119, 0.994474], [0.539634, 1.016768], [0.397485, 1.000762], [0.280488, 0.952744], [0.188643, 0.872713], [0.121951, 0.760671], [0.06936, 0.492378], [0.126715, 0.218559], [0.198409, 0.118664], [0.29878, 0.043445], [0.541159, -0.01753], [0.678354, 0.001239], [0.792683, 0.057546], [0.880145, 0.149295], [0.936738, 0.27439]]],
            "D": [[[0.10747, 1], [0.507622, 0.994665], [0.688072, 0.956936], [0.813262, 0.880335], [0.904154, 0.724848], [0.934451, 0.494665], [0.905011, 0.275629], [0.816692, 0.12157], [0.666635, 0.030393], [0.451982, 0], [0.10747, 0], [0.10747, 1]]],
            "E": [[[0.560976, 0.484756], [0.110518, 0.484756]], [[0.791921, 0.00686], [0.10747, 0.00686], [0.10747, 0.996189], [0.815549, 0.996189]]],
            "F": [[[0.801067, 0.007622], [0.060213, 0.007622], [0.060213, 0.496189], [0.060213, 1.00686]], [[0.058689, 0.496951], [0.596799, 0.496951], [0.496189, 0.496951]]],
            "G": [[[0.58003, 0.489329], [1.01372, 0.489329], [1.01372, 0.85061], [0.748476, 0.99657], [0.459985, 1.004954], [0.27439, 0.928735], [0.144055, 0.78811], [0.07622, 0.576601], [0.112805, 0.272485], [0.175305, 0.15968], [0.362424, 0.019055], [0.570884, -0.01372], [0.786585, 0.02439], [0.932165, 0.14939], [0.98247, 0.28125]]],
            "H": [[[0.895579, 1], [0.895579, 0]], [[0.11128, 0.528201], [0.895579, 0.528201]], [[0.11128, 0], [0.11128, 1]]],
            "I": [[[0.198171, 0], [0.198171, 1]]],
            "J": [[[0.589939, 0], [0.589939, 0.70503], [0.54497, 0.895579], [0.442835, 0.99314], [0.201601, 1.00343], [0.078125, 0.895579], [0.03811, 0.715701]]],
            "K": [[[0.23247, 1], [0.23247, -0.001524], [0.23247, 0.407012], [0.710366, -0.004573], [0.401677, 0.261433], [0.91997, 1]]],
            "L": [[[0.105183, -0.001524], [0.105183, 1.002287], [0.730183, 1.002287]]],
            "M": [[[0.088415, 1.002287], [0.088415, 0.003049], [0.574695, 0.86128], [1.057165, -0.00686], [1.057165, 0.997713]]],
            "N": [[[0.090701, 1], [0.090701, -0.004573], [0.902439, 1.002287], [0.902439, -0.011433]]],
            "O": [[[0.067073, 0.512957], [0.09737, 0.302973], [0.188262, 0.136433], [0.342416, 0.02096], [0.545732, -0.01753], [0.743902, 0.020198], [0.897866, 0.133384], [0.992188, 0.297828], [1.023628, 0.501524], [0.991997, 0.703697], [0.897104, 0.866616], [0.74314, 0.97923], [0.54497, 1.016768], [0.352325, 0.980183], [0.198171, 0.870427], [0.099848, 0.709413], [0.067073, 0.512957]]],
            "P": [[[0.152439, 0.902439], [0.152439, 1.003049], [0.152439, 0], [0.33689, 0], [0.44093, 0.00343], [0.612805, 0.029345], [0.741235, 0.118521], [0.790015, 0.25686], [0.768674, 0.421875], [0.661204, 0.536204], [0.395579, 0.595655], [0.15625, 0.590701]]],
            "Q": [[[0.067073, 0.512957], [0.09737, 0.302973], [0.188262, 0.136433], [0.342416, 0.02096], [0.545732, -0.01753], [0.743902, 0.020198], [0.897866, 0.133384], [0.992188, 0.297828], [1.023628, 0.501524], [0.991997, 0.703697], [0.897104, 0.866616], [0.74314, 0.97923], [0.54497, 1.016768], [0.352325, 0.980183], [0.198171, 0.870427], [0.099848, 0.709413], [0.067073, 0.512957]], [[0.615091, 0.802591], [1.073933, 1.089177], [0.90625, 0.983232]]],
            "R": [[[0.66997, 0.527439], [0.798018, 0.762957], [0.925305, 1]], [[0.25686, 0.916921], [0.25686, 1], [0.25686, 0], [0.503049, 0], [0.775915, 0.038491], [0.880335, 0.140625], [0.907774, 0.307165], [0.838415, 0.451601], [0.676829, 0.52096], [0.470274, 0.541921], [0.25686, 0.541921]]],
            "S": [[[0.833079, 0.278201], [0.789634, 0.126905], [0.633384, 0.005335], [0.360899, -0.015625], [0.18064, 0.06936], [0.11814, 0.15282], [0.097561, 0.248476], [0.15282, 0.40282], [0.289634, 0.472561], [0.386814, 0.475991], [0.47561, 0.472561], [0.761814, 0.526296], [0.824314, 0.585366], [0.85747, 0.744665], [0.803735, 0.88529], [0.642149, 0.994665], [0.449695, 1.015244], [0.21875, 0.953125], [0.116235, 0.857851], [0.066311, 0.68064]]],
            "T": [[[0.426829, 1], [0.426829, 0.003049], [0.034299, 0.003049], [0.810213, 0.003049], [0.756098, 0.003049]]],
            "U": [[[0.114329, 0.003811], [0.114329, 0.573171], [0.114329, 0.685976], [0.125, 0.76372], [0.21532, 0.925305], [0.397485, 1.004954], [0.692454, 0.987424], [0.786204, 0.932165], [0.873095, 0.783155], [0.895579, 0.573171], [0.895579, 0]]],
            "V": [[[-0.003049, 0.004573], [0.501524, 1.004573], [0.922256, 0.003049]]],
            "W": [[[0.057927, 0.000762], [0.389482, 1.002287], [0.704268, 0.11814], [1.003049, 1.002287], [1.34375, 0.002287]]],
            "X": [[[0.083841, -0.004573], [0.837652, 1], [0.458079, 0.496951], [0.083841, 0.997713], [0.837652, -0.00686]]],
            "Y": [[[-0.000762, 0.005335], [0.483994, 0.618902], [0.895579, 0.007622], [0.481707, 0.621189], [0.481707, 1.002287]]],
            "Z": [[[0.121189, 0.000762], [0.833841, 0.000762], [0.0625, 1], [0.89253, 1]]],
            "a": [[[0.641006, 1.028963], [0.602134, 0.880335], [0.601372, 0.561738], [0.595274, 0.448933], [0.554497, 0.36471], [0.471799, 0.310213], [0.436738, 0.294207], [0.390244, 0.291159], [0.22561, 0.317073], [0.133384, 0.377287], [0.090701, 0.490854]], [[0.604421, 0.88872], [0.466463, 0.976753], [0.328506, 1.006098], [0.155488, 0.956555], [0.099466, 0.889672], [0.080793, 0.79878], [0.102706, 0.702744], [0.168445, 0.631098], [0.365854, 0.572409], [0.597561, 0.53125]]],
            "b": [[[0.110518, 0.009909], [0.110518, 0.905488], [0.21189, 0.981707], [0.349085, 1.014482], [0.476944, 0.970846], [0.584604, 0.849085], [0.625, 0.573933], [0.588986, 0.419779], [0.523628, 0.321646], [0.354421, 0.255335], [0.191311, 0.300305], [0.110518, 0.366616]]],
            "c": [[[0.659299, 0.46875], [0.571265, 0.324695], [0.393674, 0.258765], [0.22561, 0.295351], [0.140625, 0.345655], [0.071265, 0.44779], [0.040015, 0.60747], [0.057165, 0.77439], [0.11814, 0.90282], [0.217226, 0.98247], [0.32279, 1.017149], [0.529726, 0.977134], [0.657774, 0.814024], [0.67378, 0.71189]]],
            "d": [[[0.584604, 0.009909], [0.583841, 0.905488], [0.504954, 0.988948], [0.396341, 1.016768], [0.263338, 0.989139], [0.158537, 0.90625], [0.095084, 0.791349], [0.073933, 0.652439], [0.090892, 0.504383], [0.141768, 0.384909], [0.240091, 0.290015], [0.376524, 0.258384], [0.490473, 0.283537], [0.583841, 0.358994]]],
            "e": [[[0.71875, 0.777439], [0.589939, 0.964939], [0.458079, 1.011814], [0.307165, 1.00686], [0.175305, 0.94436], [0.088415, 0.834985], [0.053735, 0.567835], [0.102515, 0.429116], [0.203125, 0.312881], [0.321265, 0.26753], [0.451601, 0.26753], [0.57279, 0.314405], [0.659299, 0.40282], [0.72561, 0.666921], [0.05564, 0.666921]]],
            "f": [[[0.020579, 0.276677], [0.385671, 0.276677]], [[0.438262, -0.005335], [0.354421, -0.028201], [0.234756, 0.022485], [0.179878, 0.137195], [0.179878, 1]]],
            "g": [[[0.06936, 1.059451], [0.089558, 1.165396], [0.154726, 1.240854], [0.355945, 1.293445], [0.515816, 1.266387], [0.620427, 1.185213], [0.667873, 1.06936], [0.683689, 0.901677], [0.683689, 0.275152], [0.493902, 0.240473], [0.320884, 0.244665], [0.208841, 0.285061], [0.116616, 0.378811], [0.062881, 0.494665], [0.04497, 0.633384], [0.064596, 0.7742], [0.123476, 0.88872], [0.225229, 0.97218], [0.358232, 1], [0.539825, 0.9375], [0.683689, 0.75]]],
            "h": [[[0.209604, 1.001524], [0.209604, -0.005335]], [[0.209604, 0.59375], [0.214939, 0.53811], [0.230945, 0.487043], [0.294207, 0.410061], [0.403963, 0.367378], [0.516768, 0.374238], [0.590701, 0.417683], [0.63186, 0.528201], [0.63186, 1.001524]]],
            "i": [[[0.153963, 1], [0.153963, 0.275152]], [[0.145579, 0.087652], [0.157012, 0.07622], [0.168445, 0.087652], [0.157012, 0.099085], [0.145579, 0.087652]]],
            "j": [[[0.146341, 0.087652], [0.157774, 0.07622], [0.169207, 0.087652], [0.157774, 0.099085], [0.146341, 0.087652]], [[-0.06936, 1.273628], [-0.020579, 1.285823], [0.031631, 1.291159], [0.123095, 1.253049], [0.152439, 1.134909], [0.152439, 0.28125]]],
            "k": [[[0.209604, 1], [0.209604, 0]], [[0.50686, 0.272866], [0.208079, 0.556402]], [[0.540396, 1], [0.208079, 0.556402]]],
            "l": [[[0.14939, 0.001524], [0.150152, 0.997713]]],
            "m": [[[0.140244, 0.272866], [0.140244, 1]], [[1.012195, 1], [1.012195, 0.502287], [0.99819, 0.395913], [0.956174, 0.319931], [0.886147, 0.274343], [0.78811, 0.259146], [0.663681, 0.290777], [0.564787, 0.385671], [0.491044, 0.290777], [0.359756, 0.259146], [0.232851, 0.288681], [0.140244, 0.377287]], [[0.564787, 1], [0.564787, 0.385671]]],
            "n": [[[0.146341, 1], [0.146341, 0.275152]], [[0.625762, 1], [0.625762, 0.554116], [0.578506, 0.339939], [0.499428, 0.279345], [0.378049, 0.259146], [0.245046, 0.289063], [0.146341, 0.378811]]],
            "o": [[[0.045732, 0.637957], [0.073742, 0.462843], [0.157774, 0.339939], [0.261242, 0.279345], [0.385671, 0.259146], [0.528773, 0.285633], [0.637957, 0.365091], [0.703125, 0.480183], [0.724848, 0.627287], [0.683689, 0.84032], [0.560213, 0.971799], [0.385671, 1.016006], [0.237995, 0.988948], [0.128811, 0.907774], [0.066502, 0.790015], [0.045732, 0.637957]]],
            "p": [[[0.130335, 1.270579], [0.130335, 0.268293], [0.410442, 0.276105], [0.537348, 0.333841], [0.619093, 0.455602], [0.646341, 0.644055], [0.627096, 0.780107], [0.56936, 0.891006], [0.470084, 0.971608], [0.339939, 0.998476], [0.217035, 0.980183], [0.130335, 0.925305]]],
            "q": [[[0.629573, 0.923018], [0.540587, 0.992759], [0.432165, 1.016006], [0.297637, 0.985709], [0.19436, 0.894817], [0.136052, 0.775152], [0.116616, 0.631098], [0.134718, 0.487233], [0.189024, 0.372713], [0.287729, 0.287538], [0.422256, 0.259146], [0.542111, 0.287538], [0.633384, 0.372713], [0.629573, 1.29878]]],
            "r": [[[0.110518, 0.275152], [0.110518, 1]], [[0.112043, 0.385671], [0.185976, 0.290777], [0.269055, 0.259146], [0.394817, 0.29878]]],
            "s": [[[0.621189, 0.458079], [0.53811, 0.31936], [0.44436, 0.27439], [0.204649, 0.27782], [0.110899, 0.33689], [0.0625, 0.435595], [0.071265, 0.52782], [0.130335, 0.600991], [0.234375, 0.644436], [0.336509, 0.641006], [0.426829, 0.625381], [0.540015, 0.641006], [0.62843, 0.71189], [0.644055, 0.821265], [0.58346, 0.932546], [0.454649, 1.001524], [0.31593, 1.011814], [0.199695, 0.985899], [0.110899, 0.928735], [0.041921, 0.78811]]],
            "t": [[[0.38872, 0.996951], [0.230945, 0.993902], [0.187881, 0.943979], [0.176829, 0.89253], [0.176829, 0.0625]], [[0.038872, 0.371189], [0.351372, 0.371189]]],
            "u": [[[0.635671, 1], [0.635671, 0.275152]], [[0.163872, 0.275152], [0.163872, 0.724085], [0.213415, 0.936738], [0.291921, 0.996189], [0.411585, 1.016006], [0.541921, 0.985328], [0.635671, 0.893293]]],
            "v": [[[0.020579, 0.282012], [0.364329, 0.996189], [0.686738, 0.282012]]],
            "w": [[[0.003811, 0.270579], [0.28811, 1], [0.5, 0.44436], [0.71189, 1.00686], [0.996189, 0.270579]]],
            "x": [[[0.103659, 0.28125], [0.605183, 1]], [[0.596037, 0.272866], [0.085366, 1]]],
            "y": [[[0.630335, 0.28125], [0.353659, 1]], [[0.089939, 1.22561], [0.224085, 1.234375], [0.309832, 1.14596], [0.354421, 1.003049], [0.083079, 0.26753]]],
            "z": [[[0.05564, 0.27439], [0.645579, 0.27439], [0.027439, 1], [0.66997, 1]]],
            "0": [[[0.057927, 0.50686], [0.078316, 0.283108], [0.139482, 0.123285], [0.241425, 0.027391], [0.384146, -0.004573], [0.526867, 0.027391], [0.628811, 0.123285], [0.689977, 0.283108], [0.710366, 0.50686], [0.674162, 0.786204], [0.565549, 0.958079], [0.384146, 1.016768], [0.241425, 0.984899], [0.139482, 0.889291], [0.078316, 0.729945], [0.057927, 0.50686]]],
            "1": [[[0.331555, 0.129573], [0.519817, 0], [0.519817, 1]]],
            "2": [[[0.708079, 1], [0.03811, 1], [0.041921, 0.98247], [0.054116, 0.921875], [0.16654, 0.734756], [0.33346, 0.609375], [0.425305, 0.571265], [0.532774, 0.52096], [0.626524, 0.453125], [0.685595, 0.36814], [0.70122, 0.26753], [0.680259, 0.161585], [0.616235, 0.073171], [0.432165, -0.001524], [0.237805, 0.028201], [0.09718, 0.15625], [0.0625, 0.285061]]],
            "3": [[[0.071646, 0.253049], [0.102896, 0.150915], [0.212081, 0.03487], [0.382622, -0.003811], [0.487424, 0.01372], [0.57622, 0.066311], [0.640244, 0.149009], [0.661585, 0.250762], [0.627287, 0.375953], [0.52439, 0.458841], [0.266006, 0.458841], [0.337652, 0.458841], [0.404726, 0.458079], [0.630335, 0.501524], [0.692264, 0.589558], [0.71189, 0.73628], [0.68388, 0.844322], [0.602896, 0.936738], [0.495236, 0.996761], [0.378049, 1.016768], [0.253811, 0.999428], [0.159299, 0.947409], [0.094512, 0.860709], [0.059451, 0.739329]]],
            "4": [[[0.676829, 0.75686], [0.003811, 0.75686], [0.56936, -0.009909], [0.56936, 1.003049]]],
            "5": [[[0.05564, 0.739329], [0.05907, 0.762195], [0.130335, 0.91654], [0.220655, 0.984375], [0.428735, 1.013338], [0.532774, 0.982088], [0.68407, 0.836509], [0.72561, 0.65282], [0.661204, 0.463796], [0.59375, 0.404726], [0.414634, 0.366616], [0.16311, 0.475991], [0.089939, 0.53811], [0.176829, 0.010671], [0.676829, 0.010671]]],
            "6": [[[0.05564, 0.608994], [0.20503, 0.432165], [0.309832, 0.37157], [0.416921, 0.351372], [0.537157, 0.375762], [0.632622, 0.448933], [0.692073, 0.551639], [0.71189, 0.675305], [0.69093, 0.807355], [0.628049, 0.915396], [0.527058, 0.991425], [0.39939, 1.016768], [0.247332, 0.986471], [0.13872, 0.895579], [0.073552, 0.744093], [0.051829, 0.532012], [0.074266, 0.297256], [0.141578, 0.129573], [0.253763, 0.028963], [0.410823, -0.004573], [0.518197, 0.012005], [0.60404, 0.061738], [0.664158, 0.140625], [0.69436, 0.244665]]],
            "7": [[[0.333079, 1], [0.339939, 0.932165], [0.44779, 0.53468], [0.501524, 0.425305], [0.560595, 0.31936], [0.616235, 0.21875], [0.668445, 0.126905], [0.712444, 0.011213], [0.71189, 0.010671], [0.066311, 0.010671]]],
            "8": [[[0.379573, 0.46189], [0.185976, 0.416159], [0.119093, 0.350419], [0.096799, 0.253811], [0.118521, 0.150152], [0.183689, 0.066311], [0.275724, 0.013148], [0.495427, 0.012767], [0.58689, 0.064787], [0.65263, 0.14939], [0.674543, 0.25686], [0.656107, 0.342273], [0.6008, 0.404916], [0.379573, 0.46189], [0.612805, 0.515244], [0.689977, 0.592797], [0.715701, 0.714177], [0.691502, 0.838796], [0.618902, 0.936738], [0.514101, 0.996761], [0.385671, 1.016768], [0.25686, 0.99638], [0.152439, 0.935213], [0.080412, 0.836319], [0.056402, 0.710366], [0.080412, 0.59032], [0.152439, 0.515244], [0.379573, 0.46189]]],
            "9": [[[0.715701, 0.479421], [0.549543, 0.59375], [0.353659, 0.660823], [0.232279, 0.636242], [0.136433, 0.5625], [0.077553, 0.459032], [0.057927, 0.333079], [0.078887, 0.200838], [0.141768, 0.09375], [0.243331, 0.020008], [0.372713, -0.004573], [0.536204, 0.03468], [0.648628, 0.152439], [0.698933, 0.295541], [0.698742, 0.681021], [0.647866, 0.837652], [0.530678, 0.971989], [0.35747, 1.016768], [0.250857, 1.000381], [0.165777, 0.95122], [0.106231, 0.872904], [0.07622, 0.769055]]],
            ".": [[[0.188262, 0.949695], [0.188262, 0.928354]]],
            ",": [[[0.185213, 0.918445], [0.214939, 1.019817], [0.197409, 1.107279], [0.144817, 1.166921]]],
            "-": [[[0.422256, 0.647104], [0.038872, 0.647104]]],
            "=": [[[0.077744, 0.411585], [0.737805, 0.411585]], [[0.737805, 0.60061], [0.077744, 0.60061]]],
            "(": [[[0.32622, 1.293445], [0.144436, 0.977134], [0.083841, 0.637957], [0.144436, 0.308308], [0.32622, -0.01753]]],
            ")": [[[0.172256, -0.01753], [0.35404, 0.308308], [0.414634, 0.637957], [0.35404, 0.975991], [0.172256, 1.293445]]],
            "#": [[[0.126524, 1.021341], [0.325457, -0.014482]], [[0.435976, 1.021341], [0.650152, -0.01753]], [[0.75686, 0.330793], [0.016006, 0.330793]], [[0.75686, 0.676067], [0.016006, 0.676067]]],
            "+": [[[0.740854, 0.50686], [0.073933, 0.50686]], [[0.403963, 0.84375], [0.403963, 0.176829]]],
            "*": [[[0.442073, 0.147866], [0.262957, 0.208079]], [[0.262957, -0.003049], [0.262957, 0.208079]], [[0.262957, 0.208079], [0.375762, 0.355183]], [[0.087652, 0.144817], [0.262957, 0.208079]], [[0.262957, 0.208079], [0.153963, 0.362043]]],
            "%": [[[0.942073, -0.01753], [0.396341, 1.036585]], [[0.080793, 0.240091], [0.131098, 0.0625], [0.199695, 0.002477], [0.291159, -0.01753], [0.386814, 0.002668], [0.457317, 0.063262], [0.508384, 0.247713], [0.456555, 0.429878], [0.386052, 0.491044], [0.291921, 0.511433], [0.196837, 0.490091], [0.128049, 0.426067], [0.080793, 0.240091]], [[0.727896, 0.765244], [0.778201, 0.58689], [0.846418, 0.528011], [0.938262, 0.508384], [1.034108, 0.528392], [1.105183, 0.588415], [1.15625, 0.772866], [1.104421, 0.955793], [1.033727, 1.016387], [0.939024, 1.036585], [0.844322, 1.015244], [0.775152, 0.95122], [0.727896, 0.765244]]],
            "_": [[[-0.020579, 1.188262], [0.793445, 1.188262]]],
            "/": [[[0.338415, -0.022104], [0.042683, 1.01372]]],
            ":": [[[0.195122, 0.391006], [0.195122, 0.317835]], [[0.195122, 0.970274], [0.195122, 0.910823]]],
            "?": [[[0.060976, 0.271341], [0.094655, 0.14496], [0.15987, 0.054687], [0.256622, 0.000524], [0.506288, -0.000191], [0.606707, 0.051829], [0.681593, 0.140816], [0.706555, 0.255335], [0.661585, 0.398628], [0.55564, 0.510671], [0.492378, 0.571646], [0.449695, 0.647104], [0.439787, 0.753811]], [[0.395579, 0.867378], [0.429878, 0.833841], [0.464177, 0.867378], [0.429878, 0.901677], [0.395579, 0.867378]]],
            "!": [[[0.198933, 0.76753], [0.198933, -0.0625]], [[0.198933, 0.897866], [0.198933, 0.921494]]],
            }  # Dictionary of every letter+ Number with a list of coordinate lists- {a : [ [0,1], [1,1], ...] }
        self.z_hop = z_hop # defines how far the pen retracts after each line
        self.scale = 1 / 200  # Letter size

        # reflect letters (they are mirrored in the alphabet dictionary)
        '''for letter in self.alphabet.values():
            for line in letter:
                for coordinate in line:
                    print("old coordinate:    ", coordinate)
                    coordinate[1] *= -1
                    print("okay is this it? : ", coordinate)
        print(self.alphabet)
        '''


    def letter_to_coordinates(self, letter, origin):
        # gets a letter, translates the coordinates to the new origin, adds a z hop at beginning and end of each line
        letter_coords = self.alphabet[letter].copy()
        x_offset = origin[0]
        y_offset = origin[1]
        letter_coord_list = []

        for line in letter_coords:
            i = 0  # just a value to tell me if this is the first or last point of the line
            line_length = len(line) - 1

            for point in line:
                # print("i: ", i)
                if i == 0:
                    hop_point = [0, 0, 0]
                    hop_point[0] = point[0] * self.scale + x_offset
                    hop_point[1] = point[1] * self.scale + y_offset
                    hop_point[2] = (self.z_hop)
                    # print("hop_point start: ", hop_point)
                    letter_coord_list.append(hop_point.copy())

                scaled_offset_point = [0, 0, 0]
                scaled_offset_point[0] = point[0] * self.scale + x_offset
                scaled_offset_point[1] = point[1] * self.scale + y_offset

                # print("point", scaled_offset_point)
                letter_coord_list.append(scaled_offset_point)

                if i == line_length:
                    hop_point = scaled_offset_point.copy()
                    hop_point[2] = self.z_hop
                    # print("hop_point end: ", hop_point)
                    letter_coord_list.append(hop_point)
                i +=1

        # print(letter_coord_list)
        return letter_coord_list
    # letter_to_coordinates("%",[2,2])

    # converts a string of text into coordinates as lines
    # returns a list of coordinates (x,y,z) which trace the string in space
    def string_to_coordinates(self,origin=[0,0],offset = 0.0039):
        motion_path = []
        offset_amount = offset
        text = self.string.split() # splits the string at each space
        print("text: ", text)
        # print(origin)
        x_offset = origin[0]
        y_offset = origin[1]


        for fragment in text:
            for letter in fragment:
                # print("letter:", letter)
                motion_path.extend(self.letter_to_coordinates(letter,[x_offset, y_offset]).copy())
                x_offset += offset_amount
                #print("x_offset", x_offset)

            x_offset += offset_amount # add a whitespace move here
        #print("motion_path", motion_path)
        return motion_path


# Testing:
#text_to_write: ThingToWrite("Hello, my friend % : welcome home!")
#print(text_to_write.string_to_coordinates([0, 0]))
