
from DnsClass import DnsClass


class SocketHandler:

    max_connection_queue = 5
    recive_buffer = 4096
    port = 9999

    def __init__(self,logger):
        self.logger = logger
        self.DnsClass = DnsClass()
        self.bind()

    def bind(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((socket.gethostname(), self.port))
        self.serversocket.listen(self.max_connection_queue)
        self.logger.info("The server is ready listening on port %d"%(self.port))

    def run(self):
        while True:
            (clientsocket, address) = serversocket.accept()
            self.logger.info("Connected by %s"%address)
            ip   = address[0]
            port = address[1]

            data = clientsocket.recv(self.recive_buffer)
            self.logger.info("The message from %s was %s"%(address,data))

            try:
                data = data.decode()
            except:
                self.logger.error("Can't decode %s"%data)
                conn.close()
                continue

            result =  self.DnsClass.messageHandler(ip,port,data)

            if self.DnsClass.isError(result):
                self.logger.error("Error with %s the message was %s"%(address,data))
                conn.close()
                continue

            self.logger.info("Sending %s to %s"%(result,address))
            conn.sendall(result)
            self.logger.info("Closing connecttion with %s"%address)
            conn.close()

    def __del__(self):
        self.serversocket.close()
        print("Closing the socket")