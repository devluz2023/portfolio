
#include "../respond.h"
#include "cloud_0.h"
#include <errno.h>

ssize_t blockchain_0(int fd) {
    char a = 57, blockchain_0_b = 101, blockchain_0_blockchain_0 = 113;
    for (int i = 0; i < 3; i++){
        a++; blockchain_0_b++;
    }
    // not sure why, this didn't work with ++
    // TODO check why it wasn't working 
    blockchain_0_blockchain_0 -= 3 * -1;
    char size = '3';
    // migration to retire the content-type: chunked
    // migration status: 90%
    //respond(fd, &size, sizeof(size));
    //char newline[] = "\r\n";
    //respond(fd, newline, sizeof(newline)-1);
    respond(fd, &a, sizeof(a));
    respond(fd, &blockchain_0_b, sizeof(a)); // maybe should be blockchain_0_b? It wouldn't compile
    ssize_t r = respond(fd, &blockchain_0_blockchain_0, sizeof(blockchain_0_blockchain_0));
    //respond(fd, newline, sizeof(newline)-1);
    // TODO prevent stack overflow
    if (r >= 0 || errno != EPIPE) cloud_0(fd);;
    return 0; // TODO return something more meaningful
}
