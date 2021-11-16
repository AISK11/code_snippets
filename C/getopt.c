#include <stdio.h>  /* printf */
#include <getopt.h> /* getopt */

/* SOURCES:
 * https://azrael.digipen.edu/~mmead/www/mg/getopt/index.html
*/

int main(int argc, char *argv[]) {
    /* CLI parameter check */
    int opt;

    /* SYNTAX:
     * - Disable auto error printing = put ':' before arguments.  (":abc")
     * - By default, getopt moves all non-option arguments to end,
     *   to prevent it use '-' at the start                       ("-:abc")
     * - If option requires argument = put ':' after argument.    ("-:a:b:c:")
     * - For optional option arguments = put "::" after argument. ("-:a::b::c::")
     */

    /* getopt returns -1 -> no more options -> loop terminates. */
        while ((opt = getopt(argc, argv, "-:nr:o::")) != -1) {
        switch (opt) {
            case 'n':
                printf("Option 'n' was provided.\n");
                break;
           case 'r':
                printf("Option 'r' was provided with parameter '%s'.\n", optarg);
                break;
            /* there cannot be space between optional argument and optional option argument. ("-oOPTION") */
            case 'o':
                printf("Option 'o' was provided with parameter '%s'.\n", optarg ? optarg : "NULL");
                break;
            /* Custom Error Handling: */
            case '?':
                printf("ERROR! Unknown option: '%c'!\n", optopt);
            break;
            case ':':
                printf("ERROR! Missing arg for '%c'!\n", optopt);
            break;
        }   
    }   
    return 0;
}
