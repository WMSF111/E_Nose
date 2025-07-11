'''
帧数据结构创建
'''
import struct


class FrameData():
    def __init__(self, Headflag = 0x55AA, pkgLen = 10, end_num = 0x0A):

        self.Headflag = Headflag
        self.end_num = end_num

        self.pkgLen = pkgLen

        self.buf = ['00' for i in range(self.pkgLen)]
        print(self.buf)
        # 数据头尾定义
        self.buf[0] = f"{(self.Headflag >> 8) & 0xff:02x}"
        self.buf[1] = f"{self.Headflag & 0xff:02x}"
        self.buf[self.pkgLen - 1] = f"{self.end_num:02x}"

    # 计算数据包的校验和。将数据包中除起始字节和结束字节外的所有字节相加，取低8位作为校验和。
    # def setCrc(self):
    #     r = 0
    #     for i in range(1, self.pkgLen - 2):
    #         r += self.buf[i]
    #     self.buf[self.pkgLen - 2] = r & 0xff

    # 将数据包中的数据部分全部设置为0，并更新校验和。
    def setDataToOff(self):
        for i in range(3, self.pkgLen - 2):
            self.buf[i] = '00'
        # self.setCrc()

    def setDataToArray(self, arr):
        alen = len(arr)
        dlen = self.pkgLen - 3
        rlen = alen if (alen < dlen) else dlen
        for i in range(2, rlen + 2):
            # print(i,arr[i-4])
            self.buf[i] = arr[i - 2]
            # print(self.buf)
        # self.setCrc()

    # 将数据包中的数据部分全部设置为255，并更新校验和。
    def setDataToOn(self):
        for i in range(2, self.pkgLen - 1):
            self.buf[i] = 'FF'
        # self.packBytes()
        # self.setCrc()

    def setDataTodo(self, opea, opea1 = 0, opea2 = 0):
        self.setDataToOff()
        opea = f"{opea:02x}"
        self.buf[2] = opea
        if (opea == '01'):
            self.buf[3] = f"{opea1 & 0xff:02x}"
            hex_string = f"{opea2:04x}"
            self.buf[4] = hex_string[:2]
            self.buf[5] = hex_string[-2:]
        if (opea == '02'):
            self.buf[3] = f"{opea1 & 0xff:02x}"
        if (opea == '03'):
            opea1 = 1
        if (opea == '04'): # 0-100
            opea1 *= 32
            hex_string = f"{opea1:04x}"
            self.buf[3] = hex_string[:2]
            self.buf[4] = hex_string[-2:]
        if (opea == '05'): # 00：关闭气泵 01：打开气泵
            self.buf[3] = f"{opea1 & 0xff:02x}"
        # self.packBytes()


    def packBytes(self):
        print(self.buf)
        hex_string = ' '.join(self.buf)
        byte_data = bytes.fromhex(hex_string.replace(' ', ''))
        return byte_data

'''
帧数据结构解析
'''

from event import *


class FramePkg(EventDispatcher):
    def __init__(self, pixStyle=0x14, width=1, height=1):
        EventDispatcher.__init__(self)
        self.pixStyle = pixStyle
        self.frameWidth = width
        self.frameHeight = height

        self.pkgLen = self.frameWidth * self.frameHeight * (pixStyle & 0x0f) + 6
        self.bufLen = self.pkgLen * 3
        self.buf = [0 for i in range(self.bufLen)]
        self.dataLen = self.pkgLen - 6
        self.linedata = [0 for i in range(self.dataLen)]
        self.startIdx = 0
        self.endIdx = 0

    # 获取数据长度 int
    def getDatLen(self):
        if (self.endIdx >= self.startIdx):
            return self.endIdx - self.startIdx
        return self.bufLen + self.endIdx - self.startIdx

    # 判断数据长度已经到达一个包长bool
    def pkgIsOk(self):
        return self.getDatLen() >= self.pkgLen

    # 检测包头为0xff并且有一个包长的数据bool
    def chkStart(self):
        while (self.buf[self.startIdx] != 0xff and self.pkgIsOk()):
            self.nextByte()
        return self.pkgIsOk()

    # 检测索引超出buf末尾，从头开始
    def chkMaxIdx(self, idx):
        if (idx > self.bufLen - 1):
            idx %= self.bufLen  # ??
        return idx

    # 获取包尾索引int
    def getPkgEndIdx(self):
        return self.chkMaxIdx(self.startIdx + self.pkgLen - 1)

    # 检查包尾为0xfe bool
    def chkEnd(self):
        return self.buf[self.getPkgEndIdx()] == 0xfe

    # 相对起始索引包数据的每个字节索引的映射int
    def getIdxFromStart(self, i):
        return self.chkMaxIdx(self.startIdx + i)

    # 检测校验和bool
    def chkCrc(self):
        crcidx = self.getPkgEndIdx() - 1  # 包尾之前的一个字节
        if (crcidx < 0):
            crcidx = self.bufLen + crcidx  # 包尾索引在缓冲区前面，包头在后面
        d = self.buf[crcidx]
        # print(d)
        r = 0
        # 计算和
        for i in range(1, self.pkgLen - 2):
            # print(self.getIdxFromStart(i),":",self.buf[self.getIdxFromStart(i)])
            r += self.buf[self.getIdxFromStart(i)]
        r = r & 0xff
        # print(r)
        return d == r

    # 写数据到显示区
    def writeData(self):
        r = 0
        for i in range(4, self.pkgLen - 2):
            r = self.buf[self.getIdxFromStart(i)]
            # print(r)
            self.linedata[i - 4] = r

    def nextPkg(self):
        self.startIdx = self.chkMaxIdx(self.getPkgEndIdx() + 1)

    def nextByte(self):
        self.startIdx = self.chkMaxIdx(self.startIdx + 1)

    # 解析包
    def parsePKG(self):
        while (self.pkgIsOk()):
            if (self.chkStart() and self.chkEnd() and self.chkCrc()):
                self.writeData()
                self.dispatch_event(PKGEvent(PKGEvent.PKG_DATA_OK, self.linedata))
                self.nextPkg()
            else:
                self.nextByte()

    def writeToBuf(self, byt):
        self.buf[self.endIdx] = byt
        self.endIdx = self.chkMaxIdx(self.endIdx + 1)

    def writeArrayToBuf(self, arr):
        for i in range(len(arr)):
            self.writeToBuf(arr[i])
        self.parsePKG()
    # '''

#
# if __name__ == '__main__':
#     d = FrameData(0x14, 10, 2)
#
#     print("init", d.buf)
#     d.setDataToOn()
#     print("on", d.buf)
#     d.setDataToRGBW(255)
#     print("r", d.buf)
#     d.setDataToRGBW(0, 255)
#     print("g", d.buf)
#     d.setDataToRGBW(0, 0, 255)
#     print("b", d.buf)
#     d.setDataToRGBW(0, 0, 0, 255)
#     print("w", d.buf)
#     d.setDataToRGBW(255, 255, 255, 255)
#     print("rgbw", d.buf)
#     d.setDataToArray([0, 0, 0])
#     print("000", d.buf)
#     import time
#
#     while True:
#         time.sleep(1)
