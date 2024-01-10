import os
import random
import argparse
from twisted.python import log
from twisted.internet import reactor, protocol, task
from twisted.protocols.sip import Base, Request, Response

script_dir = os.path.dirname(os.path.abspath(__file__))

class SimpleSIPProtocol(Base):

    def handle_request(self, request, addr):
        logs = {}
        dst_host, dst_port = self.get_destination_info()
        for key, value in request.headers.items():
            if value is not None:
                logs[key.upper()] = ', '.join(value)
        log.msg(logs)
        self.simulateResponse(request, addr)

    def simulateResponse(self, request, addr):
        delay = random.uniform(0.1, 1.0)
        task.deferLater(reactor, delay, self.sendFakeResponse, request, addr)

    def sendFakeResponse(self, request, addr):
        if request.method == b'INVITE':
            code = 100 
        elif request.method == b'REGISTER':
            code = 200 
        else:
            code = 404

        response = Response(code)
        response.addHeader(b'Server', b'FRITZ!OS 1.0')
        self.transport.write(response.toString(), addr)

    def get_destination_info(self):
        destination = self.transport.getHost()
        return destination.host, destination.port

class SimpleSIPFactory(protocol.Factory):
    protocol = SimpleSIPProtocol

def main():
    parser = argparse.ArgumentParser(description='Run a simple SIP honeypot server.')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind the SIP server to.')
    parser.add_argument('--port', type=int, default=5060, help='Port to bind the SIP server to.')
    args = parser.parse_args()

    LOG_FILE_PATH = os.path.join(script_dir, "sip_honeypot.log")
    print(f"SIP HONEYPOT ACTIVE ON HOST: {args.host}, PORT: {args.port}")
    print(f"ALL SIP requests will be logged in: {LOG_FILE_PATH}")

    log_observer = log.FileLogObserver(open(LOG_FILE_PATH, 'a'))
    log.startLoggingWithObserver(log_observer.emit, setStdout=False)

    sip_protocol = SimpleSIPProtocol()
    reactor.listenUDP(args.port, sip_protocol, interface=args.host)
    reactor.run()

if __name__ == "__main__":
    main()
