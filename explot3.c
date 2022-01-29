#include <unistd.h>

int main()
{
char *path = "/home/httpd/grades.txt";
unlink(path);
return 0;
}


