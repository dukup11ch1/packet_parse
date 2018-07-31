#include <pcap.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <netinet/if_ether.h>
#include <stdint.h>

void usage();
void print_mac(char head[], unsigned char data[]);
void print_data(char head[], unsigned char data[]);

int main(int argc, char* argv[]) {
  if (argc != 2) {
    usage();
    return -1;
  }

  char* dev = argv[1];
  char errbuf[PCAP_ERRBUF_SIZE];
  pcap_t* handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
  if (handle == NULL) {
    fprintf(stderr, "couldn't open device %s: %s\n", dev, errbuf);
    return -1;
  }

  while (true) {
    struct pcap_pkthdr* header;
    struct ethhdr* eth_h;
    struct ip* ip_h;
    struct tcphdr* tcp_h;
    const u_char* packet;
    unsigned char *data;
    int res = pcap_next_ex(handle, &header, &packet);//live packetcapture
    if (res == 0) continue;//buffer timeout
    if (res == -1 || res == -2) break;//error
    printf("*********************************************************\n");
    printf("%u bytes captured\n", header->caplen);
    eth_h = (struct ethhdr*)packet;
    if (htons(eth_h->h_proto) == ETHERTYPE_IP)//ETHERTYPE_IP is in if_ether.h
    {
      ip_h = (struct ip*)(packet + sizeof(struct ethhdr));
      if (ip_h->ip_p == IPPROTO_TCP)//IPPROTO_TCP in tcp.h
      {
        tcp_h = (struct tcphdr*)((void *)ip_h + ip_h->ip_hl * 4);
        data = (unsigned char *)(tcp_h + tcp_h->th_off * 4);
        print_mac("src_MAC:", (unsigned char *)eth_h->h_source);
        print_mac("dst_MAC:", (unsigned char *)eth_h->h_dest);
        printf("src ip:\t\t%s\n", inet_ntoa(ip_h->ip_src));//inet_ntoa = int ip to string
        printf("dst ip:\t\t%s\n", inet_ntoa(ip_h->ip_dst));
        printf("src port:\t%u\n", htons(tcp_h->th_sport));
        printf("dst port:\t%u\n", htons(tcp_h->th_dport));
        ip_h->ip_len-ip_h->ip_hl-sizeof(struct ethhdr)
      }
    }
    printf("*********************************************************\n");
  }

  pcap_close(handle);
  return 0;
}

void usage() 
{
printf("syntax: pcap_test <interface>\n");
printf("sample: pcap_test wlan0\n");
}

void print_mac(char head[], unsigned char data[])
{
  printf("%s\t%02x:%02x:%02x:%02x:%02x:%02x\n", head,
    data[0], data[1], data[2], data[3], data[4], data[5]);
}

void print_data(char head[], unsigned char data[])
{
  printf("%s\t%02x %02x %02x %02x %02x %02x %02x %02x\n\t\t%02x %02x %02x %02x %02x %02x %02x %02x\n", head,
    data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]);
}


//hand clone https://github.com/34t3rnull/pcap_assignment/blob/master/main.cpp
//modified by dukup11ch1