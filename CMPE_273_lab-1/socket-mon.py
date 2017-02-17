import psutil

print('"PID","Local address","Remote address","Status"')
process_Connections = [] #list for all connections
process_connections_count = {} #dict for storing process and its number of connection
ProcessId_list = [] #store the list of process id which has connection
for c in psutil.net_connections():   #function returns system wide connections hence iterating one by one
        laddr = "%s@%s" % (c.laddr)
        if c.raddr: # checks raddr is present or not
            raddr = "%s@%s" % (c.raddr)
            if c.pid != None:
                Connections = [c.pid,laddr,raddr,c.status] #stores the connection details in the list
                process_Connections.append(Connections) 
                if c.pid not in ProcessId_list: # checks processid is present or not in list of process id
                    ProcessId_list.append(c.pid)

for pid in ProcessId_list: 
    count = sum(1 for sublist in process_Connections if sublist[0] is pid) #calculates the number of connections each pid has
    process_connections_count[pid] = count
#stores 
sorted_process_connectn_count = sorted(process_connections_count.items(), key=lambda x:(-x[1],x[0])) 

#prints in the pid and socket connections on the bases of number of connections per process in descending order and for the same number of connection on the bases of pid in ascending order
for key,value in sorted_process_connectn_count:
    for sublist in process_Connections:
        if key is sublist[0]:
	    pid = sublist[0]
	    l_addr = sublist[1]
	    r_addr = sublist[2]
	    status = sublist[3]
            print(('"%s","%s","%s","%s"') % (pid,l_addr,r_addr,status))

