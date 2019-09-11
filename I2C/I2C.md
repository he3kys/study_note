
# 1. 时序

## 1.1. ACK和NAK

**时序**

> ACK ： 在第9个CLK为高电平期间，SDA保持低电平
> NAK ： 在第9个CLK为高电平期间，SDA保持高电平

**一般用途**

> ACK ： i2c write的时候，master在写完最后一个字节之后slave会回ACK，表示slave以成功接收数据，然后master发送stop信号结束通信

> NAK : i2c read的时候，master在接收完slave发送的最后一个字节之后会回NAK，因为这个时候master已经接收到足够的字节，NAK告诉slave不要再发送数据了。

