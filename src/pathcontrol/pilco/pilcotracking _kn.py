r�]v���a�7������]e[�G ����  @�ܝ�t�A޲�w8��n�t���yck���Þ�>�ǆ����$��`���Zv��P�	�Xݾ�m�9�욢g-�i��qyy��D�ؖ� �*a-  P:�^��ju���V*���*H�k��q���i�F��Yy=��d�q�ǹ��?�`��#U��r��F��dQ�9�������{�ͼk���ò��<���� �*a-  P*��x��������wm^�x��,�����߭x��-����*tB  	�IDAT[��ZX�$���e��a���-�G��7Dv�pڇ�l�nA�v�}m|�+��!��~�����# `U�Z  �Tfs�&I�Ҝ��X6om�e������aM;��Z��24�۷o�-��w���_����ܣ��Rw�N�eٚ�f<���>�>ۇ=�z����w���*�={���Sp���*�r= V!�  Je6�窽뱞��>���u��F��vo�Y��޼y$�����Ό���Q��r���a�ml{��zs�ÝyY����udY��<ͧ��l�m^؇C�?u-��j����b4�,����v��$�_%]e�Cn�� X��  (�~�?����͛�nkYϬ]�Me���sÌj��{C�)�^���{v��tٿ�v��w��rI������V������|�e�eY|���{Y��^��z}��y��n���y�!�29;;[X�ʼ�Oͣ~�m� ��  �q��f^��]z��澆��W��U�}yy��<I��BЛ����<���n0���u����k��FE����l�j5�ƽe��x��s}}��g�Fca�n������p�o��ҧ6w����\�׷���ο���P~�p8������PY�鱟{y�x�ڐe�<�_g�}o�,�# ����  @)4��{a�!��]6w�&�L�+�67���uB�W�^����w���3���~,�����f��;���e��~���T＼�Q�1�����j-�WWW����\z���9pyy��|���8^�z����Ay���C�����?6��v���v{�y�[���5f<oT����z�����so�e���ꩺ;;�֝���*�� (/a-  P�f�9��4�l��]Z m�;pٺ��U���s�O?������g�v{���n7�����G��3�V+7^'L���n�Z+'9F��m�}&E����U�9{{��BX��ի�ۻ`�|ճ��5�񋋋��5��|�RYk^�c6���͎M�ۍ����������{u�^�o4Wy��Yl��n\\\�\���q����x<�4MW>��v�繷�k�w�}��lY�Ͳl�l��Cl��� PbS  ��L&��`0�t:�z�>M�d�?I�L[�ִ��M'��V��F�����i�RY���O�V�v:��`0���h4ZZ��h4�F�^�7m�ZK�Y�T�뜽gٺf�}����gٺ����}�L&���-C�ј�i���v���g�w��4������z�m�����z����z�>m�Z�ϪR��1�k2�L{���zQ���̊�h4��h4���^��g�����^��kB�V��U�3���X�j�������xXg��������+_[�2�L��t:]8?+�ʴ�n�\��ht�s���m���Y��u��y[�Tݏ�^C�<���f5������<����d�V�]�˶�C\� ��"�  *�&�*?wúM�ή�L>.=����N���f�ca��~z�ޓ��d2Yh�ޤ����v�=m�Z�Z�v��y��c�Q^�R�c46^W�n���ϦZ�N������{�����t�c�nP��l�c\�V��j5�oV	���߫��"�ܥ�a��:��>߭˝Ng�����݇)f?I�<���:F��Ҡ�R�̃�j�����S���!�>���f��^<�wL�4��j�{�c��[?�p�m��z ��  �����˭�*]�cs��$I�N'��q�Z�����!2��a�p��F#����a���|���pI�D�Z�7o��Γ�aT*������nG�ߏ,ˢ��瞇�Z-���2��ݲu:�x���|���x�0dk��Q�Ֆ�����>?juV�g�����D�eK�r�z��t��M�i�^/��a���{�8�lI�D�^��������z��|N�Y=}Xgk�Z���[�O�ږ� p׳�t:-�   |xfs4��㸽��,�"MӨT*\pr���,�~xC��<������/�g5���8mv����Ȳ,�$�����!���E�Z]i^��p�~?~������>�C?P���x���Z皵����㙦iT�ս���V��\� ��!�      (�GE       �C$�      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
 �      (��      � �Z      �k      
��8+ p�[�    IEND�B`�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# PYTHON
import control
from control import *
import matplotlib.pyplot as plt
import numpy as np
import time 
from math import sin, cos, tan

# LOCAL
from pathcontrol.frequency_domain.hinf.control_ext import combine
from pathplanning.libs.transformations import *
from pathplanning.libs.extend_transformations import *

class Hinf():

    def __init__(self, model_type="", robot_parameter="", sim_parameter="", velocity=1.0, length_offset=-1.0):
        
        self.robot_parameter = robot_parameter
        self.sim_parameter = sim_parameter

        # Weighting Transfer Functions
        # ----------------------------
        self.Wy1 = self._make_weight(dc=1000.0, crossw=0.1, hf=0)
        # Wy2 = self._make_highpass(hf_gain=0.98, m3db_frq=2.1)
        self.Wy2 = self._make_weight(dc=0.001, crossw=0.1, hf=0)
        # self.Wu = self._make_highpass(hf_gain=0.4, m3db_frq=2.1)
        self.Wu = self._make_weight(dc=0.1, crossw=0.8, hf=1.0)

        # Get System
        # ----------
        if model_type=="errorModel_woSteer_woYawDyn":
            print("H-infinity - model:", "errorModel_woSteer_woYawDyn")
            self.Gss = self._get_errorModel_woSteer_woYawDyn(velocity=velocity, length_offset=length_offset)
        elif model_type=="errorModel_steerPT1_woYawDyn":
            print("H-infinity - model:", "errorModel_steerPT1_woYawDyn")
            try:
                self.Gss = self._get_errorModel_steer_woYawDyn(velocity=velocity, length_offset=length_offset, T_steer=robot_parameter.T_steer)
                print(self.Gss)
            except: 
                self.Gss = self._get_errorModel_steerPT1_woYawDyn(velocity=velocity, length_offset=length_offset, T_steer=0.2)
                print(self.Gss)

        G = tf(self.Gss)

        # Generate Controller
        # -------------------
        # for cross_omega in np.arange(10.0, 0.1, -0.1):
        #     print("cross_omega:", cross_omega)
        #     self.Wy1 = self._make_weight(dc=100.0, crossw=cross_omega, hf=0)
        #     Pss = self._get_extendedSystem(Wy_yE=self.Wy1, Wy_yawE=self.Wy2, Wu=self.Wu, G_yE=G[0,0], G_yawE=G[1,0])
        #     Kss, CL, gamma, rcond = hinfsyn(Pss, 2, 1)
        #     print("hinfsyn gamma:", gamma)
        #     if gamma < 1.0: break

        Pss = self._get_extendedSystem(Wy_yE=self.Wy1, Wy_yawE=self.Wy2, Wu=self.Wu, G_yE=G[0,0], G_yawE=G[1,0])
        Kss, CL, gamma, rcond = hinfsyn(Pss, 2, 1)
        print("hinfsyn gamma:", gamma)

        try:
            self.Kdss = c2d(Kss, self.sim_parameter.Ts_ctrl)
        except:
            self.Kdss = c2d(Kss, 1e-3)

        self.K_states = np.zeros( shape=(self.Kdss.A.shape[0], 1) )
        


    def execute(self, diffPose_matrix, velocity )  :
        K, x = self.Kdss, self.K_states
        lw = self.robot_parameter.wheelbase
        yE = diffPose_matrix[1, 3]
        yawE = matrix_to_yaw(diffPose_matrix)
        u = np.array( [ [-yE], [-yawE] ] )
        y = K.C @ x + K.D @ u
        x = K.A @ x + K.B @ u
        omega = y[0,0]
        self.K_states = x
        return np.arctan(omega * lw / velocity)

    def plot_weights(self):
        # Plot Transfer Functions
        mag, phase, omega = bode(self.Wy1)
        # plt.plot(omega, mag)
        mag, phase, omega = bode(self.Wy2)
        # plt.plot(omega, mag)
        mag, phase, omega = bode(self.Wu)
        # plt.plot(omega, mag)
        plt.show()
    def plot_controller(self):
        # Simulate Control Loop
        # ---------------------
        if plot == True:
            # Desired to Controlled Variable
            fig, ax = plt.subplots(3, 1)
            I = ss([], [], [], np.eye(2))
            w_to_y = feedback(self.Gss*self.K, I, -1)
            T, yout, xout = step_response(sys=w_to_y, T=np.linspace(0, 10, 1000), input=0, return_x=True)
            ax[0].plot(T, yout[0,:], 'r--')
            ax[0].plot(T, yout[1,:], 'r:')
            T, yout, xout = step_response(sys=w_to_y, T=np.linspace(0, 10, 1000), input=1, return_x=True)
            ax[0].plot(T, yout[0,:], 'b--')
            ax[0].plot(T, yout[1,:], 'b:')
            ax[0].grid(True)
            ax[0].legend( ('y-Error for desired y-Error=1', 'yaw-Error for desired y-Error=1', 'y-Error for desired yaw-Error=1', 'yaw-Error for desired yaw-Error=1') )
            # Disturbance z1 to Controlled Variable
            ax[1].grid(True)
            z2_to_y = feedback(self.Gss, self.K, -1)
            T, yout, xout = step_response(sys=z2_to_y, T=np.linspace(0, 10, 1000), input=0, return_x=True)
            ax[1].plot(T, yout[0,:], 'r--')
            ax[1].plot(T, yout[1,:], 'r:')
            ax[1].legend( ('y-Error for z2-Error/G-input-Error=1', 'yaw-Error for z2-Error/G-input-Error=1') )
            # Disturbance z2 to Controlled Variable
            ax[2].grid(True)
            z1_to_y = feedback(I, self.Gss*self.K, -1)
            T, yout, xout = step_response(sys=z1_to_y, T=np.linspace(0, 10, 1000), input=0, return_x=True)
            ax[2].plot(T, yout[0,:], 'r--')
            ax[2].plot(T, yout[1,:], 'r:')
            T, yout, xout = step_response(sys=z1_to_y, T=np.linspace(0, 10, 1000), input=1, return_x=True)
            ax[2].plot(T, yout[0,:], 'b--')
            ax[2].plot(T, yout[1,:], 'b:')
            ax[2].legend( ('y-Error for z1-yError=1', 'yaw-Error for z1-yError=1', 'y-Error for z1-yawError=1', 'yaw-Error for z1-yawError=1') )
            plt.show()

    def _get_extendedSystem(self, Wy_yE, Wy_yawE, Wu, G_yE, G_yawE):
        Wy1, Wy2, = Wy_yE, Wy_yawE
        G1, G2 = G_yE, G_yawE

        # P11 = [ [W1, 0, W1*G1], [0, W2, W2*G2], [0, 0, 0] ]
        # P12 = [ [W1*G1], [W2*G2], [Wu] ]
        # P21 = [ [1, 0, G1], [0, 1, G2] ]
        # P22 = [ [G1], [G2] ]
        # P = [ [P11, P21], [P21, P22]]
        P11=np.block( [ [Wy1, 0, Wy1*G1], [0, Wy2, Wy2*G2], [0,0,0] ] ) 
  