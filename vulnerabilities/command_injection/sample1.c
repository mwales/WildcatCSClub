// Example Code from OWASP Foundation
// Command Injection
// https://owasp.org/www-community/attacks/Command_Injection
// Author: Weilin Zhong
// Contributor(s): Wichers, Amwestgate, Rezos, Clow808, KristenS, Jason Li, Andrew Smith, Jmanico, Tal Mel, kingthorin

#include <stdio.h>
#include <unistd.h>
#include <string.h> // added by me for a clean compile
#include <stdlib.h> // added by me for a clean compile

int main(int argc, char **argv) {
 char cat[] = "cat ";
 char *command;
 size_t commandLength;

 commandLength = strlen(cat) + strlen(argv[1]) + 1;
 command = (char *) malloc(commandLength);
 strncpy(command, cat, commandLength);
 strncat(command, argv[1], (commandLength - strlen(cat)) );

 system(command);
 return (0);
}
