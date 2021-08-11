import awk

def sim_time(tfile):
    """
        Arguments : 
        - tfile : Path of Trace file

        Returns :
        - Simulation starting and end time

        Dictionary is returned

    """
    startTime = 2.0
    stopTime = 0.0
    if startTime > stopTime:
        with awk.Reader(tfile) as reader:
            for rec in reader:
                event = rec[0]
                if event == 's' or event == 'r':
                    pkt_size = int(rec[7])
                    time = float(rec[1])
                    if event == "s" and pkt_size >= 512:
                        if time < startTime:
                            startTime = time
                    if event == 'r' and pkt_size >= 512:
                        if time > stopTime:
                            stopTime = time
    return {"start_time": startTime, "stop_time": stopTime}

def throughput(tfile, rcvnode, aodv=False):
    """
        Arguments : 
        - tfile : Path of Trace file
        - rcvnode : Receiving Node (whose throughput is required)
        - aodv : True or False
                - For AODV Protocol Simulation because of different Trace Format
                
        Returns :
        - Throughput
   
    """
    recvdSize = 0
    startTime = 2.0
    stopTime = 0.0
    received = 0
    if aodv==True:
        fn = 7
    else:
        fn = 5
    with awk.Reader(tfile) as reader:
        for rec in reader:
            event = rec[0]
            if event == "s" or event == "r" or event == "f" or event == "D" \
                 or event=='d' or event=='+' or event=='-':
                time = float(rec[1])
                node_id = int(rec[2].replace("_", ""))
                pkt_size = int(rec[fn])
                if event == "s" and pkt_size >= 512:
                    if time < startTime:
                        startTime = time
                if event == 'r' and pkt_size >= 512 and node_id == rcvnode:
                    received += 1
                    if time > stopTime:
                        stopTime = time
                    hdr_size = pkt_size % 512
                    pkt_size = pkt_size-hdr_size
                    recvdSize += pkt_size
    thru = (recvdSize/(stopTime-startTime))
    return round(thru,3)

def sim_details(tfile, aodv=False):
    """
        Arguments : 
        - tfile : Path of Trace file
        - aodv : True or False
                - For AODV Protocol Simulation because of different Trace Format

        Returns simulation details such as -
        - Packet Type
        - Event Type
        - Network Trace Level

        Above will be returned as dictionary.    

    """
    if aodv==True:
        fn = 6
        events = {'sent':0,'received':0,'dropped':0,'forwarded':0}
        network_trace = {}
    else:
        fn = 4
        events = {'received':0,'dropped':0,'enqueue':0,'dequeue':0}
    pkt_types = {}
    with awk.Reader(tfile) as reader:
        for rec in reader:
            event = rec[0]
            if event=='r' or event=='s' or event=='d' or event=='D' \
                 or event=='f' or event =='+' or event=='-':
                if rec[fn] in pkt_types.keys():
                    pkt_types[rec[fn]]+=1
                else:
                    pkt_types[rec[fn]]=1
                if event == '+':
                    events['enqueue']+=1
                elif event == '-':
                    events['dequeue']+=1
                elif event == 'r':
                    events['received']+=1
                    if aodv == True:
                        if rec[3] in network_trace.keys():
                            network_trace[rec[3]]+=1
                        else: 
                            network_trace[rec[3]]=1
                elif event == 's': 
                    events['sent']+=1
                    if aodv==True:
                        if rec[3] in network_trace.keys():
                            network_trace[rec[3]]+=1
                        else: 
                            network_trace[rec[3]]=1
                elif event == 'D' or event == 'd':
                    events['dropped']+=1
                    if aodv == True:
                        if rec[3] in network_trace.keys():
                            network_trace[rec[3]]+=1
                        else: 
                            network_trace[rec[3]]=1
                elif event == 'f':
                    events['forwarded']+=1
                    if aodv == True:
                        if rec[3] in network_trace.keys():
                            network_trace[rec[3]]+=1
                        else: 
                            network_trace[rec[3]]=1
    return {"packet_type":pkt_types,"event_type":events,"network_trace_level":network_trace}

'''
def avgenergy(tfile,initial,no):
    """
    """
    with awk.Reader(tfile) as reader:
        for rec in reader:
            event = rec[0]
            pass
    return
'''