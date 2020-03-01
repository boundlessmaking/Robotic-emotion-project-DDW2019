from String_to_Path import ThingToWrite
import URBasic
import math
import math3d as m3d
import random
import dlib
import cv2
import imutils
import numpy as np
import time
import caffe_inference as cf
from Face_obj import Face

import CONFIG
from Videostream import vs


pretrained_model = cv2.dnn.readNetFromCaffe("models/deploy.prototxt.txt", "models/res10_300x300_ssd_iter_140000.caffemodel")
pretrained_model2 = cv2.dnn.readNetFromCaffe("models/RFB-320.prototxt", "models/RFB-320.caffemodel")


class Robot:
    # TODO : scale face test 
    # TODO : test paper advance

    def __init__(self, ip):
        self.ip = CONFIG.ROBOT_IP
        self.robotUR = None
        self.position = [0, 0]

        self.face_row_offset = CONFIG.FACE_ROW_OFFSET
        self.text_hor_offset = CONFIG.TEXT_HOR_OFFSET
        self.z_hop =           CONFIG.Z_HOP
        self.drawing_zval =    CONFIG.DRAWING_ZVAL
        self.current_row =     CONFIG.CURRENT_ROW
        self.max_rows =        CONFIG.MAX_ROWS
        self.line_spacing =    CONFIG.LINE_SPACING 
        self.blend_radius =    CONFIG.BLEND_RADIUS
        self.robotURModel =    URBasic.robotModel.RobotModel()
        self.max_x =           CONFIG.MAX_X
        self.max_y =           CONFIG.MAX_Y
        self.hor_rot_max =     CONFIG.HOR_ROT_MAX
        self.vert_rot_max =    CONFIG.VERT_ROT_MAX
        self.accel =           CONFIG.ACCEL
        self.vel =             CONFIG.VEL
        self.origin =          m3d.Transform()

        self.follow_time =     CONFIG.FOLLOW_TIME
        self.wander_dist =     CONFIG.WANDER_DIST
        self.w_anglechange =   CONFIG.W_ANGLECHANGE
        self.escape_anglechange = CONFIG.ESCAPE_ANGLECHANGE

        # reporting
        self.print_coordinates = CONFIG.PRINT_COORDINATES

        # self.face_detect = dlib.get_frontal_face_detector()
        #self.dnnFaceDetector = dlib.cnn_face_detection_model_v1("models/mmod_human_face_detector.dat")
        # paper advancing
        self.drag_dist =       CONFIG.DRAG_DIST  # 10 cm
        self.plunge_dist =     CONFIG.PLUNGE_DIST
        self.paperslot_start = CONFIG.PAPERSLOT_START

        # positions
        self.home_pos =        CONFIG.HOME_POS

    def initialise_robot(self):
        self.robotUR = URBasic.urScriptExt.UrScriptExt(host=self.ip, robotModel=self.robotURModel)
        self.robotUR.reset_error()
        pass

    def start_rtde(self):
        self.robotUR.init_realtime_control()  # starts the realtime control loop on the Universal-Robot Controller
        time.sleep(0.5)  # just a short wait to make sure everything is initialised
        print("rtde started")
        pass

    def wander(self):
        #global PROGRAMSTATE
        #global ROBOT_ACTION
        if CONFIG.PROGRAMSTATE == 0:
            print("wander function")
            CONFIG.ROBOT_ACTION = 3
            # use self.position to go to a close position and search for faces
            angle_a = random.uniform(-360.0, 360.0)
            exceeds = 0
            print("starting wander loop. CONFIG.ROBOT_ACTION: ", CONFIG.ROBOT_ACTION)
            while CONFIG.PROGRAMSTATE == 0:
                # wander around
                frame = vs.read()
                # face_positions, _, new_frame = self.find_faces_dnn(frame)
                face_positions, _, new_frame = self.find_face_fast(frame)

                if len(face_positions) > 0:
                    # cv2.imshow('current', new_frame)
                    # cv2.waitKey(1)
                    # time.sleep(10)
                    break
                else:
                    cv2.imshow('current', new_frame)
                    cv2.waitKey(1)

                    if exceeds != 0:
                        anglechange = random.uniform(-self.escape_anglechange, self.escape_anglechange)
                        # anglechange = 45
                    else:
                        anglechange = random.uniform(-self.w_anglechange, self.w_anglechange)
                    angle_a = angle_a + anglechange
                    # print(angle_a)
                    rad_angle_a = math.radians(angle_a)
                    x = self.wander_dist * math.cos(rad_angle_a)
                    y = self.wander_dist * math.sin(rad_angle_a)

                    next_position = [self.position[0] + x,
                                     self.position[1] + y]
                    # print(next_position)
                    next_position, exceeds = self.move_to_position(next_position)
                    # print(next_position)
            print("exiting wander function")
            print("CONFIG.PROGRAMSTATE:  ", CONFIG.PROGRAMSTATE)

        else:
            pass

    def follow_face(self, close=True):
        # either breaks or returns a face object if run for enough time 
        #global PROGRAMSTATE
        #global ROBOT_ACTION

        new_frame, face_boxes, face_positions = None, None, None
        if CONFIG.PROGRAMSTATE == 0:

            CONFIG.ROBOT_ACTION = 4
            try:
                print("starting follow_face loop. CONFIG.ROBOT_ACTION:", CONFIG.ROBOT_ACTION)
                timer = time.time()
                frame = []

                while CONFIG.PROGRAMSTATE == 0:

                    frame = vs.read()
                    # face_positions, face_boxes, new_frame = self.find_faces_dnn(frame)
                    face_positions, face_boxes, new_frame = self.find_face_fast(frame)
                    # self.show_frame(new_frame)
                    if len(face_positions) > 0:
                        if time.time() - timer < self.follow_time:
                            self.position = self.move_to_face(face_positions, self.position)
                        else:
                            print("time up returning frame")
                            print(close)
                            if close:
                                print("stopping realtime control")
                                self.robotUR.stop_realtime_control()
                                print("stopped realtime control")

                            return new_frame, face_boxes, face_positions
                    else:
                        return new_frame, face_boxes, face_positions
                        break

                        # print("end of loop")
                print("exiting loop without face ")
                return frame, False, False

            except KeyboardInterrupt:
                print("face tracking interrupted by user")
                print("closing robot connection")
                # Remember to always close the robot connection, otherwise it is not possible to reconnect
                self.robotUR.close()

            except:
                print("error during facetracking")
                self.robotUR.close()

        else:
            return new_frame, face_boxes, face_positions
            pass

    def move_to_write(self, row):

        #global PROGRAMSTATE
        #global ROBOT_ACTION
        if CONFIG.PROGRAMSTATE == 0:
            CONFIG.ROBOT_ACTION = 5  # sets ROBOT_ACTION to "move to write"

            print("moving to write ")
            self.robotUR.movej(q=(math.radians(-69),
                                  math.radians(-97),
                                  math.radians(-108),
                                  math.radians(-64),
                                  math.radians(89.5),
                                  math.radians(0)), a=self.accel, v=self.vel)
            # ueber dem papier 01 self.robot.movej((-1.186561409627096, -1.9445274511920374, -1.7661479155169886, -1.006078068410055, 1.5503629446029663, 0.3756316900253296), self.a, self.v)
            self.robotUR.movej(q=(-1.2749927679644983,
                                  -1.9379289785968226,
                                  -2.09098464647402,
                                  -0.6840408484088343,
                                  1.5629680156707764,
                                  0.28495118021965027), a=self.accel, v=self.vel)
            self.origin = self.get_origin()
            print("moved")
            CONFIG.ROBOT_ACTION = 6  # sets ROBOT_ACTION to "at write"
            return True
        else:
            print("program paused or stopped: ", CONFIG.PROGRAMSTATE)
            return False

    def move_home(self):
        #global PROGRAMSTATE
        #global ROBOT_ACTION
        if CONFIG.PROGRAMSTATE == 0 or CONFIG.PROGRAMSTATE == 1:
            CONFIG.ROBOT_ACTION = 1  # sets ROBOT_ACTION to "move home"
            print("moving Home. CONFIG.ROBOT_ACTION:  ", CONFIG.ROBOT_ACTION)

            self.robotUR.movej(q=self.home_pos, a=self.accel, v=self.vel)

            self.position = [0, 0]
            self.origin = self.set_lookorigin()
            return True
        else:
            print("program paused or stopped: ", CONFIG.PROGRAMSTATE)
            return False

    def create_coordinates(self, image_with_face, box):
        print("creating coordinates")
        Face_object = Face(image_with_face, box)
        Face_object.evaluate()
        self.draw_face(Face_object)
        self.write_emotions(Face_object)

        return None

    def orient_list_of_lines(self, listoflines):

        oriented_list = []
        for line in listoflines:
            oriented_line = []
            for coord in line:
                # print(coord)
                trans_coord = m3d.Transform(coord)
                trans_coord = self.origin * trans_coord
                vec_coord = trans_coord.get_pose_vector()
                oriented_line.append(vec_coord)
            oriented_list.append(oriented_line)

        if self.print_coordinates:
            print("oriented lines:  ", oriented_list)
        return oriented_list

    def write_emotions(self, Face_obj):

        #global PROGRAMSTATE
        #global ROBOT_ACTION
        if CONFIG.PROGRAMSTATE == 0:

            emos = Face_obj.emotions
            print(emos)
            if len(emos) == 0:
                print("no emotions to write")
                return False
            else:
                CONFIG.ROBOT_ACTION = 8  # sets ROBOT_ACTION to "writing"

                origin = self.calculate_origin(text=True)
                i = 0
                for emotion in emos:
                    emotion_coords = [ThingToWrite(emotion).string_to_coordinates(origin)]
                    if self.print_coordinates:
                        print("emotion_coords", emotion_coords)
                    self._draw_curves(emotion_coords, origin)
                    origin[1] += self.line_spacing

                return True
        else:
            print("program paused or stopped: ", CONFIG.PROGRAMSTATE)
            return False

    def draw_face(self, Face_obj):
        #global PROGRAMSTATE
        #global ROBOT_ACTION
        if CONFIG.PROGRAMSTATE == 0:

            if len(Face_obj.landmarks) == 0:
                print("no landmarks to draw")
                return False
            else:
                CONFIG.ROBOT_ACTION = 7  # sets ROBOT_ACTION to "drawing"
                origin = self.calculate_origin()
                self._draw_curves(Face_obj.landmarks, origin)
                return True
        else:
            print("program paused or stopped: ", CONFIG.PROGRAMSTATE)
            return False

    def _draw_curves(self, polylines, origin_point):
        print("polylines to be drawn: ", polylines)

        polylines_zvalue = self._add_zvalue(polylines)
        polylines_with_zhop = self._add_zhop(polylines_zvalue)
        polylines_rotvec = self._add_rotvec(polylines_with_zhop)
        polylines_oriented = self.orient_list_of_lines(polylines_rotvec)
        for line in polylines_oriented:
            list_mapped_wpts = []
            for pose6d in line:
                # it is necessary to convert the list of poses to a dict with values for acceleration and velocity
                wpt_dict = {"pose": pose6d,
                            "a": self.accel,
                            "v": self.vel,
                            "r": self.blend_radius}

                list_mapped_wpts.append(wpt_dict)
            # print(list_mapped_wpts)    
            self.robotUR.movel_waypoints(list_mapped_wpts)

        pass

    def calculate_origin(self, text=False):
        row = self.current_row
        x = self.face_row_offset[0]
        y = (row + 0) * self.face_row_offset[1]  # TODO: do I need a general offset here? 

        if text:
            x += self.text_hor_offset

        origin = [x, y]
        return origin

    def _add_zvalue(self, list):

        # lines_with_z = [coord.append(0) for line in list for coord in line]  # doesnt work as .append returns None in this way
        list_with_z = []
        for line in list:
            lines_with_z = []
            for coord in line:
                coord.append(self.drawing_zval)
                lines_with_z.append(coord)
            list_with_z.append(lines_with_z)

        if self.print_coordinates:
            print("list of lines  with added z: ", list_with_z)

        return list_with_z

    def _add_zhop(self, list):
        list_w_hop = []
        for line in list:
            line_w_hop = []

            for coord in line:
                if len(coord) != 3:
                    print("coordinate is missing a third value")

            line_w_hop.append(line[0].copy())
            line_w_hop.extend(line)
            line_w_hop.append(line[-1].copy())

            line_w_hop[0][2] = self.z_hop
            line_w_hop[-1][2] = self.z_hop
            list_w_hop.append(line_w_hop)

        if self.print_coordinates:
            print("list of lines  with zhop:    ", list_w_hop)
        return list_w_hop

    def _add_rotvec(self, list):
        # lines_with_rotvec = [coord.append(0,0,0) for line in list for coord in line]

        list_with_rotvec = []
        for line in list:
            line_with_rotvec = []
            for coord in line:
                new_coord = coord
                new_coord.extend([0, 0, 0])
                line_with_rotvec.append(new_coord)

            list_with_rotvec.append(line_with_rotvec)

            if self.print_coordinates:
                print("lines with rotation vector:   ", list_with_rotvec)

        return list_with_rotvec

    def _string_to_coords(self):
        pass

    def find_faces_dnn(self, image):
        """
        Finds human faces in the frame captured by the camera and returns the positions
        uses the pretrained model located at pretrained_model

        Input:
            image: frame captured by the camera

        Return Values:
            face_centers: list of center positions of all detected faces
                list of lists with 2 values (x and y)
            frame: new frame resized with boxes and probabilities drawn around all faces

        """

        frame = image
        frame = imutils.resize(frame, width=CONFIG.VIDEO_RESOLUTION[0])
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # rects = self.face_detect(frame, 1)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # rects = self.dnnFaceDetector(gray, 1)


        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))

        # pass the blob through the network and obtain the detections and predictions
        pretrained_model.setInput(blob)
        pretrained_model2.setInput(blob)

        # the following line handles the actual face detection
        # it is the most computationally intensive part of the entire program
        # TODO: find a quicker face detection model
        detections = pretrained_model.forward()
        print(detections.shape)
        print(detections)

        detections2 = pretrained_model2.forward()
        print(detections2.shape)
        print(detections2)

        face_centers = []
        rectangles = []
        # loop over the detections
        for i in range(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence < 0.7:
                continue

            # compute the (x, y)-coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the bounding box of the face along with the associated probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10

            face_center = (int(startX + (endX - startX) / 2), int(startY + (endY - startY) / 2))
            position_from_center = (face_center[0] - CONFIG.VIDEO_MIDPOINT[0], face_center[1] - CONFIG.VIDEO_MIDPOINT[1])
            face_centers.append(position_from_center)

            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          (0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            # cv2.putText(frame, str(position_from_center), face_center, 0, 1, (0, 200, 0))
            cv2.line(frame, CONFIG.VIDEO_MIDPOINT, face_center, (0, 200, 0), 5)
            cv2.circle(frame, face_center, 4, (0, 200, 0), 3)

            rectangle = [startX, startY, endX, endY]
            rectangles.append(rectangle)

        return face_centers, rectangles, frame

    def find_face_fast(self, image):
        face_centers, rectangles, new_frame = cf.inference(image)
        return face_centers, rectangles, new_frame

    def show_frame(self, frame):
        cv2.imshow('current', frame)
        k = cv2.waitKey(6) & 0xff

    def send_interrupting_prg(self):
        """sends a simple program to stop the one currently running"""
        self.robotUR.robotConnector.RealTimeClient.SendProgram(prg="set_digital_out(0, True)")
        pass

    """def convert_rpy(angles):

        # This is very stupid:
        # For some reason this doesnt work if exactly  one value = 0
        # the following simply make it a very small value if that happens
        # I do not understand the math behind this well enough to create a better solution
        zeros = 0
        zero_pos = None
        for i,ang in enumerate(angles):
            if ang == 0 :
                zeros += 1
                zero_pos = i
        if zeros == 1:
            #logging.debug("rotation value" + str(zero_pos+1) +"is 0 a small value is added")
            angles[zero_pos] = 1e-6

        roll = angles[0]
        pitch = angles[1]
        yaw = angles[2]

        # print ("roll = ", roll)
        # print ("pitch = ", pitch)
        # print ("yaw = ", yaw)
        # print ("")

        for ang in angles:
            # print(ang % np.pi)
            pass

        if roll == pitch == yaw:

            if roll % np.pi == 0:
                rotation_vec = [0, 0, 0]
                return rotation_vec

        yawMatrix = np.matrix([
        [math.cos(yaw), -math.sin(yaw), 0],
        [math.sin(yaw), math.cos(yaw), 0],
        [0, 0, 1]
        ])
        # print("yawmatrix")
        # print(yawMatrix)

        pitchMatrix = np.matrix([
        [math.cos(pitch), 0, math.sin(pitch)],
        [0, 1, 0],
        [-math.sin(pitch), 0, math.cos(pitch)]
        ])
        # print("pitchmatrix")
        # print(pitchMatrix)

        rollMatrix = np.matrix([
        [1, 0, 0],
        [0, math.cos(roll), -math.sin(roll)],
        [0, math.sin(roll), math.cos(roll)]
        ])
        # print("rollmatrix")
        # print(rollMatrix)

        R = yawMatrix * pitchMatrix * rollMatrix
        # print("R")
        # print(R)

        theta = math.acos(((R[0, 0] + R[1, 1] + R[2, 2]) - 1) / 2)
        # print("theta = ",theta)
        multi = 1 / (2 * math.sin(theta))
        # print("multi = ", multi)


        rx = multi * (R[2, 1] - R[1, 2]) * theta
        ry = multi * (R[0, 2] - R[2, 0]) * theta
        rz = multi * (R[1, 0] - R[0, 1]) * theta

        rotation_vec = [rx,ry,rz]
        # print(rx, ry, rz)
        return rotation_vec
    """

    def check_max_xy(self, xy_coord):
        """
        Checks if the face is outside of the predefined maximum values on the lookaraound plane

        Inputs:
            xy_coord: list of 2 values: x and y value of the face in the lookaround plane.
                These values will be evaluated against max_x and max_y

        Return Value:
            x_y: new x and y values
                if the values were within the maximum values (max_x and max_y) these are the same as the input.
                if one or both of the input values were over the maximum, the maximum will be returned instead
        """
        max_flag = 0  # 0 = inside maximum, 1= exceeds x max , 2= exceeds y-max, 3= exceeds both max
        x_y = [0, 0]
        # print("xy before conversion: ", xy_coord)
        max_x = self.max_x
        max_y = self.max_y
        if -max_x <= xy_coord[0] <= max_x:
            # checks if the resulting position would be outside of max_x
            x_y[0] = xy_coord[0]
        elif -max_x > xy_coord[0]:
            x_y[0] = -max_x
            max_flag = 1
        elif max_x < xy_coord[0]:
            x_y[0] = max_x
            max_flag = 1
        else:
            raise Exception(" x is wrong somehow:", xy_coord[0], -max_x, max_x)

        if -max_y <= xy_coord[1] <= max_y:
            # checks if the resulting position would be outside of max_y
            x_y[1] = xy_coord[1]
        elif -max_y > xy_coord[1]:
            x_y[1] = -max_y

            if max_flag == 0:
                max_flag = 2
            else:
                max_flag = 3
        elif max_y < xy_coord[1]:
            x_y[1] = max_y

            if max_flag == 0:
                max_flag = 2
            else:
                max_flag = 3
        else:
            raise Exception(" y is wrong somehow", xy_coord[1], max_y)
        # print("xy after conversion:   ", x_y)

        return x_y, max_flag

    def set_lookorigin(self):
        """
        Creates a new coordinate system at the current robot tcp position.
        This coordinate system is the basis of the face following.
        It describes the midpoint of the plane in which the robot follows faces.

        Return Value:
            orig: math3D Transform Object
                characterises location and rotation of the new coordinate system in reference to the base coordinate system
        """
        orig = self.get_origin()
        return orig

    def get_origin(self):
        position = self.robotUR.get_actual_tcp_pose()
        orig = m3d.Transform(position)
        print("origin set")
        return orig

    def move_to_face(self, list_of_facepos, robot_pos):
        """
        Function that moves the robot to the position of the face

        Inputs:
            list_of_facepos: a list of face positions captured by the camera, only the first face will be used
            robot_pos: position of the robot in 2D - coordinates

        Return Value:
            prev_robot_pos: 2D robot position the robot will move to. The basis for the next call to this funtion as robot_pos
        """

        face_from_center = list(list_of_facepos[0])  # TODO: find way of making the selected face persistent

        prev_robot_pos = self.position
        scaled_face_pos = [c * CONFIG.M_PER_PIXEL for c in face_from_center]

        robot_target_xy = [a + b for a, b in zip(prev_robot_pos, scaled_face_pos)]
        # print("..", robot_target_xy)


        next_robot_pos, _ = self.move_to_position(robot_target_xy)

        return next_robot_pos

    def move_to_position(self, target, face_bool=False):
        """ moves robot to target inside of the lookarea"""

        target, exceeds = self.check_max_xy(target)
        # TODO: make sure the target actually is the real position otherwise it is possible the robot might drift outside of the area or the area gets smaller and smaller

        if face_bool:
            print("moving to face at", target)
        else:
            print("moving to position:", target)

        x = target[0]
        y = target[1]
        z = 0
        xyz_coords = m3d.Vector(x, y, z)

        x_pos_perc = x / self.max_x
        y_pos_perc = y / self.max_y

        x_rot = x_pos_perc * self.hor_rot_max
        y_rot = y_pos_perc * self.vert_rot_max * -1

        tcp_rotation_rpy = [y_rot, x_rot, 0]
        # tcp_rotation_rvec = convert_rpy(tcp_rotation_rpy)
        tcp_orient = m3d.Orientation.new_euler(tcp_rotation_rpy, encoding='xyz')
        position_vec_coords = m3d.Transform(tcp_orient, xyz_coords)

        oriented_xyz = self.origin * position_vec_coords
        oriented_xyz_coord = oriented_xyz.get_pose_vector()

        coordinates = oriented_xyz_coord

        # qnear = self.robotUR.get_actual_joint_positions()
        next_pose = coordinates  # TODO: why do I rename this variable 3 times ?? 
        self.robotUR.set_realtime_pose(next_pose)
        self.position = target

        return target, exceeds

    def check_paper(self):
        if self.current_row == self.max_rows:
            self.advance_paper()
            self.current_row = 0

    def advance_paper(self):
        #global PROGRAMSTATE
        #global ROBOT_ACTION
        if CONFIG.PROGRAMSTATE == 0:
            CONFIG.ROBOT_ACTION = 9  # sets current ROBOT_ACTION to "moving paper" 

            x = self.paperslot_start[0]
            y = self.paperslot_start[1]
            z = self.paperslot_start[2]

            print("moving paper")

            # self.robotUR.set_csys(m3d.Transform())  # reset csys otherwise weird things happen...
            self.robotUR.movel(self.paperslot_start, self.accel, self.vel)  # move above the slot start point
            self.robotUR.movel((x,
                                y,
                                z - self.plunge_dist,
                                0, -math.pi, 0), self.accel, self.vel)  # plunge into the slot
            self.robotUR.movel((x - self.drag_dist,
                                y,
                                z - self.plunge_dist,
                                0, -math.pi, 0), self.accel, self.vel)  # drag the desired drag distance
            time.sleep(2)
            self.robotUR.movel((x - self.drag_dist,
                                y,
                                z,
                                0, -math.pi, 0), self.accel, self.vel)  # raise up to initial z height
            self.robotUR.movel((x - self.drag_dist,
                                y,
                                z - self.plunge_dist / 3,
                                0, -math.pi, 0), self.accel * 2.5, self.vel * 2.6)  # plunge down by half z
            self.robotUR.movel((x - self.drag_dist,
                                y,
                                z + self.plunge_dist,
                                0, -math.pi, 0), self.accel * 2.7, self.vel * 2.7)  # raise by plunge dist  

            time.sleep(2)

            print("paper moved")

            return True
        else:
            print("program paused or stopped: ", CONFIG.PROGRAMSTATE)
            return False

    def move_safe(self, curr_action):
        print("safety-move")
        pass