import rospy
from std_msgs.msg import String

# Criacao do No1
rospy.init_node('Node_1')

#Declaracao de Variaveis
soma = String()
matricula = String()

       
def CallBack (msg): #Recebe a soma enviada pelo No2
    global soma
    soma = msg
    print ("Valor da soma dos algarismos:" +soma.data)
    print (soma.data) #imprime na tela o valor da soma dos algoritmos
    
def timerCallBack(event): #Enviar o valor da Matricula para o No2
    msg = String()
    msg.data = '2018000309'
  
    pub.publish(msg) 

    
pub = rospy.Publisher ('/Node_1', String, queue_size =1) #Publicar a mensagem do No1, no caso a matricula
sub = rospy.Subscriber('/Node_2', String, CallBack) #Subscriber para receber o valor da soma
timer = rospy.Timer(rospy.Duration(0.1),timerCallBack)

rospy.spin()