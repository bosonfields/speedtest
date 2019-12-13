import rpyc
import time

path = '/root/speedtest/data/'


class MyServer(rpyc.Service):
    #on_connect and on_disconnect is not required
    server_download_end = 0.0
    server_upload_start = 0.0

    test_time = [0.0, 0.0]

    def on_connect(self, conn):
        print('Connected to the server!')

    def on_disconnect(self, conn):
        print('Disconnected with the server.')


    # add 'exposed_' before function name
    # no need to add 'exposed_' when call this function in client


    def exposed_write(self, filename, data):
        filename = path + "3.jpg"
        with open(filename, "wb") as f:
            f.write(data)
        self.server_download_end = float(time.time())

    def exposed_read(self, filename):
        filename = path + "3.jpg"

        self.server_upload_start = float(time.time())
        with open(filename, "rb") as f:
            data = f.read()
        return data

    def exposed_getTime(self):
        return (self.server_download_end, self.server_upload_start)

    def exposed_getTest(self, data):
        tmp = data
        test_time.append(float(time.time()))

    def exposed_estimate(self):
        return test_time[-1] - test_time[-2]



if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyServer, port=3154)
    t.start()
