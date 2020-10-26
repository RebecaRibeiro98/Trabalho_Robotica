import rospy
from std_msgs.msg import String
    
rospy.init_node('Node_2')

matricula = String()
soma = String()

def CallBack (msg): #Recebe a matricula e calcula a soma
    global matricula
    matricula = msg
    resultado = 0
    
    for i in range(10):
        resultado += int(matricula.data[i])
    soma.data = str(resultado) 
    

def timerCallBack(event): #enviar o valor da soma
    pub.publish(soma)
    
    
pub = rospy.Publisher ('/Node_2', String, queue_size =1)
sub = rospy.Subscriber('/Node_1', String, CallBack)
timer = rospy.Timer(rospy.Duration(0.1),timerCallBack)

rospy.spin()