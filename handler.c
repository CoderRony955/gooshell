#include <stdio.h>
#include <ctype.h>
#include "colors.h"
#include "handler.h"
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

void welcome()
{
    system("python others/welcome_msg.py");
}

void MainHandler()
{
    welcome();
    while (true)
    {
        printf("> %s%s", BOLD_TXT, RESET);
        char user[100];
        if (fgets(user, sizeof(user), stdin))
        {
            user[strcspn(user, "\n")] = '\0';
            if (strcmp(user, "joke") == 0)
            {
                printf("\n");
                system("python others/getjoke.py");
                printf("\n");
                continue;
            }
            else if (strcmp(user, "q") == 0 || strcmp(user, "quit") == 0)
            {
                printf("%sBye!%s", ITALIX_TXT, RESET);
                break;
            }
            else if (strcmp(user, "roastme") == 0)
            {
                printf("\n");
                system("python others/roast.py");
                printf("\n");
            }
            else if (strcmp(user, "curhealth") == 0)
            {
                printf("\n");
                system("python others/checkhealth.py");
                printf("\n");
            }
            else if (strlen(user) == 0)
            {
                continue;
            }
            else
            {
                printf("\n%s", BOLD_TXT);
                system(user);
                printf("%s\n", RESET);
            }
        }
        else
        {
            printf("\n%sOops! Try again.%s\n", RED, RESET);
        }
    }
}