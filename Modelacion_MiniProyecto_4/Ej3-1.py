from cmath import inf
import random
import math
# Time of arrival of the next request
def funcExp(before, lamVal):
    return before - float((1/lamVal)*math.log(random.random()))

def mountainService():
    T = 3600 # Simulation Time
    Na = 0 # Number of arrivals
    Nd = 0 # Number of departures
    N = 0 # Number of requests on time T
    Ta = 0 # Time of arrival
    Td = 0 # Time of departure

    # Times of arrival and departure on i
    A = []
    D = []
    t0 = random.random()
    Ta = t0
    Td = inf
    t = 0
    while t < T:
        t += funcExp(t, 40)

        # Caso 1
        # Request arrived, Time is running
        if (Ta <= Td and Ta <= T):
            t = Ta
            Na += 1
            N += 1
            t_t = funcExp(Ta, 40) # Ta - (1/100) * math.log(random.random())
            Ta = t_t
            if (N == 1):
                Td = -(1/100) * math.log(random.random()) ##sería para el primer proveedor
                
            
            A.append(Ta)
            
        # Caso 2
        if (Td < Ta and Td <= T):
            # Request finished, Time is running
            t = Td
            N -= 1
            Nd += 1
            if (N != 0):
            #     Td = inf
            # else:
                Td = t + funcExp(Td, 40)

            D.append(t)

        # Caso 3
        if (min(Ta, Td) > T and N > 0):
            # Request arrived but has to wait
            t = Td
            N -= 1
            Nd += 1
            
            if(N > 0):
                Td = t + funcExp(Td, 40)
            D.append(t)

        # Caso 4
        elif (min(Ta, Td) > T , N == 0):
            # Request arrived after time, no request ton queue
            Tp = max(t - T, 0)
        
    print("------------Mounting Mega----------")
    print("A) Solicitudes atendidas por el servidor: ", Nd)
    print("B) Tiempo que el servidor estuvo ocupado: ", Ta+Td)
    print("C) Tiempo que el servidor estuvo desocupado: ", -T+Td)
    print("D) Tiempo total estuvieron las solicitudes en el sistema: ", Td + Tp)
    print("E) Tiempo promedio de espera en la cola: ", Td/Nd)
    print("F) En promedio ", Na/T, " solicitudes estuvieron en cola cada segundo")
    print("G) Momento de salida de la última solicitud: ", D[-1])
            

def pizzitaService():
    T = 3600 # Simulation Time
    Na = 0 # Number of arrivals
    Nd = 0 # Number of departures
    N = 0 # Number of requests on time T
    Ta = 0 # Time of arrival
    Td = 0 # Time of departure

    # Times of arrival and departure on i
    A = []
    D = []
    t0 = random.random()
    Ta = t0
    Td = inf
    t = 0
    t0 = random.random()
    Ta = t0
    Td = inf
    t = 0
    while t < T:
        t += funcExp(t, 40)

        # Caso 1
        # Request arrived, Time is running
        if (Ta <= Td and Ta <= T):
            t = Ta
            Na += 1
            N += 1
            t_t = funcExp(Ta, 40) # Ta - (1/100) * math.log(random.random())
            Ta = t_t
            if (N == 1):
                Td = -(1/10) * math.log(random.random()) ##sería para el segundo proveedor
            
            A.append(Ta)
            
        # Caso 2
        if (Td < Ta and Td <= T):
            # Request finished, Time is running
            t = Td
            N -= 1
            Nd += 1
            if (N != 0):
            #     Td = inf
            # else:
                Td = t + funcExp(Td, 40)

            D.append(t)

        # Caso 3
        if (min(Ta, Td) > T and N > 0):
            # Request arrived but has to wait
            t = Td
            N -= 1
            Nd += 1
            
            if(N > 0):
                Td = t + funcExp(Td, 40)
            D.append(t)

        # Caso 4
        if (min(Ta, Td) > T , N == 0):
            # Request arrived after time, no request ton queue
            Tp = max(t - T, 0)
            # break
    
    print("\n------------Pizzita Computing----------")
    print("A) Solicitudes atendidas por el servidor: ", Nd)
    print("B) Tiempo que el servidor estuvo ocupado: ", Ta+Td)
    print("C) Tiempo que el servidor estuvo desocupado: ", -T+Td)
    print("D) Tiempo total estuvieron las solicitudes en el sistema: ", Td + Tp)
    print("E) Tiempo promedio de espera en la cola: ", Td/Nd)
    print("F) En promedio ", Na/T, " solicitudes estuvieron en cola cada segundo")
    print("G) Momento de salida de la última solicitud: ", D[-1])



mountainService()
pizzitaService()