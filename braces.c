
#include <stdbool.h>
#include <stdio.h>

bool valid_braces (const char *braces);

/* Function test */
int main()
{
    const char str[100] = "()";
    if (valid_braces(str) == true)
        printf("TRUE\n");
    else
        printf("FALSE\n");
    return 0;
}

/* Testing if brace organizasion is valid or not */
bool valid_braces (const char *braces)
{
    bool valid = true;
    char expected_brace_stack[250];
    int i = 0, ebs_i = -1;

    for (i; braces[i] != '\0'; i++)
    {
        if (braces[i] == '(') {
            ebs_i++;
            expected_brace_stack[ebs_i] = ')'; 
        }
        else if (braces[i] == '[') {
            ebs_i++;
            expected_brace_stack[ebs_i] = ']'; 
        }
        else if (braces[i] == '{') {
            ebs_i++;
            expected_brace_stack[ebs_i] = '}'; 
        }
        else if (braces[i] == expected_brace_stack[ebs_i]) {
            ebs_i--;
        }
        else 
        {
            valid = false;
            break;
        }
    }
    if (ebs_i != -1) 
        valid = false;
    return valid;
}

