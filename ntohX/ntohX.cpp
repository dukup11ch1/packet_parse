#include "stdio.h"
#include "stdint.h"

uint16_t my_ntohs(uint16_t n){
    uint16_t a=n&0xff00;
    uint16_t b=n&0x00ff;
    return (a>>8)|(b<<8);
    /*__asm{
        mov ax, word ptr [ebp+8];
        xchg ah, al;
    }*/
}

uint32_t my_ntohl(uint32_t n){//0x78563412
    uint32_t a=n&0xff000000;//0x78000000
    uint32_t b=n&0x00ff0000;//0x00560000
    uint32_t c=n&0x0000ff00;//0x00003400
    uint32_t d=n&0x000000ff;//0x00000012

    return (a>>24)|(b>>8)|(c<<8)|(d<<24);
}
int main(){
    uint8_t buf[]={0x12,0x34,0x56,0x78};
    uint16_t* p =(uint16_t*)buf;
    uint16_t port = *p;
    port=my_ntohs(port);
    //uint32_t* p =(uint32_t*)buf;
    //uint32_t ip = *p;
    //ip=my_ntohl(ip);
    printf("%x\n",port);

}